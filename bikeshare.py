import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

##create variables for all functions

cities = ['chicago','new york city', 'washington']
months = ['january','february','march','april','may','june','all']
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('Would you like to see data for Chicago, New York City or Washington? \n').lower()
        if city in cities:
            break

    # get user input for month (all, january, february, ... , june)

    while True:
        month = input('Which month would you like to see data for? Type "All" to see data for all months \n').lower()
        if month in months:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Which day of the week would you like to see data for? Type "All" to see data for all days \n').lower()
        if day in days: 
            break


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
    
    ## create dataframe for the filtered city

    df = pd.read_csv(CITY_DATA[city])
    
    ##convert Start Time to datetime column

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    ##get month and day of week from Start Time

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    ## filter data for month

    if month != 'all':
        month = months.index(month)+1
        df = df[df['month'] == month]
        
    ## filter data for day

    if day != 'all':
        df = df[df['day'] == day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    df['month_name'] = df['Start Time'].dt.month_name()
    most_common_month = df['month_name'].mode()[0]
    print('The most common month is: \n', most_common_month)

    # display the most common day of week

    most_common_day = df['day'].mode()[0]
    print('The most common day of week is: \n', most_common_day)


    # display the most common start hour

    most_common_start_hour = df['hour'].mode()[0]
    print('The most common start hour is: \n', most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_start = df['Start Station'].mode()[0]
    print('The most commonly used start station is: \n', most_common_start)


    # display most commonly used end station

    most_common_end = df['End Station'].mode()[0]
    print('The most commonly used end station is: \n', most_common_end)


    # display most frequent combination of start station and end station trip

    most_frequent_combination = (df['Start Station'] + '|' + df['End Station']).mode()[0]
    print('The most frequent combination of start and end station is: \n', str(most_frequent_combination.split('|')).replace("'","").replace(","," / ")[1:-1])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: \n',int(round(total_travel_time/3600,0)), ' hours')


    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('The average travel time is: \n',round(mean_travel_time/60,2), ' minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('The count of each user type is: \n',user_types)
       

    # Display counts of gender

    while True:
        if 'Gender' in df.columns:
            gender = df['Gender'].value_counts()
            print('The count of each gender is: \n',gender)
            break
            
        else:
            print('The city selected does not contain gender data.')
        break

              
    # Display earliest, most recent, and most common year of birth
    
    while True:
        if 'Birth Year' in df.columns:
            earliest_year = df['Birth Year'].min()
            print('The earliest birth year is: \n',int(earliest_year))
                  
            most_recent_year = df['Birth Year'].max()
            print('The most recent birth year is: \n',int(most_recent_year))
                  
            most_common_year = df['Birth Year'].mode()[0]
            print('The most common birth year is: \n',int(most_common_year))
            break
                  
        else:
            print('The city selected does not contain birth year data.')
                  
        break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    

    while True:
        
        responses = ['yes','no']
        response = input('Would you like to see raw data behind these outputs? Yes or No? \n').lower()
        
        if response in responses:
            if response == 'yes':
                start = 0
                end = 5               
                print(df[start:end])
            break
        break  
        
    if response == 'yes':
        while True:
            more_response = input('Would you like to see more raw data? Yes or No? \n').lower()
            if more_response in responses:
                if more_response == 'no':
                    break
                elif more_response == 'yes':
                    start+=5
                    end+=5
                    print(df[start:end])
                    
                    
    
        
          

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
