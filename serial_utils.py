import ctypes
import serial

_ser = None

SWITCH_B = 0b10000000
SWITCH_Y = 0b01000000
SWITCH_ZL = 0b00100000
SWITCH_A = 0b00010000
SWITCH_L = 0b00001000
SWITCH_MINUS = 0b00000100
SWITCH_CAPTURE = 0b00000100

class SerialReport(ctypes.Structure):
    _fields_ = [("xp", ctypes.c_byte),
        ("yp", ctypes.c_byte),
        ("rxp", ctypes.c_byte),
        ("ryp", ctypes.c_byte),
        ("c", ctypes.c_byte)]

def _dict_to_serial_report(input):
    report = SerialReport()
    report.xp = ctypes.c_byte(input['lx'])
    report.yp = ctypes.c_byte(input['ly'])
    report.rxp = ctypes.c_byte(0)
    report.ryp = ctypes.c_byte(0)

    c = 0b00000000
    if input['a']:
        c |= SWITCH_A
    if input['b']:
        c |= SWITCH_B
    if input['y']:
        c |= SWITCH_Y
    report.c = ctypes.c_byte(c)
    return report

def set_serial_port(port):
    global _ser
    _ser = serial.Serial(port)

def report_out(report):
    _ser.write(_dict_to_serial_report(report))