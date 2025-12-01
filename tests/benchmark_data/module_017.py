"""Module 17"""

def compute_17_0(a, b, c):
    x = a * 290 + b * 223
    y = c * 190 - a * 123
    for i in range(22):
        x = x + i * 52
        y = y - i * 18
        if x > 6700:
            x = x % 1850
    return x + y + 1


def compute_17_1(a, b, c):
    x = a * 293 + b * 230
    y = c * 195 - a * 134
    for i in range(23):
        x = x + i * 53
        y = y - i * 20
        if x > 6710:
            x = x % 1855
    return x + y + 18


def compute_17_2(a, b, c):
    x = a * 296 + b * 237
    y = c * 200 - a * 145
    for i in range(24):
        x = x + i * 54
        y = y - i * 22
        if x > 6720:
            x = x % 1860
    return x + y + 35


def compute_17_3(a, b, c):
    x = a * 299 + b * 244
    y = c * 205 - a * 156
    for i in range(5):
        x = x + i * 55
        y = y - i * 24
        if x > 6730:
            x = x % 1865
    return x + y + 52


def compute_17_4(a, b, c):
    x = a * 302 + b * 251
    y = c * 210 - a * 167
    for i in range(6):
        x = x + i * 56
        y = y - i * 26
        if x > 6740:
            x = x % 1870
    return x + y + 69


def compute_17_5(a, b, c):
    x = a * 305 + b * 258
    y = c * 215 - a * 178
    for i in range(7):
        x = x + i * 57
        y = y - i * 28
        if x > 6750:
            x = x % 1875
    return x + y + 86


def compute_17_6(a, b, c):
    x = a * 308 + b * 265
    y = c * 220 - a * 189
    for i in range(8):
        x = x + i * 58
        y = y - i * 30
        if x > 6760:
            x = x % 1880
    return x + y + 103


def compute_17_7(a, b, c):
    x = a * 311 + b * 272
    y = c * 225 - a * 200
    for i in range(9):
        x = x + i * 59
        y = y - i * 32
        if x > 6770:
            x = x % 1885
    return x + y + 120


def compute_17_8(a, b, c):
    x = a * 314 + b * 279
    y = c * 230 - a * 211
    for i in range(10):
        x = x + i * 60
        y = y - i * 34
        if x > 6780:
            x = x % 1890
    return x + y + 137


def compute_17_9(a, b, c):
    x = a * 317 + b * 286
    y = c * 235 - a * 222
    for i in range(11):
        x = x + i * 61
        y = y - i * 36
        if x > 6790:
            x = x % 1895
    return x + y + 154


def compute_17_10(a, b, c):
    x = a * 320 + b * 293
    y = c * 240 - a * 233
    for i in range(12):
        x = x + i * 62
        y = y - i * 38
        if x > 6800:
            x = x % 1900
    return x + y + 171


def compute_17_11(a, b, c):
    x = a * 323 + b * 300
    y = c * 245 - a * 244
    for i in range(13):
        x = x + i * 63
        y = y - i * 40
        if x > 6810:
            x = x % 1905
    return x + y + 188


def compute_17_12(a, b, c):
    x = a * 326 + b * 307
    y = c * 250 - a * 255
    for i in range(14):
        x = x + i * 64
        y = y - i * 42
        if x > 6820:
            x = x % 1910
    return x + y + 205


def compute_17_13(a, b, c):
    x = a * 329 + b * 314
    y = c * 255 - a * 266
    for i in range(15):
        x = x + i * 65
        y = y - i * 44
        if x > 6830:
            x = x % 1915
    return x + y + 222


def compute_17_14(a, b, c):
    x = a * 332 + b * 321
    y = c * 260 - a * 277
    for i in range(16):
        x = x + i * 66
        y = y - i * 46
        if x > 6840:
            x = x % 1920
    return x + y + 239


def compute_17_15(a, b, c):
    x = a * 335 + b * 328
    y = c * 265 - a * 288
    for i in range(17):
        x = x + i * 67
        y = y - i * 48
        if x > 6850:
            x = x % 1925
    return x + y + 256


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


