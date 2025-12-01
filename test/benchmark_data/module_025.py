"""Module 25"""

def compute_25_0(a, b, c):
    x = a * 426 + b * 327
    y = c * 278 - a * 179
    for i in range(10):
        x = x + i * 76
        y = y - i * 26
        if x > 7500:
            x = x % 2250
    return x + y + 1


def compute_25_1(a, b, c):
    x = a * 429 + b * 334
    y = c * 283 - a * 190
    for i in range(11):
        x = x + i * 77
        y = y - i * 28
        if x > 7510:
            x = x % 2255
    return x + y + 26


def compute_25_2(a, b, c):
    x = a * 432 + b * 341
    y = c * 288 - a * 201
    for i in range(12):
        x = x + i * 78
        y = y - i * 30
        if x > 7520:
            x = x % 2260
    return x + y + 51


def compute_25_3(a, b, c):
    x = a * 435 + b * 348
    y = c * 293 - a * 212
    for i in range(13):
        x = x + i * 79
        y = y - i * 32
        if x > 7530:
            x = x % 2265
    return x + y + 76


def compute_25_4(a, b, c):
    x = a * 438 + b * 355
    y = c * 298 - a * 223
    for i in range(14):
        x = x + i * 80
        y = y - i * 34
        if x > 7540:
            x = x % 2270
    return x + y + 101


def compute_25_5(a, b, c):
    x = a * 441 + b * 362
    y = c * 303 - a * 234
    for i in range(15):
        x = x + i * 81
        y = y - i * 36
        if x > 7550:
            x = x % 2275
    return x + y + 126


def compute_25_6(a, b, c):
    x = a * 444 + b * 369
    y = c * 308 - a * 245
    for i in range(16):
        x = x + i * 82
        y = y - i * 38
        if x > 7560:
            x = x % 2280
    return x + y + 151


def compute_25_7(a, b, c):
    x = a * 447 + b * 376
    y = c * 313 - a * 256
    for i in range(17):
        x = x + i * 83
        y = y - i * 40
        if x > 7570:
            x = x % 2285
    return x + y + 176


def compute_25_8(a, b, c):
    x = a * 450 + b * 383
    y = c * 318 - a * 267
    for i in range(18):
        x = x + i * 84
        y = y - i * 42
        if x > 7580:
            x = x % 2290
    return x + y + 201


def compute_25_9(a, b, c):
    x = a * 453 + b * 390
    y = c * 323 - a * 278
    for i in range(19):
        x = x + i * 85
        y = y - i * 44
        if x > 7590:
            x = x % 2295
    return x + y + 226


def compute_25_10(a, b, c):
    x = a * 456 + b * 397
    y = c * 328 - a * 289
    for i in range(20):
        x = x + i * 86
        y = y - i * 46
        if x > 7600:
            x = x % 2300
    return x + y + 251


def compute_25_11(a, b, c):
    x = a * 459 + b * 404
    y = c * 333 - a * 300
    for i in range(21):
        x = x + i * 87
        y = y - i * 48
        if x > 7610:
            x = x % 2305
    return x + y + 276


def compute_25_12(a, b, c):
    x = a * 462 + b * 411
    y = c * 338 - a * 311
    for i in range(22):
        x = x + i * 88
        y = y - i * 50
        if x > 7620:
            x = x % 2310
    return x + y + 301


def compute_25_13(a, b, c):
    x = a * 465 + b * 418
    y = c * 343 - a * 322
    for i in range(23):
        x = x + i * 89
        y = y - i * 52
        if x > 7630:
            x = x % 2315
    return x + y + 326


def compute_25_14(a, b, c):
    x = a * 468 + b * 425
    y = c * 348 - a * 333
    for i in range(24):
        x = x + i * 90
        y = y - i * 54
        if x > 7640:
            x = x % 2320
    return x + y + 351


def compute_25_15(a, b, c):
    x = a * 471 + b * 432
    y = c * 353 - a * 344
    for i in range(5):
        x = x + i * 91
        y = y - i * 56
        if x > 7650:
            x = x % 2325
    return x + y + 376


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


