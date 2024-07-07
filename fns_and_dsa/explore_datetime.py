from datetime import datetime, timedelta

def display_current_datetime():
    '''Prints the current date and time.'''
    current_date = datetime.now()
    return(current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    '''Calculates future date'''
    number_of_days = input("Enter the number of days to add to the current date: ")
    future_date = datetime.now() + timedelta(days=number_of_days)
    return(future_date.strftime("%Y-%m-%d"))
