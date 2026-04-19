"""六爻装卦用到的静态规则。

这个文件只放固定规则，不处理某一次起卦的动爻、日辰、月建、旬空。
真正给 AI 的时候，建议先在 zhuanggua.py 里把这些静态信息和动态信息合并好。
"""

from data.gua_table import HEXAGRAM_BY_TRIGRAMS as LIUSHISIGUA_BY_SHANGXIA


# 爻位编号。所有列表都按从初爻到上爻的顺序存。
YAOMING_BY_WEI = {
    1: "初爻",
    2: "二爻",
    3: "三爻",
    4: "四爻",
    5: "五爻",
    6: "上爻",
}


# 八卦纳甲基础表。
# yaoxiang：1 表示阳爻，0 表示阴爻，顺序是从下往上。
# nei_tiangan / nei_dizhi：该八卦作为下卦时使用的天干地支。
# wai_tiangan / wai_dizhi：该八卦作为上卦时使用的天干地支。
BAGUA_XINXI = {
    "乾": {
        "fuhao": "☰",
        "wuxing": "金",
        "yaoxiang": (1, 1, 1),
        "nei_tiangan": "甲",
        "wai_tiangan": "壬",
        "nei_dizhi": ("子", "寅", "辰"),
        "wai_dizhi": ("午", "申", "戌"),
    },
    "兑": {
        "fuhao": "☱",
        "wuxing": "金",
        "yaoxiang": (1, 1, 0),
        "nei_tiangan": "丁",
        "wai_tiangan": "丁",
        "nei_dizhi": ("巳", "卯", "丑"),
        "wai_dizhi": ("亥", "酉", "未"),
    },
    "离": {
        "fuhao": "☲",
        "wuxing": "火",
        "yaoxiang": (1, 0, 1),
        "nei_tiangan": "己",
        "wai_tiangan": "己",
        "nei_dizhi": ("卯", "丑", "亥"),
        "wai_dizhi": ("酉", "未", "巳"),
    },
    "震": {
        "fuhao": "☳",
        "wuxing": "木",
        "yaoxiang": (1, 0, 0),
        "nei_tiangan": "庚",
        "wai_tiangan": "庚",
        "nei_dizhi": ("子", "寅", "辰"),
        "wai_dizhi": ("午", "申", "戌"),
    },
    "巽": {
        "fuhao": "☴",
        "wuxing": "木",
        "yaoxiang": (0, 1, 1),
        "nei_tiangan": "辛",
        "wai_tiangan": "辛",
        "nei_dizhi": ("丑", "亥", "酉"),
        "wai_dizhi": ("未", "巳", "卯"),
    },
    "坎": {
        "fuhao": "☵",
        "wuxing": "水",
        "yaoxiang": (0, 1, 0),
        "nei_tiangan": "戊",
        "wai_tiangan": "戊",
        "nei_dizhi": ("寅", "辰", "午"),
        "wai_dizhi": ("申", "戌", "子"),
    },
    "艮": {
        "fuhao": "☶",
        "wuxing": "土",
        "yaoxiang": (0, 0, 1),
        "nei_tiangan": "丙",
        "wai_tiangan": "丙",
        "nei_dizhi": ("辰", "午", "申"),
        "wai_dizhi": ("戌", "子", "寅"),
    },
    "坤": {
        "fuhao": "☷",
        "wuxing": "土",
        "yaoxiang": (0, 0, 0),
        "nei_tiangan": "乙",
        "wai_tiangan": "癸",
        "nei_dizhi": ("未", "巳", "卯"),
        "wai_dizhi": ("丑", "亥", "酉"),
    },
}


# 十二地支五行。
DIZHI_WUXING = {
    "子": "水",
    "丑": "土",
    "寅": "木",
    "卯": "木",
    "辰": "土",
    "巳": "火",
    "午": "火",
    "未": "土",
    "申": "金",
    "酉": "金",
    "戌": "土",
    "亥": "水",
}


# 五行相生：键生值。
WUXING_SHENG = {
    "木": "火",
    "火": "土",
    "土": "金",
    "金": "水",
    "水": "木",
}


# 五行相克：键克值。
WUXING_KE = {
    "木": "土",
    "土": "水",
    "水": "火",
    "火": "金",
    "金": "木",
}


# 六亲全集。后面判断伏神时用它来找本卦明面缺了哪些六亲。
QUANBU_LIUQIN = (
    "父母",
    "兄弟",
    "官鬼",
    "妻财",
    "子孙",
)


