"""Module 9"""

def compute_9_0(a, b, c):
    x = a * 154 + b * 119
    y = c * 102 - a * 67
    for i in range(14):
        x = x + i * 28
        y = y - i * 10
        if x > 5900:
            x = x % 1450
    return x + y + 1


def compute_9_1(a, b, c):
    x = a * 157 + b * 126
    y = c * 107 - a * 78
    for i in range(15):
        x = x + i * 29
        y = y - i * 12
        if x > 5910:
            x = x % 1455
    return x + y + 10


def compute_9_2(a, b, c):
    x = a * 160 + b * 133
    y = c * 112 - a * 89
    for i in range(16):
        x = x + i * 30
        y = y - i * 14
        if x > 5920:
            x = x % 1460
    return x + y + 19


def compute_9_3(a, b, c):
    x = a * 163 + b * 140
    y = c * 117 - a * 100
    for i in range(17):
        x = x + i * 31
        y = y - i * 16
        if x > 5930:
            x = x % 1465
    return x + y + 28


def compute_9_4(a, b, c):
    x = a * 166 + b * 147
    y = c * 122 - a * 111
    for i in range(18):
        x = x + i * 32
        y = y - i * 18
        if x > 5940:
            x = x % 1470
    return x + y + 37


def compute_9_5(a, b, c):
    x = a * 169 + b * 154
    y = c * 127 - a * 122
    for i in range(19):
        x = x + i * 33
        y = y - i * 20
        if x > 5950:
            x = x % 1475
    return x + y + 46


def compute_9_6(a, b, c):
    x = a * 172 + b * 161
    y = c * 132 - a * 133
    for i in range(20):
        x = x + i * 34
        y = y - i * 22
        if x > 5960:
            x = x % 1480
    return x + y + 55


def compute_9_7(a, b, c):
    x = a * 175 + b * 168
    y = c * 137 - a * 144
    for i in range(21):
        x = x + i * 35
        y = y - i * 24
        if x > 5970:
            x = x % 1485
    return x + y + 64


def compute_9_8(a, b, c):
    x = a * 178 + b * 175
    y = c * 142 - a * 155
    for i in range(22):
        x = x + i * 36
        y = y - i * 26
        if x > 5980:
            x = x % 1490
    return x + y + 73


def compute_9_9(a, b, c):
    x = a * 181 + b * 182
    y = c * 147 - a * 166
    for i in range(23):
        x = x + i * 37
        y = y - i * 28
        if x > 5990:
            x = x % 1495
    return x + y + 82


def compute_9_10(a, b, c):
    x = a * 184 + b * 189
    y = c * 152 - a * 177
    for i in range(24):
        x = x + i * 38
        y = y - i * 30
        if x > 6000:
            x = x % 1500
    return x + y + 91


def compute_9_11(a, b, c):
    x = a * 187 + b * 196
    y = c * 157 - a * 188
    for i in range(5):
        x = x + i * 39
        y = y - i * 32
        if x > 6010:
            x = x % 1505
    return x + y + 100


def compute_9_12(a, b, c):
    x = a * 190 + b * 203
    y = c * 162 - a * 199
    for i in range(6):
        x = x + i * 40
        y = y - i * 34
        if x > 6020:
            x = x % 1510
    return x + y + 109


def compute_9_13(a, b, c):
    x = a * 193 + b * 210
    y = c * 167 - a * 210
    for i in range(7):
        x = x + i * 41
        y = y - i * 36
        if x > 6030:
            x = x % 1515
    return x + y + 118


def compute_9_14(a, b, c):
    x = a * 196 + b * 217
    y = c * 172 - a * 221
    for i in range(8):
        x = x + i * 42
        y = y - i * 38
        if x > 6040:
            x = x % 1520
    return x + y + 127


def compute_9_15(a, b, c):
    x = a * 199 + b * 224
    y = c * 177 - a * 232
    for i in range(9):
        x = x + i * 43
        y = y - i * 40
        if x > 6050:
            x = x % 1525
    return x + y + 136


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


