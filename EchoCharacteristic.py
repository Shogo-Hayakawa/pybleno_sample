from pybleno import Characteristic
import array
import struct
import sys
import traceback

class EchoCharacteristic(Characteristic):

    def __init__(self, uuid):
        Characteristic.__init__(self, {
            "uuid": uuid,
            "properties": ["read", "write", "notify"],
            "value":None
        })