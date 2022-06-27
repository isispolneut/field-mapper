import time
from lakeshore import Teslameter

class f71():
    def __init__(self, addr,wait_time):
        self.inst =Teslameter()
        print(self.inst.query('*IDN?'))

        self.wait_time = wait_time

    @property
    def field(self):
        time.sleep(self.wait_time)
        return float(self.inst.query("FETCh:DC?"))

    def allf(self):
        time.sleep(self.wait_time)
        return list(float(b) for b in self.inst.query("FETCh:FIELd:DC? ALL").split(','))
        