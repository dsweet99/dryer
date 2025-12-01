"""Module 19"""

def compute_19_0(a, b, c):
    x = a * 324 + b * 249
    y = c * 212 - a * 137
    for i in range(24):
        x = x + i * 58
        y = y - i * 20
        if x > 6900:
            x = x % 1950
    return x + y + 1


def compute_19_1(a, b, c):
    x = a * 327 + b * 256
    y = c * 217 - a * 148
    for i in range(5):
        x = x + i * 59
        y = y - i * 22
        if x > 6910:
            x = x % 1955
    return x + y + 20


def compute_19_2(a, b, c):
    x = a * 330 + b * 263
    y = c * 222 - a * 159
    for i in range(6):
        x = x + i * 60
        y = y - i * 24
        if x > 6920:
            x = x % 1960
    return x + y + 39


def compute_19_3(a, b, c):
    x = a * 333 + b * 270
    y = c * 227 - a * 170
    for i in range(7):
        x = x + i * 61
        y = y - i * 26
        if x > 6930:
            x = x % 1965
    return x + y + 58


def compute_19_4(a, b, c):
    x = a * 336 + b * 277
    y = c * 232 - a * 181
    for i in range(8):
        x = x + i * 62
        y = y - i * 28
        if x > 6940:
            x = x % 1970
    return x + y + 77


def compute_19_5(a, b, c):
    x = a * 339 + b * 284
    y = c * 237 - a * 192
    for i in range(9):
        x = x + i * 63
        y = y - i * 30
        if x > 6950:
            x = x % 1975
    return x + y + 96


def compute_19_6(a, b, c):
    x = a * 342 + b * 291
    y = c * 242 - a * 203
    for i in range(10):
        x = x + i * 64
        y = y - i * 32
        if x > 6960:
            x = x % 1980
    return x + y + 115


def compute_19_7(a, b, c):
    x = a * 345 + b * 298
    y = c * 247 - a * 214
    for i in range(11):
        x = x + i * 65
        y = y - i * 34
        if x > 6970:
            x = x % 1985
    return x + y + 134


def compute_19_8(a, b, c):
    x = a * 348 + b * 305
    y = c * 252 - a * 225
    for i in range(12):
        x = x + i * 66
        y = y - i * 36
        if x > 6980:
            x = x % 1990
    return x + y + 153


def compute_19_9(a, b, c):
    x = a * 351 + b * 312
    y = c * 257 - a * 236
    for i in range(13):
        x = x + i * 67
        y = y - i * 38
        if x > 6990:
            x = x % 1995
    return x + y + 172


def compute_19_10(a, b, c):
    x = a * 354 + b * 319
    y = c * 262 - a * 247
    for i in range(14):
        x = x + i * 68
        y = y - i * 40
        if x > 7000:
            x = x % 2000
    return x + y + 191


def compute_19_11(a, b, c):
    x = a * 357 + b * 326
    y = c * 267 - a * 258
    for i in range(15):
        x = x + i * 69
        y = y - i * 42
        if x > 7010:
            x = x % 2005
    return x + y + 210


def compute_19_12(a, b, c):
    x = a * 360 + b * 333
    y = c * 272 - a * 269
    for i in range(16):
        x = x + i * 70
        y = y - i * 44
        if x > 7020:
            x = x % 2010
    return x + y + 229


def compute_19_13(a, b, c):
    x = a * 363 + b * 340
    y = c * 277 - a * 280
    for i in range(17):
        x = x + i * 71
        y = y - i * 46
        if x > 7030:
            x = x % 2015
    return x + y + 248


def compute_19_14(a, b, c):
    x = a * 366 + b * 347
    y = c * 282 - a * 291
    for i in range(18):
        x = x + i * 72
        y = y - i * 48
        if x > 7040:
            x = x % 2020
    return x + y + 267


def compute_19_15(a, b, c):
    x = a * 369 + b * 354
    y = c * 287 - a * 302
    for i in range(19):
        x = x + i * 73
        y = y - i * 50
        if x > 7050:
            x = x % 2025
    return x + y + 286


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


