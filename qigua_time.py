"""起卦时间信息。

对外主要使用 get_qigua_time_info()。

返回四项：
    qigua_time：起卦时间
    richen_ganzhi：日辰干支
    xunkong：旬空
    liushen：六神，从初爻到上爻
"""

import datetime

from data.liushen_qili import pai_liushen


TIANGAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
DIZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]


# 六旬旬首对应旬空。
# 例如甲子旬内只有十天，地支走不到戌亥，所以戌亥空。
XUNKONG_BY_XUNSHOU = {
    "甲子": ["戌", "亥"],
    "甲戌": ["申", "酉"],
    "甲申": ["午", "未"],
    "甲午": ["辰", "巳"],
    "甲辰": ["寅", "卯"],
    "甲寅": ["子", "丑"],
}


def shengcheng_60_jiazi():
    """生成六十甲子列表。"""

    return [
        TIANGAN[i % 10] + DIZHI[i % 12]
        for i in range(60)
    ]


def qiu_xunkong(richen_ganzhi):
    """根据日辰干支求旬空。"""

    liushi_jiazi = shengcheng_60_jiazi()
    dangqian_weizhi = liushi_jiazi.index(richen_ganzhi)
    xunshou_weizhi = dangqian_weizhi // 10 * 10
    xunshou = liushi_jiazi[xunshou_weizhi]

    return XUNKONG_BY_XUNSHOU[xunshou]


def _get_sxtwl_day(dt):
    """把公历日期交给 sxtwl。

    sxtwl 是专门做农历和干支历的库。这里把 import 放在函数里，
    这样即使环境还没装 sxtwl，导入本模块时也不会立刻崩掉。
    """

    try:
        import sxtwl
    except ImportError as exc:
        raise ImportError(
            "缺少依赖 sxtwl。请先在当前 Python 环境执行：pip install sxtwl"
        ) from exc

    return sxtwl.fromSolar(dt.year, dt.month, dt.day)


def get_richen_ganzhi(dt):
    """根据起卦时间求日辰干支。"""

    day = _get_sxtwl_day(dt)
    day_gz = day.getDayGZ()

    rigan = TIANGAN[day_gz.tg]
    rizhi = DIZHI[day_gz.dz]

    return rigan + rizhi


def get_qigua_time_info(dt=None):
    """返回起卦时间、日辰干支、旬空、六神这四项。

    参数：
        dt：可选 datetime.datetime。
            不传时使用当前本地时间。

    返回：
        {
            "qigua_time": "2026-04-19 17:50:00",
            "richen_ganzhi": "甲子",
            "xunkong": ["戌", "亥"],
            "liushen": {
                1: "青龙",
                ...
                6: "玄武",
            },
        }
    """

    if dt is None:
        dt = datetime.datetime.now()

    richen_ganzhi = get_richen_ganzhi(dt)
    rigan = richen_ganzhi[0]

    return {
        "qigua_time": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "richen_ganzhi": richen_ganzhi,
        "xunkong": qiu_xunkong(richen_ganzhi),
        "liushen": pai_liushen(rigan),
    }


if __name__ == "__main__":
    print(get_qigua_time_info())
