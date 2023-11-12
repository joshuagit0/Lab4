from hal import hal_input_switch as switch
from hal import hal_led as led
from time import sleep


def main():
    switch.init()
    led.init()

    while True:
        if switch.read_slide_switch():
            led.set_output(0, 1)
            sleep(0.1)
            led.set_output(0, 0)
            sleep(0.1)
        else:
            for x in range(50):
                led.set_output(0, 1)
                sleep(0.05)
                led.set_output(0, 0)
                sleep(0.05)

            while switch.read_slide_switch() == 0:
                led.set_output(0, 0)


if __name__ == "__main__":
    main()
