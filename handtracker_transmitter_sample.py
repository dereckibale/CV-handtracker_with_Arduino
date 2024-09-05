
from cvzone.SerialModule import SerialObject
import time

arduino = SerialObject()

while True:
    data1 = [1,0]
    data0 = [0,1]
    arduino.sendData(data1)
    print(data1)
    time.sleep(1)
    arduino.sendData(data0)
    print(data0)
    time.sleep(1)


 