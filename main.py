from pybleno import *
import sys
import signal
from EchoCharacteristic import *

def onStateChange(state):
    print('on -> stateChange: ' + state)

    if(state == "poweredOn"):
        bleno.startAdvertising()
    else:
        bleno.stopAdvertising()

def onAdvertisingStart(error):
    print("on -> advertisingStart:" + ("error " + error if error else "success"))

    if not error:
        bleno.setServices([
            BlenoPrimaryService({
                "uuid": "ec00",
                "characteristics": [
                    EchoCharacteristic("ec0F")
                ]
            })
        ])


def main():
    bleno.on("stateChange", onStateChange)
    bleno.on("advertisingStart", onAdvertisingStart)
    bleno.start()
    

if __name__ == "__main__":
    bleno = Bleno()
    main()

