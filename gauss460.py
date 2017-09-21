import visa

class gauss460():
    def __init__(self, addr):
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource("GPIB0::{}::INSTR".format(addr))

        self.inst.write("CHNL X")

    @property
    def field(self):
        return float(self.inst.query("FIELD?"))

    def allf(self):
        return list(float(b) for b in self.inst.query("ALLF?").split(','))
        