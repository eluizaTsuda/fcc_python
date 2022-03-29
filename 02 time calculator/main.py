# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))  # 1:08 AM
#print(add_time("3:30 PM", "2:12"))   # 5:42 PM
#print(add_time("11:55 AM", "3:12"))  # 3:07 PM
#print(add_time("11:40 AM", "0:25"))  # 12:05 PM
print(add_time("5:01 AM", "0:00"))   # 5:01 AM

print(add_time("9:15 PM", "5:30"))   # "2:45 AM (next day)"


# Run unit tests automatically
#main(module='test_module', exit=False)