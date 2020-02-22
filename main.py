from PyQt5 import uic
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox, QDialog
from schedule_class import *
import re


class signup_window(QDialog):
    account_signal = pyqtSignal(str)
    password_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.sign = uic.loadUi("sign.ui")
        self.sign.pushButton_create.clicked.connect(lambda: self.send_account())
        self.sign.pushButton_create.clicked.connect(lambda: self.send_password())

    def send_account(self):
        account = self.sign.lineEdit_account.text()
        self.account_signal.emit(account)

    def send_password(self):
        password = self.sign.lineEdit_password.text()
        self.password_signal.emit(password)


class login_window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.login = uic.loadUi("login.ui")
        self.user = user_class()
        self.sign_window = signup_window()
        self.login.pushButton_signup.clicked.connect(self.open_sign)
        self.login.pushButton_admin.clicked.connect(self.open_admin)
        # self.login.pushButton_view.clicked.connect()

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

    def open_admin(self):
        self.admin_win = admin_window(self.login.lineEdit_account.text())
        self.admin_win.admin.show()
        self.admin_win.admin_signal.connect(self.get_admin_mode)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = login_window()
    login.login.show()
    sys.exit(app.exec_())
