import numpy as np
import pandas
import statsmodels.api as sm
import time
import scipy
import matplotlib.pyplot as plt
import sys

"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""

def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    
    This can be the same code as in the lesson #3 exercise.
    """
    
    Y = values
    X = features
    #X = sm.add_constant(X)
    
    results = sm.OLS(Y,X).fit()
    mParams = results.params

    t = results.summary()
    #print type(t)
    print t
    
    params = mParams
    return params
    
    intercept = mParams[0]
    params = mParams[1:]
    #return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with ordinary least squares.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################
    dataframe = dataframe.dropna()

    print list(dataframe.columns.values)

    #[ 'TIMEn', DESCn', 'maxdewpti',
    #'mindewpti', '', 'meandewpti']
    # no effect : 'meanwindspdi', 'thunder' , 'meandewpti'
    # other :  'mintempi', 'maxtempi', 'maxpressurei', 'minpressurei'
    features = dataframe[[ 'rain', 'fog',  'precipi', 'meanpressurei', 'meantempi']]
    #features = dataframe[[ 'rain',  'meanpressurei', 'meantempi']]

    # add weekday to the features.
    weekDay = dataframe.DATEn.apply(lambda x: time.strptime(x, '%Y-%m-%d').tm_wday)
    dummy_weekday = pandas.get_dummies(weekDay, prefix = 'weekday')
    features = features.join(dummy_weekday)
    
    # add 'HOUR' dummies
    dummy_units = pandas.get_dummies(dataframe['Hour'], prefix='hour')
    dummy_units.drop(['hour_1', 'hour_2', 'hour_6', 'hour_7', 'hour_14'], axis=1, inplace=True)
    features = features.join(dummy_units)
    
    # add 'UNIT' column
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    #dummy_units.drop(['unit_R460', 'unit_R015', 'unit_R016', 'unit_R024', 'unit_R030', 'unit_R091', 'unit_R092', 'unit_R093', 'unit_R094', 'unit_R095', 'unit_R096', 'unit_R098', 'unit_R099', 'unit_R136', 'unit_R152', 'unit_R159', 'unit_R187', 'unit_R192', 'unit_R192', 'unit_R197', 'unit_R211', 'unit_R223', 'unit_R238', 'unit_R272', 'unit_R288', 'unit_R290', 'unit_R302', 'unit_R359'], axis=1, inplace=True)
    features = features.join(dummy_units)
    
    
    # add 'DESCn' column
    #dummy_units = pandas.get_dummies(dataframe['DESCn'], prefix='desc_')
    #features = features.join(dummy_units)
    
    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    #intercept, params = linear_regression(features, values)
    params = linear_regression(features, values)
    predictions = np.dot(features, params)
    return predictions

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    plt.title('Residuals histogram. Number of bins = 25.')
    (turnstile_weather['''ENTRIESn_hourly'''] - predictions).hist(range=(-4000,4000),bins=25)
    return plt

def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    # your code here
    denom = ((data-np.mean(data))**2).sum()
    numer = ((data-predictions)**2).sum()
    r_squared = 1 - numer/denom
    return r_squared

nycSubwayDF = pandas.DataFrame.from_csv('turnstile_data_master_with_weather.csv');
subwayEntryPredictions = predictions(nycSubwayDF)
plot_residuals(nycSubwayDF, subwayEntryPredictions)
print compute_r_squared(nycSubwayDF["ENTRIESn_hourly"], subwayEntryPredictions)
