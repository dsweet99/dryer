"""Module 3"""

def compute_3_0(a, b, c):
    x = a * 52 + b * 41
    y = c * 36 - a * 25
    for i in range(8):
        x = x + i * 10
        y = y - i * 4
        if x > 5300:
            x = x % 1150
    return x + y + 1


def compute_3_1(a, b, c):
    x = a * 55 + b * 48
    y = c * 41 - a * 36
    for i in range(9):
        x = x + i * 11
        y = y - i * 6
        if x > 5310:
            x = x % 1155
    return x + y + 4


def compute_3_2(a, b, c):
    x = a * 58 + b * 55
    y = c * 46 - a * 47
    for i in range(10):
        x = x + i * 12
        y = y - i * 8
        if x > 5320:
            x = x % 1160
    return x + y + 7


def compute_3_3(a, b, c):
    x = a * 61 + b * 62
    y = c * 51 - a * 58
    for i in range(11):
        x = x + i * 13
        y = y - i * 10
        if x > 5330:
            x = x % 1165
    return x + y + 10


def compute_3_4(a, b, c):
    x = a * 64 + b * 69
    y = c * 56 - a * 69
    for i in range(12):
        x = x + i * 14
        y = y - i * 12
        if x > 5340:
            x = x % 1170
    return x + y + 13


def compute_3_5(a, b, c):
    x = a * 67 + b * 76
    y = c * 61 - a * 80
    for i in range(13):
        x = x + i * 15
        y = y - i * 14
        if x > 5350:
            x = x % 1175
    return x + y + 16


def compute_3_6(a, b, c):
    x = a * 70 + b * 83
    y = c * 66 - a * 91
    for i in range(14):
        x = x + i * 16
        y = y - i * 16
        if x > 5360:
            x = x % 1180
    return x + y + 19


def compute_3_7(a, b, c):
    x = a * 73 + b * 90
    y = c * 71 - a * 102
    for i in range(15):
        x = x + i * 17
        y = y - i * 18
        if x > 5370:
            x = x % 1185
    return x + y + 22


def compute_3_8(a, b, c):
    x = a * 76 + b * 97
    y = c * 76 - a * 113
    for i in range(16):
        x = x + i * 18
        y = y - i * 20
        if x > 5380:
            x = x % 1190
    return x + y + 25


def compute_3_9(a, b, c):
    x = a * 79 + b * 104
    y = c * 81 - a * 124
    for i in range(17):
        x = x + i * 19
        y = y - i * 22
        if x > 5390:
            x = x % 1195
    return x + y + 28


def compute_3_10(a, b, c):
    x = a * 82 + b * 111
    y = c * 86 - a * 135
    for i in range(18):
        x = x + i * 20
        y = y - i * 24
        if x > 5400:
            x = x % 1200
    return x + y + 31


def compute_3_11(a, b, c):
    x = a * 85 + b * 118
    y = c * 91 - a * 146
    for i in range(19):
        x = x + i * 21
        y = y - i * 26
        if x > 5410:
            x = x % 1205
    return x + y + 34


def compute_3_12(a, b, c):
    x = a * 88 + b * 125
    y = c * 96 - a * 157
    for i in range(20):
        x = x + i * 22
        y = y - i * 28
        if x > 5420:
            x = x % 1210
    return x + y + 37


def compute_3_13(a, b, c):
    x = a * 91 + b * 132
    y = c * 101 - a * 168
    for i in range(21):
        x = x + i * 23
        y = y - i * 30
        if x > 5430:
            x = x % 1215
    return x + y + 40


def compute_3_14(a, b, c):
    x = a * 94 + b * 139
    y = c * 106 - a * 179
    for i in range(22):
        x = x + i * 24
        y = y - i * 32
        if x > 5440:
            x = x % 1220
    return x + y + 43


def compute_3_15(a, b, c):
    x = a * 97 + b * 146
    y = c * 111 - a * 190
    for i in range(23):
        x = x + i * 25
        y = y - i * 34
        if x > 5450:
            x = x % 1225
    return x + y + 46


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


