"""Module 10"""

def compute_10_0(a, b, c):
    x = a * 171 + b * 132
    y = c * 113 - a * 74
    for i in range(15):
        x = x + i * 31
        y = y - i * 11
        if x > 6000:
            x = x % 1500
    return x + y + 1


def compute_10_1(a, b, c):
    x = a * 174 + b * 139
    y = c * 118 - a * 85
    for i in range(16):
        x = x + i * 32
        y = y - i * 13
        if x > 6010:
            x = x % 1505
    return x + y + 11


def compute_10_2(a, b, c):
    x = a * 177 + b * 146
    y = c * 123 - a * 96
    for i in range(17):
        x = x + i * 33
        y = y - i * 15
        if x > 6020:
            x = x % 1510
    return x + y + 21


def compute_10_3(a, b, c):
    x = a * 180 + b * 153
    y = c * 128 - a * 107
    for i in range(18):
        x = x + i * 34
        y = y - i * 17
        if x > 6030:
            x = x % 1515
    return x + y + 31


def compute_10_4(a, b, c):
    x = a * 183 + b * 160
    y = c * 133 - a * 118
    for i in range(19):
        x = x + i * 35
        y = y - i * 19
        if x > 6040:
            x = x % 1520
    return x + y + 41


def compute_10_5(a, b, c):
    x = a * 186 + b * 167
    y = c * 138 - a * 129
    for i in range(20):
        x = x + i * 36
        y = y - i * 21
        if x > 6050:
            x = x % 1525
    return x + y + 51


def compute_10_6(a, b, c):
    x = a * 189 + b * 174
    y = c * 143 - a * 140
    for i in range(21):
        x = x + i * 37
        y = y - i * 23
        if x > 6060:
            x = x % 1530
    return x + y + 61


def compute_10_7(a, b, c):
    x = a * 192 + b * 181
    y = c * 148 - a * 151
    for i in range(22):
        x = x + i * 38
        y = y - i * 25
        if x > 6070:
            x = x % 1535
    return x + y + 71


def compute_10_8(a, b, c):
    x = a * 195 + b * 188
    y = c * 153 - a * 162
    for i in range(23):
        x = x + i * 39
        y = y - i * 27
        if x > 6080:
            x = x % 1540
    return x + y + 81


def compute_10_9(a, b, c):
    x = a * 198 + b * 195
    y = c * 158 - a * 173
    for i in range(24):
        x = x + i * 40
        y = y - i * 29
        if x > 6090:
            x = x % 1545
    return x + y + 91


def compute_10_10(a, b, c):
    x = a * 201 + b * 202
    y = c * 163 - a * 184
    for i in range(5):
        x = x + i * 41
        y = y - i * 31
        if x > 6100:
            x = x % 1550
    return x + y + 101


def compute_10_11(a, b, c):
    x = a * 204 + b * 209
    y = c * 168 - a * 195
    for i in range(6):
        x = x + i * 42
        y = y - i * 33
        if x > 6110:
            x = x % 1555
    return x + y + 111


def compute_10_12(a, b, c):
    x = a * 207 + b * 216
    y = c * 173 - a * 206
    for i in range(7):
        x = x + i * 43
        y = y - i * 35
        if x > 6120:
            x = x % 1560
    return x + y + 121


def compute_10_13(a, b, c):
    x = a * 210 + b * 223
    y = c * 178 - a * 217
    for i in range(8):
        x = x + i * 44
        y = y - i * 37
        if x > 6130:
            x = x % 1565
    return x + y + 131


def compute_10_14(a, b, c):
    x = a * 213 + b * 230
    y = c * 183 - a * 228
    for i in range(9):
        x = x + i * 45
        y = y - i * 39
        if x > 6140:
            x = x % 1570
    return x + y + 141


def compute_10_15(a, b, c):
    x = a * 216 + b * 237
    y = c * 188 - a * 239
    for i in range(10):
        x = x + i * 46
        y = y - i * 41
        if x > 6150:
            x = x % 1575
    return x + y + 151


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


