# These are the links that i used to help solve the project.
# https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
# https://stackoverflow.com/questions/12719586/how-to-let-python-recognize-both-lower-and-uppercase-input
# https://knowledge.udacity.com/questions/263877
# https://knowledge.udacity.com/questions/780589
# https://knowledge.udacity.com/questions/86491
# https://knowledge.udacity.com/questions/181095
# https://knowledge.udacity.com/questions/26261

#importing the module
import time
import pandas as pd
import numpy as np
import tabulate

#creating the dataframe
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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

    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nWhat city would you like to get data for? Chicago, New York City, or Washington?\n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
            print("We were able to analyze that city.")
        else:
            print("I'm sorry, you have entered an invalid city.")


    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWhat month would you like data for?\n")
        if month_name.lower() in MONTH_DATA:
            month = month_name.lower()
            print("We are able to analyze that date range.")
        else:
            print("I'm sorry, you have selected an invalid date range.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhat day would you like data for?\n")
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
            print("We are able to analyze that date range.")
        else:
            print("I'm sorry, you have selected an invalid date range.")

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

    # Load data file into Pandas Data Frame
    df = pd.read_csv(city)

    # Column Start Time converted to datetime from string
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns by extracting month, day, and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print("The most popular month from the given inputs is: ", popular_month)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular day from the given inputs is: ", popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular hour from the given inputs is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_pop_start_station = df['Start Station'].value_counts().idxmax()
    print("The most popular start station from the given inputs is: ", most_pop_start_station)

    # TO DO: display most commonly used end station
    most_pop_end_station = df['End Station'].value_counts().idxmax()
    print("The most popular end station from the given inputs is: ", most_pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " and " + df['End Station']
    print('The most combination of start station and end station trip is\n {}'.format((df['combination'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total travel time is:, {} hours, {} minutes, and {} seconds.\n'.format(hour, minute, second))

    # TO DO: display mean travel time
    total_travel_time = df['Trip Duration'].mean()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    print('The total mean travel time is:, {} hours, {} minutes, and {} seconds.\n'.format(hour, minute, second))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("Gender information cannot be found for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        ear_birth_year = df['Birth Year'].min()
        print("The earliest birth year from the given inputs is: ", ear_birth_year)

        recent_birth_year = df['Birth Year'].max()
        print("The most recent birth year from the given inputs is: ", recent_birth_year)

        most_common_birth_year = df['Birth Year'].mode()[0]
        print("The most common birth year from the given inputs is: ", most_common_birth_year)

    else:
        print("\nBirth Year information cannot be found for Washington\n")

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)

     # Ask user if they would like to see 5 lines of raw data.

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    if view_data == 'yes':
        start_loc = 0
    while True:
        print(tabulate(df.iloc[start_loc:start_loc+5]))
        start_loc += 5
        more_data = input('Would you like to see more data?: Enter yes or no.').lower()
        if more_data != 'yes':
            break
    pd.set_option(???display.max_columns',200)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
