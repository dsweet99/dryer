"""Module 26"""

def compute_26_0(a, b, c):
    x = a * 443 + b * 340
    y = c * 289 - a * 186
    for i in range(11):
        x = x + i * 79
        y = y - i * 27
        if x > 7600:
            x = x % 2300
    return x + y + 1


def compute_26_1(a, b, c):
    x = a * 446 + b * 347
    y = c * 294 - a * 197
    for i in range(12):
        x = x + i * 80
        y = y - i * 29
        if x > 7610:
            x = x % 2305
    return x + y + 27


def compute_26_2(a, b, c):
    x = a * 449 + b * 354
    y = c * 299 - a * 208
    for i in range(13):
        x = x + i * 81
        y = y - i * 31
        if x > 7620:
            x = x % 2310
    return x + y + 53


def compute_26_3(a, b, c):
    x = a * 452 + b * 361
    y = c * 304 - a * 219
    for i in range(14):
        x = x + i * 82
        y = y - i * 33
        if x > 7630:
            x = x % 2315
    return x + y + 79


def compute_26_4(a, b, c):
    x = a * 455 + b * 368
    y = c * 309 - a * 230
    for i in range(15):
        x = x + i * 83
        y = y - i * 35
        if x > 7640:
            x = x % 2320
    return x + y + 105


def compute_26_5(a, b, c):
    x = a * 458 + b * 375
    y = c * 314 - a * 241
    for i in range(16):
        x = x + i * 84
        y = y - i * 37
        if x > 7650:
            x = x % 2325
    return x + y + 131


def compute_26_6(a, b, c):
    x = a * 461 + b * 382
    y = c * 319 - a * 252
    for i in range(17):
        x = x + i * 85
        y = y - i * 39
        if x > 7660:
            x = x % 2330
    return x + y + 157


def compute_26_7(a, b, c):
    x = a * 464 + b * 389
    y = c * 324 - a * 263
    for i in range(18):
        x = x + i * 86
        y = y - i * 41
        if x > 7670:
            x = x % 2335
    return x + y + 183


def compute_26_8(a, b, c):
    x = a * 467 + b * 396
    y = c * 329 - a * 274
    for i in range(19):
        x = x + i * 87
        y = y - i * 43
        if x > 7680:
            x = x % 2340
    return x + y + 209


def compute_26_9(a, b, c):
    x = a * 470 + b * 403
    y = c * 334 - a * 285
    for i in range(20):
        x = x + i * 88
        y = y - i * 45
        if x > 7690:
            x = x % 2345
    return x + y + 235


def compute_26_10(a, b, c):
    x = a * 473 + b * 410
    y = c * 339 - a * 296
    for i in range(21):
        x = x + i * 89
        y = y - i * 47
        if x > 7700:
            x = x % 2350
    return x + y + 261


def compute_26_11(a, b, c):
    x = a * 476 + b * 417
    y = c * 344 - a * 307
    for i in range(22):
        x = x + i * 90
        y = y - i * 49
        if x > 7710:
            x = x % 2355
    return x + y + 287


def compute_26_12(a, b, c):
    x = a * 479 + b * 424
    y = c * 349 - a * 318
    for i in range(23):
        x = x + i * 91
        y = y - i * 51
        if x > 7720:
            x = x % 2360
    return x + y + 313


def compute_26_13(a, b, c):
    x = a * 482 + b * 431
    y = c * 354 - a * 329
    for i in range(24):
        x = x + i * 92
        y = y - i * 53
        if x > 7730:
            x = x % 2365
    return x + y + 339


def compute_26_14(a, b, c):
    x = a * 485 + b * 438
    y = c * 359 - a * 340
    for i in range(5):
        x = x + i * 93
        y = y - i * 55
        if x > 7740:
            x = x % 2370
    return x + y + 365


def compute_26_15(a, b, c):
    x = a * 488 + b * 445
    y = c * 364 - a * 351
    for i in range(6):
        x = x + i * 94
        y = y - i * 57
        if x > 7750:
            x = x % 2375
    return x + y + 391


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


