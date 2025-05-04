import os
os.system("sudo pigpiod")

import pigpio
import time
import sys

PIN_BTN  = 14
PIN_LEDR = 16

brightness = 0
BRIGHTNESS_STEP = 64  # 0~255 범위에서 단계 증가


if __name__ == "__main__":
    pi = pigpio.pi()
    if not pi.connected:
        print("pigpio demon error!", file=sys.stderr)
        sys.exit(1)

    # 핀 설정
    pi.set_mode(PIN_BTN, pigpio.INPUT)
    pi.set_pull_up_down(PIN_BTN, pigpio.PUD_UP)

    pi.set_mode(PIN_LEDR, pigpio.OUTPUT)
    pi.set_PWM_dutycycle(PIN_LEDR, brightness)  # 초기 밝기 0

    print("PWM LED Brightness Control (Polling)")

    try:
        while True:
            btn = pi.read(PIN_BTN)

            if btn == 0:  # 눌림 감지
            ################ Write Codes From Here ################
                print(f"LED Brightness: {brightness}/255")
                time.sleep(0.2)  # 디바운싱 대기

            prev_btn = btn
            time.sleep(0.01)
    finally:
        pi.set_PWM_dutycycle(PIN_LEDR, 0)
        pi.stop()
        os.system("sudo killall pigpiod")


