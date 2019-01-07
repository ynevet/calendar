import sys
from Calendar import *
from time import localtime

filename = sys.argv[1]
with open(filename) as f:
    c = Calendar()
    events = f.readlines()
    for event in events:
        event = event.split(" ")
        name = event[0]
        date_values = event[1].rstrip().split(".")

        if not (not date_values[0].isdigit() or not date_values[1].isdigit()) and date_values[2].isdigit():
            try:
                date = Date(int(date_values[0]), int(date_values[1]), int(date_values[2]))
                c.add_event(name, date)
            except DateException as date_e:
                sys.stderr.write(date_e)
                print(date_e)
            except CalendarException as cal_e:
                sys.stderr.write(cal_e)
                print(cal_e)
        else:
            print("date must be initialized with numbers")

current_month = localtime()[1]
monthly_events = c.get_all_events_in_month(current_month)
print("Events of the month:")
for name in monthly_events.keys():
    print(name, " happened at: ", monthly_events[name])
