"""Module 28"""

def compute_28_0(a, b, c):
    x = a * 477 + b * 366
    y = c * 311 - a * 200
    for i in range(13):
        x = x + i * 85
        y = y - i * 29
        if x > 7800:
            x = x % 2400
    return x + y + 1


def compute_28_1(a, b, c):
    x = a * 480 + b * 373
    y = c * 316 - a * 211
    for i in range(14):
        x = x + i * 86
        y = y - i * 31
        if x > 7810:
            x = x % 2405
    return x + y + 29


def compute_28_2(a, b, c):
    x = a * 483 + b * 380
    y = c * 321 - a * 222
    for i in range(15):
        x = x + i * 87
        y = y - i * 33
        if x > 7820:
            x = x % 2410
    return x + y + 57


def compute_28_3(a, b, c):
    x = a * 486 + b * 387
    y = c * 326 - a * 233
    for i in range(16):
        x = x + i * 88
        y = y - i * 35
        if x > 7830:
            x = x % 2415
    return x + y + 85


def compute_28_4(a, b, c):
    x = a * 489 + b * 394
    y = c * 331 - a * 244
    for i in range(17):
        x = x + i * 89
        y = y - i * 37
        if x > 7840:
            x = x % 2420
    return x + y + 113


def compute_28_5(a, b, c):
    x = a * 492 + b * 401
    y = c * 336 - a * 255
    for i in range(18):
        x = x + i * 90
        y = y - i * 39
        if x > 7850:
            x = x % 2425
    return x + y + 141


def compute_28_6(a, b, c):
    x = a * 495 + b * 408
    y = c * 341 - a * 266
    for i in range(19):
        x = x + i * 91
        y = y - i * 41
        if x > 7860:
            x = x % 2430
    return x + y + 169


def compute_28_7(a, b, c):
    x = a * 498 + b * 415
    y = c * 346 - a * 277
    for i in range(20):
        x = x + i * 92
        y = y - i * 43
        if x > 7870:
            x = x % 2435
    return x + y + 197


def compute_28_8(a, b, c):
    x = a * 501 + b * 422
    y = c * 351 - a * 288
    for i in range(21):
        x = x + i * 93
        y = y - i * 45
        if x > 7880:
            x = x % 2440
    return x + y + 225


def compute_28_9(a, b, c):
    x = a * 504 + b * 429
    y = c * 356 - a * 299
    for i in range(22):
        x = x + i * 94
        y = y - i * 47
        if x > 7890:
            x = x % 2445
    return x + y + 253


def compute_28_10(a, b, c):
    x = a * 507 + b * 436
    y = c * 361 - a * 310
    for i in range(23):
        x = x + i * 95
        y = y - i * 49
        if x > 7900:
            x = x % 2450
    return x + y + 281


def compute_28_11(a, b, c):
    x = a * 510 + b * 443
    y = c * 366 - a * 321
    for i in range(24):
        x = x + i * 96
        y = y - i * 51
        if x > 7910:
            x = x % 2455
    return x + y + 309


def compute_28_12(a, b, c):
    x = a * 513 + b * 450
    y = c * 371 - a * 332
    for i in range(5):
        x = x + i * 97
        y = y - i * 53
        if x > 7920:
            x = x % 2460
    return x + y + 337


def compute_28_13(a, b, c):
    x = a * 516 + b * 457
    y = c * 376 - a * 343
    for i in range(6):
        x = x + i * 98
        y = y - i * 55
        if x > 7930:
            x = x % 2465
    return x + y + 365


def compute_28_14(a, b, c):
    x = a * 519 + b * 464
    y = c * 381 - a * 354
    for i in range(7):
        x = x + i * 99
        y = y - i * 57
        if x > 7940:
            x = x % 2470
    return x + y + 393


def compute_28_15(a, b, c):
    x = a * 522 + b * 471
    y = c * 386 - a * 365
    for i in range(8):
        x = x + i * 100
        y = y - i * 59
        if x > 7950:
            x = x % 2475
    return x + y + 421


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


