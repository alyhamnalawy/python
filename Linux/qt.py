import dbus
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QApplication

class DBusClient(QWidget):
    def __init__(self):
        super().__init__()
        
        self.label = QLabel("No data")
        
        self.setDataButton = QPushButton("Set Data")
        self.setDataButton.clicked.connect(self.setData)
        
        self.getDataButton = QPushButton("Get Data")
        self.getDataButton.clicked.connect(self.getData)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.setDataButton)
        layout.addWidget(self.getDataButton)
        self.setLayout(layout)
        
    def setData(self):
        bus = dbus.SessionBus()
        service = bus.get_object('com.example.MyService', '/com/example/MyService')
        interface = dbus.Interface(service, 'com.example.MyService')
        interface.SetData("Some data")
        
    def getData(self):
        bus = dbus.SessionBus()
        service = bus.get_object('com.example.MyService', '/com/example/MyService')
        interface = dbus.Interface(service, 'com.example.MyService')
        data = interface.GetData()
        self.label.setText(data)
        
app = QApplication([])
window = DBusClient()
window.show()
app.exec_()