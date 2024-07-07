import datetime

def display_current_datetime():
    '''Prints the current date and time.'''
    current_date = datetime.datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
