"""
CMPS 6100  Lab 2
Author: 
"""

### You will need or may find these imports useful
### You may add other imports to this section.
import tabulate
import matplotlib.pyplot as plt
import math
import csv
from datetime import date
###

def read_in_dataset(filename):
    """
    Read in the dataset

    Parameters
    ----------
    filename : string
        the name of the csv file containing the daily summaries data

    Returns
    -------
    dictionary
        a dictionary containing the data.
    """
    daily_summaries = {}
    return daily_summaries

def calculate_month_averages(daily_summaries, year, month):
    """
    Return a tuple: the average precip, highs, and lows
    for a single month.

    If this month is missing from the dataset, return:
    (math.nan, math.nan, math.nan)

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    year : int
        the year
    month : int
        the month of that year to return the averages for.
        For example, for november, pass in 11.

    Returns
    -------
    tuple
        (ave_precip, ave_daily_high, ave_daily_low)
    """
    pass # replace this line with your implementation

def calculate_year_averages(daily_summaries, year):
    """
    Return a tuple: the average precip, highs, and lows
    for a single year: 

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    year : int
        the year to return the averages for

    Returns
    -------
    tuple
        (ave_precip, ave_daily_high, ave_daily_low)
    """
    pass # replace this line with your implementation


def calculate_decade_averages(daily_summaries, decade):
    """
    Return a tuple: the average precip, highs, and lows
    for one decade.

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    decade : int
        an int for the decade. For the 1940s, pass
        in 1940

    Returns
    -------
    tuple
        (ave_precip, ave_daily_high, ave_daily_low)
    """
    pass # replace this line with your implementation

def get_yearly_averages(daily_summaries, years=[]):
    """
    Return a list of tuples, containing the precipitation,
    daily high, and daily low averages for each year

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    years : list
        a list of years to get the averages for

    Returns
    -------
    list<tuple>
        containing tuples of the form:
        (year, ave_precip, ave_daily_high, ave_daily_low)
        for each year
    """
    pass # replace this line with your implementation

def get_decadal_averages(daily_summaries, decades=[]):
    """
    Return a list of tuples, containing the precipitation,
    daily high, and daily low averages for each decade

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    decades : list
        a list of decades to get the averages for. For example,
        for the decades of the 1940's, 1950's, and 1960's, pass in
        [1940, 1950, 1960]

    Returns
    -------
    list<tuple>
        A list containing tuples of the form:
        (decade, ave_precip, ave_daily_high, ave_daily_low)
        for each decade
    """
    pass # replace this line with your implementation

def print_table(climate_averages, table_headers):
    """
    Print a table of the climate_averages

    Parameters
    ----------
    table_headers : list<string>
        a list containing the header text that will go at the top
        of each column.
        For example: 
            ['Year', 'Ave Precip', 'Ave High', 'Ave Low']
    climate_averages : list<tuple>
        Every other row contains the values
    """
    print(tabulate.tabulate(climate_averages[1:],
        headers = table_headers,
        floatfmt=".2f",
        tablefmt="github"))

def plot_yearly_temperatures(daily_summaries, plot_title):
    yearly_aves = get_yearly_averages(daily_summaries)
    years = list(daily_summaries.keys())
    plot_temperatures(yearly_aves, years, "Year", plot_title)
  
def get_decades_in_dataset(data):
    """
    Return a list of the full decades included in the dataset

    Parameters
    ----------
    daily_summaries : dict
        the dictionary containing all the daily summary data
    decades : list
        a list of decades to get the averages for. For example,
        for the decades of the 1940's, 1950's, and 1960's, pass in
        [1940, 1950, 1960]

    Returns
    -------
    list<int>
        A list of ints representing the decades included in the dataset.
        For example, if the dataset contained the years 1984-2023, this
        function will return [1990, 2000, 2010]
    """
    years = list(data.keys())
    first_year = years[0]
    last_year = years[-1]
    if(first_year % 10 == 0):
        first_decade = first_year
    else:
        # example: if first year is 1893, the first complete decade
        # is 1900.
        # 1893 % 3 = 3.
        # 10 - 3 = 7
        # 1893 + 7 = 1900
        first_decade = first_year + (10 - (first_year % 10))
    if(last_year % 10 == 0):
        last_decade = first_year
    else:
        # example: if last year is 2023, last complete decade
        # is 2010.
        # 2023 - (10 + (2023 % 10)) = 2010
        last_decade = last_year - (10 + (last_year % 10))
    return [decade for decade in range(first_decade, last_decade+1, 10)]

def plot_temperatures(aves, x_values, xlabel, title):
    low_temps = []
    high_temps = []
    for tup in aves:
        high_temps.append(tup[2])
        low_temps.append(tup[3])
    # plot
    plt.figure()
    plt.title(title)
    plt.plot(x_values, high_temps, label='High Temperatures', color='red')
    plt.plot(x_values, low_temps, label='Low Temperatures', color='blue')
    plt.xlabel(xlabel)
    plt.ylabel('Temp')
    plt.legend()
    plt.show()

###################
#  Example Usage  #
###################

# daily_summaries = read_in_dataset("nola-temps.csv")

# yearly_aves = get_yearly_averages(daily_summaries)
#
#   yearly_aves is a list of tuples of the form: 
#   (year, ave_precip, ave_daily_high, ave_daily_low)
#   a tuple for each year

# print_table(yearly_aves, ['Year', 'Ave Precip', 'Ave High', 'Ave Low'])

# title = "New Orleans Average Temperatures"
# plot_yearly_temperatures(daily_summaries, title)
