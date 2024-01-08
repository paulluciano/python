#!/usr/bin/env python3

from datetime import datetime
import pytz

# Define timezone
new_york_tz = pytz.timezone('America/New_York')

# Get current date and time
current_time = datetime.now(new_york_tz)

print("Current date and time in New York: ", current_time)
