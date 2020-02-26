class user_class:
    def __init__(self):
        self.account = ""
        self.password = ""
        self.admin = admin_mode


class admin_mode:
    def __init__(self):
        self.events_list = []

    def checkevent_date(self, year, month, day, start_hour, start_minute, end_hour, end_minute):
        for i in range(len(self.events_list)):
            if year == self.events_list[i].event_date.year and month == self.events_list[i].event_date.month and day == self.events_list[i].event_date.day:
                if not self.events_list[i].event_date.time_slot.checktime_day(start_hour, start_minute, end_hour,
                                                                              end_minute):
                    return False
        return True

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

    def info_text_24(self):
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
            for j in range(len(self.events_list[i].event_date.time_slot.time_slot)):
                if self.events_list[i].event_date.time_slot.time_slot[j] == 1:
                    name_string = ' '
                    if len(self.events_list[i].event_date.time_slot.attend_slot[j]) > 0:
                        for k in range(len(self.events_list[i].event_date.time_slot.attend_slot[j])):
                            name_string += (self.events_list[i].event_date.time_slot.attend_slot[j][k] + ' ')
                    current_time = j * 20
                    current_hour = int(current_time / 60)
                    current_minute = current_time % 60
                    if current_minute == 0:
                        all_text += str("{}:00-{}:{}".format(current_hour, current_hour,
                                                             current_minute + 20)) + " " + name_string + '\n'
                    elif current_minute == 40:
                        all_text += str("{}:{}-{}:00".format(current_hour, current_minute,
                                                             current_hour + 1)) + " " + name_string + '\n'
                    else:
                        all_text += str("{}:{}-{}:{}".format(current_hour, current_minute, current_hour,
                                                             current_minute + 20)) + " " + name_string + '\n'
        return all_text

    def info_text_12(self):
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
            for j in range(0, 35):
                if self.events_list[i].event_date.time_slot.time_slot[j] == 1:
                    name_string = ' '
                    if len(self.events_list[i].event_date.time_slot.attend_slot[j]) > 0:
                        for k in range(len(self.events_list[i].event_date.time_slot.attend_slot[j])):
                            name_string += (self.events_list[i].event_date.time_slot.attend_slot[j][k] + ' ')
                    current_time = j * 20
                    current_hour = int(current_time / 60)
                    current_minute = current_time % 60
                    if current_minute == 0:
                        all_text += str("{}:00 am-{}:{} am".format(current_hour,
                                                                   current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'
                    elif current_minute == 40:
                        all_text += str("{}:{} am-{}:00 am".format(current_hour,
                                                                   current_minute,
                                                                   current_hour + 1)) + " " + name_string + '\n'
                    else:
                        all_text += str("{}:{} am-{}:{} am".format(current_hour,
                                                                   current_minute, current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'
            if self.events_list[i].event_date.time_slot.time_slot[35] == 1:
                name_string = ' '
                if len(self.events_list[i].event_date.time_slot.attend_slot[35]) > 0:
                    for k in range(len(self.events_list[i].event_date.time_slot.attend_slot[j])):
                        name_string += (self.events_list[i].event_date.time_slot.attend_slot[j][k] + ' ')
                all_text += str("11:40 am-12:00 pm") + " " + name_string + '\n'
            for j in range(36, 39):
                if self.events_list[i].event_date.time_slot.time_slot[j] == 1:
                    name_string = ' '
                    if len(self.events_list[i].event_date.time_slot.attend_slot[j]) > 0:
                        for k in range(len(self.events_list[i].event_date.time_slot.attend_slot[j])):
                            name_string += (self.events_list[i].event_date.time_slot.attend_slot[j][k] + ' ')
                    current_time = j * 20
                    current_hour = int(current_time / 60)
                    current_minute = current_time % 60
                    if current_minute == 0:
                        all_text += str("{}:00 pm-{}:{} pm".format(current_hour,
                                                                   current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'
                    elif current_minute == 40:
                        all_text += str("{}:{} pm-{}:00 pm".format(current_hour,
                                                                   current_minute,
                                                                   current_hour + 1)) + " " + name_string + '\n'
                    else:
                        all_text += str("{}:{} pm-{}:{} pm".format(current_hour,
                                                                   current_minute, current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'

            for j in range(39, 72):
                if self.events_list[i].event_date.time_slot.time_slot[j] == 1:
                    name_string = ' '
                    if len(self.events_list[i].event_date.time_slot.attend_slot[j]) > 0:
                        for k in range(len(self.events_list[i].event_date.time_slot.attend_slot[j])):
                            name_string += (self.events_list[i].event_date.time_slot.attend_slot[j][k] + ' ')
                    current_time = j * 20
                    current_hour = int(current_time / 60) - 12
                    current_minute = current_time % 60
                    if current_minute == 0:
                        all_text += str("{}:00 pm-{}:{} pm".format(current_hour,
                                                                   current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'
                    elif current_minute == 40:
                        all_text += str("{}:{} pm-{}:00 pm".format(current_hour,
                                                                   current_minute,
                                                                   current_hour + 1)) + " " + name_string + '\n'
                    else:
                        all_text += str("{}:{} pm-{}:{} pm".format(current_hour,
                                                                   current_minute, current_hour,
                                                                   current_minute + 20)) + " " + name_string + '\n'

        return all_text


class event:
    def __init__(self, event_name, event_date):
        self.event_name = event_name
        self.event_date = event_date

    def set_event_name(self, name):
        self.event_name = name

    def print_event(self):
        print("Event name: " + self.event_name)
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

    def compare_date(self, current_year, current_month, current_day):
        if self.year == current_year and self.month == current_month and self.day == current_day:
            return False
        else:
            return True


class slot:
    def __init__(self, start_hour, start_minute, end_hour, end_minute):
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.time_slot = [0] * 72
        self.fill_slot()
        self.attend_slot = []
        for i in range(72):
            self.attend_slot.append([])
        self.check_event_attend = False

    def fill_slot(self):
        beginning = int(3 * self.start_hour + self.start_minute / 20)
        end = int(3 * self.end_hour + self.end_minute / 20)
        for i in range(beginning, end):
            self.time_slot[i] = 1

    def fill_attend_slot(self, start_hour, start_minute, end_hour, end_minute, account):
        beginning = int(3 * start_hour + start_minute / 20)
        end = int(3 * end_hour + end_minute / 20)
        print("from fill attend,", beginning, end)
        valid_time = True
        for i in range(beginning, end):
            if self.time_slot[i] == 0:
                print("Time slot error")
                valid_time = False
                break
        if valid_time:
            for i in range(beginning, end):
                if account in self.attend_slot[i]:
                    print("Have attended")
                else:
                    self.attend_slot[i].append(account)

            self.check_event_attend = True
            print("Add success")

    def pure_attend_slot(self, start_hour, start_minute, end_hour, end_minute, account):
        beginning = int(3 * start_hour + start_minute / 20)
        end = int(3 * end_hour + end_minute / 20)
        for i in range(beginning, end):
            self.attend_slot[i].append(account)

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
        if self.start_minute == 0:
            print("Beginning time: {}:00".format(self.start_hour))
        else:
            print("Beginning time: {}:{}".format(
                self.start_hour, self.start_minute))
        if self.end_minute == 0:
            print("End time: {}:00".format(self.end_hour))
        else:
            print("End time: {}:{}".format(self.end_hour, self.end_minute))

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

    def checktime_day(self, start_hour, start_minute, end_hour, end_minute):
        beginning = int(3 * start_hour + start_minute / 20)
        end = int(3 * end_hour + end_minute / 20)
        for i in range(beginning, end):
            if self.time_slot[i] == 1:
                return False
        return True
