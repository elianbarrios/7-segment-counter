from machine import Pin
import time

# Led a, b, c, d, e, f, g
display_pins = (18, 19, 13, 15, 14, 16, 17)
display = list()

# 1, 2, 3, 4, 5, 6, 7, 8, 9
numbershx = (0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F)

for i in display_pins:
    display.append(Pin(i, Pin.OUT))
    
def show(number):
    numberhx = numbershx[number]
    
    for i, pin in enumerate(display):
        is_active = bool(numberhx & (1 << i))
        
        if is_active:
            pin.on()
        else:
            pin.off()

while True:
    for i in range(10):
        show(i)
        time.sleep(1)

