"""Module 29"""

def compute_29_0(a, b, c):
    x = a * 494 + b * 379
    y = c * 322 - a * 207
    for i in range(14):
        x = x + i * 88
        y = y - i * 30
        if x > 7900:
            x = x % 2450
    return x + y + 1


def compute_29_1(a, b, c):
    x = a * 497 + b * 386
    y = c * 327 - a * 218
    for i in range(15):
        x = x + i * 89
        y = y - i * 32
        if x > 7910:
            x = x % 2455
    return x + y + 30


def compute_29_2(a, b, c):
    x = a * 500 + b * 393
    y = c * 332 - a * 229
    for i in range(16):
        x = x + i * 90
        y = y - i * 34
        if x > 7920:
            x = x % 2460
    return x + y + 59


def compute_29_3(a, b, c):
    x = a * 503 + b * 400
    y = c * 337 - a * 240
    for i in range(17):
        x = x + i * 91
        y = y - i * 36
        if x > 7930:
            x = x % 2465
    return x + y + 88


def compute_29_4(a, b, c):
    x = a * 506 + b * 407
    y = c * 342 - a * 251
    for i in range(18):
        x = x + i * 92
        y = y - i * 38
        if x > 7940:
            x = x % 2470
    return x + y + 117


def compute_29_5(a, b, c):
    x = a * 509 + b * 414
    y = c * 347 - a * 262
    for i in range(19):
        x = x + i * 93
        y = y - i * 40
        if x > 7950:
            x = x % 2475
    return x + y + 146


def compute_29_6(a, b, c):
    x = a * 512 + b * 421
    y = c * 352 - a * 273
    for i in range(20):
        x = x + i * 94
        y = y - i * 42
        if x > 7960:
            x = x % 2480
    return x + y + 175


def compute_29_7(a, b, c):
    x = a * 515 + b * 428
    y = c * 357 - a * 284
    for i in range(21):
        x = x + i * 95
        y = y - i * 44
        if x > 7970:
            x = x % 2485
    return x + y + 204


def compute_29_8(a, b, c):
    x = a * 518 + b * 435
    y = c * 362 - a * 295
    for i in range(22):
        x = x + i * 96
        y = y - i * 46
        if x > 7980:
            x = x % 2490
    return x + y + 233


def compute_29_9(a, b, c):
    x = a * 521 + b * 442
    y = c * 367 - a * 306
    for i in range(23):
        x = x + i * 97
        y = y - i * 48
        if x > 7990:
            x = x % 2495
    return x + y + 262


def compute_29_10(a, b, c):
    x = a * 524 + b * 449
    y = c * 372 - a * 317
    for i in range(24):
        x = x + i * 98
        y = y - i * 50
        if x > 8000:
            x = x % 2500
    return x + y + 291


def compute_29_11(a, b, c):
    x = a * 527 + b * 456
    y = c * 377 - a * 328
    for i in range(5):
        x = x + i * 99
        y = y - i * 52
        if x > 8010:
            x = x % 2505
    return x + y + 320


def compute_29_12(a, b, c):
    x = a * 530 + b * 463
    y = c * 382 - a * 339
    for i in range(6):
        x = x + i * 100
        y = y - i * 54
        if x > 8020:
            x = x % 2510
    return x + y + 349


def compute_29_13(a, b, c):
    x = a * 533 + b * 470
    y = c * 387 - a * 350
    for i in range(7):
        x = x + i * 101
        y = y - i * 56
        if x > 8030:
            x = x % 2515
    return x + y + 378


def compute_29_14(a, b, c):
    x = a * 536 + b * 477
    y = c * 392 - a * 361
    for i in range(8):
        x = x + i * 102
        y = y - i * 58
        if x > 8040:
            x = x % 2520
    return x + y + 407


def compute_29_15(a, b, c):
    x = a * 539 + b * 484
    y = c * 397 - a * 372
    for i in range(9):
        x = x + i * 103
        y = y - i * 60
        if x > 8050:
            x = x % 2525
    return x + y + 436


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


