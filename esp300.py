import visa, time

class esp300():
    def __init__(self, addr):
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource('GPIB0::{}::INSTR'.format(addr))

        self.axis1 = axis(1, self)
        self.axis2 = axis(2, self)
        self.axis3 = axis(3, self)

class axis():
    def __init__(self,num,parent=None):
        self.num = num
        self.parent = parent
        self.pos = None

        self.go_home()

    def go_home(self):
        self.parent.inst.write("{}MO".format(self.num))
        self.parent.inst.write("{}SH0".format(self.num))
        self.parent.inst.write("{}OR1".format(self.num))

        while not self.parent.inst.query("{}MD?".format(self.num)):
            time.sleep(0.1)

    @property
    def pos(self):
        return self.parent.inst.query("{}TP".format(self.num))

    @pos.setter
    def pos(self, value):
        if self.parent.inst.query("{}MD?".format(self.num)):
            self.parent.inst.write("{}PA{}".format(self.num, value))
