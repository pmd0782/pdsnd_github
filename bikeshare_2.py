import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ["chicago", "new york city", "washington"]
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = ""
    while True :
        city = input("Enter city from chicago, new york city or washington: \n").lower()
        if city not in cities:
            print ("The city entered is not valid")
            continue
        else:
            break
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    while True :
        month = input(" Enter: january, february, march, april, may, june:\nType All to filter data by all months.\n").lower()
        if month not in months:
            print ("The month entered is not valid")
            continue
        else:
            break                
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while True :
        day = input("Enter day: monday, tuesday, wednesday, thursday, friday, saturday or sunday: \nType All to filter by all days. \n").lower()
        if day not in days:
            print ("The day entered is not valid")
            continue
        else:
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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        
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
    common_month = df['month'].value_counts().idxmax()
    print('Most common month:', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day of week:',common_day)
    
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common start hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

     # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}.".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}.".format(most_common_end_station))
    
   
    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}".format(most_common_start_end_station[0], most_common_start_end_station[1]))
    
     #calculate trip duration 
    total_trip = df['Start Station'] + ' - ' + df['End Station']
    
    # Find most Frequent Trip
    most_frequent_trip = total_trip.mode()[0]
    print('Most frequent Trip is: {}'.format(most_frequent_trip))
    print('Frequent Trip Counts: {}'.format(total_trip.value_counts()[most_frequent_trip]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_length = df['Trip Duration'].sum()
    total_travel_time = trip_length
    print("The total travel time is {}.".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("The average travel time is {}.".format(average_travel_time))
    
    # Display the quickest travel time
    quickest_travel_time = df['Trip Duration'].min()
    print("The fastest travel time was {}.".format(quickest_travel_time))
                       
    #Display the longest travel time
    longest_travel_time = df['Trip Duration'].max()
    print("The slowest travel time was {}.".format(longest_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        gender_types = df["Gender"].value_counts()
        earliest_birth_year = int(df["Birth Year"].min())
        most_recent_birth_year = int(df["Birth Year"].max())
        most_common_birth_year = int(df["Birth Year"].mode()[0])
    except KeyError:
        #print error statement for 'Gender' Column
        print('Gender column not available.\nCannot display statistics.\n')
    else:
        # display counts of gender, earliest birth year, most recent birth year and most common birth year.
        print('Gender Types: \n{}\n'.format(gender_types))
        print("The gender counts include the following: {}.".format(gender_types))
        print("The earliest Birth year is: {}".format(earliest_birth_year))
        print('The most recent Birth year is: {}'.format(most_recent_birth_year))
        print('The most common Birth year is: {}'.format(most_common_birth_year))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """ Accesses csv and displays 5 rows of its raw data if user types "yes" """
 
 
    raw_data_request = input('\nWould you like to see 5 rows of raw data?  (Yes or No)\n> ').lower()
    if raw_data_request == 'yes':
        print('\nAccessing Raw Data...\n')
        start_time = time.time()
        # index number = 0
        i = 0
        # this while loop cycles through raw data in csv and displays it
        while True:
            print(df.iloc[i:i + 5])
            i += 5
            print("\nThis took %s seconds." % (time.time() - start_time))
            more_data_request = input('\nWould you like to see 5 more rows of raw data?  (Yes or No)\n> ').lower()
            # breaks out of loop if user doesn't type "yes"
            if more_data_request != 'yes':
                break    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():    
    while True :
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
