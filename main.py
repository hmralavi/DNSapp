import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from qtui.mainwindow import Ui_MainWindow
import subprocess
import json


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dns_buttons_list = []
        self.dns_buttons_list.append(self.btn_nodns)
        self.create_buttons()
        self.connect_signals()

    def create_buttons(self):
        _translate = QtCore.QCoreApplication.translate
        with open('config.json', 'r') as file:
            config = json.load(file)
        for dnsname in config["DNS List"].keys():
            newbtn = QPushButton(self.centralwidget)
            newbtn.setMinimumSize(QtCore.QSize(0, 50))
            newbtn.setObjectName(f"btn_{dnsname}")
            newbtn.setText(_translate("MainWindow", dnsname))
            newbtn.setToolTip("\n".join((config["DNS List"][dnsname]["primary"], config["DNS List"][dnsname]["secondary"])))
            self.verticalLayout.addWidget(newbtn)
            self.dns_buttons_list.append(newbtn)
        self.adaptor_name = config["Adaptor"]["name"]

    def connect_signals(self):
        for btn in self.dns_buttons_list:
            btn.clicked.connect(self.set_dns)

    def set_dns(self, dns):
        btncolor = "background-color: rgb(85, 255, 0)"
        dns_command = lambda ip, index: f'netsh interface ipv4 add dnsservers name="{self.adaptor_name}" {ip} index={index}'

        # set background color of all buttons to default color
        for btn in self.dns_buttons_list:
            btn.setStyleSheet(None)

        # first clear dns server
        self.run_cmd_command(f'netsh interface ipv4 set dnsservers name="{self.adaptor_name}" source=dhcp')

        # then set new dns servers
        clicked_btn = self.sender()
        index = 0
        for ip in clicked_btn.toolTip().split('\n'):
            if ip != "":
                index += 1
                self.run_cmd_command(dns_command(ip, index))
        clicked_btn.setStyleSheet(btncolor)

    @staticmethod
    def run_cmd_command(command: str):
        # Run the command
        try:
            # Execute the command and capture the output
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

            # Print the output of the command
            print("Output:", result.stdout)
        except subprocess.CalledProcessError as e:
            # If the command returns a non-zero exit status, it raises CalledProcessError
            print("Command failed with return code:", e.returncode)
            print("Error:", e.stderr)
        except Exception as e:
            print("An error occurred:", str(e))


if __name__ == '__main__':
    qtapp = QApplication.instance()
    if qtapp is None:
        qtapp = QApplication(sys.argv)


    def my_excepthook(errtype, value, tback):  # this function captures runtime errors.
        print(errtype, value, tback)
        qtapp.exit()
        raise Exception


    sys.excepthook = my_excepthook
    win = MainWindow()
    win.show()
    sys.exit(qtapp.exec_())
