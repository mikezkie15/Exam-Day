# Get current time and covert to milisecond
# then display the result

from datetime import datetime

current_time = datetime.now()
mili = int(current_time.timestamp() * 1000)

print(mili)
