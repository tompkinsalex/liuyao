"""六神起例表。

六神不是某个卦固定自带的东西，而是根据起卦当天的日干来排。
排法是：先按日干确定初爻起哪一个六神，然后从初爻到上爻顺排。
"""

# 六神固定顺序。排到末尾以后从青龙重新接上。
LIUSHEN_SHUNXU = (
    "青龙",
    "朱雀",
    "勾陈",
    "螣蛇",
    "白虎",
    "玄武",
)


# 日干到初爻六神的起例。
# 甲乙日起青龙，丙丁日起朱雀，戊日起勾陈，己日起螣蛇，
# 庚辛日起白虎，壬癸日起玄武。
LIUSHEN_QILI_BY_RIGAN = {
    "甲": "青龙",
    "乙": "青龙",
    "丙": "朱雀",
    "丁": "朱雀",
    "戊": "勾陈",
    "己": "螣蛇",
    "庚": "白虎",
    "辛": "白虎",
    "壬": "玄武",
    "癸": "玄武",
}


def pai_liushen(rigan):
    """根据日干返回六神排布。

    返回格式：
        {
            1: "青龙",
            2: "朱雀",
            ...
            6: "玄武",
        }

    这里的 1 到 6 仍然是从初爻到上爻。
    """

    qishi_liushen = LIUSHEN_QILI_BY_RIGAN[rigan]
    qishi_weizhi = LIUSHEN_SHUNXU.index(qishi_liushen)
    paiguo_de_liushen = LIUSHEN_SHUNXU[qishi_weizhi:] + LIUSHEN_SHUNXU[:qishi_weizhi]

    return {
        1: paiguo_de_liushen[0],
        2: paiguo_de_liushen[1],
        3: paiguo_de_liushen[2],
        4: paiguo_de_liushen[3],
        5: paiguo_de_liushen[4],
        6: paiguo_de_liushen[5],
    }
