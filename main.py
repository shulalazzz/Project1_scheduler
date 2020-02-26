from PyQt5 import uic
import sys
from PyQt5.QtCore import pyqtSignal, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QDialog
from schedule_class import *
import re


class signup_window(QDialog):
    account_signal = pyqtSignal(str)
    password_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.sign = uic.loadUi("sign.ui")
        self.name_arr = []
        self.password_arr = []
        self.sign.pushButton_create.clicked.connect(lambda: self.check_new_account())

    def send_account(self):
        account = self.sign.lineEdit_account.text()
        self.account_signal.emit(account)

    def send_password(self):
        password = self.sign.lineEdit_password.text()
        self.password_signal.emit(password)

    def check_new_account(self):
        read_in_file = open("account.txt", "r")
        name_exit = False

        while 1:
            account = re.findall(r'\w+', read_in_file.readline())

            if (account == []):
                break
            else:
                name = account[0]
                password = account[1]

                if name == []:
                    pass
                else:
                    self.name_arr.append(name)
                if password != []:
                    self.password_arr.append(password)
                else:
                    break

        if len(self.name_arr) == 0:
            if self.sign.lineEdit_account.text() == "":
                QMessageBox.information(self, "Error", "User name cannot be empty!")
            elif self.sign.lineEdit_password.text() == "" and self.sign.lineEdit_rePassword.text() == "":
                QMessageBox.information(self, "Error", "User password cannot be empty!")
            elif self.sign.lineEdit_password.text() != self.sign.lineEdit_rePassword.text():
                QMessageBox.information(self, "Error", "Two passwords are different! Please check it.")
            else:
                get_name_space = False
                get_password_space = False

                for i in range(len(self.sign.lineEdit_account.text())):
                    if self.sign.lineEdit_account.text()[i] == " ":
                        get_name_space = True
                        break

                for i in range(len(self.sign.lineEdit_password.text())):
                    if self.sign.lineEdit_password.text()[i] == " ":
                        get_password_space = True
                        break

                if get_name_space:
                    QMessageBox.information(self, "Error", "User name cannnot have space.")
                elif get_password_space:
                    QMessageBox.information(self, "Error", "Password cannot have space")
                else:
                    add_in_file = open("account.txt", "a")
                    self.name_arr.append(self.sign.lineEdit_account.text())
                    self.password_arr.append(self.sign.lineEdit_password.text())
                    add_in_file.write(
                        self.sign.lineEdit_account.text() + " " + self.sign.lineEdit_password.text() + '\n')
                    add_in_file.close()
                    QMessageBox.information(self, "Congratulation", "Create account success.", QMessageBox.Ok)
                    self.send_account()
                    self.send_password()
        else:
            for i in range(len(self.name_arr)):
                if self.sign.lineEdit_account.text() == self.name_arr[i]:
                    QMessageBox.information(self, "Error", "User name has been created. Please try another one.")
                    name_exit = True
                    break

            if not name_exit:
                if self.sign.lineEdit_account.text() == "":
                    QMessageBox.information(self, "Error", "User name cannot be empty!")
                elif self.sign.lineEdit_password.text() == "" and self.sign.lineEdit_rePassword.text() == "":
                    QMessageBox.information(self, "Error", "User password cannot be empty!")
                elif self.sign.lineEdit_password.text() != self.sign.lineEdit_rePassword.text():
                    QMessageBox.information(self, "Error", "Two passwords are different! Please check it.")
                else:
                    get_name_space = False
                    get_password_space = False

                    for i in range(len(self.sign.lineEdit_account.text())):
                        if self.sign.lineEdit_account.text()[i] == " ":
                            get_name_space = True
                            break

                    for i in range(len(self.sign.lineEdit_password.text())):
                        if self.sign.lineEdit_password.text()[i] == " ":
                            get_password_space = True
                            break

                    if get_name_space:
                        QMessageBox.information(self, "Error", "User name cannnot have space.")
                    elif get_password_space:
                        QMessageBox.information(self, "Error", "Password cannot have space")
                    else:
                        add_in_file = open("account.txt", "a")
                        self.name_arr.append(self.sign.lineEdit_account.text())
                        self.password_arr.append(self.sign.lineEdit_password.text())
                        add_in_file.write(
                            self.sign.lineEdit_account.text() + " " + self.sign.lineEdit_password.text() + '\n')
                        add_in_file.close()
                        reply = QMessageBox.information(self, "Congratulation", "Create account success.",
                                                        QMessageBox.Ok)
                        self.send_account()
                        self.send_password()


