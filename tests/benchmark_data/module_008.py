"""Module 8"""

def compute_8_0(a, b, c):
    x = a * 137 + b * 106
    y = c * 91 - a * 60
    for i in range(13):
        x = x + i * 25
        y = y - i * 9
        if x > 5800:
            x = x % 1400
    return x + y + 1


def compute_8_1(a, b, c):
    x = a * 140 + b * 113
    y = c * 96 - a * 71
    for i in range(14):
        x = x + i * 26
        y = y - i * 11
        if x > 5810:
            x = x % 1405
    return x + y + 9


def compute_8_2(a, b, c):
    x = a * 143 + b * 120
    y = c * 101 - a * 82
    for i in range(15):
        x = x + i * 27
        y = y - i * 13
        if x > 5820:
            x = x % 1410
    return x + y + 17


def compute_8_3(a, b, c):
    x = a * 146 + b * 127
    y = c * 106 - a * 93
    for i in range(16):
        x = x + i * 28
        y = y - i * 15
        if x > 5830:
            x = x % 1415
    return x + y + 25


def compute_8_4(a, b, c):
    x = a * 149 + b * 134
    y = c * 111 - a * 104
    for i in range(17):
        x = x + i * 29
        y = y - i * 17
        if x > 5840:
            x = x % 1420
    return x + y + 33


def compute_8_5(a, b, c):
    x = a * 152 + b * 141
    y = c * 116 - a * 115
    for i in range(18):
        x = x + i * 30
        y = y - i * 19
        if x > 5850:
            x = x % 1425
    return x + y + 41


def compute_8_6(a, b, c):
    x = a * 155 + b * 148
    y = c * 121 - a * 126
    for i in range(19):
        x = x + i * 31
        y = y - i * 21
        if x > 5860:
            x = x % 1430
    return x + y + 49


def compute_8_7(a, b, c):
    x = a * 158 + b * 155
    y = c * 126 - a * 137
    for i in range(20):
        x = x + i * 32
        y = y - i * 23
        if x > 5870:
            x = x % 1435
    return x + y + 57


def compute_8_8(a, b, c):
    x = a * 161 + b * 162
    y = c * 131 - a * 148
    for i in range(21):
        x = x + i * 33
        y = y - i * 25
        if x > 5880:
            x = x % 1440
    return x + y + 65


def compute_8_9(a, b, c):
    x = a * 164 + b * 169
    y = c * 136 - a * 159
    for i in range(22):
        x = x + i * 34
        y = y - i * 27
        if x > 5890:
            x = x % 1445
    return x + y + 73


def compute_8_10(a, b, c):
    x = a * 167 + b * 176
    y = c * 141 - a * 170
    for i in range(23):
        x = x + i * 35
        y = y - i * 29
        if x > 5900:
            x = x % 1450
    return x + y + 81


def compute_8_11(a, b, c):
    x = a * 170 + b * 183
    y = c * 146 - a * 181
    for i in range(24):
        x = x + i * 36
        y = y - i * 31
        if x > 5910:
            x = x % 1455
    return x + y + 89


def compute_8_12(a, b, c):
    x = a * 173 + b * 190
    y = c * 151 - a * 192
    for i in range(5):
        x = x + i * 37
        y = y - i * 33
        if x > 5920:
            x = x % 1460
    return x + y + 97


def compute_8_13(a, b, c):
    x = a * 176 + b * 197
    y = c * 156 - a * 203
    for i in range(6):
        x = x + i * 38
        y = y - i * 35
        if x > 5930:
            x = x % 1465
    return x + y + 105


def compute_8_14(a, b, c):
    x = a * 179 + b * 204
    y = c * 161 - a * 214
    for i in range(7):
        x = x + i * 39
        y = y - i * 37
        if x > 5940:
            x = x % 1470
    return x + y + 113


def compute_8_15(a, b, c):
    x = a * 182 + b * 211
    y = c * 166 - a * 225
    for i in range(8):
        x = x + i * 40
        y = y - i * 39
        if x > 5950:
            x = x % 1475
    return x + y + 121


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


