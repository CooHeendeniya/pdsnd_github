import time
import pandas as pd
import numpy as np
import calendar as cal

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

DAY_TO_INDEX = {
    "monday": 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday": 5,
    "sunday": 6
}

MONTH_TO_INDEX = {
    'january': 1, 
    'february': 2, 
    'march': 3, 
    'april': 4, 
    'may': 5, 
    'june': 6
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('*' * 60)
    print('Hello! Let\'s explore some US bikeshare data!')
    print('*' * 60)
    
    # List the correct options for city, month, and day.
    valid_city_options = ('new york city', 'chicago', 'washington')
    valid_month_options = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
    valid_day_options = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

    # Collect user input for the city they are interested in (Chicago, New York City, or Washington).
    while True:
        selected_city = input("\nFirst, please select a city: Chicago, New York City, or Washington?\n>>> ").lower()
        
        # Address incorrect city inputs.
        if selected_city not in valid_city_options:
            print("Invalid city selection. Please choose either Chicago, New York City, or Washington.")
        else:
            break

    # Collect user input for the month, which can be any month from January to June, or 'all' for no month filter.
    while True:
        selected_month = input(f"\nWhich month would you like to analyze for {selected_city.title()}? You can select from January, February, March, April, May, June, or type 'all' if you don't want to specify a month.\n>>> ").lower()
        
        # Address incorrect city inputs.
        if selected_month not in valid_month_options:
            print("Invalid month selection. Please choose a valid month or 'all' for no month filter.")
        else:
            break

    # Collect user input for the day of the week, which can be any day from Monday to Sunday, or 'all' for no day filter.
    while True:
        selected_day = input(f"\nNow, let's pick a day. You can select from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or type 'all' if you don't want to specify a day.\n>>> ").lower()
        
        # Address incorrect city inputs.
        if selected_day not in valid_day_options:
            print("Invalid day selection. Please choose a valid day or 'all' for no day filter.")
        else:
            break

    print('-'*40)
    return selected_city, selected_month, selected_day

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
    # 1. read the dataframe of the selected city, using the pandas package
    df = pd.read_csv(CITY_DATA[city])
    
    # 2. convert Start Time to a datetime object, for subsequent extraction of
    # month and weekday (and later, hour)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # 3. extraction of month and day
    df['Month'] = df['Start Time'].dt.month
    df['Weekday'] = df['Start Time'].dt.weekday
    
    # 4. filtering of dataset, based on selections
    if month != 'all':
        month = MONTH_TO_INDEX.get(month)
        df = df[df['Month'] == month]
    
    if day != 'all':
        day = DAY_TO_INDEX.get(day)
        df = df[df['Weekday'] == day]
    
    return df

def time_stats(df, city, month, day):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df (DataFrame): The DataFrame containing bikeshare data.
        city (str): The selected city for analysis.
        month (str): The chosen month for filtering.
        day (str): The selected day of the week for filtering.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Show the month that appears most frequently for the chosen city.
    if month != 'all':
        # Filter the data according to the chosen month.
        filtered_df = df[df['Month'] == MONTH_TO_INDEX.get(month)]
        most_common_month = filtered_df['Month'].value_counts().idxmax()
        print(f'* For your selection in {city.title()} and the month of {month.title()}, the most common month is {cal.month_name[most_common_month]}.\n')
    else:
        most_common_month = df['Month'].value_counts().idxmax()
        print(f'* For your selection in {city.title()}, the most common month is {cal.month_name[most_common_month]}.\n')

    # Show the most frequently occurring day of the week in the selected city.
    if day != 'all':
        # Filter the data based on the chosen day.
        filtered_df = df[df['Weekday'] == DAY_TO_INDEX.get(day)]
        most_common_day = filtered_df['Weekday'].value_counts().idxmax()
        print(f'* For your selection in {city.title()} and the day of the week {day.title()}, the most common day is {cal.day_name[most_common_day]}.\n')
    else:
        most_common_day = df['Weekday'].value_counts().idxmax()
        print(f'* For your selection in {city.title()}, the most common day of the week is {cal.day_name[most_common_day]}.\n')

    # Show the most frequently occurring starting hour for the selected city.
    df['Start Hour'] = df['Start Time'].dt.hour
    most_common_hour = df['Start Hour'].value_counts().idxmax()
    print(f'* The most common start hour for your selection in {city.title()} is {most_common_hour} o\'clock.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        df (DataFrame): The DataFrame containing bikeshare data.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Find the start station that users most often use.
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('* The frequently chosen start station is:', popular_start_station, '\n')

    # Find the end station that users choose most frequently.
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('* The commonly chosen end station is:', popular_end_station, '\n')

    # Show the most common combination of start and end stations for trips. To do this:
    # 1. Combine the start and end stations into a new column.
    df['Station Combination'] = df['Start Station'] + ' (departure) and ' + df['End Station'] + ' (arrival).'

    # Examine the common combination of departure and arrival stations for journeys.
    common_station_combination = df['Station Combination'].value_counts().idxmax()
    print('* The prevalent station combination for trips is:', common_station_combination, '\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics related to total and average trip durations.

    Args:
        df (DataFrame): The DataFrame containing bikeshare data.
    """

    print('\nCalculating Trip Duration Statistics...\n')
    start_time = time.time()

    # Show the total time spent on traveling.
    # 1. Compute total time spent on traveling in seconds using .sum()
    total_travel_time_seconds = df['Trip Duration'].sum()

    # 2. Convert the total travel time from seconds to hours and round it to the nearest whole number.
    total_travel_time_hours = round(total_travel_time_seconds / 60 / 60, 0)

    # 3. Display the total travel time.
    print('* The total travel time for your selection is', total_travel_time_hours, 'hours.\n')

    # Show the average travel time.
    # 1. Compute average travel time in seconds using .mean()
    mean_travel_time_seconds = df['Trip Duration'].mean()

    # 2. Convert the average travel time from seconds to minutes and round it to the nearest whole number.
    mean_travel_time_minutes = round(mean_travel_time_seconds / 60, 0)

    # 3. Display the average travel time either in minutes or hours, and print it.
    if mean_travel_time_minutes < 60:
        print('* The mean travel time for your selection is', mean_travel_time_minutes, 'minutes.\n')
    else:
        mean_travel_time_hours = round(mean_travel_time_minutes / 60, 1)
        print('* The mean travel time for your selection is', mean_travel_time_hours, 'hours.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df, selected_city):
    """Displays statistics related to bikeshare users using NumPy.

    Args:
        df (DataFrame): The DataFrame containing bikeshare data.
        selected_city (str): The selected city for analysis.
    """

    print('\nCalculating User Statistics...\n')
    start_time = time.time()

    # Show the number of different user types.
    # 1. Convert the 'User Type' column into a NumPy array to facilitate counting later.
    user_types = df['User Type'].values

    # 2. Count the frequency of each user type.
    subscriber_count = (user_types == 'Subscriber').sum()
    customer_count = (user_types == 'Customer').sum()

    # 3. Display user type counts
    print(f'* Total number of subscribers in {selected_city.title()}: {subscriber_count}\n')
    print(f'* Total number of customers in {selected_city.title()}: {customer_count}\n')

    # Display gender counts and present the earliest, most recent, and most common birth years.
    # Note that gender and birth year data are not available for the Washington dataset.
    if selected_city.title() != 'Washington':
        # Counts of gender
        # 1. Convert the 'Gender' column into a NumPy array for later counting.
        genders = df['Gender'].values

        # 2. Count the occurrences of different gender categories.
        male_count = (genders == 'Male').sum()
        female_count = (genders == 'Female').sum()

        # 3. Display different gender counts
        print(f'* Total number of male users in {selected_city.title()}: {male_count}\n')
        print(f'* Total number of female users in {selected_city.title()}: {female_count}\n')

        # Year of birth
        # 1. Convert the 'Birth Year' column into a NumPy array for further statistical analysis.
        birth_years = df['Birth Year'].values

        # 2. Retrieve unique birth years while excluding any missing values (NaNs).
        unique_birth_years = np.unique(birth_years[~np.isnan(birth_years)])

        # 3. The most recent birth year corresponds to the highest numerical value.
        latest_birth_year = unique_birth_years.max()

        # 4. The oldest birth year corresponds to the lowest numerical value.
        earliest_birth_year = unique_birth_years.min()

        # 5. Display the most recent and earliest birth years.
        print(f'* Most recent birth year of users in {selected_city.title()}: {int(latest_birth_year)}\n')
        print(f'* Earliest birth year of users in {selected_city.title()}: {int(earliest_birth_year)}\n')

        # 6. Display the most common year of birth
        most_common_birth_year = int(df['Birth Year'].value_counts().idxmax())
        print(f'* Most common birth year of users in {selected_city.title()}: {most_common_birth_year}\n')

    else:
        # Display a message if Washington is selected as the city.
        print('* Gender and birth year information are not available for Washington.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def raw_data(data_frame):
    """Displays 5 lines of raw data at a time upon user request.

    Args:
        data_frame (DataFrame): The DataFrame containing bikeshare data.
    """

    print('\nDisplaying Raw Data...\n')
    start_index = 0
    end_index = 5

    while True:
        show_data = input('Do you want to view 5 lines of unprocessed data? Please respond with either \'yes\' or \'no\'.\n>>> ')
        if show_data.lower() == 'yes':
            # Display the next 5 rows of raw data
            print(data_frame.iloc[start_index:end_index])
            
            # Increment start and end indices for the next 5 lines
            start_index += 5
            end_index += 5
        else:
            # Exit the loop when 'no' is selected
            break

    print('-' * 60)
    

def main():
    while True:
        try:
            # Get user input for city, month, and day
            city, month, day = get_filters()
            
            # Load data for the selected city, month, and day
            df = load_data(city, month, day)
            
            # Display statistics on the most frequent times of travel
            time_stats(df, city, month, day)
            
            # Display statistics on popular stations and trips
            station_stats(df)
            
            # Display statistics on trip duration
            trip_duration_stats(df)
            
            # Display statistics on bikeshare users
            user_stats(df, city)
            
            # Additional function to display raw data
            raw_data(df)
        except Exception as error:
            print(f"\nAn error occurred: {error}")
        
        restart = input('\nDo you wish to restart the program? Please type \'yes\' or \'no\' to respond.\n>>> ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
