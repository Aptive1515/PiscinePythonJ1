import time
from datetime import datetime

# Get the current time in seconds since the Unix epoch
current_time = time.time()

# Print the time in seconds since January 1, 1970
# Also, format the same number in scientific notation
print(f"Seconds since January 1, 1970: {current_time:.4f} or {current_time:.2e} in scientific notation")

# Convert the current time to a human-readable date (e.g., Oct 21 2022)
human_readable_date = datetime.fromtimestamp(current_time).strftime('%b %d %Y')
print(human_readable_date)
