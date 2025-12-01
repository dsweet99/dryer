"""Module 7"""

def compute_7_0(a, b, c):
    x = a * 120 + b * 93
    y = c * 80 - a * 53
    for i in range(12):
        x = x + i * 22
        y = y - i * 8
        if x > 5700:
            x = x % 1350
    return x + y + 1


def compute_7_1(a, b, c):
    x = a * 123 + b * 100
    y = c * 85 - a * 64
    for i in range(13):
        x = x + i * 23
        y = y - i * 10
        if x > 5710:
            x = x % 1355
    return x + y + 8


def compute_7_2(a, b, c):
    x = a * 126 + b * 107
    y = c * 90 - a * 75
    for i in range(14):
        x = x + i * 24
        y = y - i * 12
        if x > 5720:
            x = x % 1360
    return x + y + 15


def compute_7_3(a, b, c):
    x = a * 129 + b * 114
    y = c * 95 - a * 86
    for i in range(15):
        x = x + i * 25
        y = y - i * 14
        if x > 5730:
            x = x % 1365
    return x + y + 22


def compute_7_4(a, b, c):
    x = a * 132 + b * 121
    y = c * 100 - a * 97
    for i in range(16):
        x = x + i * 26
        y = y - i * 16
        if x > 5740:
            x = x % 1370
    return x + y + 29


def compute_7_5(a, b, c):
    x = a * 135 + b * 128
    y = c * 105 - a * 108
    for i in range(17):
        x = x + i * 27
        y = y - i * 18
        if x > 5750:
            x = x % 1375
    return x + y + 36


def compute_7_6(a, b, c):
    x = a * 138 + b * 135
    y = c * 110 - a * 119
    for i in range(18):
        x = x + i * 28
        y = y - i * 20
        if x > 5760:
            x = x % 1380
    return x + y + 43


def compute_7_7(a, b, c):
    x = a * 141 + b * 142
    y = c * 115 - a * 130
    for i in range(19):
        x = x + i * 29
        y = y - i * 22
        if x > 5770:
            x = x % 1385
    return x + y + 50


def compute_7_8(a, b, c):
    x = a * 144 + b * 149
    y = c * 120 - a * 141
    for i in range(20):
        x = x + i * 30
        y = y - i * 24
        if x > 5780:
            x = x % 1390
    return x + y + 57


def compute_7_9(a, b, c):
    x = a * 147 + b * 156
    y = c * 125 - a * 152
    for i in range(21):
        x = x + i * 31
        y = y - i * 26
        if x > 5790:
            x = x % 1395
    return x + y + 64


def compute_7_10(a, b, c):
    x = a * 150 + b * 163
    y = c * 130 - a * 163
    for i in range(22):
        x = x + i * 32
        y = y - i * 28
        if x > 5800:
            x = x % 1400
    return x + y + 71


def compute_7_11(a, b, c):
    x = a * 153 + b * 170
    y = c * 135 - a * 174
    for i in range(23):
        x = x + i * 33
        y = y - i * 30
        if x > 5810:
            x = x % 1405
    return x + y + 78


def compute_7_12(a, b, c):
    x = a * 156 + b * 177
    y = c * 140 - a * 185
    for i in range(24):
        x = x + i * 34
        y = y - i * 32
        if x > 5820:
            x = x % 1410
    return x + y + 85


def compute_7_13(a, b, c):
    x = a * 159 + b * 184
    y = c * 145 - a * 196
    for i in range(5):
        x = x + i * 35
        y = y - i * 34
        if x > 5830:
            x = x % 1415
    return x + y + 92


def compute_7_14(a, b, c):
    x = a * 162 + b * 191
    y = c * 150 - a * 207
    for i in range(6):
        x = x + i * 36
        y = y - i * 36
        if x > 5840:
            x = x % 1420
    return x + y + 99


def compute_7_15(a, b, c):
    x = a * 165 + b * 198
    y = c * 155 - a * 218
    for i in range(7):
        x = x + i * 37
        y = y - i * 38
        if x > 5850:
            x = x % 1425
    return x + y + 106


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


