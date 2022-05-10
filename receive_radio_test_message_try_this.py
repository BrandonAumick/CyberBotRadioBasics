from microbit import *
import radio

radio.on()
ch = 7
radio.config(channel = ch)

sleep(1000)

print("micro:bit radio receiver")

while True:
    message = radio.receive()
    if message is not None:
        print("Receive: ", message)
	if ch == 7:                   
            ch = 14                   
        elif ch == 14:                
            ch = 7                    
        radio.config(channel = ch)    