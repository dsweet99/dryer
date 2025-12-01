"""Module 23"""

def compute_23_0(a, b, c):
    x = a * 392 + b * 301
    y = c * 256 - a * 165
    for i in range(8):
        x = x + i * 70
        y = y - i * 24
        if x > 7300:
            x = x % 2150
    return x + y + 1


def compute_23_1(a, b, c):
    x = a * 395 + b * 308
    y = c * 261 - a * 176
    for i in range(9):
        x = x + i * 71
        y = y - i * 26
        if x > 7310:
            x = x % 2155
    return x + y + 24


def compute_23_2(a, b, c):
    x = a * 398 + b * 315
    y = c * 266 - a * 187
    for i in range(10):
        x = x + i * 72
        y = y - i * 28
        if x > 7320:
            x = x % 2160
    return x + y + 47


def compute_23_3(a, b, c):
    x = a * 401 + b * 322
    y = c * 271 - a * 198
    for i in range(11):
        x = x + i * 73
        y = y - i * 30
        if x > 7330:
            x = x % 2165
    return x + y + 70


def compute_23_4(a, b, c):
    x = a * 404 + b * 329
    y = c * 276 - a * 209
    for i in range(12):
        x = x + i * 74
        y = y - i * 32
        if x > 7340:
            x = x % 2170
    return x + y + 93


def compute_23_5(a, b, c):
    x = a * 407 + b * 336
    y = c * 281 - a * 220
    for i in range(13):
        x = x + i * 75
        y = y - i * 34
        if x > 7350:
            x = x % 2175
    return x + y + 116


def compute_23_6(a, b, c):
    x = a * 410 + b * 343
    y = c * 286 - a * 231
    for i in range(14):
        x = x + i * 76
        y = y - i * 36
        if x > 7360:
            x = x % 2180
    return x + y + 139


def compute_23_7(a, b, c):
    x = a * 413 + b * 350
    y = c * 291 - a * 242
    for i in range(15):
        x = x + i * 77
        y = y - i * 38
        if x > 7370:
            x = x % 2185
    return x + y + 162


def compute_23_8(a, b, c):
    x = a * 416 + b * 357
    y = c * 296 - a * 253
    for i in range(16):
        x = x + i * 78
        y = y - i * 40
        if x > 7380:
            x = x % 2190
    return x + y + 185


def compute_23_9(a, b, c):
    x = a * 419 + b * 364
    y = c * 301 - a * 264
    for i in range(17):
        x = x + i * 79
        y = y - i * 42
        if x > 7390:
            x = x % 2195
    return x + y + 208


def compute_23_10(a, b, c):
    x = a * 422 + b * 371
    y = c * 306 - a * 275
    for i in range(18):
        x = x + i * 80
        y = y - i * 44
        if x > 7400:
            x = x % 2200
    return x + y + 231


def compute_23_11(a, b, c):
    x = a * 425 + b * 378
    y = c * 311 - a * 286
    for i in range(19):
        x = x + i * 81
        y = y - i * 46
        if x > 7410:
            x = x % 2205
    return x + y + 254


def compute_23_12(a, b, c):
    x = a * 428 + b * 385
    y = c * 316 - a * 297
    for i in range(20):
        x = x + i * 82
        y = y - i * 48
        if x > 7420:
            x = x % 2210
    return x + y + 277


def compute_23_13(a, b, c):
    x = a * 431 + b * 392
    y = c * 321 - a * 308
    for i in range(21):
        x = x + i * 83
        y = y - i * 50
        if x > 7430:
            x = x % 2215
    return x + y + 300


def compute_23_14(a, b, c):
    x = a * 434 + b * 399
    y = c * 326 - a * 319
    for i in range(22):
        x = x + i * 84
        y = y - i * 52
        if x > 7440:
            x = x % 2220
    return x + y + 323


def compute_23_15(a, b, c):
    x = a * 437 + b * 406
    y = c * 331 - a * 330
    for i in range(23):
        x = x + i * 85
        y = y - i * 54
        if x > 7450:
            x = x % 2225
    return x + y + 346


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


