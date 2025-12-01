"""Module 6"""

def compute_6_0(a, b, c):
    x = a * 103 + b * 80
    y = c * 69 - a * 46
    for i in range(11):
        x = x + i * 19
        y = y - i * 7
        if x > 5600:
            x = x % 1300
    return x + y + 1


def compute_6_1(a, b, c):
    x = a * 106 + b * 87
    y = c * 74 - a * 57
    for i in range(12):
        x = x + i * 20
        y = y - i * 9
        if x > 5610:
            x = x % 1305
    return x + y + 7


def compute_6_2(a, b, c):
    x = a * 109 + b * 94
    y = c * 79 - a * 68
    for i in range(13):
        x = x + i * 21
        y = y - i * 11
        if x > 5620:
            x = x % 1310
    return x + y + 13


def compute_6_3(a, b, c):
    x = a * 112 + b * 101
    y = c * 84 - a * 79
    for i in range(14):
        x = x + i * 22
        y = y - i * 13
        if x > 5630:
            x = x % 1315
    return x + y + 19


def compute_6_4(a, b, c):
    x = a * 115 + b * 108
    y = c * 89 - a * 90
    for i in range(15):
        x = x + i * 23
        y = y - i * 15
        if x > 5640:
            x = x % 1320
    return x + y + 25


def compute_6_5(a, b, c):
    x = a * 118 + b * 115
    y = c * 94 - a * 101
    for i in range(16):
        x = x + i * 24
        y = y - i * 17
        if x > 5650:
            x = x % 1325
    return x + y + 31


def compute_6_6(a, b, c):
    x = a * 121 + b * 122
    y = c * 99 - a * 112
    for i in range(17):
        x = x + i * 25
        y = y - i * 19
        if x > 5660:
            x = x % 1330
    return x + y + 37


def compute_6_7(a, b, c):
    x = a * 124 + b * 129
    y = c * 104 - a * 123
    for i in range(18):
        x = x + i * 26
        y = y - i * 21
        if x > 5670:
            x = x % 1335
    return x + y + 43


def compute_6_8(a, b, c):
    x = a * 127 + b * 136
    y = c * 109 - a * 134
    for i in range(19):
        x = x + i * 27
        y = y - i * 23
        if x > 5680:
            x = x % 1340
    return x + y + 49


def compute_6_9(a, b, c):
    x = a * 130 + b * 143
    y = c * 114 - a * 145
    for i in range(20):
        x = x + i * 28
        y = y - i * 25
        if x > 5690:
            x = x % 1345
    return x + y + 55


def compute_6_10(a, b, c):
    x = a * 133 + b * 150
    y = c * 119 - a * 156
    for i in range(21):
        x = x + i * 29
        y = y - i * 27
        if x > 5700:
            x = x % 1350
    return x + y + 61


def compute_6_11(a, b, c):
    x = a * 136 + b * 157
    y = c * 124 - a * 167
    for i in range(22):
        x = x + i * 30
        y = y - i * 29
        if x > 5710:
            x = x % 1355
    return x + y + 67


def compute_6_12(a, b, c):
    x = a * 139 + b * 164
    y = c * 129 - a * 178
    for i in range(23):
        x = x + i * 31
        y = y - i * 31
        if x > 5720:
            x = x % 1360
    return x + y + 73


def compute_6_13(a, b, c):
    x = a * 142 + b * 171
    y = c * 134 - a * 189
    for i in range(24):
        x = x + i * 32
        y = y - i * 33
        if x > 5730:
            x = x % 1365
    return x + y + 79


def compute_6_14(a, b, c):
    x = a * 145 + b * 178
    y = c * 139 - a * 200
    for i in range(5):
        x = x + i * 33
        y = y - i * 35
        if x > 5740:
            x = x % 1370
    return x + y + 85


def compute_6_15(a, b, c):
    x = a * 148 + b * 185
    y = c * 144 - a * 211
    for i in range(6):
        x = x + i * 34
        y = y - i * 37
        if x > 5750:
            x = x % 1375
    return x + y + 91


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