class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("login.ui")
        self.total_list = []
        self.read_event_file()
        self.user = user_class()
        self.sign_window = signup_window()
        self.user.account = self.login.lineEdit_account.text()
        self.user.password = self.login.lineEdit_password.text()
        self.name_arr = []
        self.password_arr = []
        self.login.pushButton_signup.clicked.connect(self.open_sign)
        self.login.pushButton_admin.clicked.connect(self.check_account)
        self.login.pushButton_view.clicked.connect(self.check_account_view)

    def read_event_file(self):
        read_file = open("event.txt", "r")

        while 1:
            indiv_user = user_class()
            user_admin = admin_mode()

            try:
                total = re.findall(r'\w+', read_file.readline())

                indiv_user.account = total[0]
                total_index = 1

                if total[total_index] == "Admin":
                    total_index += 1
                else:
                    print("Error")
                    break

                while total[total_index] != "AdminEnd":
                    if total[total_index] == "EventName":
                        total_index += 1
                    else:
                        print("Error")
                        break

                    event_name_in_file = ""
                    while total[total_index] != "EventEnd":
                        partial_name_in_file = total[total_index]

                        if event_name_in_file == "":
                            event_name_in_file = partial_name_in_file
                        else:
                            event_name_in_file = event_name_in_file + " " + partial_name_in_file

                        total_index += 1
                    total_index += 1

                    event_year_in_file = total[total_index]
                    total_index += 1
                    event_month_in_file = total[total_index]
                    total_index += 1
                    event_day_in_file = total[total_index]
                    total_index += 1
                    start_hour_in_file = int(total[total_index])
                    total_index += 1
                    start_minute_in_file = int(total[total_index])
                    total_index += 1
                    end_hour_in_file = int(total[total_index])
                    total_index += 1
                    end_minute_in_file = int(total[total_index])
                    total_index += 1

                    event_time_slot_file = slot(start_hour_in_file, start_minute_in_file, end_hour_in_file,
                                                end_minute_in_file)
                    event_date_file = date(event_year_in_file, event_month_in_file, event_day_in_file,
                                           event_time_slot_file)
                    event_file = event(event_name_in_file, event_date_file)
                    user_admin.add_event(event_file)

                total_index += 1

                if total[total_index] == "View":
                    total_index += 1
                else:
                    print("Error")
                    break

                while total[total_index] != "ViewEnd":
                    events_list_index = total[total_index]
                    total_index += 1
                    outside_index = total[total_index]
                    total_index += 1
                    inside_index = total[total_index]
                    total_index += 1
                    attend_name = total[total_index]
                    total_index += 1

                    print("Length of the attend list: " + str(len(
                        user_admin.events_list[int(events_list_index)].event_date.time_slot.attend_slot[
                            int(outside_index)])))
                    user_admin.events_list[int(events_list_index)].event_date.time_slot.attend_slot[
                        int(outside_index)].append(attend_name)
                    print("Length of the attend list: " + str(len(
                        user_admin.events_list[int(events_list_index)].event_date.time_slot.attend_slot[
                            int(outside_index)])))

                print("indiv_user.account: " + indiv_user.account)
                indiv_user.admin = user_admin

                self.total_list.append(indiv_user)
                print("Add to total_list")
            except:
                print("End of file")
                break

    def set_user_info(self):
        self.user.account = self.login.lineEdit_account.text()
        self.user.password = self.login.lineEdit_password.text()
        print(self.user.account, self.user.password)

    def open_sign(self):
        self.sign_window.sign.show()
        self.sign_window.account_signal.connect(self.get_account)
        self.sign_window.password_signal.connect(self.get_password)

    def get_account(self, connect):
        self.login.lineEdit_account.setText(connect)

    def get_password(self, connect):
        self.login.lineEdit_password.setText(connect)

    # def get_admin_mode(self, connect):
    #     self.user.admin = connect

    def check_account(self):
        read_in_file = open("account.txt", "r")

        while 1:
            account = re.findall(r'\w+', read_in_file.readline())

            if account == []:
                break
            else:
                name = account[0]
                password = account[1]

                if name == []:
                    pass
                else:
                    self.name_arr.append(name)
                if password == []:
                    break
                else:
                    self.password_arr.append(password)

        get_account = False

        for i in range(len(self.name_arr)):
            if self.login.lineEdit_account.text() == self.name_arr[i]:
                get_account = True

                if self.login.lineEdit_password.text() == self.password_arr[i]:
                    self.set_user_info()
                    self.open_admin()
                    break
                else:
                    QMessageBox.information(self, "Error", "Wrong password!")
                    break

        if not get_account:
            QMessageBox.information(self, "Error", "No account with this user name!")

    def check_account_view(self):
        read_in_file = open("account.txt", "r")

        while 1:
            account = re.findall(r'\w+', read_in_file.readline())

            if account == []:
                break
            else:
                name = account[0]
                password = account[1]

                if name == []:
                    pass
                else:
                    self.name_arr.append(name)
                if password == []:
                    break
                else:
                    self.password_arr.append(password)

        get_account = False

        for i in range(len(self.name_arr)):
            if self.login.lineEdit_account.text() == self.name_arr[i]:
                get_account = True

                if self.login.lineEdit_password.text() == self.password_arr[i]:
                    self.set_user_info()
                    self.open_view()
                    break
                else:
                    QMessageBox.information(self, "Error", "Wrong password!")
                    break

        if not get_account:
            QMessageBox.information(self, "Error", "No account with this user name!")

    def open_admin(self):
        self.admin_win = admin_window(self.login.lineEdit_account.text(), self.total_list)
        self.admin_win.admin.show()
        # self.admin_win.admin_signal.connect(self.get_admin_mode)

    def open_view(self):
        self.view_win = view_mode(self.login.lineEdit_account.text(), self.total_list)
        self.view_win.view.show()


