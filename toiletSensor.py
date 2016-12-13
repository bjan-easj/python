import smbus
import time
import urllib3

http = urllib3.PoolManager()


class sensor:
    bus = smbus.SMBus(1)

    def readLight(self):
        self.bus.write_byte(0x48, 0x00)
        self.bus.read_byte(0x48)
        return self.bus.read_byte(0x48)


sens = sensor()

while True:
    http.request("GET", "http://bjan-toilet.azurewebsites.net/Gem.php?tal=" + str(sens.readLight()) )

    time.sleep(1)
