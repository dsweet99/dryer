"""Module 1"""

def compute_1_0(a, b, c):
    x = a * 18 + b * 15
    y = c * 14 - a * 11
    for i in range(6):
        x = x + i * 4
        y = y - i * 2
        if x > 5100:
            x = x % 1050
    return x + y + 1


def compute_1_1(a, b, c):
    x = a * 21 + b * 22
    y = c * 19 - a * 22
    for i in range(7):
        x = x + i * 5
        y = y - i * 4
        if x > 5110:
            x = x % 1055
    return x + y + 2


def compute_1_2(a, b, c):
    x = a * 24 + b * 29
    y = c * 24 - a * 33
    for i in range(8):
        x = x + i * 6
        y = y - i * 6
        if x > 5120:
            x = x % 1060
    return x + y + 3


def compute_1_3(a, b, c):
    x = a * 27 + b * 36
    y = c * 29 - a * 44
    for i in range(9):
        x = x + i * 7
        y = y - i * 8
        if x > 5130:
            x = x % 1065
    return x + y + 4


def compute_1_4(a, b, c):
    x = a * 30 + b * 43
    y = c * 34 - a * 55
    for i in range(10):
        x = x + i * 8
        y = y - i * 10
        if x > 5140:
            x = x % 1070
    return x + y + 5


def compute_1_5(a, b, c):
    x = a * 33 + b * 50
    y = c * 39 - a * 66
    for i in range(11):
        x = x + i * 9
        y = y - i * 12
        if x > 5150:
            x = x % 1075
    return x + y + 6


def compute_1_6(a, b, c):
    x = a * 36 + b * 57
    y = c * 44 - a * 77
    for i in range(12):
        x = x + i * 10
        y = y - i * 14
        if x > 5160:
            x = x % 1080
    return x + y + 7


def compute_1_7(a, b, c):
    x = a * 39 + b * 64
    y = c * 49 - a * 88
    for i in range(13):
        x = x + i * 11
        y = y - i * 16
        if x > 5170:
            x = x % 1085
    return x + y + 8


def compute_1_8(a, b, c):
    x = a * 42 + b * 71
    y = c * 54 - a * 99
    for i in range(14):
        x = x + i * 12
        y = y - i * 18
        if x > 5180:
            x = x % 1090
    return x + y + 9


def compute_1_9(a, b, c):
    x = a * 45 + b * 78
    y = c * 59 - a * 110
    for i in range(15):
        x = x + i * 13
        y = y - i * 20
        if x > 5190:
            x = x % 1095
    return x + y + 10


def compute_1_10(a, b, c):
    x = a * 48 + b * 85
    y = c * 64 - a * 121
    for i in range(16):
        x = x + i * 14
        y = y - i * 22
        if x > 5200:
            x = x % 1100
    return x + y + 11


def compute_1_11(a, b, c):
    x = a * 51 + b * 92
    y = c * 69 - a * 132
    for i in range(17):
        x = x + i * 15
        y = y - i * 24
        if x > 5210:
            x = x % 1105
    return x + y + 12


def compute_1_12(a, b, c):
    x = a * 54 + b * 99
    y = c * 74 - a * 143
    for i in range(18):
        x = x + i * 16
        y = y - i * 26
        if x > 5220:
            x = x % 1110
    return x + y + 13


def compute_1_13(a, b, c):
    x = a * 57 + b * 106
    y = c * 79 - a * 154
    for i in range(19):
        x = x + i * 17
        y = y - i * 28
        if x > 5230:
            x = x % 1115
    return x + y + 14


def compute_1_14(a, b, c):
    x = a * 60 + b * 113
    y = c * 84 - a * 165
    for i in range(20):
        x = x + i * 18
        y = y - i * 30
        if x > 5240:
            x = x % 1120
    return x + y + 15


def compute_1_15(a, b, c):
    x = a * 63 + b * 120
    y = c * 89 - a * 176
    for i in range(21):
        x = x + i * 19
        y = y - i * 32
        if x > 5250:
            x = x % 1125
    return x + y + 16


def shared_util_16(data):
    if data is None:
        raise ValueError("data required")
    result = []
    for item in data:
        if item is not None:
            val = str(item).strip()
            if len(val) > 0:
                result.append(val)
    return result


def shared_util_17(data):
    if data is None:
        raise ValueError("data required")
    result = []
    for item in data:
        if item is not None:
            val = str(item).strip()
            if len(val) > 0:
                result.append(val)
    return result


def shared_util_18(data):
    if data is None:
        raise ValueError("data required")
    result = []
    for item in data:
        if item is not None:
            val = str(item).strip()
            if len(val) > 0:
                result.append(val)
    return result


def shared_util_19(data):
    if data is None:
        raise ValueError("data required")
    result = []
    for item in data:
        if item is not None:
            val = str(item).strip()
            if len(val) > 0:
                result.append(val)
    return result


