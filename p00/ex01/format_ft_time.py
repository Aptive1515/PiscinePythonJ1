import time
from datetime import datetime

current_time = time.time()

bgn = "Seconds since January 1, 1970:"

print(f"{bgn} {current_time:.4f} or {current_time:.2e} in scientific notation")

human_readable_date = datetime.fromtimestamp(current_time).strftime('%b %d %Y')
print(human_readable_date)
