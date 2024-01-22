import time
from kaspersmicrobit import KaspersMicrobit
from kaspersmicrobit.services.accelerometer import AccelerometerData

import vgamepad as vg

gamepad = vg.VX360Gamepad()

def pressedA(button):
    print(f"button {button} pressed")
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()
    time.sleep(0.5)


def pressedB(button):
    print(f"button {button} pressed")
    gamepad.update()
    gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.5)
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
    gamepad.update()
    time.sleep(0.5)


def accelerometer_data(data: AccelerometerData):
    #print(data.x*32)
    gamepad.left_joystick(x_value=data.x*32, y_value=data.y*-32)  # values between -32768 and 32767
    gamepad.update()

with KaspersMicrobit.find_one_microbit() as microbit:
    print("mb connected")
    microbit.buttons.on_button_a(press=pressedA)
    microbit.buttons.on_button_b(press=pressedB)
    # read the current accelerometer data / lees de huidige accelerometer gegevens
    print(f"Current accelerometer reading: {microbit.accelerometer.read()}")
    # check how often accelerometer updates will occur if you listen to them with notify
    # / lees hoe vaak accelerometer updates doorgestuurd worden wanneer je er naar luistert met notify
    print(f"Current period: {microbit.accelerometer.read_period()}")
    # listen for accelerometer data updates / luister naar updates van de accelerometer gegevens
    microbit.accelerometer.notify(accelerometer_data)
    while True:
        time.sleep(1)



   


#typewrite('quick brown fox')
#hotkey('ctrl', 'w')