class user_class:
    def __init__(self):
        self.account = ""
        self.password = ""
        self.admin = admin_mode
        self.attend = attend_mode


class admin_mode:
    def __init__(self):
        self.events_list = []
        self.creator_name = ""

    def set_name(self, creator_name):
        self.creator_name = creator_name

    def add_event(self, single_event):
        self.events_list.append(single_event)

    def print_all(self):
        for i in range(len(self.events_list)):
            self.events_list[i].print_event()

    def print_event_name(self):
        for i in range(len(self.events_list)):
            self.events_list[i].print_event_name()

    def check_exist(self, event_name):
        for i in range(len(self.events_list)):
            if self.events_list[i].event_name == event_name:
                return True
        return False

    def find_event(self, event_name):
        for i in range(len(self.events_list)):
            if self.events_list[i].event_name == event_name:
                return self.events_list[i]

    def info_text(self):
        all_text = ''
        for i in range(len(self.events_list)):
            all_text += self.events_list[i].event_name
            all_text += '\n'
            all_text += str(self.events_list[i].event_date.month)
            all_text += ' '
            all_text += str(self.events_list[i].event_date.day)
            all_text += ' '
            all_text += str(self.events_list[i].event_date.year)
            all_text += '(mm\dd\yyyy)\n'

        return all_text


class event:
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date

    def set_event_name(self, name):
        self.event_name = name

    def print_event(self):
        print("Event name: " + self.event_name)
        add_events = open("event.txt", "a")
        add_events.write("%s\r\n" % self.event_name)
        self.event_date.print_date()

    def print_event_name(self):
        print(self.event_name)


class date:
    def __init__(self, year, month, day, time_slot):
        self.year = year
        self.month = month
        self.day = day
        self.time_slot = time_slot

    def print_date(self):
        print(self.month, self.day, self.year)
        add_events = open("event.txt", "a")
        add_events.write(str(self.year) + " ")
        add_events.write(str(self.month) + " ")
        add_events.write(str(self.day) + " ")
        self.time_slot.print_time()


class slot:
    def __init__(self, start_hour, start_minute, end_hour, end_minute):
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.time_slot = [0] * 72
        self.fill_slot()

    def fill_slot(self):
        beginning = int(3 * self.start_hour + self.start_minute / 20)
        end = int(3 * self.end_hour + self.end_minute / 20)
        for i in range(beginning, end):
            self.time_slot[i] = 1

    def print_slot(self):
        for i in range(len(self.time_slot)):
            if self.time_slot[i] == 1:
                print(i)

    def convert_time_24(self):
        for i in range(len(self.time_slot)):
            if self.time_slot[i] == 1:
                current_time = i * 20
                current_hour = int(current_time / 60)
                current_minute = current_time % 60
                if current_minute == 0:
                    print("{}:00-{}:{}".format(current_hour,
                                               current_hour, current_minute + 20))
                elif current_minute == 40:
                    print("{}:{}-{}:00".format(current_hour,
                                               current_minute, current_hour + 1))
                else:
                    print("{}:{}-{}:{}".format(current_hour,
                                               current_minute, current_hour, current_minute + 20))

    def convert_time_12(self):
        for i in range(0, 35):
            if self.time_slot[i] == 1:
                current_time = i * 20
                current_hour = int(current_time / 60)
                current_minute = current_time % 60
                if current_minute == 0:
                    print("{}:00 am-{}:{} am".format(current_hour,
                                                     current_hour, current_minute + 20))
                elif current_minute == 40:
                    print("{}:{} am-{}:00 am".format(current_hour,
                                                     current_minute, current_hour + 1))
                else:
                    print("{}:{} am-{}:{} am".format(current_hour,
                                                     current_minute, current_hour, current_minute + 20))
        if self.time_slot[35] == 1:
            print("11:40 am-12:00 pm")
        for i in range(36, 39):
            current_time = i * 20
            current_hour = int(current_time / 60)
            current_minute = current_time % 60
            if current_minute == 0:
                print("{}:00 pm-{}:{} pm".format(current_hour,
                                                 current_hour, current_minute + 20))
            elif current_minute == 40:
                print("{}:{} pm-{}:00 pm".format(current_hour,
                                                 current_minute, current_hour + 1))
            else:
                print("{}:{} pm-{}:{} pm".format(current_hour,
                                                 current_minute, current_hour, current_minute + 20))

        for i in range(39, 72):
            if self.time_slot[i] == 1:
                current_time = i * 20
                current_hour = int(current_time / 60) - 12
                current_minute = current_time % 60
                if current_minute == 0:
                    print("{}:00 pm-{}:{} pm".format(current_hour,
                                                     current_hour, current_minute + 20))
                elif current_minute == 40:
                    print("{}:{} pm-{}:00 pm".format(current_hour,
                                                     current_minute, current_hour + 1))
                else:
                    print("{}:{} pm-{}:{} pm".format(current_hour,
                                                     current_minute, current_hour, current_minute + 20))

    def print_time(self):
        add_events = open("event.txt", "a")
        if self.start_minute == 0:
            print("Beginning time: {}:00".format(self.start_hour))
            add_events.write(str(self.start_hour) + " 00 ")
        else:
            print("Beginning time: {}:{}".format(
                self.start_hour, self.start_minute))
            add_events.write(str(self.start_hour) + " " + str(self.start_minutes) + " ")
        if self.end_minute == 0:
            print("End time: {}:00".format(self.end_hour))
            add_events.write(str(self.end_hour) + " 00 ")
        else:
            print("End time: {}:{}".format(self.end_hour, self.end_minute))
            add_events.write(str(self.end_hour) + " " + str(self.end_minutes) + " ")

    def compare_time_slot(self, start_hour, start_minute, end_hour, end_minute):
        is_occupied = False
        beginning = int(3 * start_hour + start_minute / 20)
        end = int(3 * end_hour + end_minute / 20)
        for i in range(beginning, end):
            if self.time_slot[i] == 1:
                is_occupied = True
                current_time = i * 20
                current_hour = int(current_time / 60)
                current_minute = current_time % 60
                if current_minute == 0:
                    print("{}:00-{}:{} occupied".format(current_hour,
                                                        current_hour, current_minute + 20))
                elif current_minute == 40:
                    print("{}:{}-{}:00 occupied".format(current_hour,
                                                        current_minute, current_hour + 1))
                else:
                    print(
                        "{}:{}-{}:{} occupied".format(current_hour, current_minute, current_hour, current_minute + 20))
        if not is_occupied:
            for i in range(beginning, end):
                self.time_slot[i] = 1
        else:
            print("Nothing is added.")


class attend_mode:
    def __init__(self):
        self.event_list = []

    def add_event(self, the_event):
        self.event_list.append(the_event)
