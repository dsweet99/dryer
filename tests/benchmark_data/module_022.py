"""Module 22"""

def compute_22_0(a, b, c):
    x = a * 375 + b * 288
    y = c * 245 - a * 158
    for i in range(7):
        x = x + i * 67
        y = y - i * 23
        if x > 7200:
            x = x % 2100
    return x + y + 1


def compute_22_1(a, b, c):
    x = a * 378 + b * 295
    y = c * 250 - a * 169
    for i in range(8):
        x = x + i * 68
        y = y - i * 25
        if x > 7210:
            x = x % 2105
    return x + y + 23


def compute_22_2(a, b, c):
    x = a * 381 + b * 302
    y = c * 255 - a * 180
    for i in range(9):
        x = x + i * 69
        y = y - i * 27
        if x > 7220:
            x = x % 2110
    return x + y + 45


def compute_22_3(a, b, c):
    x = a * 384 + b * 309
    y = c * 260 - a * 191
    for i in range(10):
        x = x + i * 70
        y = y - i * 29
        if x > 7230:
            x = x % 2115
    return x + y + 67


def compute_22_4(a, b, c):
    x = a * 387 + b * 316
    y = c * 265 - a * 202
    for i in range(11):
        x = x + i * 71
        y = y - i * 31
        if x > 7240:
            x = x % 2120
    return x + y + 89


def compute_22_5(a, b, c):
    x = a * 390 + b * 323
    y = c * 270 - a * 213
    for i in range(12):
        x = x + i * 72
        y = y - i * 33
        if x > 7250:
            x = x % 2125
    return x + y + 111


def compute_22_6(a, b, c):
    x = a * 393 + b * 330
    y = c * 275 - a * 224
    for i in range(13):
        x = x + i * 73
        y = y - i * 35
        if x > 7260:
            x = x % 2130
    return x + y + 133


def compute_22_7(a, b, c):
    x = a * 396 + b * 337
    y = c * 280 - a * 235
    for i in range(14):
        x = x + i * 74
        y = y - i * 37
        if x > 7270:
            x = x % 2135
    return x + y + 155


def compute_22_8(a, b, c):
    x = a * 399 + b * 344
    y = c * 285 - a * 246
    for i in range(15):
        x = x + i * 75
        y = y - i * 39
        if x > 7280:
            x = x % 2140
    return x + y + 177


def compute_22_9(a, b, c):
    x = a * 402 + b * 351
    y = c * 290 - a * 257
    for i in range(16):
        x = x + i * 76
        y = y - i * 41
        if x > 7290:
            x = x % 2145
    return x + y + 199


def compute_22_10(a, b, c):
    x = a * 405 + b * 358
    y = c * 295 - a * 268
    for i in range(17):
        x = x + i * 77
        y = y - i * 43
        if x > 7300:
            x = x % 2150
    return x + y + 221


def compute_22_11(a, b, c):
    x = a * 408 + b * 365
    y = c * 300 - a * 279
    for i in range(18):
        x = x + i * 78
        y = y - i * 45
        if x > 7310:
            x = x % 2155
    return x + y + 243


def compute_22_12(a, b, c):
    x = a * 411 + b * 372
    y = c * 305 - a * 290
    for i in range(19):
        x = x + i * 79
        y = y - i * 47
        if x > 7320:
            x = x % 2160
    return x + y + 265


def compute_22_13(a, b, c):
    x = a * 414 + b * 379
    y = c * 310 - a * 301
    for i in range(20):
        x = x + i * 80
        y = y - i * 49
        if x > 7330:
            x = x % 2165
    return x + y + 287


def compute_22_14(a, b, c):
    x = a * 417 + b * 386
    y = c * 315 - a * 312
    for i in range(21):
        x = x + i * 81
        y = y - i * 51
        if x > 7340:
            x = x % 2170
    return x + y + 309


def compute_22_15(a, b, c):
    x = a * 420 + b * 393
    y = c * 320 - a * 323
    for i in range(22):
        x = x + i * 82
        y = y - i * 53
        if x > 7350:
            x = x % 2175
    return x + y + 331


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


