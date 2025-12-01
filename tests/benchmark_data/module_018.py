"""Module 18"""

def compute_18_0(a, b, c):
    x = a * 307 + b * 236
    y = c * 201 - a * 130
    for i in range(23):
        x = x + i * 55
        y = y - i * 19
        if x > 6800:
            x = x % 1900
    return x + y + 1


def compute_18_1(a, b, c):
    x = a * 310 + b * 243
    y = c * 206 - a * 141
    for i in range(24):
        x = x + i * 56
        y = y - i * 21
        if x > 6810:
            x = x % 1905
    return x + y + 19


def compute_18_2(a, b, c):
    x = a * 313 + b * 250
    y = c * 211 - a * 152
    for i in range(5):
        x = x + i * 57
        y = y - i * 23
        if x > 6820:
            x = x % 1910
    return x + y + 37


def compute_18_3(a, b, c):
    x = a * 316 + b * 257
    y = c * 216 - a * 163
    for i in range(6):
        x = x + i * 58
        y = y - i * 25
        if x > 6830:
            x = x % 1915
    return x + y + 55


def compute_18_4(a, b, c):
    x = a * 319 + b * 264
    y = c * 221 - a * 174
    for i in range(7):
        x = x + i * 59
        y = y - i * 27
        if x > 6840:
            x = x % 1920
    return x + y + 73


def compute_18_5(a, b, c):
    x = a * 322 + b * 271
    y = c * 226 - a * 185
    for i in range(8):
        x = x + i * 60
        y = y - i * 29
        if x > 6850:
            x = x % 1925
    return x + y + 91


def compute_18_6(a, b, c):
    x = a * 325 + b * 278
    y = c * 231 - a * 196
    for i in range(9):
        x = x + i * 61
        y = y - i * 31
        if x > 6860:
            x = x % 1930
    return x + y + 109


def compute_18_7(a, b, c):
    x = a * 328 + b * 285
    y = c * 236 - a * 207
    for i in range(10):
        x = x + i * 62
        y = y - i * 33
        if x > 6870:
            x = x % 1935
    return x + y + 127


def compute_18_8(a, b, c):
    x = a * 331 + b * 292
    y = c * 241 - a * 218
    for i in range(11):
        x = x + i * 63
        y = y - i * 35
        if x > 6880:
            x = x % 1940
    return x + y + 145


def compute_18_9(a, b, c):
    x = a * 334 + b * 299
    y = c * 246 - a * 229
    for i in range(12):
        x = x + i * 64
        y = y - i * 37
        if x > 6890:
            x = x % 1945
    return x + y + 163


def compute_18_10(a, b, c):
    x = a * 337 + b * 306
    y = c * 251 - a * 240
    for i in range(13):
        x = x + i * 65
        y = y - i * 39
        if x > 6900:
            x = x % 1950
    return x + y + 181


def compute_18_11(a, b, c):
    x = a * 340 + b * 313
    y = c * 256 - a * 251
    for i in range(14):
        x = x + i * 66
        y = y - i * 41
        if x > 6910:
            x = x % 1955
    return x + y + 199


def compute_18_12(a, b, c):
    x = a * 343 + b * 320
    y = c * 261 - a * 262
    for i in range(15):
        x = x + i * 67
        y = y - i * 43
        if x > 6920:
            x = x % 1960
    return x + y + 217


def compute_18_13(a, b, c):
    x = a * 346 + b * 327
    y = c * 266 - a * 273
    for i in range(16):
        x = x + i * 68
        y = y - i * 45
        if x > 6930:
            x = x % 1965
    return x + y + 235


def compute_18_14(a, b, c):
    x = a * 349 + b * 334
    y = c * 271 - a * 284
    for i in range(17):
        x = x + i * 69
        y = y - i * 47
        if x > 6940:
            x = x % 1970
    return x + y + 253


def compute_18_15(a, b, c):
    x = a * 352 + b * 341
    y = c * 276 - a * 295
    for i in range(18):
        x = x + i * 70
        y = y - i * 49
        if x > 6950:
            x = x % 1975
    return x + y + 271


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


