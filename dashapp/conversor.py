import time

ADS1x15_DEFAULT_ADDRESS = 0x48
ADS1x15_POINTER_CONVERSION = 0x00
ADS1x15_POINTER_CONFIG = 0x01
ADS1x15_POINTER_LOW_THRESHOLD = 0x02
ADS1x15_POINTER_HIGH_THRESHOLD = 0x03
ADS1x15_CONFIG_OS_SINGLE = 0x8000
ADS1x15_CONFIG_MUX_OFFSET = 12
ADS1x15_CONFIG_GAIN = {
    2 / 3: 0x0000,
    1: 0x0200,
    2: 0x0400,
    4: 0x0600,
    8: 0x0800,
    16: 0x0A00
}
ADS1x15_CONFIG_MODE_CONTINUOUS = 0x0000
ADS1x15_CONFIG_MODE_SINGLE = 0x0100

ADS1115_CONFIG_DR = {
    8: 0x0000,
    16: 0x0020,
    32: 0x0040,
    64: 0x0060,
    128: 0x0080,
    250: 0x00A0,
    475: 0x00C0,
    860: 0x00E0
}
ADS1x15_CONFIG_COMP_WINDOW = 0x0010
ADS1x15_CONFIG_COMP_ACTIVE_HIGH = 0x0008
ADS1x15_CONFIG_COMP_LATCHING = 0x0004
ADS1x15_CONFIG_COMP_QUE = {
    1: 0x0000,
    2: 0x0001,
    4: 0x0002
}
ADS1x15_CONFIG_COMP_QUE_DISABLE = 0x0003


class ADS1115(object):
    def __init__(self, address=ADS1x15_DEFAULT_ADDRESS, i2c=None, **kwargs):
        if i2c is None:
            from . import I2C
            i2c = I2C

        self._device = i2c.get_i2c_device(address, **kwargs)

    def _read(self, mux, gain, data_rate, mode):
        config = ADS1x15_CONFIG_OS_SINGLE
        config |= (mux & 0x07) << ADS1x15_CONFIG_MUX_OFFSET

        if gain not in ADS1x15_CONFIG_GAIN:
            raise ValueError('Gain must be one of: 2/3, 1, 2, 4, 8, 16')

        config |= ADS1x15_CONFIG_GAIN[gain]
        config |= mode

        if data_rate is None:
            data_rate = self.data_rate_default()

        config |= self.data_rate_config(data_rate)
        config |= ADS1x15_CONFIG_COMP_QUE_DISABLE
        self._device.writeList(ADS1x15_POINTER_CONFIG, [(config >> 8) & 0xFF, config & 0xFF])
        time.sleep(1.0 / data_rate + 0.0001)
        result = self._device.readList(ADS1x15_POINTER_CONVERSION, 2)

        return self.conversion_value(result[1], result[0])

    def read_adc(self, channel, gain=1, data_rate=None):
        assert 0 <= channel <= 3, 'Channel must be a value within 0-3!'

        return self._read(channel + 0x04, gain, data_rate, ADS1x15_CONFIG_MODE_SINGLE)

    @staticmethod
    def data_rate_default():
        return 128

    @staticmethod
    def data_rate_config(data_rate):
        if data_rate not in ADS1115_CONFIG_DR:
            raise ValueError('Data rate must be one of: 8, 16, 32, 64, 128, 250, 475, 860')

        return ADS1115_CONFIG_DR[data_rate]

    @staticmethod
    def conversion_value(low, high):
        value = ((high & 0xFF) << 8) | (low & 0xFF)

        if value & 0x8000 != 0:
            value -= 1 << 16

        return value
