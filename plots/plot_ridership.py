from ggplot import *
import time
import pandas as pd


# mean hourly ridership
def plot_hourly_ridership(turnstile_weather):
    tmp = turnstile_weather.groupby(turnstile_weather.Hour).mean().reset_index()
    plot = ggplot(tmp,  aes(x ='Hour', weight = 'ENTRIESn_hourly'));# your code here
    plot = plot + geom_bar(binwidth=1) + ylab("Mean Hourly Entires")
    plot = plot + labs(title = "Hour (of the day) vs Mean Hourly Entries", x = "Hour (of the day)") + xlim(0, 23)
    return plot + scale_x_continuous(breaks = (0.5,3.5,6.5,9.5,12.5,15.5,18.5,21.5), labels = ("12 AM", "3 AM", "6 AM", "9 AM", "12 PM", "3 PM", "6 PM", "9 PM"))

# mean ridership vs day of the week
def ridership_day_of_week(turnstile_weather):
    weekDay = turnstile_weather.DATEn.apply(lambda x: time.strptime(x, '%Y-%m-%d').tm_wday)
    turnstile_weather["day_of_week"] = weekDay
    turnstile_weather = turnstile_weather.groupby(turnstile_weather.day_of_week).mean().reset_index()
    plot = ggplot(turnstile_weather,  aes(x ='day_of_week', weight = 'ENTRIESn_hourly'));
    plot = plot + geom_bar() + labs(title = "Day of the week vs Mean Hourly Entries", x = "Weekday") 
    plot =  plot +  scale_x_continuous(limits = (-1, 7) , breaks = (0.1, 1.1, 2.1, 3.1, 4.1, 5.1, 6.1), labels = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") )
    plot = plot + ylab('Mean Hourly Entries')
    return plot 

df = pd.DataFrame.from_csv('../turnstile_data_master_with_weather.csv')
plot_hourly_ridership(df)
plot_ridership_day_of_week(df)
