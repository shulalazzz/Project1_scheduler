import schedule_class
import re
my_admin = schedule_class.admin_mode()
while 1:
    print("1.Admin mode\n2.Adding availability mode\n3.Quit")
    try:
        menu_selection = int(input("Enter a number:"))
    except ValueError:
        print("Not a number.")
        continue
    if menu_selection == 1:
        if my_admin.creator_name == "":
            creator_name = input("Please enter your name:")

        while 1:
            print("1.Add events\n2.View your events\n3.Check available attendees\n4.Quit")
            try:
                admin_selection = int(input())
            except ValueError:
                print("Not a number.")
                continue
            if admin_selection == 1:
                event_name = input("Please enter the event name:")
                event_year = int(input("Please enter the year:"))
                event_month = int(input("Please enter the month:"))
                event_day = int(input("Please enter the day:"))
                time_string = input(
                    "Please enter the beginning time(eg:10.30):")
                temp = re.findall(r'\d+', time_string)
                time = list(map(int, temp))
                start_hour = time[0]
                start_minute = time[1]
                time_string = input("Please enter the end time(eg:10.30):")
                temp = re.findall(r'\d+', time_string)
                time = list(map(int, temp))
                end_hour = time[0]
                end_minute = time[1]
                event_time_slot = schedule_class.slot(
                    start_hour, start_minute, end_hour, end_minute)
                event_date = schedule_class.date(
                    event_year, event_month, event_day, event_time_slot)
                current_event = schedule_class.event(event_name, event_date)
                my_admin.add_event(current_event)
            elif admin_selection == 2:
                my_admin.print_all()
            elif admin_selection == 3:
                event_time_slot.print_slot()
                event_time_slot.convert_time()

            elif admin_selection == 4:
                break
