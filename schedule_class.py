class admin_mode:
    def __init__(self):
        self.__events_list = []
        self.creator_name = ""

    def set_name(self, creator_name):
        self.creator_name = creator_name

    def add_event(self, single_event):
        self.__events_list.append(single_event)

    def print_all(self):
        print("Creator of events:", self.creator_name)
        for i in range(len(self.__events_list)):
            self.__events_list[i].print_event()

    def print_event_name(self):
        for i in range(len(self.__events_list)):
            self.__events_list[i].print_event_name()


class event:
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date

    def print_event(self):
        print(self.event_name)
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

    def convert_time(self):
        for i in range(len(self.time_slot)):
            if self.time_slot[i] == 1:
                current_time = i * 20
                current_hour = int(current_time/60)
                current_minute = current_time % 60
                if current_minute == 0:
                    print("{}:00-{}:{}".format(current_hour,
                                               current_hour, current_minute + 20))
                elif current_minute == 40:
                    print("{}:{}-{}:00".format(current_hour,
                                               current_minute, current_hour+1))
                else:
                    print("{}:{}-{}:{}".format(current_hour,
                                               current_minute, current_hour, current_minute + 20))

    def print_time(self):
        if self.start_minute == 0:
            print("Beginning time: {}:00".format(self.start_hour))
        else:
            print("Beginning time: {}:{}".format(
                self.start_hour, self.start_minute))
        if self.end_minute == 0:
            print("End time: {}:00".format(self.end_hour))
        else:
            print("End time: {}:{}".format(self.end_hour, self.end_minute))


class availability:
    def __init__(self):
        self.users_list = []

    def add_user(self, the_user):
        self.users_list.append(the_user)


class user:
    def __init__(self, name, start_hour, start_minute, end_hour, end_minute):
        self.name = name
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.time_slot = [0] * 72
