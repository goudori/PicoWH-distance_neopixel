import machine  # type: ignore
import time
import neopixel  # type: ignore

TRIG = machine.Pin(17, machine.Pin.OUT)
ECHO = machine.Pin(16, machine.Pin.IN)

ws = neopixel.NeoPixel(machine.Pin(0), 8)


def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while not ECHO.value():
        pass
    time1 = time.ticks_us()
    while ECHO.value():
        pass
    time2 = time.ticks_us()
    during = time.ticks_diff(time2, time1)
    return during * 340 / 2 / 10000


def led_strip(is_detected):
    for i in range(8):
        ws[i] = (0, 0, 0) if not is_detected else (0, 0, 30)  # LEDを消す or 点灯
    ws.write()


while True:
    dis = distance()
    is_detected = dis < 10  # 10cm以内であれば反応したとみなす
    led_strip(is_detected)
    print("Distance: %.2f" % dis)
    time.sleep_ms(300)
