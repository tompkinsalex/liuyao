"""Static rules for arranging the six spirits in LiuYao charts."""

liushen_order = (
    "青龙",
    "朱雀",
    "勾陈",
    "螣蛇",
    "白虎",
    "玄武",
)


liushen_start_by_day_gan = {
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


def get_liushen_for_day_gan(day_gan):
    """Return the six-spirit arrangement from 初爻 to 上爻."""

    start = liushen_start_by_day_gan[day_gan]
    start_index = liushen_order.index(start)
    rotated = liushen_order[start_index:] + liushen_order[:start_index]
    return {
        1: rotated[0],
        2: rotated[1],
        3: rotated[2],
        4: rotated[3],
        5: rotated[4],
        6: rotated[5],
    }
