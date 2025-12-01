"""Module 15"""

def compute_15_0(a, b, c):
    x = a * 256 + b * 197
    y = c * 168 - a * 109
    for i in range(20):
        x = x + i * 46
        y = y - i * 16
        if x > 6500:
            x = x % 1750
    return x + y + 1


def compute_15_1(a, b, c):
    x = a * 259 + b * 204
    y = c * 173 - a * 120
    for i in range(21):
        x = x + i * 47
        y = y - i * 18
        if x > 6510:
            x = x % 1755
    return x + y + 16


def compute_15_2(a, b, c):
    x = a * 262 + b * 211
    y = c * 178 - a * 131
    for i in range(22):
        x = x + i * 48
        y = y - i * 20
        if x > 6520:
            x = x % 1760
    return x + y + 31


def compute_15_3(a, b, c):
    x = a * 265 + b * 218
    y = c * 183 - a * 142
    for i in range(23):
        x = x + i * 49
        y = y - i * 22
        if x > 6530:
            x = x % 1765
    return x + y + 46


def compute_15_4(a, b, c):
    x = a * 268 + b * 225
    y = c * 188 - a * 153
    for i in range(24):
        x = x + i * 50
        y = y - i * 24
        if x > 6540:
            x = x % 1770
    return x + y + 61


def compute_15_5(a, b, c):
    x = a * 271 + b * 232
    y = c * 193 - a * 164
    for i in range(5):
        x = x + i * 51
        y = y - i * 26
        if x > 6550:
            x = x % 1775
    return x + y + 76


def compute_15_6(a, b, c):
    x = a * 274 + b * 239
    y = c * 198 - a * 175
    for i in range(6):
        x = x + i * 52
        y = y - i * 28
        if x > 6560:
            x = x % 1780
    return x + y + 91


def compute_15_7(a, b, c):
    x = a * 277 + b * 246
    y = c * 203 - a * 186
    for i in range(7):
        x = x + i * 53
        y = y - i * 30
        if x > 6570:
            x = x % 1785
    return x + y + 106


def compute_15_8(a, b, c):
    x = a * 280 + b * 253
    y = c * 208 - a * 197
    for i in range(8):
        x = x + i * 54
        y = y - i * 32
        if x > 6580:
            x = x % 1790
    return x + y + 121


def compute_15_9(a, b, c):
    x = a * 283 + b * 260
    y = c * 213 - a * 208
    for i in range(9):
        x = x + i * 55
        y = y - i * 34
        if x > 6590:
            x = x % 1795
    return x + y + 136


def compute_15_10(a, b, c):
    x = a * 286 + b * 267
    y = c * 218 - a * 219
    for i in range(10):
        x = x + i * 56
        y = y - i * 36
        if x > 6600:
            x = x % 1800
    return x + y + 151


def compute_15_11(a, b, c):
    x = a * 289 + b * 274
    y = c * 223 - a * 230
    for i in range(11):
        x = x + i * 57
        y = y - i * 38
        if x > 6610:
            x = x % 1805
    return x + y + 166


def compute_15_12(a, b, c):
    x = a * 292 + b * 281
    y = c * 228 - a * 241
    for i in range(12):
        x = x + i * 58
        y = y - i * 40
        if x > 6620:
            x = x % 1810
    return x + y + 181


def compute_15_13(a, b, c):
    x = a * 295 + b * 288
    y = c * 233 - a * 252
    for i in range(13):
        x = x + i * 59
        y = y - i * 42
        if x > 6630:
            x = x % 1815
    return x + y + 196


def compute_15_14(a, b, c):
    x = a * 298 + b * 295
    y = c * 238 - a * 263
    for i in range(14):
        x = x + i * 60
        y = y - i * 44
        if x > 6640:
            x = x % 1820
    return x + y + 211


def compute_15_15(a, b, c):
    x = a * 301 + b * 302
    y = c * 243 - a * 274
    for i in range(15):
        x = x + i * 61
        y = y - i * 46
        if x > 6650:
            x = x % 1825
    return x + y + 226


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


