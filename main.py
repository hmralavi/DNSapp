import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from qtui.mainwindow import Ui_MainWindow
import subprocess

NODNS = 0
CLOUDFLARE = 1
GOOGLE = 2
ELECTRO = 3
RADAR = 4
SHECAN = 5
DNS403 = 6
BEGZAR = 7


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setup_connect_slots_signals()

    def setup_connect_slots_signals(self):
        self.nodns_btn.clicked.connect(lambda: self.set_dns(NODNS))
        self.cloudflare_btn.clicked.connect(lambda: self.set_dns(CLOUDFLARE))
        self.google_btn.clicked.connect(lambda: self.set_dns(GOOGLE))
        self.electro_btn.clicked.connect(lambda: self.set_dns(ELECTRO))
        self.radar_btn.clicked.connect(lambda: self.set_dns(RADAR))
        self.shecan_btn.clicked.connect(lambda: self.set_dns(SHECAN))
        self.dns403_btn.clicked.connect(lambda: self.set_dns(DNS403))
        self.begzar_btn.clicked.connect(lambda: self.set_dns(BEGZAR))

    def set_dns(self, dns):
        btncolor = "background-color: rgb(85, 255, 0)"
        primary_dns = lambda ip: f'netsh interface ipv4 add dnsservers name="Wi-Fi" {ip} index=1'
        secondary_dns = lambda ip: f'netsh interface ipv4 add dnsservers name="Wi-Fi" {ip} index=2'

        # set background color of all buttons to default color
        for btn in self.children()[1].children():
            if "_btn" in btn.objectName():
                btn.setStyleSheet(None)

        # first clear dns server
        self.run_cmd_command('netsh interface ipv4 set dnsservers name="Wi-Fi" source=dhcp')

        # then set new dns servers
        if dns == NODNS:
            self.nodns_btn.setStyleSheet(btncolor)
        elif dns == CLOUDFLARE:
            self.run_cmd_command(primary_dns("1.1.1.1"))
            self.run_cmd_command(secondary_dns("1.0.0.1"))
            self.cloudflare_btn.setStyleSheet(btncolor)
        elif dns == GOOGLE:
            self.run_cmd_command(primary_dns("8.8.8.8"))
            self.run_cmd_command(secondary_dns("8.8.4.4"))
            self.google_btn.setStyleSheet(btncolor)
        elif dns == ELECTRO:
            self.run_cmd_command(primary_dns("78.157.42.100"))
            self.run_cmd_command(secondary_dns("78.157.42.101"))
            self.electro_btn.setStyleSheet(btncolor)
        elif dns == RADAR:
            self.run_cmd_command(primary_dns("10.202.10.10"))
            self.run_cmd_command(secondary_dns("10.202.10.11"))
            self.radar_btn.setStyleSheet(btncolor)
        elif dns == SHECAN:
            self.run_cmd_command(primary_dns("178.22.122.100"))
            self.run_cmd_command(secondary_dns("185.51.200.2"))
            self.shecan_btn.setStyleSheet(btncolor)
        elif dns == DNS403:
            self.run_cmd_command(primary_dns("10.202.10.202"))
            self.run_cmd_command(secondary_dns("10.202.10.102"))
            self.dns403_btn.setStyleSheet(btncolor)
        elif dns == BEGZAR:
            self.run_cmd_command(primary_dns("185.55.226.26"))
            self.run_cmd_command(secondary_dns("185.55.225.25"))
            self.begzar_btn.setStyleSheet(btncolor)

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