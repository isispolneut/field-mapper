import visa, time

class gauss460():
    def __init__(self, addr,wait_time):
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource("GPIB0::{}::INSTR".format(addr))

        self.inst.write("CHNL V")

        self.wait_time = wait_time

    @property
    def field(self):
        time.sleep(self.wait_time)
        return float(self.inst.query("FIELD?"))

    def allf(self):
        return list(float(b) for b in self.inst.query("ALLF?").split(','))
        