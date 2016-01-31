from ggplot import *
import time
import pandas as pd


def plot_hourly_ridership(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    #print list(turnstile_weather.columns.values)
    plot = ggplot(turnstile_weather,  aes(x ='Hour', y = 'ENTRIESn_hourly'));# your code here
    plot = plot + geom_point() + labs(title = "Hour (of the day) vs Hourly Entries", x = "Hour (of the day)") + xlim(-1, 24) + ylim(0, 60000)
    return plot + scale_x_continuous(breaks = (0,3,6,9,12,15,18,21), labels = ("12:00 AM", "3:00 Am", "6:00 AM", "9:00 AM", "12:00 PM", "3:00 PM", "6:00PM", "9:00PM"))

def plot_ridership_day_of_week(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    weekDay = turnstile_weather.DATEn.apply(lambda x: time.strptime(x, '%Y-%m-%d').tm_wday)
    turnstile_weather["day_of_week"] = weekDay
    plot = ggplot(turnstile_weather,  aes(x ='day_of_week', y = 'ENTRIESn_hourly'));# your code here
    plot = plot + geom_point() + labs(title = "Day of the week vs Hourly Entries", x = "Weekday") + ylim(0, 60000)
    return plot + xlim(-1, 7) +  scale_x_continuous(breaks = (0,1,2,3,4,5,6), labels = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") )

df = pd.DataFrame.from_csv('../turnstile_data_master_with_weather.csv')
plot_hourly_ridership(df)
plot_ridership_day_of_week(df)