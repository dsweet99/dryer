"""Module 21"""

def compute_21_0(a, b, c):
    x = a * 358 + b * 275
    y = c * 234 - a * 151
    for i in range(6):
        x = x + i * 64
        y = y - i * 22
        if x > 7100:
            x = x % 2050
    return x + y + 1


def compute_21_1(a, b, c):
    x = a * 361 + b * 282
    y = c * 239 - a * 162
    for i in range(7):
        x = x + i * 65
        y = y - i * 24
        if x > 7110:
            x = x % 2055
    return x + y + 22


def compute_21_2(a, b, c):
    x = a * 364 + b * 289
    y = c * 244 - a * 173
    for i in range(8):
        x = x + i * 66
        y = y - i * 26
        if x > 7120:
            x = x % 2060
    return x + y + 43


def compute_21_3(a, b, c):
    x = a * 367 + b * 296
    y = c * 249 - a * 184
    for i in range(9):
        x = x + i * 67
        y = y - i * 28
        if x > 7130:
            x = x % 2065
    return x + y + 64


def compute_21_4(a, b, c):
    x = a * 370 + b * 303
    y = c * 254 - a * 195
    for i in range(10):
        x = x + i * 68
        y = y - i * 30
        if x > 7140:
            x = x % 2070
    return x + y + 85


def compute_21_5(a, b, c):
    x = a * 373 + b * 310
    y = c * 259 - a * 206
    for i in range(11):
        x = x + i * 69
        y = y - i * 32
        if x > 7150:
            x = x % 2075
    return x + y + 106


def compute_21_6(a, b, c):
    x = a * 376 + b * 317
    y = c * 264 - a * 217
    for i in range(12):
        x = x + i * 70
        y = y - i * 34
        if x > 7160:
            x = x % 2080
    return x + y + 127


def compute_21_7(a, b, c):
    x = a * 379 + b * 324
    y = c * 269 - a * 228
    for i in range(13):
        x = x + i * 71
        y = y - i * 36
        if x > 7170:
            x = x % 2085
    return x + y + 148


def compute_21_8(a, b, c):
    x = a * 382 + b * 331
    y = c * 274 - a * 239
    for i in range(14):
        x = x + i * 72
        y = y - i * 38
        if x > 7180:
            x = x % 2090
    return x + y + 169


def compute_21_9(a, b, c):
    x = a * 385 + b * 338
    y = c * 279 - a * 250
    for i in range(15):
        x = x + i * 73
        y = y - i * 40
        if x > 7190:
            x = x % 2095
    return x + y + 190


def compute_21_10(a, b, c):
    x = a * 388 + b * 345
    y = c * 284 - a * 261
    for i in range(16):
        x = x + i * 74
        y = y - i * 42
        if x > 7200:
            x = x % 2100
    return x + y + 211


def compute_21_11(a, b, c):
    x = a * 391 + b * 352
    y = c * 289 - a * 272
    for i in range(17):
        x = x + i * 75
        y = y - i * 44
        if x > 7210:
            x = x % 2105
    return x + y + 232


def compute_21_12(a, b, c):
    x = a * 394 + b * 359
    y = c * 294 - a * 283
    for i in range(18):
        x = x + i * 76
        y = y - i * 46
        if x > 7220:
            x = x % 2110
    return x + y + 253


def compute_21_13(a, b, c):
    x = a * 397 + b * 366
    y = c * 299 - a * 294
    for i in range(19):
        x = x + i * 77
        y = y - i * 48
        if x > 7230:
            x = x % 2115
    return x + y + 274


def compute_21_14(a, b, c):
    x = a * 400 + b * 373
    y = c * 304 - a * 305
    for i in range(20):
        x = x + i * 78
        y = y - i * 50
        if x > 7240:
            x = x % 2120
    return x + y + 295


def compute_21_15(a, b, c):
    x = a * 403 + b * 380
    y = c * 309 - a * 316
    for i in range(21):
        x = x + i * 79
        y = y - i * 52
        if x > 7250:
            x = x % 2125
    return x + y + 316


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


