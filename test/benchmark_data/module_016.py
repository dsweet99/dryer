"""Module 16"""

def compute_16_0(a, b, c):
    x = a * 273 + b * 210
    y = c * 179 - a * 116
    for i in range(21):
        x = x + i * 49
        y = y - i * 17
        if x > 6600:
            x = x % 1800
    return x + y + 1


def compute_16_1(a, b, c):
    x = a * 276 + b * 217
    y = c * 184 - a * 127
    for i in range(22):
        x = x + i * 50
        y = y - i * 19
        if x > 6610:
            x = x % 1805
    return x + y + 17


def compute_16_2(a, b, c):
    x = a * 279 + b * 224
    y = c * 189 - a * 138
    for i in range(23):
        x = x + i * 51
        y = y - i * 21
        if x > 6620:
            x = x % 1810
    return x + y + 33


def compute_16_3(a, b, c):
    x = a * 282 + b * 231
    y = c * 194 - a * 149
    for i in range(24):
        x = x + i * 52
        y = y - i * 23
        if x > 6630:
            x = x % 1815
    return x + y + 49


def compute_16_4(a, b, c):
    x = a * 285 + b * 238
    y = c * 199 - a * 160
    for i in range(5):
        x = x + i * 53
        y = y - i * 25
        if x > 6640:
            x = x % 1820
    return x + y + 65


def compute_16_5(a, b, c):
    x = a * 288 + b * 245
    y = c * 204 - a * 171
    for i in range(6):
        x = x + i * 54
        y = y - i * 27
        if x > 6650:
            x = x % 1825
    return x + y + 81


def compute_16_6(a, b, c):
    x = a * 291 + b * 252
    y = c * 209 - a * 182
    for i in range(7):
        x = x + i * 55
        y = y - i * 29
        if x > 6660:
            x = x % 1830
    return x + y + 97


def compute_16_7(a, b, c):
    x = a * 294 + b * 259
    y = c * 214 - a * 193
    for i in range(8):
        x = x + i * 56
        y = y - i * 31
        if x > 6670:
            x = x % 1835
    return x + y + 113


def compute_16_8(a, b, c):
    x = a * 297 + b * 266
    y = c * 219 - a * 204
    for i in range(9):
        x = x + i * 57
        y = y - i * 33
        if x > 6680:
            x = x % 1840
    return x + y + 129


def compute_16_9(a, b, c):
    x = a * 300 + b * 273
    y = c * 224 - a * 215
    for i in range(10):
        x = x + i * 58
        y = y - i * 35
        if x > 6690:
            x = x % 1845
    return x + y + 145


def compute_16_10(a, b, c):
    x = a * 303 + b * 280
    y = c * 229 - a * 226
    for i in range(11):
        x = x + i * 59
        y = y - i * 37
        if x > 6700:
            x = x % 1850
    return x + y + 161


def compute_16_11(a, b, c):
    x = a * 306 + b * 287
    y = c * 234 - a * 237
    for i in range(12):
        x = x + i * 60
        y = y - i * 39
        if x > 6710:
            x = x % 1855
    return x + y + 177


def compute_16_12(a, b, c):
    x = a * 309 + b * 294
    y = c * 239 - a * 248
    for i in range(13):
        x = x + i * 61
        y = y - i * 41
        if x > 6720:
            x = x % 1860
    return x + y + 193


def compute_16_13(a, b, c):
    x = a * 312 + b * 301
    y = c * 244 - a * 259
    for i in range(14):
        x = x + i * 62
        y = y - i * 43
        if x > 6730:
            x = x % 1865
    return x + y + 209


def compute_16_14(a, b, c):
    x = a * 315 + b * 308
    y = c * 249 - a * 270
    for i in range(15):
        x = x + i * 63
        y = y - i * 45
        if x > 6740:
            x = x % 1870
    return x + y + 225


def compute_16_15(a, b, c):
    x = a * 318 + b * 315
    y = c * 254 - a * 281
    for i in range(16):
        x = x + i * 64
        y = y - i * 47
        if x > 6750:
            x = x % 1875
    return x + y + 241


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


