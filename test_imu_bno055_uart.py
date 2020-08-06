# https://cdn-learn.adafruit.com/downloads/pdf/bno055-absolute-orientation-sensor-with-raspberry-pi-and-beaglebone-black.pdf
# https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor/python-circuitpython
# https://github.com/adafruit/Adafruit_CircuitPython_BNO055
import serial
import adafruit_bno055
uart = serial.Serial("/dev/serial0")
sensor = adafruit_bno055.BNO055_UART(uart)

print("Temperature: {} degrees C".format(sensor.temperature))
print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
print("Magnetometer (microteslas): {}".format(sensor.magnetic))
print("Gyroscope (rad/sec): {}".format(sensor.gyro))
print("Euler angle: {}".format(sensor.euler))
print("Quaternion: {}".format(sensor.quaternion))
print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
print("Gravity (m/s^2): {}".format(sensor.gravity))
