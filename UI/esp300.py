import visa, time

class esp300():
    def __init__(self, addr, wait_time):
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource('GPIB0::{}::INSTR'.format(addr))
        
        self.wait_time = wait_time

        self.axis1 = axis(1, self)
        self.axis2 = axis(2, self)
        self.axis3 = axis(3, self)



    def go_home(self):
        self.axis1.go_home()
        self.axis2.go_home()
        self.axis3.go_home()

class axis():
    def __init__(self,num,parent=None):
        self.num = num
        self.parent = parent

        self.go_home()
        self.pos=0

    def go_home(self):
        print(self.parent.inst.query("*IDN?"))
        self.parent.inst.write("{}MO".format(self.num))
        self.parent.inst.write("{}SH0".format(self.num))
        self.parent.inst.write("{}OR".format(self.num))

        while not self.is_not_moving():
            time.sleep(0.1)

    def is_not_moving(self):
        return self.parent.inst.query("{}MD?".format(self.num))

    @property
    def pos(self):
        return float(self.parent.inst.query("{}TP".format(self.num)))

    @pos.setter
    def pos(self, value):
        if self.is_not_moving():
            self.parent.inst.write("{}PA{}".format(self.num, value))
            time.sleep(self.parent.wait_time)
