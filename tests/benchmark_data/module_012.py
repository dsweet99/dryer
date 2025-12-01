"""Module 12"""

def compute_12_0(a, b, c):
    x = a * 205 + b * 158
    y = c * 135 - a * 88
    for i in range(17):
        x = x + i * 37
        y = y - i * 13
        if x > 6200:
            x = x % 1600
    return x + y + 1


def compute_12_1(a, b, c):
    x = a * 208 + b * 165
    y = c * 140 - a * 99
    for i in range(18):
        x = x + i * 38
        y = y - i * 15
        if x > 6210:
            x = x % 1605
    return x + y + 13


def compute_12_2(a, b, c):
    x = a * 211 + b * 172
    y = c * 145 - a * 110
    for i in range(19):
        x = x + i * 39
        y = y - i * 17
        if x > 6220:
            x = x % 1610
    return x + y + 25


def compute_12_3(a, b, c):
    x = a * 214 + b * 179
    y = c * 150 - a * 121
    for i in range(20):
        x = x + i * 40
        y = y - i * 19
        if x > 6230:
            x = x % 1615
    return x + y + 37


def compute_12_4(a, b, c):
    x = a * 217 + b * 186
    y = c * 155 - a * 132
    for i in range(21):
        x = x + i * 41
        y = y - i * 21
        if x > 6240:
            x = x % 1620
    return x + y + 49


def compute_12_5(a, b, c):
    x = a * 220 + b * 193
    y = c * 160 - a * 143
    for i in range(22):
        x = x + i * 42
        y = y - i * 23
        if x > 6250:
            x = x % 1625
    return x + y + 61


def compute_12_6(a, b, c):
    x = a * 223 + b * 200
    y = c * 165 - a * 154
    for i in range(23):
        x = x + i * 43
        y = y - i * 25
        if x > 6260:
            x = x % 1630
    return x + y + 73


def compute_12_7(a, b, c):
    x = a * 226 + b * 207
    y = c * 170 - a * 165
    for i in range(24):
        x = x + i * 44
        y = y - i * 27
        if x > 6270:
            x = x % 1635
    return x + y + 85


def compute_12_8(a, b, c):
    x = a * 229 + b * 214
    y = c * 175 - a * 176
    for i in range(5):
        x = x + i * 45
        y = y - i * 29
        if x > 6280:
            x = x % 1640
    return x + y + 97


def compute_12_9(a, b, c):
    x = a * 232 + b * 221
    y = c * 180 - a * 187
    for i in range(6):
        x = x + i * 46
        y = y - i * 31
        if x > 6290:
            x = x % 1645
    return x + y + 109


def compute_12_10(a, b, c):
    x = a * 235 + b * 228
    y = c * 185 - a * 198
    for i in range(7):
        x = x + i * 47
        y = y - i * 33
        if x > 6300:
            x = x % 1650
    return x + y + 121


def compute_12_11(a, b, c):
    x = a * 238 + b * 235
    y = c * 190 - a * 209
    for i in range(8):
        x = x + i * 48
        y = y - i * 35
        if x > 6310:
            x = x % 1655
    return x + y + 133


def compute_12_12(a, b, c):
    x = a * 241 + b * 242
    y = c * 195 - a * 220
    for i in range(9):
        x = x + i * 49
        y = y - i * 37
        if x > 6320:
            x = x % 1660
    return x + y + 145


def compute_12_13(a, b, c):
    x = a * 244 + b * 249
    y = c * 200 - a * 231
    for i in range(10):
        x = x + i * 50
        y = y - i * 39
        if x > 6330:
            x = x % 1665
    return x + y + 157


def compute_12_14(a, b, c):
    x = a * 247 + b * 256
    y = c * 205 - a * 242
    for i in range(11):
        x = x + i * 51
        y = y - i * 41
        if x > 6340:
            x = x % 1670
    return x + y + 169


def compute_12_15(a, b, c):
    x = a * 250 + b * 263
    y = c * 210 - a * 253
    for i in range(12):
        x = x + i * 52
        y = y - i * 43
        if x > 6350:
            x = x % 1675
    return x + y + 181


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


