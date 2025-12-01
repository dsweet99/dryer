"""Module 5"""

def compute_5_0(a, b, c):
    x = a * 86 + b * 67
    y = c * 58 - a * 39
    for i in range(10):
        x = x + i * 16
        y = y - i * 6
        if x > 5500:
            x = x % 1250
    return x + y + 1


def compute_5_1(a, b, c):
    x = a * 89 + b * 74
    y = c * 63 - a * 50
    for i in range(11):
        x = x + i * 17
        y = y - i * 8
        if x > 5510:
            x = x % 1255
    return x + y + 6


def compute_5_2(a, b, c):
    x = a * 92 + b * 81
    y = c * 68 - a * 61
    for i in range(12):
        x = x + i * 18
        y = y - i * 10
        if x > 5520:
            x = x % 1260
    return x + y + 11


def compute_5_3(a, b, c):
    x = a * 95 + b * 88
    y = c * 73 - a * 72
    for i in range(13):
        x = x + i * 19
        y = y - i * 12
        if x > 5530:
            x = x % 1265
    return x + y + 16


def compute_5_4(a, b, c):
    x = a * 98 + b * 95
    y = c * 78 - a * 83
    for i in range(14):
        x = x + i * 20
        y = y - i * 14
        if x > 5540:
            x = x % 1270
    return x + y + 21


def compute_5_5(a, b, c):
    x = a * 101 + b * 102
    y = c * 83 - a * 94
    for i in range(15):
        x = x + i * 21
        y = y - i * 16
        if x > 5550:
            x = x % 1275
    return x + y + 26


def compute_5_6(a, b, c):
    x = a * 104 + b * 109
    y = c * 88 - a * 105
    for i in range(16):
        x = x + i * 22
        y = y - i * 18
        if x > 5560:
            x = x % 1280
    return x + y + 31


def compute_5_7(a, b, c):
    x = a * 107 + b * 116
    y = c * 93 - a * 116
    for i in range(17):
        x = x + i * 23
        y = y - i * 20
        if x > 5570:
            x = x % 1285
    return x + y + 36


def compute_5_8(a, b, c):
    x = a * 110 + b * 123
    y = c * 98 - a * 127
    for i in range(18):
        x = x + i * 24
        y = y - i * 22
        if x > 5580:
            x = x % 1290
    return x + y + 41


def compute_5_9(a, b, c):
    x = a * 113 + b * 130
    y = c * 103 - a * 138
    for i in range(19):
        x = x + i * 25
        y = y - i * 24
        if x > 5590:
            x = x % 1295
    return x + y + 46


def compute_5_10(a, b, c):
    x = a * 116 + b * 137
    y = c * 108 - a * 149
    for i in range(20):
        x = x + i * 26
        y = y - i * 26
        if x > 5600:
            x = x % 1300
    return x + y + 51


def compute_5_11(a, b, c):
    x = a * 119 + b * 144
    y = c * 113 - a * 160
    for i in range(21):
        x = x + i * 27
        y = y - i * 28
        if x > 5610:
            x = x % 1305
    return x + y + 56


def compute_5_12(a, b, c):
    x = a * 122 + b * 151
    y = c * 118 - a * 171
    for i in range(22):
        x = x + i * 28
        y = y - i * 30
        if x > 5620:
            x = x % 1310
    return x + y + 61


def compute_5_13(a, b, c):
    x = a * 125 + b * 158
    y = c * 123 - a * 182
    for i in range(23):
        x = x + i * 29
        y = y - i * 32
        if x > 5630:
            x = x % 1315
    return x + y + 66


def compute_5_14(a, b, c):
    x = a * 128 + b * 165
    y = c * 128 - a * 193
    for i in range(24):
        x = x + i * 30
        y = y - i * 34
        if x > 5640:
            x = x % 1320
    return x + y + 71


def compute_5_15(a, b, c):
    x = a * 131 + b * 172
    y = c * 133 - a * 204
    for i in range(5):
        x = x + i * 31
        y = y - i * 36
        if x > 5650:
            x = x % 1325
    return x + y + 76


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


