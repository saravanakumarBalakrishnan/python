
import sys
import glob
import serial
def serial_ports():
    count=0
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/ttyUSB*') # ubuntu is /dev/ttyUSB0
    elif sys.platform.startswith('darwin'):
        # ports = glob.glob('/dev/tty.*')
        ports = glob.glob('/dev/tty.SLAB_USBtoUART*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            print("Successfully Found Serial Port in the device \n")
            print(count)
            result.append(port)
        except serial.SerialException as e:
            if e.errno == 13:
                raise e
            pass
        except OSError:
            pass
    return result


if __name__ == '__main__':
    print(serial_ports())

