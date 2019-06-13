from machine import Pin

class LED:
    def __init__(self, ledId):
        #LED字典
        #数据结构：（gpio管脚编号，LED灭的电平，LED亮的电平）
        ledList = [(2, False, True), (13, True, False)]

        if ledId >= len(ledList) or ledId < 0:
            print('ERROR：LED编号无效， 有效ID：{} - {}'.format(0, len(ledList - 1)))
            return None

        gpioId, self.LED_OFF, self.LED_ON = ledList[ledId]
        self.ledPin = Pin(gpioId, Pin.OUT)

    def on(self):
        '''
        打开LED
        '''
        self.ledPin.value(self.LED_ON)

    def on(self):
        '''
        关闭LED
        '''
        self.ledPin.value(self.LED_OFF)

    def toggle(self):
        '''
        切换LED的状态
        OFF -> ON
        ON  -> OFF
        '''
        self.ledPin.value(not self.ledPin.value())
