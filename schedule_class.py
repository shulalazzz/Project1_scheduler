class admin_mode:
    def __init__(self, creator_name):
        self.creator_name = creator_name
        self.__events_list = []

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

    def print_time(self):
        print("Beginning time: ", self.start_hour, ":", self.start_minute)
        print("End time: ", self.end_hour, ":", self.end_minute)
