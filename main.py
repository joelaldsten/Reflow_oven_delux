from machine import Pin, SPI, Timer

#spi = SPI(0, baudrate=100000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))


led = Pin(25, Pin.OUT)
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq=2.5, mode=Timer.PERIODIC, callback=tick)
