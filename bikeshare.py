import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to analyze: Chicago, New York City or Washington? ").lower()
        if city in ('chicago','new york city', 'washington'):
            break
        else:
            city = input("Please re-enter which city you would like to analyze chicago, new york city or washington? ").lower()
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please input the month to filter by or 'all' to apply no month filter: ")
        if month in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            break
        else:
            month = input("Please re-enter 'all', 'january', 'february', 'march', 'april, 'may' or 'june': ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please input the day of the week to filter, or 'all' to apply no day of the week filter: ")
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
        else:
            day = input("Please re-enter 'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' or 'sunday': ").lower()

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    """Displays stats on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of the week: {}'.format(common_day))

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('\nThe most common start hour: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays stats on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip; found similar code from blog
    df['Start End'] = df['Start Station'].map(str) + ' AND ' + df['End Station']
    most_frq_start_end = df['Start End'].value_counts().idxmax()
    print('\nThe most freqent combination of start station and end station is: {}'.format(most_frq_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays stats on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trav = df['Trip Duration'].sum()
    print('\nThe total travel time: {}'.format(tot_trav))

    # TO DO: display mean travel time
    trav_counts = df['Trip Duration'].count()
    mean_trav = tot_trav / trav_counts
    print('\nThe mean travel time: {}'.format(mean_trav))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays stats on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: \n{}'.format(user_types))
   
    # TO DO: Display counts of gender
    column_headers = list(df)
    if 'Gender' in column_headers:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of Gender: \n{}'.format(gender_count))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in column_headers:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is: {}'.format(int(earliest_year)))
        print('\nThe most recent birth year is: {}'.format(int(recent_year)))
        print('\nThe most common birth year is: {}\n'.format(int(common_year)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_loop(df):
    row1 = 0
    row5 = 5
    while True:
        raw_data = input('\nDo you want to see 5 rows of raw data?\nPlease answer yes or no: ').lower()
        if raw_data == 'yes':
            print(df.iloc[row1:row5],'\n')
            row1 += 5
            row5 +=5
            continue
        elif raw_data == 'no':
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        raw_data_loop(df)
        station_stats(df)
        raw_data_loop(df)
        trip_duration_stats(df)
        raw_data_loop(df)
        user_stats(df)
        raw_data_loop(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
