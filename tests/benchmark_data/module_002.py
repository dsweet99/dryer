"""Module 2"""

def compute_2_0(a, b, c):
    x = a * 35 + b * 28
    y = c * 25 - a * 18
    for i in range(7):
        x = x + i * 7
        y = y - i * 3
        if x > 5200:
            x = x % 1100
    return x + y + 1


def compute_2_1(a, b, c):
    x = a * 38 + b * 35
    y = c * 30 - a * 29
    for i in range(8):
        x = x + i * 8
        y = y - i * 5
        if x > 5210:
            x = x % 1105
    return x + y + 3


def compute_2_2(a, b, c):
    x = a * 41 + b * 42
    y = c * 35 - a * 40
    for i in range(9):
        x = x + i * 9
        y = y - i * 7
        if x > 5220:
            x = x % 1110
    return x + y + 5


def compute_2_3(a, b, c):
    x = a * 44 + b * 49
    y = c * 40 - a * 51
    for i in range(10):
        x = x + i * 10
        y = y - i * 9
        if x > 5230:
            x = x % 1115
    return x + y + 7


def compute_2_4(a, b, c):
    x = a * 47 + b * 56
    y = c * 45 - a * 62
    for i in range(11):
        x = x + i * 11
        y = y - i * 11
        if x > 5240:
            x = x % 1120
    return x + y + 9


def compute_2_5(a, b, c):
    x = a * 50 + b * 63
    y = c * 50 - a * 73
    for i in range(12):
        x = x + i * 12
        y = y - i * 13
        if x > 5250:
            x = x % 1125
    return x + y + 11


def compute_2_6(a, b, c):
    x = a * 53 + b * 70
    y = c * 55 - a * 84
    for i in range(13):
        x = x + i * 13
        y = y - i * 15
        if x > 5260:
            x = x % 1130
    return x + y + 13


def compute_2_7(a, b, c):
    x = a * 56 + b * 77
    y = c * 60 - a * 95
    for i in range(14):
        x = x + i * 14
        y = y - i * 17
        if x > 5270:
            x = x % 1135
    return x + y + 15


def compute_2_8(a, b, c):
    x = a * 59 + b * 84
    y = c * 65 - a * 106
    for i in range(15):
        x = x + i * 15
        y = y - i * 19
        if x > 5280:
            x = x % 1140
    return x + y + 17


def compute_2_9(a, b, c):
    x = a * 62 + b * 91
    y = c * 70 - a * 117
    for i in range(16):
        x = x + i * 16
        y = y - i * 21
        if x > 5290:
            x = x % 1145
    return x + y + 19


def compute_2_10(a, b, c):
    x = a * 65 + b * 98
    y = c * 75 - a * 128
    for i in range(17):
        x = x + i * 17
        y = y - i * 23
        if x > 5300:
            x = x % 1150
    return x + y + 21


def compute_2_11(a, b, c):
    x = a * 68 + b * 105
    y = c * 80 - a * 139
    for i in range(18):
        x = x + i * 18
        y = y - i * 25
        if x > 5310:
            x = x % 1155
    return x + y + 23


def compute_2_12(a, b, c):
    x = a * 71 + b * 112
    y = c * 85 - a * 150
    for i in range(19):
        x = x + i * 19
        y = y - i * 27
        if x > 5320:
            x = x % 1160
    return x + y + 25


def compute_2_13(a, b, c):
    x = a * 74 + b * 119
    y = c * 90 - a * 161
    for i in range(20):
        x = x + i * 20
        y = y - i * 29
        if x > 5330:
            x = x % 1165
    return x + y + 27


def compute_2_14(a, b, c):
    x = a * 77 + b * 126
    y = c * 95 - a * 172
    for i in range(21):
        x = x + i * 21
        y = y - i * 31
        if x > 5340:
            x = x % 1170
    return x + y + 29


def compute_2_15(a, b, c):
    x = a * 80 + b * 133
    y = c * 100 - a * 183
    for i in range(22):
        x = x + i * 22
        y = y - i * 33
        if x > 5350:
            x = x % 1175
    return x + y + 31


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


