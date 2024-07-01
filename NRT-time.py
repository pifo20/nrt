import time
from datetime import datetime, timedelta

"""
Non-planetary Round Time (NRT) is a system I created for galactically neutral time.
It has 360 days in a year, 12 months each with 30 days, and 60 weeks.
Every single year has the exact same calendar; there are no leap years nor leap seconds nor leap days.

It is not aligned with the seasons or days of Earth, nor Mars, nor Venus or any planet humans could ever pay attention to.
NRT Time is galactically neutral and its purpose is not for alignment of a planet, but to help people across the world and across all worlds share the exact same time for timekeeping and convenience.

It is round because all numbers in it divide nicely:
360 days; 12 months in each year; 5 weeks in each month; 6 days in each week; 24 hours in each day; 60 minutes in each hour; 60 seconds in each minute.
30 days in each month; 60 weeks in each year.

You do not need to buy a new calendar every 360 days, as each NRT year has the exact same layout as the last.

This is what all 12 months of all years look like:

(We no longer have Sunday; Monday, Tuesday, Wednestay, Thurstay, Friday, and Saturday are the days of the week.)

Mo Tu We Th Fr Sa
 1  2  3  4  5  6 
 7  8  9 10 11 12 
13 14 15 16 17 18 
19 20 21 22 23 24 
25 26 27 28 29 30 
"""

# Define the NRT Time constants
SECONDS_IN_A_DAY = 24 * 60 * 60
DAYS_IN_A_MONTH = 30
DAYS_IN_A_YEAR = 360
MONTHS_IN_A_YEAR = 12

# Reference start date in NRT
NRT_START_DATE = datetime(1, 1, 1)

def calculate_nrt_time(current_utc):
    # Calculate the total number of seconds since the start of NRT
    delta_seconds = int((current_utc - NRT_START_DATE).total_seconds())

    # Calculate the number of NRT days passed since the start
    nrt_days_passed = delta_seconds // SECONDS_IN_A_DAY

    # Calculate current year in NRT
    nrt_year = nrt_days_passed // DAYS_IN_A_YEAR + 1

    # Calculate the day of the year in NRT
    day_of_year = nrt_days_passed % DAYS_IN_A_YEAR

    # Calculate current month and day
    nrt_month = day_of_year // DAYS_IN_A_MONTH + 1
    nrt_day = day_of_year % DAYS_IN_A_MONTH + 1

    # Calculate the remaining seconds in the current NRT day
    remaining_seconds_in_day = delta_seconds % SECONDS_IN_A_DAY
    nrt_hour = remaining_seconds_in_day // 3600
    nrt_minute = (remaining_seconds_in_day % 3600) // 60
    nrt_second = remaining_seconds_in_day % 60

    return nrt_year, nrt_month, nrt_day, nrt_hour, nrt_minute, nrt_second

def display_nrt_time():
    while True:
        # Get the current UTC time
        current_utc = datetime.utcnow()

        # Calculate the NRT time
        nrt_year, nrt_month, nrt_day, nrt_hour, nrt_minute, nrt_second = calculate_nrt_time(current_utc)

        # Display the NRT time
        print(f"NRT Time: {nrt_year:04}-{nrt_month:02}-{nrt_day:02} {nrt_hour:02}:{nrt_minute:02}:{nrt_second:02}", end='\r')

        # Sleep for 1 second before updating the time
        time.sleep(1)

# Run the display function
display_nrt_time()
