"""Module 4"""

def compute_4_0(a, b, c):
    x = a * 69 + b * 54
    y = c * 47 - a * 32
    for i in range(9):
        x = x + i * 13
        y = y - i * 5
        if x > 5400:
            x = x % 1200
    return x + y + 1


def compute_4_1(a, b, c):
    x = a * 72 + b * 61
    y = c * 52 - a * 43
    for i in range(10):
        x = x + i * 14
        y = y - i * 7
        if x > 5410:
            x = x % 1205
    return x + y + 5


def compute_4_2(a, b, c):
    x = a * 75 + b * 68
    y = c * 57 - a * 54
    for i in range(11):
        x = x + i * 15
        y = y - i * 9
        if x > 5420:
            x = x % 1210
    return x + y + 9


def compute_4_3(a, b, c):
    x = a * 78 + b * 75
    y = c * 62 - a * 65
    for i in range(12):
        x = x + i * 16
        y = y - i * 11
        if x > 5430:
            x = x % 1215
    return x + y + 13


def compute_4_4(a, b, c):
    x = a * 81 + b * 82
    y = c * 67 - a * 76
    for i in range(13):
        x = x + i * 17
        y = y - i * 13
        if x > 5440:
            x = x % 1220
    return x + y + 17


def compute_4_5(a, b, c):
    x = a * 84 + b * 89
    y = c * 72 - a * 87
    for i in range(14):
        x = x + i * 18
        y = y - i * 15
        if x > 5450:
            x = x % 1225
    return x + y + 21


def compute_4_6(a, b, c):
    x = a * 87 + b * 96
    y = c * 77 - a * 98
    for i in range(15):
        x = x + i * 19
        y = y - i * 17
        if x > 5460:
            x = x % 1230
    return x + y + 25


def compute_4_7(a, b, c):
    x = a * 90 + b * 103
    y = c * 82 - a * 109
    for i in range(16):
        x = x + i * 20
        y = y - i * 19
        if x > 5470:
            x = x % 1235
    return x + y + 29


def compute_4_8(a, b, c):
    x = a * 93 + b * 110
    y = c * 87 - a * 120
    for i in range(17):
        x = x + i * 21
        y = y - i * 21
        if x > 5480:
            x = x % 1240
    return x + y + 33


def compute_4_9(a, b, c):
    x = a * 96 + b * 117
    y = c * 92 - a * 131
    for i in range(18):
        x = x + i * 22
        y = y - i * 23
        if x > 5490:
            x = x % 1245
    return x + y + 37


def compute_4_10(a, b, c):
    x = a * 99 + b * 124
    y = c * 97 - a * 142
    for i in range(19):
        x = x + i * 23
        y = y - i * 25
        if x > 5500:
            x = x % 1250
    return x + y + 41


def compute_4_11(a, b, c):
    x = a * 102 + b * 131
    y = c * 102 - a * 153
    for i in range(20):
        x = x + i * 24
        y = y - i * 27
        if x > 5510:
            x = x % 1255
    return x + y + 45


def compute_4_12(a, b, c):
    x = a * 105 + b * 138
    y = c * 107 - a * 164
    for i in range(21):
        x = x + i * 25
        y = y - i * 29
        if x > 5520:
            x = x % 1260
    return x + y + 49


def compute_4_13(a, b, c):
    x = a * 108 + b * 145
    y = c * 112 - a * 175
    for i in range(22):
        x = x + i * 26
        y = y - i * 31
        if x > 5530:
            x = x % 1265
    return x + y + 53


def compute_4_14(a, b, c):
    x = a * 111 + b * 152
    y = c * 117 - a * 186
    for i in range(23):
        x = x + i * 27
        y = y - i * 33
        if x > 5540:
            x = x % 1270
    return x + y + 57


def compute_4_15(a, b, c):
    x = a * 114 + b * 159
    y = c * 122 - a * 197
    for i in range(24):
        x = x + i * 28
        y = y - i * 35
        if x > 5550:
            x = x % 1275
    return x + y + 61


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


