from microbit import *
import radio

radio.on()

sleep(1000)

print("micro:bit radio sender")

while True:
    radio.config(channel = 7)           
    message = "Hello from channel 7!"   
    print("Send: ", message)
    radio.send(message)

    sleep(1000)                        

    radio.config(channel = 14)          
    message = "Hello from channel 14!"  
    print("Send: ", message)            
    radio.send(message)                 
    
    print("Done!")
    sleep(1000)                        