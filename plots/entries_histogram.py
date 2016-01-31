import numpy as np
import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from ggplot import *

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    dfRain = turnstile_weather[turnstile_weather["rain"] == 1]
    dfNoRain = turnstile_weather[turnstile_weather["rain"] == 0]
    dfNoRain.reset_index()
    print len(dfNoRain)
    print len(dfRain)
    histNoRain = dfNoRain['ENTRIESn_hourly'].hist(bins=60,range=(0,6000), label="No Rain", color="blue")
    histRain = dfRain['ENTRIESn_hourly'].hist(bins=60,range=(0,6000), label="Rain", color="green") 
    
    #add legend
    NoRainLegend = mpatches.Patch(color='blue', label='No Rain')
    RainLegend = mpatches.Patch(color='green', label='Rain')
    plt.legend(handles=[NoRainLegend, RainLegend])
    
    # add axes label
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.title('Histrogram of ENTRIESn hourly. Bin size: 100')
    return plt

def rainy_vs_non_rainy_random(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    
    dfRain = turnstile_weather[turnstile_weather["rain"] == 1].sample(10000)
    dfNoRain = turnstile_weather[turnstile_weather["rain"] == 0].sample(10000)
    dfNoRain.reset_index()
    print len(dfNoRain)
    print len(dfRain)
    
    # Rainy days
    plt.figure()
    histRain = dfRain['ENTRIESn_hourly'].hist(bins=60,range=(0,6000), label="Rain", color="green") 
    #add legend
    RainLegend = mpatches.Patch(color='green', label='Rain')
    plt.legend(handles=[RainLegend])
    
    # add axes label
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.title('Rainy Days : Histrogram of ENTRIESn hourly. Bin size: 100')
    
    # Non Rainy Days
    plt.figure()
    histNoRain = dfNoRain['ENTRIESn_hourly'].hist(bins=60,range=(0,6000), label="No Rain", color="blue")
    #add legend
    NoRainLegend = mpatches.Patch(color='blue', label='No Rain')
    plt.legend(handles=[NoRainLegend])
    # add axes label
    plt.xlabel('ENTRIESn_hourly')
    plt.ylabel('Frequency')
    plt.title('Non-Rainy Days : Histrogram of ENTRIESn hourly. Bin size: 100')
    
    return plt


df = pd.DataFrame.from_csv('../turnstile_data_master_with_weather.csv')
entries_histogram(df)
rainy_vs_non_rainy_random(df)