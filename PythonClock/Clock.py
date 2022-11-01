from UI_Clock import *
import sys
import time

class Clock(QMainWindow):
    def __init__(self):
        super(Clock,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint|Qt.Tool)

        self.move(1365-240,0)

        self.weekdays = {"0":"Monday","1":"Tuesday","2":"Wednesday","3":"Thursday","4":"Friday","5":"Saturday","6":"Sunday"}

        self.monthnames = {"1":"January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}

        self.hours = {"0":["12","AM"],"1":["01","AM"],"2":["02","AM"],"3":["03","AM"],"4":["04","AM"],"5":["05","AM"],"6":["06","AM"],"7":["07","AM"],"8":["08","AM"],"9":["09","AM"],"10":["10","AM"],"11":["11","AM"],"12":["12","PM"],"13":["01","PM"],"14":["02","PM"],"15":["03","PM"],"16":["04","PM"],"17":["05","PM"],"18":["06","PM"],"19":["07","PM"],"20":["08","PM"],"21":["09","PM"],"22":["10","PM"],"23":["11","PM"]}
        
        self.nums = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61"]

        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(500)
        self.ui.clockbox.mouseMoveEvent = self.moveWindow
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0,0,0,200))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.clock.setGraphicsEffect(self.shadow)
        print("showing")
        self.show()

    def updateTime(self):
        data = time.localtime()
        self.ui.hour.setText(self.hours[str(data.tm_hour)][0])
        self.ui.minute.setText(self.nums[data.tm_min])
        self.ui.AMPM.setText(self.hours[str(data.tm_hour)][1])
        self.ui.day.setText(self.weekdays[str(data.tm_wday)])
        dateformat = "{} {}, {}".format(self.monthnames[str(data.tm_mon)],str(data.tm_mday),str(data.tm_year))
        self.ui.date.setText(dateformat)
        # self.update()

    def moveWindow(self,event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Clock()
