"""Module 27"""

def compute_27_0(a, b, c):
    x = a * 460 + b * 353
    y = c * 300 - a * 193
    for i in range(12):
        x = x + i * 82
        y = y - i * 28
        if x > 7700:
            x = x % 2350
    return x + y + 1


def compute_27_1(a, b, c):
    x = a * 463 + b * 360
    y = c * 305 - a * 204
    for i in range(13):
        x = x + i * 83
        y = y - i * 30
        if x > 7710:
            x = x % 2355
    return x + y + 28


def compute_27_2(a, b, c):
    x = a * 466 + b * 367
    y = c * 310 - a * 215
    for i in range(14):
        x = x + i * 84
        y = y - i * 32
        if x > 7720:
            x = x % 2360
    return x + y + 55


def compute_27_3(a, b, c):
    x = a * 469 + b * 374
    y = c * 315 - a * 226
    for i in range(15):
        x = x + i * 85
        y = y - i * 34
        if x > 7730:
            x = x % 2365
    return x + y + 82


def compute_27_4(a, b, c):
    x = a * 472 + b * 381
    y = c * 320 - a * 237
    for i in range(16):
        x = x + i * 86
        y = y - i * 36
        if x > 7740:
            x = x % 2370
    return x + y + 109


def compute_27_5(a, b, c):
    x = a * 475 + b * 388
    y = c * 325 - a * 248
    for i in range(17):
        x = x + i * 87
        y = y - i * 38
        if x > 7750:
            x = x % 2375
    return x + y + 136


def compute_27_6(a, b, c):
    x = a * 478 + b * 395
    y = c * 330 - a * 259
    for i in range(18):
        x = x + i * 88
        y = y - i * 40
        if x > 7760:
            x = x % 2380
    return x + y + 163


def compute_27_7(a, b, c):
    x = a * 481 + b * 402
    y = c * 335 - a * 270
    for i in range(19):
        x = x + i * 89
        y = y - i * 42
        if x > 7770:
            x = x % 2385
    return x + y + 190


def compute_27_8(a, b, c):
    x = a * 484 + b * 409
    y = c * 340 - a * 281
    for i in range(20):
        x = x + i * 90
        y = y - i * 44
        if x > 7780:
            x = x % 2390
    return x + y + 217


def compute_27_9(a, b, c):
    x = a * 487 + b * 416
    y = c * 345 - a * 292
    for i in range(21):
        x = x + i * 91
        y = y - i * 46
        if x > 7790:
            x = x % 2395
    return x + y + 244


def compute_27_10(a, b, c):
    x = a * 490 + b * 423
    y = c * 350 - a * 303
    for i in range(22):
        x = x + i * 92
        y = y - i * 48
        if x > 7800:
            x = x % 2400
    return x + y + 271


def compute_27_11(a, b, c):
    x = a * 493 + b * 430
    y = c * 355 - a * 314
    for i in range(23):
        x = x + i * 93
        y = y - i * 50
        if x > 7810:
            x = x % 2405
    return x + y + 298


def compute_27_12(a, b, c):
    x = a * 496 + b * 437
    y = c * 360 - a * 325
    for i in range(24):
        x = x + i * 94
        y = y - i * 52
        if x > 7820:
            x = x % 2410
    return x + y + 325


def compute_27_13(a, b, c):
    x = a * 499 + b * 444
    y = c * 365 - a * 336
    for i in range(5):
        x = x + i * 95
        y = y - i * 54
        if x > 7830:
            x = x % 2415
    return x + y + 352


def compute_27_14(a, b, c):
    x = a * 502 + b * 451
    y = c * 370 - a * 347
    for i in range(6):
        x = x + i * 96
        y = y - i * 56
        if x > 7840:
            x = x % 2420
    return x + y + 379


def compute_27_15(a, b, c):
    x = a * 505 + b * 458
    y = c * 375 - a * 358
    for i in range(7):
        x = x + i * 97
        y = y - i * 58
        if x > 7850:
            x = x % 2425
    return x + y + 406


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


