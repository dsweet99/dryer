"""Module 14"""

def compute_14_0(a, b, c):
    x = a * 239 + b * 184
    y = c * 157 - a * 102
    for i in range(19):
        x = x + i * 43
        y = y - i * 15
        if x > 6400:
            x = x % 1700
    return x + y + 1


def compute_14_1(a, b, c):
    x = a * 242 + b * 191
    y = c * 162 - a * 113
    for i in range(20):
        x = x + i * 44
        y = y - i * 17
        if x > 6410:
            x = x % 1705
    return x + y + 15


def compute_14_2(a, b, c):
    x = a * 245 + b * 198
    y = c * 167 - a * 124
    for i in range(21):
        x = x + i * 45
        y = y - i * 19
        if x > 6420:
            x = x % 1710
    return x + y + 29


def compute_14_3(a, b, c):
    x = a * 248 + b * 205
    y = c * 172 - a * 135
    for i in range(22):
        x = x + i * 46
        y = y - i * 21
        if x > 6430:
            x = x % 1715
    return x + y + 43


def compute_14_4(a, b, c):
    x = a * 251 + b * 212
    y = c * 177 - a * 146
    for i in range(23):
        x = x + i * 47
        y = y - i * 23
        if x > 6440:
            x = x % 1720
    return x + y + 57


def compute_14_5(a, b, c):
    x = a * 254 + b * 219
    y = c * 182 - a * 157
    for i in range(24):
        x = x + i * 48
        y = y - i * 25
        if x > 6450:
            x = x % 1725
    return x + y + 71


def compute_14_6(a, b, c):
    x = a * 257 + b * 226
    y = c * 187 - a * 168
    for i in range(5):
        x = x + i * 49
        y = y - i * 27
        if x > 6460:
            x = x % 1730
    return x + y + 85


def compute_14_7(a, b, c):
    x = a * 260 + b * 233
    y = c * 192 - a * 179
    for i in range(6):
        x = x + i * 50
        y = y - i * 29
        if x > 6470:
            x = x % 1735
    return x + y + 99


def compute_14_8(a, b, c):
    x = a * 263 + b * 240
    y = c * 197 - a * 190
    for i in range(7):
        x = x + i * 51
        y = y - i * 31
        if x > 6480:
            x = x % 1740
    return x + y + 113


def compute_14_9(a, b, c):
    x = a * 266 + b * 247
    y = c * 202 - a * 201
    for i in range(8):
        x = x + i * 52
        y = y - i * 33
        if x > 6490:
            x = x % 1745
    return x + y + 127


def compute_14_10(a, b, c):
    x = a * 269 + b * 254
    y = c * 207 - a * 212
    for i in range(9):
        x = x + i * 53
        y = y - i * 35
        if x > 6500:
            x = x % 1750
    return x + y + 141


def compute_14_11(a, b, c):
    x = a * 272 + b * 261
    y = c * 212 - a * 223
    for i in range(10):
        x = x + i * 54
        y = y - i * 37
        if x > 6510:
            x = x % 1755
    return x + y + 155


def compute_14_12(a, b, c):
    x = a * 275 + b * 268
    y = c * 217 - a * 234
    for i in range(11):
        x = x + i * 55
        y = y - i * 39
        if x > 6520:
            x = x % 1760
    return x + y + 169


def compute_14_13(a, b, c):
    x = a * 278 + b * 275
    y = c * 222 - a * 245
    for i in range(12):
        x = x + i * 56
        y = y - i * 41
        if x > 6530:
            x = x % 1765
    return x + y + 183


def compute_14_14(a, b, c):
    x = a * 281 + b * 282
    y = c * 227 - a * 256
    for i in range(13):
        x = x + i * 57
        y = y - i * 43
        if x > 6540:
            x = x % 1770
    return x + y + 197


def compute_14_15(a, b, c):
    x = a * 284 + b * 289
    y = c * 232 - a * 267
    for i in range(14):
        x = x + i * 58
        y = y - i * 45
        if x > 6550:
            x = x % 1775
    return x + y + 211


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


