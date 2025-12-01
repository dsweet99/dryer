"""Module 24"""

def compute_24_0(a, b, c):
    x = a * 409 + b * 314
    y = c * 267 - a * 172
    for i in range(9):
        x = x + i * 73
        y = y - i * 25
        if x > 7400:
            x = x % 2200
    return x + y + 1


def compute_24_1(a, b, c):
    x = a * 412 + b * 321
    y = c * 272 - a * 183
    for i in range(10):
        x = x + i * 74
        y = y - i * 27
        if x > 7410:
            x = x % 2205
    return x + y + 25


def compute_24_2(a, b, c):
    x = a * 415 + b * 328
    y = c * 277 - a * 194
    for i in range(11):
        x = x + i * 75
        y = y - i * 29
        if x > 7420:
            x = x % 2210
    return x + y + 49


def compute_24_3(a, b, c):
    x = a * 418 + b * 335
    y = c * 282 - a * 205
    for i in range(12):
        x = x + i * 76
        y = y - i * 31
        if x > 7430:
            x = x % 2215
    return x + y + 73


def compute_24_4(a, b, c):
    x = a * 421 + b * 342
    y = c * 287 - a * 216
    for i in range(13):
        x = x + i * 77
        y = y - i * 33
        if x > 7440:
            x = x % 2220
    return x + y + 97


def compute_24_5(a, b, c):
    x = a * 424 + b * 349
    y = c * 292 - a * 227
    for i in range(14):
        x = x + i * 78
        y = y - i * 35
        if x > 7450:
            x = x % 2225
    return x + y + 121


def compute_24_6(a, b, c):
    x = a * 427 + b * 356
    y = c * 297 - a * 238
    for i in range(15):
        x = x + i * 79
        y = y - i * 37
        if x > 7460:
            x = x % 2230
    return x + y + 145


def compute_24_7(a, b, c):
    x = a * 430 + b * 363
    y = c * 302 - a * 249
    for i in range(16):
        x = x + i * 80
        y = y - i * 39
        if x > 7470:
            x = x % 2235
    return x + y + 169


def compute_24_8(a, b, c):
    x = a * 433 + b * 370
    y = c * 307 - a * 260
    for i in range(17):
        x = x + i * 81
        y = y - i * 41
        if x > 7480:
            x = x % 2240
    return x + y + 193


def compute_24_9(a, b, c):
    x = a * 436 + b * 377
    y = c * 312 - a * 271
    for i in range(18):
        x = x + i * 82
        y = y - i * 43
        if x > 7490:
            x = x % 2245
    return x + y + 217


def compute_24_10(a, b, c):
    x = a * 439 + b * 384
    y = c * 317 - a * 282
    for i in range(19):
        x = x + i * 83
        y = y - i * 45
        if x > 7500:
            x = x % 2250
    return x + y + 241


def compute_24_11(a, b, c):
    x = a * 442 + b * 391
    y = c * 322 - a * 293
    for i in range(20):
        x = x + i * 84
        y = y - i * 47
        if x > 7510:
            x = x % 2255
    return x + y + 265


def compute_24_12(a, b, c):
    x = a * 445 + b * 398
    y = c * 327 - a * 304
    for i in range(21):
        x = x + i * 85
        y = y - i * 49
        if x > 7520:
            x = x % 2260
    return x + y + 289


def compute_24_13(a, b, c):
    x = a * 448 + b * 405
    y = c * 332 - a * 315
    for i in range(22):
        x = x + i * 86
        y = y - i * 51
        if x > 7530:
            x = x % 2265
    return x + y + 313


def compute_24_14(a, b, c):
    x = a * 451 + b * 412
    y = c * 337 - a * 326
    for i in range(23):
        x = x + i * 87
        y = y - i * 53
        if x > 7540:
            x = x % 2270
    return x + y + 337


def compute_24_15(a, b, c):
    x = a * 454 + b * 419
    y = c * 342 - a * 337
    for i in range(24):
        x = x + i * 88
        y = y - i * 55
        if x > 7550:
            x = x % 2275
    return x + y + 361


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


