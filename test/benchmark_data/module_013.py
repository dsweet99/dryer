"""Module 13"""

def compute_13_0(a, b, c):
    x = a * 222 + b * 171
    y = c * 146 - a * 95
    for i in range(18):
        x = x + i * 40
        y = y - i * 14
        if x > 6300:
            x = x % 1650
    return x + y + 1


def compute_13_1(a, b, c):
    x = a * 225 + b * 178
    y = c * 151 - a * 106
    for i in range(19):
        x = x + i * 41
        y = y - i * 16
        if x > 6310:
            x = x % 1655
    return x + y + 14


def compute_13_2(a, b, c):
    x = a * 228 + b * 185
    y = c * 156 - a * 117
    for i in range(20):
        x = x + i * 42
        y = y - i * 18
        if x > 6320:
            x = x % 1660
    return x + y + 27


def compute_13_3(a, b, c):
    x = a * 231 + b * 192
    y = c * 161 - a * 128
    for i in range(21):
        x = x + i * 43
        y = y - i * 20
        if x > 6330:
            x = x % 1665
    return x + y + 40


def compute_13_4(a, b, c):
    x = a * 234 + b * 199
    y = c * 166 - a * 139
    for i in range(22):
        x = x + i * 44
        y = y - i * 22
        if x > 6340:
            x = x % 1670
    return x + y + 53


def compute_13_5(a, b, c):
    x = a * 237 + b * 206
    y = c * 171 - a * 150
    for i in range(23):
        x = x + i * 45
        y = y - i * 24
        if x > 6350:
            x = x % 1675
    return x + y + 66


def compute_13_6(a, b, c):
    x = a * 240 + b * 213
    y = c * 176 - a * 161
    for i in range(24):
        x = x + i * 46
        y = y - i * 26
        if x > 6360:
            x = x % 1680
    return x + y + 79


def compute_13_7(a, b, c):
    x = a * 243 + b * 220
    y = c * 181 - a * 172
    for i in range(5):
        x = x + i * 47
        y = y - i * 28
        if x > 6370:
            x = x % 1685
    return x + y + 92


def compute_13_8(a, b, c):
    x = a * 246 + b * 227
    y = c * 186 - a * 183
    for i in range(6):
        x = x + i * 48
        y = y - i * 30
        if x > 6380:
            x = x % 1690
    return x + y + 105


def compute_13_9(a, b, c):
    x = a * 249 + b * 234
    y = c * 191 - a * 194
    for i in range(7):
        x = x + i * 49
        y = y - i * 32
        if x > 6390:
            x = x % 1695
    return x + y + 118


def compute_13_10(a, b, c):
    x = a * 252 + b * 241
    y = c * 196 - a * 205
    for i in range(8):
        x = x + i * 50
        y = y - i * 34
        if x > 6400:
            x = x % 1700
    return x + y + 131


def compute_13_11(a, b, c):
    x = a * 255 + b * 248
    y = c * 201 - a * 216
    for i in range(9):
        x = x + i * 51
        y = y - i * 36
        if x > 6410:
            x = x % 1705
    return x + y + 144


def compute_13_12(a, b, c):
    x = a * 258 + b * 255
    y = c * 206 - a * 227
    for i in range(10):
        x = x + i * 52
        y = y - i * 38
        if x > 6420:
            x = x % 1710
    return x + y + 157


def compute_13_13(a, b, c):
    x = a * 261 + b * 262
    y = c * 211 - a * 238
    for i in range(11):
        x = x + i * 53
        y = y - i * 40
        if x > 6430:
            x = x % 1715
    return x + y + 170


def compute_13_14(a, b, c):
    x = a * 264 + b * 269
    y = c * 216 - a * 249
    for i in range(12):
        x = x + i * 54
        y = y - i * 42
        if x > 6440:
            x = x % 1720
    return x + y + 183


def compute_13_15(a, b, c):
    x = a * 267 + b * 276
    y = c * 221 - a * 260
    for i in range(13):
        x = x + i * 55
        y = y - i * 44
        if x > 6450:
            x = x % 1725
    return x + y + 196


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


