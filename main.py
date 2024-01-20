from machine import Pin, SPI, Timer

spi = SPI(0, baudrate=100000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
cs = Pin(17, Pin.OUT)
buf = bytearray(2)
tim = Timer()
led = Pin("LED", Pin.OUT)
def tick(timer):
    global led
    global cs
    global spi
    global buf
    cs.value(0)
    spi.readinto(buf)
    print(((((buf[0] & 0b01111111) << 8) + buf[1]) >> 3)*0.25)
    cs.value(1)
    led.toggle()
tim.init(freq=1, mode=Timer.PERIODIC, callback=tick)
