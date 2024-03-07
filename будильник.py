import datetime
class MainScreen:
    def __init__(self):
        self.alarms = []
        
    class Signal:
        def __init__(self, time, sost=True, name=None, desc=None):
            self.time = time
            self.sost = sost
            self.name = name
            self.desc = desc
        def set_time(self, time):
            self.time = time #datetime.time(time)
        def set_state(self, sost):
            self.sost = sost
        def set_name(self, name):
            self.name = name
        def set_description(self, desc):
            self.desc = desc
        def time_checker(self, time):
            self.time = time
    
    def addAlarm(self, time, sost=True, name=None, desc=None):
        self.alarms.append(self.Signal(time, sost, name, desc))
    
    def deleteAlarm(self, time, sost=True, name=None, desc=None):
        self.alarms.delete()
        
alpha_test_1 = input("Введите время:")
alpha_test_2 = input("Введите название:")
alpha_test_3 = input("Введите описание:")
alpha_test_4 = input("Введите данные 4")
mainscreen = MainScreen()
signal = mainscreen.Signal(alpha_test_1,alpha_test_2, alpha_test_3, alpha_test_4)
print(signal.time)