class admin_window(QMainWindow):
    admin_signal = pyqtSignal(admin_mode)

    def __init__(self, login_account, pass_list):
        # 从文件中加载UI定义
        super().__init__()
        self.admin = uic.loadUi("admin.ui")
        self.admin.calendarWidget.clicked.connect(self.admin.calendarWidget.showToday)
        self.admin.button_calendar.clicked.connect(lambda: self.set_all_info())
        self.search_account = login_account
        self.admin.label_current_user.setText("Current user is: " + login_account)
        self.admin.label_current_user.adjustSize()
        self.total_user_list = pass_list
        self.admin_mode = admin_mode()
        self.total_user_list_index = -1
        self.admin.pushButton_show_24.clicked.connect(self.print_user_event_24)
        self.admin.pushButton_show_12.clicked.connect(self.print_user_event_12)
        print("Current user is: ", self.search_account)

    def print_user_event_24(self):
        find_search_name = False
        find_index = 0

        for i in range(len(self.total_user_list)):
            if self.total_user_list[i].account == self.search_account:
                find_search_name = True
                find_index = i
                break

        if find_search_name:
            return self.admin.textBrowser.append(self.total_user_list[find_index].admin.info_text_24())
        else:
            return self.admin.textBrowser.append("You haven't created any event.")

    def print_user_event_12(self):
        find_search_name = False
        find_index = 0

        for i in range(len(self.total_user_list)):
            if self.total_user_list[i].account == self.search_account:
                find_search_name = True
                find_index = i
                break

        if find_search_name:
            return self.admin.textBrowser.append(self.total_user_list[find_index].admin.info_text_12())
        else:
            return self.admin.textBrowser.append("You haven't created any event.")

    def write_event_file(self):
        write_file = open("event.txt", "w+")

        print("total_list length: " + str(len(self.total_user_list)))
        for i in range(len(self.total_user_list)):
            write_file.write(self.total_user_list[i].account + " Admin ")

            for j in range(len(self.total_user_list[i].admin.events_list)):
                write_file.write("EventName ")
                write_file.write(self.total_user_list[i].admin.events_list[j].event_name + " ")
                write_file.write("EventEnd ")
                write_file.write(str(self.total_user_list[i].admin.events_list[j].event_date.year) + " " + str(
                    self.total_user_list[i].admin.events_list[j].event_date.month) + " " + str(
                    self.total_user_list[i].admin.events_list[j].event_date.day) + " ")
                write_file.write(
                    str(self.total_user_list[i].admin.events_list[j].event_date.time_slot.start_hour) + " " + str(
                        self.total_user_list[i].admin.events_list[j].event_date.time_slot.start_minute) + " ")
                write_file.write(
                    str(self.total_user_list[i].admin.events_list[j].event_date.time_slot.end_hour) + " " + str(
                        self.total_user_list[i].admin.events_list[j].event_date.time_slot.end_minute) + " ")

            write_file.write("AdminEnd View ")

            for j in range(len(self.total_user_list[i].admin.events_list)):
                for m in range(len(self.total_user_list[i].admin.events_list[j].event_date.time_slot.attend_slot)):
                    if len(self.total_user_list[i].admin.events_list[j].event_date.time_slot.attend_slot[m]) > 0:
                        write_file.write(str(j) + " ")
                        for n in range(
                                len(self.total_user_list[i].admin.events_list[j].event_date.time_slot.attend_slot[m])):
                            write_file.write(str(m) + " " + str(n) + " " + self.total_user_list[i].admin.events_list[
                                j].event_date.time_slot.attend_slot[m][n] + " ")

            write_file.write("ViewEnd\n")

        write_file.close()
        print("Rewrite finish")

    def check_valid_info(self, year, month_, date_, start_hour_, start_min_, end_hour_, end_min_):
        if year < 0:
            return "Invalid year!"
        if month_ == 12 and date_ == 25:
            return "Invalid date! Dec. 25th"
        if month_ == 1 and date_ == 1:
            return "Invalid date! Jan. 1st"
        if month_ == 7 and date_ == 4:
            return "Invalid date! July 4th"

        beginning = int(3 * start_hour_ + start_min_ / 20)
        end = int(3 * end_hour_ + end_min_ / 20)

        if beginning < 14 and beginning >= 0:
            return "Can't meet between 0:00 am to 5:00 am"
        if beginning >= 35 and beginning < 38:
            return "Can't meet between 12:00 pm to 1:00 pm"
        if end > 36 and end < 38:
            return "Can't meet between 12:00 pm to 1:00 pm"
        if beginning < 35 and end > 38:
            return "Can't meet between 12:00 pm to 1:00 pm"
        if end <= beginning:
            return "End time can't earlier than beginning time"

        return "True"

    def set_all_info(self):
        start_hour = self.admin.timeEdit_start.time().hour()
        start_min = self.admin.timeEdit_start.time().minute()
        end_hour = self.admin.timeEdit_end.time().hour()
        end_min = self.admin.timeEdit_end.time().minute()
        timeslot_ = slot(start_hour, start_min, end_hour, end_min)
        temp_date = self.admin.calendarWidget.selectedDate()
        date_string = str(temp_date.toPyDate())
        temp = re.findall(r'\d+', date_string)
        _date = list(map(int, temp))
        year = _date[0]
        month = _date[1]
        day = _date[2]

        is_valid = self.check_valid_info(year, month, day, start_hour, start_min, end_hour, end_min)

        if is_valid == "True":
            date_obj = date(year, month, day, timeslot_)
            event_name = self.admin.lineEdit_eventname.text()
            event_obj = event(event_name, date_obj)
            mode = admin_mode()
            mode.add_event(event_obj)

            if event_name == "":
                QMessageBox.about(self.admin, "Error", "Event name can't be empty.")
            else:
                confirm = QMessageBox.question(self.admin, 'Message',
                                               'Confirm adding this event \n{}'.format(event_name),
                                               QMessageBox.Yes | QMessageBox.No)
                if confirm == QMessageBox.Yes:
                    self.admin_mode = mode

                    for i in range(len(self.total_user_list)):
                        if self.total_user_list[i].account == self.search_account:
                            self.total_user_list_index = i
                            break

                    if self.total_user_list_index == -1:
                        event_name_exist_in_total = False

                        for i in range(len(self.total_user_list)):
                            for j in range(len(self.total_user_list[i].admin.events_list)):
                                if self.total_user_list[i].admin.events_list[j].event_name == \
                                        self.admin_mode.events_list[0].event_name:
                                    event_name_exist_in_total = True
                                    break

                        if event_name_exist_in_total:
                            QMessageBox.about(self.admin, "Message",
                                              "This event name is existed. Please try another one.")
                        else:
                            user_temp = user_class()

                            admin_temp = self.admin_mode

                            user_temp.account = self.search_account
                            user_temp.admin = admin_temp

                            self.total_user_list.append(user_temp)
                            self.write_event_file()
                            self.admin.textBrowser.append(self.admin_mode.info_text_24())
                            # self.send_admin_mode()
                    else:
                        event_name_exit = False
                        for i in range(len(self.total_user_list[self.total_user_list_index].admin.events_list)):
                            print(self.total_user_list[self.total_user_list_index].admin.events_list[i].event_name)
                            if event_name == self.total_user_list[self.total_user_list_index].admin.events_list[
                                i].event_name:
                                self.admin.textBrowser.append("Event existed")
                                event_name_exit = True
                                break

                        if not event_name_exit:
                            event_name_exist_in_total = False

                            for i in range(len(self.total_user_list)):
                                for j in range(len(self.total_user_list[i].admin.events_list)):
                                    if self.total_user_list[i].admin.events_list[j].event_name == \
                                            self.admin_mode.events_list[0].event_name:
                                        event_name_exist_in_total = True
                                        break

                            if event_name_exist_in_total:
                                QMessageBox.about(self.admin, "Message",
                                                  "This event name is existed. Please try another one.")
                            else:
                                year_temp = self.admin_mode.events_list[0].event_date.year
                                month_temp = self.admin_mode.events_list[0].event_date.month
                                day_temp = self.admin_mode.events_list[0].event_date.day
                                start_hour_temp = self.admin_mode.events_list[0].event_date.time_slot.start_hour
                                start_min_temp = self.admin_mode.events_list[0].event_date.time_slot.start_minute
                                end_hour_temp = self.admin_mode.events_list[0].event_date.time_slot.end_hour
                                end_min_temp = self.admin_mode.events_list[0].event_date.time_slot.end_minute

                                self.total_user_list[self.total_user_list_index].admin.events_list.append(event_obj)
                                self.write_event_file()
                                self.admin.textBrowser.append(self.admin_mode.info_text_24())

                                # if self.total_user_list[self.total_user_list_index].admin.checkevent_date(year_temp, month_temp, day_temp, start_hour_temp, start_min_temp, end_hour_temp, end_min_temp):
                                #     self.total_user_list[self.total_user_list_index].admin.events_list.append(event_obj)
                                #     self.write_event_file()
                                #     self.admin.textBrowser.append(self.admin_mode.info_text_24())
                                #     # self.send_admin_mode()
                                # else:
                                #     QMessageBox.about(self.admin, "Message", "Time slot occupied!")
                                #     pass
                        else:
                            QMessageBox.about(self.admin, "Message", "You have created this event.")
                else:
                    QMessageBox.about(self.admin, 'Message', 'Canceled')
        else:
            QMessageBox.about(self.admin, "Message", is_valid)

    # def send_admin_mode(self):
    #     print("send admin")
    #     send_mode = self.admin_mode
    #     self.admin_signal.emit(send_mode)

    def write_username(self):
        add_username = open("event.txt", 'a')
        add_username.write(str(self.search_account) + '\n')