# 八宫卦序。
# 每宫八个：本宫、一世、二世、三世、四世、五世、游魂、归魂。
BAGONG_GUA = {
    "乾": (
        "乾为天",
        "天风姤",
        "天山遁",
        "天地否",
        "风地观",
        "山地剥",
        "火地晋",
        "火天大有",
    ),
    "兑": (
        "兑为泽",
        "泽水困",
        "泽地萃",
        "泽山咸",
        "水山蹇",
        "地山谦",
        "雷山小过",
        "雷泽归妹",
    ),
    "离": (
        "离为火",
        "火山旅",
        "火风鼎",
        "火水未济",
        "山水蒙",
        "风水涣",
        "天水讼",
        "天火同人",
    ),
    "震": (
        "震为雷",
        "雷地豫",
        "雷水解",
        "雷风恒",
        "地风升",
        "水风井",
        "泽风大过",
        "泽雷随",
    ),
    "巽": (
        "巽为风",
        "风天小畜",
        "风火家人",
        "风雷益",
        "天雷无妄",
        "火雷噬嗑",
        "山雷颐",
        "山风蛊",
    ),
    "坎": (
        "坎为水",
        "水泽节",
        "水雷屯",
        "水火既济",
        "泽火革",
        "雷火丰",
        "地火明夷",
        "地水师",
    ),
    "艮": (
        "艮为山",
        "山火贲",
        "山天大畜",
        "山泽损",
        "火泽睽",
        "天泽履",
        "风泽中孚",
        "风山渐",
    ),
    "坤": (
        "坤为地",
        "地雷复",
        "地泽临",
        "地天泰",
        "雷天大壮",
        "泽天夬",
        "水天需",
        "水地比",
    ),
}


GONG_JIEDUAN_MING = (
    "本宫",
    "一世",
    "二世",
    "三世",
    "四世",
    "五世",
    "游魂",
    "归魂",
)


# 八宫阶段对应世爻位置。
SHIYAO_BY_JIEDUAN = {
    0: 6,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 4,
    7: 3,
}


# 六冲卦固定名单，以及初四、二五、三上三组冲。
LIUCHONG_XIANGQING = {
    "乾为天": ("子午", "寅申", "辰戌"),
    "兑为泽": ("巳亥", "卯酉", "丑未"),
    "离为火": ("卯酉", "丑未", "亥巳"),
    "震为雷": ("子午", "寅申", "辰戌"),
    "巽为风": ("丑未", "亥巳", "酉卯"),
    "坎为水": ("寅申", "辰戌", "午子"),
    "艮为山": ("辰戌", "午子", "申寅"),
    "坤为地": ("未丑", "巳亥", "卯酉"),
}


# 六合卦固定名单，以及初四、二五、三上三组合。
LIUHE_XIANGQING = {
    "天地否": ("未午", "巳申", "卯戌"),
    "地天泰": ("子丑", "寅亥", "辰酉"),
    "水泽节": ("巳申", "卯戌", "丑子"),
    "山火贲": ("卯戌", "丑子", "亥寅"),
    "雷地豫": ("未午", "巳申", "卯戌"),
    "地雷复": ("子丑", "寅亥", "辰酉"),
    "火山旅": ("辰酉", "午未", "申巳"),
    "泽水困": ("寅亥", "辰酉", "午未"),
}


# 从“卦名 -> (上卦, 下卦)”反查。
SHANGXIA_BY_GUAMING = {
    guaming: shangxia for shangxia, guaming in LIUSHISIGUA_BY_SHANGXIA.items()
}


# 这里沿用 data/gua_table.py 里的六十四卦顺序。
# 当前顺序就是文王六十四卦顺序，所以可以直接推 Unicode 卦符。
WENWANG_GUAMING = list(LIUSHISIGUA_BY_SHANGXIA.values())


XUHAO_BY_GUAMING = {
    guaming: xuhao for xuhao, guaming in enumerate(WENWANG_GUAMING, start=1)
}


FUHAO_BY_GUAMING = {
    guaming: chr(0x4DC0 + xuhao - 1)
    for guaming, xuhao in XUHAO_BY_GUAMING.items()
}


# 反查某个卦属于哪个宫，以及它在该宫的第几个阶段。
GONG_BY_GUAMING = {}
JIEDUAN_BY_GUAMING = {}
for gong, guaming_list in BAGONG_GUA.items():
    for jieduan, guaming in enumerate(guaming_list):
        GONG_BY_GUAMING[guaming] = gong
        JIEDUAN_BY_GUAMING[guaming] = jieduan


