import schedule_class
import re
my_admin = schedule_class.admin_mode()
while 1:
    print("1.Admin mode\n2.Adding availability mode\n3.Quit")
    menu_selection = int(input())
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
                while 1:
                    event_month = int(input("Please enter the month:"))
                    if event_month < 1 or event_month > 12:
                        print("Enter a valid month!")
                    elif event_month >= 1 or event_month <= 12:
                        break
                while 1:
                    event_day = int(input("Please enter the day:"))
                    if event_year % 4 == 0 and event_year % 100 != 0:
                        if event_month == 1 or event_month == 3 or event_month == 5 or event_month == 7 or event_month == 8 or event_month == 10 or event_month == 12:
                            if event_day < 1 or event_day > 31:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 31:
                                break
                        elif event_month == 4 or event_month == 6 or event_month == 9 or event_month == 11:
                            if event_day < 1 or event_day > 30:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 30:
                                break
                        elif event_month == 2:
                            if event_day < 1 or event_day > 29:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 29:
                                break
                    else:
                        if event_month == 1 or event_month == 3 or event_month == 5 or event_month == 7 or event_month == 8 or event_month == 10 or event_month == 12:
                            if event_day < 1 or event_day > 31:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 31:
                                break
                        elif event_month == 4 or event_month == 6 or event_month == 9 or event_month == 11:
                            if event_day < 1 or event_day > 30:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 30:
                                break
                        elif event_month == 2:
                            if event_day < 1 or event_day > 28:
                                print("Enter a valid day!")
                            elif event_day >= 1 or event_day <= 28:
                                break
                        elif event_month == 12:
                            if event_day == 25:
                                print("is Christmas, pls enter a valid day!")
                            elif event_month != 12 or event_day!= 25:
                                break
                        elif event_month == 1:
                            if event_day == 1:
                                print("Enter a valid day!")
                            elif event_month != 1 or event_day != 1:
                                break
                        elif event_month == 7:
                            if event_day == 4:
                                print("enter a valid day!")
                            elif event_month != 7 or event_day != 4:
                                break
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
            elif admin_selection == 4:
                break
            else:
                print()
    elif menu_selection == 2:
        my_avail = schedule_class.availability_mode()
    while 1:
        print("here is all the events on Calendar: \n")
        my_admin.print_all()
        can_come_event_name= input("what event are you going to intend: ")



