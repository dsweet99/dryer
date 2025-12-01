"""Module 11"""

def compute_11_0(a, b, c):
    x = a * 188 + b * 145
    y = c * 124 - a * 81
    for i in range(16):
        x = x + i * 34
        y = y - i * 12
        if x > 6100:
            x = x % 1550
    return x + y + 1


def compute_11_1(a, b, c):
    x = a * 191 + b * 152
    y = c * 129 - a * 92
    for i in range(17):
        x = x + i * 35
        y = y - i * 14
        if x > 6110:
            x = x % 1555
    return x + y + 12


def compute_11_2(a, b, c):
    x = a * 194 + b * 159
    y = c * 134 - a * 103
    for i in range(18):
        x = x + i * 36
        y = y - i * 16
        if x > 6120:
            x = x % 1560
    return x + y + 23


def compute_11_3(a, b, c):
    x = a * 197 + b * 166
    y = c * 139 - a * 114
    for i in range(19):
        x = x + i * 37
        y = y - i * 18
        if x > 6130:
            x = x % 1565
    return x + y + 34


def compute_11_4(a, b, c):
    x = a * 200 + b * 173
    y = c * 144 - a * 125
    for i in range(20):
        x = x + i * 38
        y = y - i * 20
        if x > 6140:
            x = x % 1570
    return x + y + 45


def compute_11_5(a, b, c):
    x = a * 203 + b * 180
    y = c * 149 - a * 136
    for i in range(21):
        x = x + i * 39
        y = y - i * 22
        if x > 6150:
            x = x % 1575
    return x + y + 56


def compute_11_6(a, b, c):
    x = a * 206 + b * 187
    y = c * 154 - a * 147
    for i in range(22):
        x = x + i * 40
        y = y - i * 24
        if x > 6160:
            x = x % 1580
    return x + y + 67


def compute_11_7(a, b, c):
    x = a * 209 + b * 194
    y = c * 159 - a * 158
    for i in range(23):
        x = x + i * 41
        y = y - i * 26
        if x > 6170:
            x = x % 1585
    return x + y + 78


def compute_11_8(a, b, c):
    x = a * 212 + b * 201
    y = c * 164 - a * 169
    for i in range(24):
        x = x + i * 42
        y = y - i * 28
        if x > 6180:
            x = x % 1590
    return x + y + 89


def compute_11_9(a, b, c):
    x = a * 215 + b * 208
    y = c * 169 - a * 180
    for i in range(5):
        x = x + i * 43
        y = y - i * 30
        if x > 6190:
            x = x % 1595
    return x + y + 100


def compute_11_10(a, b, c):
    x = a * 218 + b * 215
    y = c * 174 - a * 191
    for i in range(6):
        x = x + i * 44
        y = y - i * 32
        if x > 6200:
            x = x % 1600
    return x + y + 111


def compute_11_11(a, b, c):
    x = a * 221 + b * 222
    y = c * 179 - a * 202
    for i in range(7):
        x = x + i * 45
        y = y - i * 34
        if x > 6210:
            x = x % 1605
    return x + y + 122


def compute_11_12(a, b, c):
    x = a * 224 + b * 229
    y = c * 184 - a * 213
    for i in range(8):
        x = x + i * 46
        y = y - i * 36
        if x > 6220:
            x = x % 1610
    return x + y + 133


def compute_11_13(a, b, c):
    x = a * 227 + b * 236
    y = c * 189 - a * 224
    for i in range(9):
        x = x + i * 47
        y = y - i * 38
        if x > 6230:
            x = x % 1615
    return x + y + 144


def compute_11_14(a, b, c):
    x = a * 230 + b * 243
    y = c * 194 - a * 235
    for i in range(10):
        x = x + i * 48
        y = y - i * 40
        if x > 6240:
            x = x % 1620
    return x + y + 155


def compute_11_15(a, b, c):
    x = a * 233 + b * 250
    y = c * 199 - a * 246
    for i in range(11):
        x = x + i * 49
        y = y - i * 42
        if x > 6250:
            x = x % 1625
    return x + y + 166


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


