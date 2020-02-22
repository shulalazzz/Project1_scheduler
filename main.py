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
                add_in_file = open("account.txt", "a")
                self.name_arr.append(self.sign.lineEdit_account.text())
                self.password_arr.append(self.sign.lineEdit_password.text())
                add_in_file.write(self.sign.lineEdit_account.text() + " " + self.sign.lineEdit_password.text() + '\n')
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
                    add_in_file = open("account.txt", "a")
                    self.name_arr.append(self.sign.lineEdit_account.text())
                    self.password_arr.append(self.sign.lineEdit_password.text())
                    add_in_file.write(self.sign.lineEdit_account.text() + " " + self.sign.lineEdit_password.text() + '\n')
                    add_in_file.close()
                    reply = QMessageBox.information(self, "Congratulation", "Create account success.", QMessageBox.Ok)
                    self.send_account()
                    self.send_password()

class login_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("login.ui")
        self.user = user_class()
        self.sign_window = signup_window()
        self.user.account = self.login.lineEdit_account.text()
        self.user.password = self.login.lineEdit_password.text()
        self.name_arr = []
        self.password_arr = []
        self.login.pushButton_signup.clicked.connect(self.open_sign)
        self.login.pushButton_admin.clicked.connect(self.check_account_admin)
        self.login.pushButton_view.clicked.connect(self.check_account_view)
        
    def set_user_info(self):
        self.user.account = self.login.lineEdit_account.text()
        print("Set account name")
        self.user.password = self.login.lineEdit_password.text()
        print("Set password")
        print(self.user.account, self.user.password)

    def open_sign(self):
        self.sign_window.sign.show()
        self.sign_window.account_signal.connect(self.get_account)
        self.sign_window.password_signal.connect(self.get_password)

    def get_account(self, connect):
        self.login.lineEdit_account.setText(connect)

    def get_password(self, connect):
        self.login.lineEdit_password.setText(connect)

    def get_admin_mode(self, connect):
        self.user.admin = connect
        self.user.admin.print_all()

    def check_account_admin(self):
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
        self.admin_win = admin_window(self.login.lineEdit_account.text())
        self.admin_win.admin.show()
        self.admin_win.admin_signal.connect(self.get_admin_mode)

    def open_view(self):
        self.view_win = view_mode(self.login.lineEdit_account.text())
        self.view_win.view.show()
    
class admin_window(QMainWindow):
    admin_signal = pyqtSignal(admin_mode)

    def __init__(self, login_account):
        # 从文件中加载UI定义
        super().__init__()
        self.admin = uic.loadUi("admin.ui")
        self.admin.calendarWidget.clicked.connect(
            self.admin.calendarWidget.showToday)
        self.admin.button_calendar.clicked.connect(lambda: self.set_all_info())
        self.search_account = login_account
        self.admin_mode = admin_mode()
        print("Current user is: ", self.search_account)

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
        date_obj = date(year, month, day, timeslot_)
        event_name = self.admin.lineEdit_eventname.text()
        event_obj = event(event_name, date_obj)
        mode = admin_mode()
        mode.add_event(event_obj)
        confirm = QMessageBox.question(self.admin, 'Message', 'Confirm adding this event \n{}'.format(
            event_name), QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.admin_mode = mode
            self.admin_mode.print_all()
            self.admin.textBrowser.append(self.admin_mode.info_text())
            self.send_admin_mode()
        else:
            QMessageBox.about(self.admin, 'Message', 'Canceled')

    def send_admin_mode(self):
        print("send admin")
        send_mode = self.admin_mode
        self.admin_signal.emit(send_mode)

class view_mode(QMainWindow):
    def __init__(self,login_account):
        # 从文件中加载UI定义
        super().__init__()
        self.view = uic.loadUi("view2.ui")
        self.search_account = login_account
        self.view.show_events.clicked.connect(self.read_events)
    def get_time(self):
        start_hour = self.view.timeEdit_start.time().hour()
        start_min = self.view.timeEdit_start.time().minute()
        end_hour = self.view.timeEdit_end.time().hour()
        end_min = self.view.timeEdit_end.time().minute()
        print("start time is {}:{}, end time is {}:{}".format(start_hour, start_min, end_hour, end_min))

    def read_events(self):
        read_events = open("event.txt", "r")
        # read_events.readline()
        while 1:
            try:
                rec = re.findall(r'\w+', read_events.readline())
                start_hour = rec[0]
                start_minute = rec[1]
                end_hour = rec[2]
                end_minutes = rec[3]
                year = rec[4]
                month = rec[5]
                day = rec[6]
                event_name = rec[7]
                self.view.text.append("Event name:" + event_name)
                self.view.text.append("Date: " + year + "-" + month + "-" + day)
                self.view.text.append("Time: "+ start_hour +":"+start_minute+" - "+end_hour+":"+end_minutes)
                self.view.text.append('\n')
            except:
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = login_window()
    login.login.show()
    sys.exit(app.exec_())
