import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    ### YOUR CODE HERE ###
    dfRain = turnstile_weather[turnstile_weather["rain"] == 1]
    dfRain.reset_index()
    with_rain_mean = dfRain.ENTRIESn_hourly.mean()
    dfNoRain = turnstile_weather[turnstile_weather["rain"] == 0]
    dfNoRain.reset_index()
    without_rain_mean = dfNoRain.ENTRIESn_hourly.mean()
    
    U, p = scipy.stats.mannwhitneyu(dfRain.ENTRIESn_hourly, dfNoRain.ENTRIESn_hourly, use_continuity=True)
    
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader

nycSubwayDF = pandas.DataFrame.from_csv('turnstile_data_master_with_weather.csv');
print mann_whitney_plus_means(nycSubwayDF)