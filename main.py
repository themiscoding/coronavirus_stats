from PyQt5 import QtCore, QtGui, QtWidgets
from gui import gui
import sys
from scraper import scraper
import os 
from countries import supported_countries


get_world_stats, get_country_stats = scraper.get_world_stats, scraper.get_country_stats
ui = gui.Ui_MainWindow()



def button_clicked():
    ui.error.setText('')
    search_input = ui.user_input.toPlainText().strip()
    if search_input == '':

        ui.error.setText('You have to enter something')
        ui.deaths.setText('0.000.000')
        ui.infected.setText('0.000.000')
        ui.recovered.setText('0.000.000')
    else:
        if search_input == 'world':
            stats = get_world_stats()
            if 'error' in stats:
                 ui.error.setText(stats.get('error'))
            else:
                ui.set_stats(stats)
        else:
            if search_input in supported_countries:
                stats = get_country_stats(search_input)
                if 'error' in stats:
                    ui.error.setText(stats.get('error'))
                else:
                    set_stats(stats)       
             
            else:
                ui.error.setText('I couldn\'t recognize that country.')
                   
def set_stats(stats):
    infected_stats = str(stats.get('cases'))
    deaths_stats = str(stats.get('deaths'))
    recovered_stats = str(stats.get('recovered'))

    ui.infected.setText(infected_stats)
    ui.deaths.setText(deaths_stats)
    ui.recovered.setText(recovered_stats)
    

def run_app():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui.setupUi(MainWindow)
    ui.search_btn.clicked.connect(button_clicked)
    MainWindow.show()
    sys.exit(app.exec_())

run_app()