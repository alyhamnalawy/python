import dbus

bus = dbus.SessionBus()
service_name = 'com.example.MyService'
object_path = '/com/example/MyService'

interface_name = 'com.example.MyService'

class MyService(dbus.service.Object):
    def __init__(self, service_name, object_path):
        dbus.service.Object.__init__(self, bus, service_name, object_path)

    @dbus.service.method(interface_name)
    def SetData(self, data):
        self.data = data

    @dbus.service.method(interface_name)
    def GetData(self):
        return self.data

myservice = MyService(service_name, object_path)
bus.request_name(service_name)  

loop = dbus.mainloop.glib.DBusGMainLoop(set_as_default=True) 
loop.run()