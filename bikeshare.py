import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITY_LIST = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Would you like to see data for Chicago, New Yor, or Washington?")).lower()
        if city in CITY_LIST:
            break
    
    # Get user input for month (all, january, february, ... , june)
    while True:
        month = str(input("Which month - January, February, March, April, May, June, or all?")).lower()
        if month in MONTHS:
            break

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?")).lower()
        if day in DAYS:
            break 

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most common month
    mc_month = df['month'].value_counts().idxmax()
    print("Most common month:", mc_month)

    # Displays the most common day of week
    mc_week_day = df['day_of_week'].value_counts().idxmax()
    print("Most common weekday:", mc_week_day)

    # Displays the most common start hour
    mc_start_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print("Most common start hour:", mc_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displays most commonly used start station
    mc_start = df['Start Station'].value_counts().idxmax()
    print("Most common start station: ", mc_start)

    # Displays most commonly used end station
    mc_end = df['End Station'].value_counts().idxmax()
    print("Most common end station: ", mc_end)


    # Displays most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'].map(str) + ' and ' +  df['End Station']
    mc_start_and_end = df['Start End'].mode()[0]
    print("Most common start station and end station : {}"\
            .format(mc_start_and_end))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays total travel time
    tot_travel = df['Trip Duration'].sum()
    print("Total travel time: ", tot_travel)


    # Displays mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displays counts of user types
    user_counts = df['User Type'].value_counts()
    print("Counts of user types: ", user_counts)


    # Displays counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender: ", gender_counts)
    except:
        print("Gender data is not available in selected city.")
        
    
    # Displays earliest, most recent, and most common year of birth
    try:
        birth_year = df['Birth Year']
        mc_year = birth_year.value_counts().idxmax()
        print("Most common birth year: ", mc_year)
        mr_birth = birth_year.max()
        print("Most recent birth year: ", mr_birth)
        earliest_year = birth_year.min()
        print("Most earliest birth year: ", earliest_year)
    except:
        print("Birth Year data is not available in selected city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_input_data(df):
    """Shows five rows of raw data upon user request."""
    std=0
    end=5
    while True:
        show_5 = input('\nWould you like to see 5 rows of input data? Enter yes or no.\n')
        if show_5.lower() != 'yes':
            break
        print(df[std:end])
        std += 5
        end += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)    
        show_input_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