def qiu_liuqin(gong_wuxing, yao_wuxing):
    """根据宫位五行和爻的五行求六亲。

    这里以宫位五行为“我”：
    生我者父母，同我者兄弟，我生者子孙，我克者妻财，克我者官鬼。
    """

    if gong_wuxing == yao_wuxing:
        return "兄弟"
    if WUXING_SHENG[yao_wuxing] == gong_wuxing:
        return "父母"
    if WUXING_SHENG[gong_wuxing] == yao_wuxing:
        return "子孙"
    if WUXING_KE[gong_wuxing] == yao_wuxing:
        return "妻财"
    if WUXING_KE[yao_wuxing] == gong_wuxing:
        return "官鬼"
    raise ValueError(f"无法判断六亲：宫位五行={gong_wuxing}，爻五行={yao_wuxing}")


def qiu_yingyao(shiyao):
    """由世爻求应爻。

    世应总是隔两位相对：初四、二五、三上。
    """

    return ((shiyao + 2) % 6) + 1


def shengcheng_bagua_yaos(bagua, gong_wuxing, shifou_waigua):
    """生成一个三爻卦的纳甲信息。

    参数：
        bagua：八卦名，如“乾”“艮”。
        gong_wuxing：本卦所属宫位五行，用来定六亲。
        shifou_waigua：False 表示下卦，True 表示上卦。
    """

    bagua_xinxi = BAGUA_XINXI[bagua]
    tiangan_key = "wai_tiangan" if shifou_waigua else "nei_tiangan"
    dizhi_key = "wai_dizhi" if shifou_waigua else "nei_dizhi"
    yaowei_pianyi = 3 if shifou_waigua else 0
    neiwai = "外卦" if shifou_waigua else "内卦"

    yaos = []
    for juzhong_weizhi, (yaoxiang, dizhi) in enumerate(
        zip(bagua_xinxi["yaoxiang"], bagua_xinxi[dizhi_key]),
        start=1,
    ):
        yaowei = yaowei_pianyi + juzhong_weizhi
        yao_wuxing = DIZHI_WUXING[dizhi]
        tiangan = bagua_xinxi[tiangan_key]

        yaos.append(
            {
                "yaowei": yaowei,
                "yaoming": YAOMING_BY_WEI[yaowei],
                "yaoxiang": yaoxiang,
                "yinyang": "阳" if yaoxiang else "阴",
                "neiwai": neiwai,
                "suoshu_bagua": bagua,
                "bagua_fuhao": bagua_xinxi["fuhao"],
                "liuqin": qiu_liuqin(gong_wuxing, yao_wuxing),
                "tiangan": tiangan,
                "dizhi": dizhi,
                "ganzhi": f"{tiangan}{dizhi}",
                "wuxing": yao_wuxing,
            }
        )

    return yaos


def shengcheng_mingyao(xiagua, shanggua, gong_wuxing):
    """生成一卦明面六爻。

    返回列表固定为从初爻到上爻，前三条来自下卦，后三条来自上卦。
    """

    return shengcheng_bagua_yaos(xiagua, gong_wuxing, shifou_waigua=False) + shengcheng_bagua_yaos(
        shanggua,
        gong_wuxing,
        shifou_waigua=True,
    )


def jiazai_fushen(yaos, bengong_yaos):
    """根据本宫首卦给缺失六亲的爻位挂伏神。

    伏神不是第七爻、第八爻，而是挂在某一个已有爻位旁边。
    图里的左侧伏神栏，就是这里的 fushen 字段。
    """

    queshi_liuqin = set(QUANBU_LIUQIN) - {yao["liuqin"] for yao in yaos}
    xin_yaos = []

    for yao, bengong_yao in zip(yaos, bengong_yaos):
        xin_yao = dict(yao)
        if bengong_yao["liuqin"] in queshi_liuqin:
            xin_yao["fushen"] = {
                "liuqin": bengong_yao["liuqin"],
                "tiangan": bengong_yao["tiangan"],
                "dizhi": bengong_yao["dizhi"],
                "ganzhi": bengong_yao["ganzhi"],
                "wuxing": bengong_yao["wuxing"],
            }
        else:
            xin_yao["fushen"] = None
        xin_yaos.append(xin_yao)

    return xin_yaos