class view_mode(QMainWindow):
    def __init__(self, login_account, pass_list):
        # 从文件中加载UI定义
        super().__init__()
        self.view = uic.loadUi("view2.ui")
        self.total_user_view_list = pass_list
        self.total_user_view_list_index = -1
        self.view_event_list = []
        self.search_account = login_account
        self.view.show_events.clicked.connect(self.read_events)
        self.view.arrow.clicked.connect(lambda: self.set_all_info())
        self.view.viewEnd.clicked.connect(lambda: self.view_End())

    def read_events(self):
        for i in range(len(self.total_user_view_list)):
            for j in range(len(self.total_user_view_list[i].admin.events_list)):
                start_hour = self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.start_hour
                start_minute = self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.start_minute
                end_hour = self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.end_hour
                end_minutes = self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.end_minute
                year = self.total_user_view_list[i].admin.events_list[j].event_date.year
                month = self.total_user_view_list[i].admin.events_list[j].event_date.month
                day = self.total_user_view_list[i].admin.events_list[j].event_date.day
                event_name = self.total_user_view_list[i].admin.events_list[j].event_name
                host = self.total_user_view_list[i].account

                self.view.listWidget.addItem(
                    "Event name: " + event_name + '\n' + "Date: " + str(year) + "-" + str(month) + "-" + str(
                        day) + '\n' + "Time: " + str(start_hour) + ":" + str(start_minute) + " - " + str(
                        end_hour) + ":" + str(end_minutes) + '\n' + "Host: " + host + '\n')
                self.view.verticalLayout.addWidget(self.view.listWidget)

        self.view.listWidget.itemSelectionChanged.connect(self.selectionChanged)
        self.view.verticalLayout.addWidget(self.view.listWidget)

    def selectionChanged(self):
        text_length = len(self.view.listWidget.currentItem().text().split())
        print("text_length: " + str(text_length))

        full_event_name = ""
        for i in range(2, text_length - 8):
            if full_event_name == "":
                full_event_name = self.view.listWidget.currentItem().text().split()[i]
            else:
                full_event_name += " " + self.view.listWidget.currentItem().text().split()[i]

        print(self.view.listWidget.currentItem().text().split()[0] + " " +
              self.view.listWidget.currentItem().text().split()[1] + " " + full_event_name)
        print(self.view.listWidget.currentItem().text().split()[text_length - 8] + " " +
              self.view.listWidget.currentItem().text().split()[text_length - 7])
        print(self.view.listWidget.currentItem().text().split()[text_length - 6] + " " +
              self.view.listWidget.currentItem().text().split()[text_length - 5] +
              self.view.listWidget.currentItem().text().split()[text_length - 4] +
              self.view.listWidget.currentItem().text().split()[text_length - 3])
        print(self.view.listWidget.currentItem().text().split()[text_length - 2] + " " +
              self.view.listWidget.currentItem().text().split()[text_length - 1] + '\n')

    def set_all_info(self):
        start_hour = self.view.start_time.time().hour()
        start_min = self.view.start_time.time().minute()
        end_hour = self.view.end_time.time().hour()
        end_min = self.view.end_time.time().minute()

        beginning = int(3 * start_hour + start_min / 20)
        end = int(3 * end_hour + end_min / 20)

        if end <= beginning:
            QMessageBox.about(self.view, "Error", "End time can't earlier than beginning time.")
        else:
            print("Start time: " + str(start_hour) + ":" + str(start_min) + '\n' + "End time: " + str(
                end_hour) + ":" + str(end_min) + '\n')

            try:
                event_name = self.view.listWidget.currentItem().text().split()[2]

                if len(self.view_event_list) != 0:
                    QMessageBox.about(self.view, "Message", "You have added an event. Please click finish add.")
                else:
                    confirm = QMessageBox.question(self.view, 'Message',
                                                   'Confirm adding this event \n{}'.format(event_name),
                                                   QMessageBox.Yes | QMessageBox.No)

                    if confirm == QMessageBox.Yes:
                        text_length = len(self.view.listWidget.currentItem().text().split())
                        print("text length: " + str(text_length))
                        # for i in range(len(self.view.listWidget.currentItem().text())):
                        #     print(self.view.listWidget.currentItem().test().split()[i])
                        # pass

                        num = re.findall('\w+', self.view.listWidget.currentItem().text().split()[text_length - 7])
                        cur_year = num[0]
                        cur_month = num[1]
                        cur_day = num[2]

                        num = re.findall('\w+', self.view.listWidget.currentItem().text().split()[text_length - 5])
                        cur_start_hour = num[0]
                        cur_start_minute = num[1]

                        num = re.findall('\w+', self.view.listWidget.currentItem().text().split()[text_length - 3])
                        cur_end_hour = num[0]
                        cur_end_minute = num[1]

                        print("Year: " + cur_year + "\nMonth: " + cur_month + "\nDay: " + cur_day)
                        print("Start time: " + cur_start_hour + ":" + cur_start_minute)
                        print("End time: " + cur_end_hour + ":" + cur_end_minute + '\n')

                        event_time_slot_temp = slot(start_hour, start_min, end_hour, end_min)
                        event_date_temp = date(int(cur_year), int(cur_month), int(cur_day), event_time_slot_temp)
                        event_temp = event(event_name, event_date_temp)

                        self.view_event_list.append(event_temp)
                        print("Total length of view_event_list: " + str(len(self.view_event_list)) + '\n')

                        self.view.textBrowser.append("Event name:" + event_name)
                        self.view.textBrowser.append(
                            "Time slot you participated: " + str(start_hour) + ":" + str(start_min) + "-" + str(
                                end_hour) + ":" + str(end_min) + '\n')
                    else:
                        QMessageBox.about(self.view, 'Message', 'Canceled')
            except:
                QMessageBox.information(self.view, "Error",
                                        "Please click one event which you want to attend, then click the red arrow.")

    def view_End(self):
        reply = QMessageBox.question(self.view, "Message", "You want to attend above event.",
                                     QMessageBox.Yes | QMessageBox.No)

        if reply == QMessageBox.Yes:
            if len(self.view_event_list) == 0:
                QMessageBox.about(self.view, 'Error', "You don't select any event.")
            else:
                print("Length of view_event_list: " + str(len(self.view_event_list)))

                for i in range(len(self.view_event_list)):
                    view_event_name = self.view_event_list[i].event_name

                    for j in range(len(self.total_user_view_list)):
                        exit_attend = False

                        for k in range(len(self.total_user_view_list[j].admin.events_list)):
                            if view_event_name == self.total_user_view_list[j].admin.events_list[k].event_name:
                                view_event_creator = self.total_user_view_list[j].account

                                if view_event_creator == self.search_account:
                                    QMessageBox.about(self.view, "Error",
                                                      "Can't attent " + view_event_name + " which is created by you.")
                                    exit_attend = True
                                    break
                                else:
                                    start_hour_temp = self.view_event_list[i].event_date.time_slot.start_hour
                                    start_min_temp = self.view_event_list[i].event_date.time_slot.start_minute
                                    end_hour_temp = self.view_event_list[i].event_date.time_slot.end_hour
                                    end_min_temp = self.view_event_list[i].event_date.time_slot.end_minute

                                    self.total_user_view_list[j].admin.events_list[
                                        k].event_date.time_slot.fill_attend_slot(start_hour_temp, start_min_temp,
                                                                                 end_hour_temp, end_min_temp,
                                                                                 self.search_account)

                                    if not self.total_user_view_list[j].admin.events_list[
                                        k].event_date.time_slot.check_event_attend:
                                        QMessageBox.about(self.view, "Error",
                                                          "Your chosen participation time is not in the event time")
                                        exit_attend = True
                                        break
                                    else:
                                        QMessageBox.about(self.view, "Message",
                                                          "Successfully attend " + view_event_name + ".")
                                        exit_attend = True
                                        break

                                    # print(len(self.total_user_view_list[j].admin.events_list[k].event_date.time_slot.attend_slot))
                                    # print(len(self.total_user_view_list[j].admin.events_list[k].event_date.time_slot.attend_slot[0]))
                                    # for m in range(len(self.total_user_view_list[j].admin.events_list[k].event_date.time_slot.attend_slot)):
                                    #     for n in range(len(self.total_user_view_list[j].admin.events_list[k].event_date.time_slot.attend_slot[m])):
                                    #         print("m: " + str(m) + " n: " + str(n) + " " + self.total_user_view_list[j].admin.events_list[k].event_date.time_slot.attend_slot[m][n])
                        if exit_attend:
                            break

                self.view_event_list = []
                write_file = open("event.txt", "w+")

                for i in range(len(self.total_user_view_list)):
                    write_file.write(self.total_user_view_list[i].account + " Admin ")

                    for j in range(len(self.total_user_view_list[i].admin.events_list)):
                        write_file.write("EventName ")
                        write_file.write(self.total_user_view_list[i].admin.events_list[j].event_name + " ")
                        write_file.write("EventEnd ")
                        write_file.write(
                            str(self.total_user_view_list[i].admin.events_list[j].event_date.year) + " " + str(
                                self.total_user_view_list[i].admin.events_list[j].event_date.month) + " " + str(
                                self.total_user_view_list[i].admin.events_list[j].event_date.day) + " ")
                        write_file.write(str(self.total_user_view_list[i].admin.events_list[
                                                 j].event_date.time_slot.start_hour) + " " + str(
                            self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.start_minute) + " ")
                        write_file.write(str(self.total_user_view_list[i].admin.events_list[
                                                 j].event_date.time_slot.end_hour) + " " + str(
                            self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.end_minute) + " ")

                    write_file.write("AdminEnd View ")

                    for j in range(len(self.total_user_view_list[i].admin.events_list)):
                        for m in range(len(
                                self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.attend_slot)):
                            if len(self.total_user_view_list[i].admin.events_list[j].event_date.time_slot.attend_slot[
                                       m]) > 0:
                                write_file.write(str(j) + " ")
                                for n in range(len(self.total_user_view_list[i].admin.events_list[
                                                       j].event_date.time_slot.attend_slot[m])):
                                    write_file.write(str(m) + " " + str(n) + " " +
                                                     self.total_user_view_list[i].admin.events_list[
                                                         j].event_date.time_slot.attend_slot[m][n] + " ")

                    write_file.write("ViewEnd\n")
                write_file.close()
        else:
            QMessageBox.about(self.view, 'Message', 'Canceled')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = login_window()
    login.login.show()
    sys.exit(app.exec_())
