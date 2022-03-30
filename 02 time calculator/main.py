# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main



print(add_time("3:30 PM", "2:12"))   # 5:42 PM
#print(add_time("11:55 AM", "3:12"))  # 3:07 PM
#print(add_time("11:40 AM", "0:25"))  # 12:05 PM
#print(add_time("5:01 AM", "0:00"))   # 5:01 AM

print(add_time("11:06 PM", "2:02"))  # 1:08 AM (next day)
#print(add_time("9:15 PM", "5:30"))   # "2:45 AM (next day)"
#print(add_time("2:59 AM", "24:00"))  # "2:59 AM (next day)"
#print(add_time("11:59 PM", "24:05")) # "12:04 AM (2 days later)"
#print(add_time("8:16 PM", "466:02")) # "6:18 AM (20 days later)"

#print(add_time("3:30 PM", "2:12", "Monday"))      # "5:42 PM, Monday"
#print(add_time("2:59 AM", "24:00", "saturDay"))   # "2:59 AM, Sunday (next day)"
#print(add_time("11:59 PM", "24:05", "Wednesday")) # "12:04 AM, Friday (2 days later)"
#print(add_time("8:16 PM", "466:02", "tuesday"))   # "6:18 AM, Monday (20 days later)"


# Run unit tests automatically
#main(module='test_module', exit=False)