def shengcheng_guashen(yaos, shiyao):
    """生成卦身信息。

    常用起法：阳世从子起，阴世从午起，顺数到世爻。
    这里先求出卦身地支，再看它出现在明面本卦里，还是伏神里。
    """

    shiyao_xinxi = yaos[shiyao - 1]
    shifou_yangshi = shiyao_xinxi["yaoxiang"] == 1
    dizhi_shunxu = ("子", "丑", "寅", "卯", "辰", "巳") if shifou_yangshi else ("午", "未", "申", "酉", "戌", "亥")
    guashen_dizhi = dizhi_shunxu[shiyao - 1]

    bengua_weizhi = []
    fushen_weizhi = []
    for yao in yaos:
        if yao["dizhi"] == guashen_dizhi:
            bengua_weizhi.append(
                {
                    "yaowei": yao["yaowei"],
                    "yaoming": yao["yaoming"],
                    "liuqin": yao["liuqin"],
                    "ganzhi": yao["ganzhi"],
                }
            )

        if yao["fushen"] and yao["fushen"]["dizhi"] == guashen_dizhi:
            fushen_weizhi.append(
                {
                    "yaowei": yao["yaowei"],
                    "yaoming": yao["yaoming"],
                    "liuqin": yao["fushen"]["liuqin"],
                    "ganzhi": yao["fushen"]["ganzhi"],
                }
            )

    return {
        "dizhi": guashen_dizhi,
        "wuxing": DIZHI_WUXING[guashen_dizhi],
        "genju_shiyao": shiyao,
        "genju_shiyao_ming": YAOMING_BY_WEI[shiyao],
        "shiyao_yinyang": shiyao_xinxi["yinyang"],
        "qishi_dizhi": "子" if shifou_yangshi else "午",
        "zai_bengua": bool(bengua_weizhi),
        "zai_fushen": bool(fushen_weizhi),
        "bengua_weizhi": bengua_weizhi,
        "fushen_weizhi": fushen_weizhi,
    }


def shengcheng_dangua(guaming):
    """生成一个卦的完整静态数据。"""

    shanggua, xiagua = SHANGXIA_BY_GUAMING[guaming]
    gong = GONG_BY_GUAMING[guaming]
    gong_wuxing = BAGUA_XINXI[gong]["wuxing"]
    jieduan = JIEDUAN_BY_GUAMING[guaming]
    shiyao = SHIYAO_BY_JIEDUAN[jieduan]
    yingyao = qiu_yingyao(shiyao)

    yaos = shengcheng_mingyao(xiagua, shanggua, gong_wuxing)

    bengong_guaming = BAGONG_GUA[gong][0]
    bengong_shanggua, bengong_xiagua = SHANGXIA_BY_GUAMING[bengong_guaming]
    bengong_yaos = shengcheng_mingyao(bengong_xiagua, bengong_shanggua, gong_wuxing)
    yaos = jiazai_fushen(yaos, bengong_yaos)

    for yao in yaos:
        yao["shifou_shiyao"] = yao["yaowei"] == shiyao
        yao["shifou_yingyao"] = yao["yaowei"] == yingyao

    return {
        "guaming": guaming,
        "xuhao": XUHAO_BY_GUAMING[guaming],
        "fuhao": FUHAO_BY_GUAMING[guaming],
        "shanggua": shanggua,
        "shanggua_fuhao": BAGUA_XINXI[shanggua]["fuhao"],
        "xiagua": xiagua,
        "xiagua_fuhao": BAGUA_XINXI[xiagua]["fuhao"],
        "gong": gong,
        "gong_wuxing": gong_wuxing,
        "gong_jieduan": GONG_JIEDUAN_MING[jieduan],
        "shiyao": shiyao,
        "shiyao_ming": YAOMING_BY_WEI[shiyao],
        "yingyao": yingyao,
        "yingyao_ming": YAOMING_BY_WEI[yingyao],
        "guashen": shengcheng_guashen(yaos, shiyao),
        "shifou_liuchong": guaming in LIUCHONG_XIANGQING,
        "shifou_liuhe": guaming in LIUHE_XIANGQING,
        "liuchong_dui": list(LIUCHONG_XIANGQING.get(guaming, ())),
        "liuhe_dui": list(LIUHE_XIANGQING.get(guaming, ())),
        "yaos": yaos,
    }


def shengcheng_all_64gua_table():
    """生成六十四卦总表。"""

    return {
        guaming: shengcheng_dangua(guaming)
        for guaming in WENWANG_GUAMING
    }
