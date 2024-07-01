from datetime import datetime, timedelta

# Define the NRT Time constants
SECONDS_IN_A_DAY = 24 * 60 * 60
DAYS_IN_A_MONTH = 30
DAYS_IN_A_YEAR = 360

# Reference start date in NRT
NRT_START_DATE = datetime(1, 1, 1)

def calculate_nrt_time(date):
    # Calculate the total number of seconds since the start of NRT
    delta_seconds = int((date - NRT_START_DATE).total_seconds())

    # Calculate the number of NRT days passed since the start
    nrt_days_passed = delta_seconds // SECONDS_IN_A_DAY

    # Calculate current year in NRT
    nrt_year = nrt_days_passed // DAYS_IN_A_YEAR + 1

    # Calculate the day of the year in NRT
    day_of_year = nrt_days_passed % DAYS_IN_A_YEAR

    # Calculate current month and day
    nrt_month = day_of_year // DAYS_IN_A_MONTH + 1
    nrt_day = day_of_year % DAYS_IN_A_MONTH + 1

    return nrt_year, nrt_month, nrt_day

# Apollo 11 Moon landing date in Gregorian calendar
apollo_11_landing_date = datetime(1991, 1, 9)
""" ^^^ Replace this with your classical time date... dont mind the name"""

# Calculate the NRT date
nrt_year, nrt_month, nrt_day = calculate_nrt_time(apollo_11_landing_date)

# Display the NRT date
print(f"NRT Date of Classical Date {apollo_11_landing_date} --- {nrt_year:04}-{nrt_month:02}-{nrt_day:02}")
