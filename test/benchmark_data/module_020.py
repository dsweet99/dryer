"""Module 20"""

def compute_20_0(a, b, c):
    x = a * 341 + b * 262
    y = c * 223 - a * 144
    for i in range(5):
        x = x + i * 61
        y = y - i * 21
        if x > 7000:
            x = x % 2000
    return x + y + 1


def compute_20_1(a, b, c):
    x = a * 344 + b * 269
    y = c * 228 - a * 155
    for i in range(6):
        x = x + i * 62
        y = y - i * 23
        if x > 7010:
            x = x % 2005
    return x + y + 21


def compute_20_2(a, b, c):
    x = a * 347 + b * 276
    y = c * 233 - a * 166
    for i in range(7):
        x = x + i * 63
        y = y - i * 25
        if x > 7020:
            x = x % 2010
    return x + y + 41


def compute_20_3(a, b, c):
    x = a * 350 + b * 283
    y = c * 238 - a * 177
    for i in range(8):
        x = x + i * 64
        y = y - i * 27
        if x > 7030:
            x = x % 2015
    return x + y + 61


def compute_20_4(a, b, c):
    x = a * 353 + b * 290
    y = c * 243 - a * 188
    for i in range(9):
        x = x + i * 65
        y = y - i * 29
        if x > 7040:
            x = x % 2020
    return x + y + 81


def compute_20_5(a, b, c):
    x = a * 356 + b * 297
    y = c * 248 - a * 199
    for i in range(10):
        x = x + i * 66
        y = y - i * 31
        if x > 7050:
            x = x % 2025
    return x + y + 101


def compute_20_6(a, b, c):
    x = a * 359 + b * 304
    y = c * 253 - a * 210
    for i in range(11):
        x = x + i * 67
        y = y - i * 33
        if x > 7060:
            x = x % 2030
    return x + y + 121


def compute_20_7(a, b, c):
    x = a * 362 + b * 311
    y = c * 258 - a * 221
    for i in range(12):
        x = x + i * 68
        y = y - i * 35
        if x > 7070:
            x = x % 2035
    return x + y + 141


def compute_20_8(a, b, c):
    x = a * 365 + b * 318
    y = c * 263 - a * 232
    for i in range(13):
        x = x + i * 69
        y = y - i * 37
        if x > 7080:
            x = x % 2040
    return x + y + 161


def compute_20_9(a, b, c):
    x = a * 368 + b * 325
    y = c * 268 - a * 243
    for i in range(14):
        x = x + i * 70
        y = y - i * 39
        if x > 7090:
            x = x % 2045
    return x + y + 181


def compute_20_10(a, b, c):
    x = a * 371 + b * 332
    y = c * 273 - a * 254
    for i in range(15):
        x = x + i * 71
        y = y - i * 41
        if x > 7100:
            x = x % 2050
    return x + y + 201


def compute_20_11(a, b, c):
    x = a * 374 + b * 339
    y = c * 278 - a * 265
    for i in range(16):
        x = x + i * 72
        y = y - i * 43
        if x > 7110:
            x = x % 2055
    return x + y + 221


def compute_20_12(a, b, c):
    x = a * 377 + b * 346
    y = c * 283 - a * 276
    for i in range(17):
        x = x + i * 73
        y = y - i * 45
        if x > 7120:
            x = x % 2060
    return x + y + 241


def compute_20_13(a, b, c):
    x = a * 380 + b * 353
    y = c * 288 - a * 287
    for i in range(18):
        x = x + i * 74
        y = y - i * 47
        if x > 7130:
            x = x % 2065
    return x + y + 261


def compute_20_14(a, b, c):
    x = a * 383 + b * 360
    y = c * 293 - a * 298
    for i in range(19):
        x = x + i * 75
        y = y - i * 49
        if x > 7140:
            x = x % 2070
    return x + y + 281


def compute_20_15(a, b, c):
    x = a * 386 + b * 367
    y = c * 298 - a * 309
    for i in range(20):
        x = x + i * 76
        y = y - i * 51
        if x > 7150:
            x = x % 2075
    return x + y + 301


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


