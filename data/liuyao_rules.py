

from data.gua_table import HEXAGRAM_BY_TRIGRAMS


LINE_LABELS = {
    1: "初爻",
    2: "二爻",
    3: "三爻",
    4: "四爻",
    5: "五爻",
    6: "上爻",
}


TRIGRAM_META = {
    "乾": {
        "symbol": "☰",
        "wuxing": "金",
        "lines": (1, 1, 1),
        "inner_stem": "甲",
        "outer_stem": "壬",
        "inner_branches": ("子", "寅", "辰"),
        "outer_branches": ("午", "申", "戌"),
    },
    "兑": {
        "symbol": "☱",
        "wuxing": "金",
        "lines": (1, 1, 0),
        "inner_stem": "丁",
        "outer_stem": "丁",
        "inner_branches": ("巳", "卯", "丑"),
        "outer_branches": ("亥", "酉", "未"),
    },
    "离": {
        "symbol": "☲",
        "wuxing": "火",
        "lines": (1, 0, 1),
        "inner_stem": "己",
        "outer_stem": "己",
        "inner_branches": ("卯", "丑", "亥"),
        "outer_branches": ("酉", "未", "巳"),
    },
    "震": {
        "symbol": "☳",
        "wuxing": "木",
        "lines": (1, 0, 0),
        "inner_stem": "庚",
        "outer_stem": "庚",
        "inner_branches": ("子", "寅", "辰"),
        "outer_branches": ("午", "申", "戌"),
    },
    "巽": {
        "symbol": "☴",
        "wuxing": "木",
        "lines": (0, 1, 1),
        "inner_stem": "辛",
        "outer_stem": "辛",
        "inner_branches": ("丑", "亥", "酉"),
        "outer_branches": ("未", "巳", "卯"),
    },
    "坎": {
        "symbol": "☵",
        "wuxing": "水",
        "lines": (0, 1, 0),
        "inner_stem": "戊",
        "outer_stem": "戊",
        "inner_branches": ("寅", "辰", "午"),
        "outer_branches": ("申", "戌", "子"),
    },
    "艮": {
        "symbol": "☶",
        "wuxing": "土",
        "lines": (0, 0, 1),
        "inner_stem": "丙",
        "outer_stem": "丙",
        "inner_branches": ("辰", "午", "申"),
        "outer_branches": ("戌", "子", "寅"),
    },
    "坤": {
        "symbol": "☷",
        "wuxing": "土",
        "lines": (0, 0, 0),
        "inner_stem": "乙",
        "outer_stem": "癸",
        "inner_branches": ("未", "巳", "卯"),
        "outer_branches": ("丑", "亥", "酉"),
    },
}


BRANCH_TO_WUXING = {
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


WUXING_GENERATES = {
    "木": "火",
    "火": "土",
    "土": "金",
    "金": "水",
    "水": "木",
}


WUXING_CONTROLS = {
    "木": "土",
    "土": "水",
    "水": "火",
    "火": "金",
    "金": "木",
}


ALL_LIUQIN = (
    "父母",
    "兄弟",
    "官鬼",
    "妻财",
    "子孙",
)


PALACE_HEXAGRAMS = {
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


PALACE_STAGE_NAMES = (
    "本宫",
    "一世",
    "二世",
    "三世",
    "四世",
    "五世",
    "游魂",
    "归魂",
)


SHI_LINE_BY_STAGE_INDEX = {
    0: 6,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 4,
    7: 3,
}


SIX_CHONG_DETAIL = {
    "乾为天": ("子午", "寅申", "辰戌"),
    "兑为泽": ("巳亥", "卯酉", "丑未"),
    "离为火": ("卯酉", "丑未", "亥巳"),
    "震为雷": ("子午", "寅申", "辰戌"),
    "巽为风": ("丑未", "亥巳", "酉卯"),
    "坎为水": ("寅申", "辰戌", "午子"),
    "艮为山": ("辰戌", "午子", "申寅"),
    "坤为地": ("未丑", "巳亥", "卯酉"),
}


SIX_HE_DETAIL = {
    "天地否": ("未午", "巳申", "卯戌"),
    "地天泰": ("子丑", "寅亥", "辰酉"),
    "水泽节": ("巳申", "卯戌", "丑子"),
    "山火贲": ("卯戌", "丑子", "亥寅"),
    "雷地豫": ("未午", "巳申", "卯戌"),
    "地雷复": ("子丑", "寅亥", "辰酉"),
    "火山旅": ("辰酉", "午未", "申巳"),
    "泽水困": ("寅亥", "辰酉", "午未"),
}


HEXAGRAM_NAME_TO_PAIR = {
    hexagram_name: pair for pair, hexagram_name in HEXAGRAM_BY_TRIGRAMS.items()
}


KING_WEN_NAMES = list(HEXAGRAM_BY_TRIGRAMS.values())


HEXAGRAM_NUMBER_BY_NAME = {
    name: index for index, name in enumerate(KING_WEN_NAMES, start=1)
}


HEXAGRAM_SYMBOL_BY_NAME = {
    name: chr(0x4DC0 + number - 1)
    for name, number in HEXAGRAM_NUMBER_BY_NAME.items()
}


PALACE_BY_HEXAGRAM = {}
PALACE_STAGE_INDEX_BY_HEXAGRAM = {}
for palace_name, hexagram_names in PALACE_HEXAGRAMS.items():
    for stage_index, hexagram_name in enumerate(hexagram_names):
        PALACE_BY_HEXAGRAM[hexagram_name] = palace_name
        PALACE_STAGE_INDEX_BY_HEXAGRAM[hexagram_name] = stage_index


def get_liuqin(gong_wuxing, line_wuxing):
    """Map a line's five-element relationship to one of the five relatives."""

    if gong_wuxing == line_wuxing:
        return "兄弟"
    if WUXING_GENERATES[line_wuxing] == gong_wuxing:
        return "父母"
    if WUXING_GENERATES[gong_wuxing] == line_wuxing:
        return "子孙"
    if WUXING_CONTROLS[gong_wuxing] == line_wuxing:
        return "妻财"
    if WUXING_CONTROLS[line_wuxing] == gong_wuxing:
        return "官鬼"
    raise ValueError(f"无法判断六亲: 宫位五行={gong_wuxing}, 爻五行={line_wuxing}")


def get_opposite_line(line_index):
    """Return the paired 应位 for a given 世位."""

    return ((line_index + 2) % 6) + 1


def build_trigram_lines(trigram_name, palace_wuxing, is_outer):
    """Build three line records for either the lower or upper trigram."""

    trigram_meta = TRIGRAM_META[trigram_name]
    stem_key = "outer_stem" if is_outer else "inner_stem"
    branch_key = "outer_branches" if is_outer else "inner_branches"
    line_offset = 3 if is_outer else 0
    part_name = "外卦" if is_outer else "内卦"

    records = []
    for local_index, (line_value, branch) in enumerate(
        zip(trigram_meta["lines"], trigram_meta[branch_key]),
        start=1,
    ):
        line_index = line_offset + local_index
        line_wuxing = BRANCH_TO_WUXING[branch]
        records.append(
            {
                "index": line_index,
                "name": LINE_LABELS[line_index],
                "line_value": line_value,
                "yin_yang": "阳" if line_value else "阴",
                "part": part_name,
                "trigram": trigram_name,
                "trigram_symbol": trigram_meta["symbol"],
                "liuqin": get_liuqin(palace_wuxing, line_wuxing),
                "tiangan": trigram_meta[stem_key],
                "dizhi": branch,
                "ganzhi": f"{trigram_meta[stem_key]}{branch}",
                "wuxing": line_wuxing,
            }
        )
    return records


def build_main_lines(down_trigram, up_trigram, palace_wuxing):
    """Build the six visible lines from bottom to top."""

    return build_trigram_lines(down_trigram, palace_wuxing, is_outer=False) + build_trigram_lines(
        up_trigram,
        palace_wuxing,
        is_outer=True,
    )


def attach_fushen(lines, pure_palace_lines):
    """Attach hidden lines from the palace head hexagram for missing relatives."""

    missing_liuqin = set(ALL_LIUQIN) - {line["liuqin"] for line in lines}
    enriched_lines = []

    for line, pure_line in zip(lines, pure_palace_lines):
        new_line = dict(line)
        if pure_line["liuqin"] in missing_liuqin:
            new_line["fushen"] = {
                "liuqin": pure_line["liuqin"],
                "tiangan": pure_line["tiangan"],
                "dizhi": pure_line["dizhi"],
                "ganzhi": pure_line["ganzhi"],
                "wuxing": pure_line["wuxing"],
            }
        else:
            new_line["fushen"] = None
        enriched_lines.append(new_line)

    return enriched_lines


def build_gua_shen(lines, shi_line):
    """Build the month-hexagram-body info from the static chart."""

    shi_line_record = lines[shi_line - 1]
    is_yang_shi = shi_line_record["line_value"] == 1
    sequence = ("子", "丑", "寅", "卯", "辰", "巳") if is_yang_shi else ("午", "未", "申", "酉", "戌", "亥")
    branch = sequence[shi_line - 1]

    main_matches = []
    fushen_matches = []
    for line in lines:
        if line["dizhi"] == branch:
            main_matches.append(
                {
                    "index": line["index"],
                    "name": line["name"],
                    "liuqin": line["liuqin"],
                    "ganzhi": line["ganzhi"],
                }
            )

        if line["fushen"] and line["fushen"]["dizhi"] == branch:
            fushen_matches.append(
                {
                    "index": line["index"],
                    "name": line["name"],
                    "liuqin": line["fushen"]["liuqin"],
                    "ganzhi": line["fushen"]["ganzhi"],
                }
            )

    return {
        "branch": branch,
        "wuxing": BRANCH_TO_WUXING[branch],
        "shi_line": shi_line,
        "shi_line_name": LINE_LABELS[shi_line],
        "shi_line_yin_yang": shi_line_record["yin_yang"],
        "start_branch": "子" if is_yang_shi else "午",
        "appears_in_main": bool(main_matches),
        "appears_in_fushen": bool(fushen_matches),
        "main_matches": main_matches,
        "fushen_matches": fushen_matches,
    }


def build_hexagram_record(hexagram_name):
    """Build one fully-expanded static record for a hexagram."""

    up_trigram, down_trigram = HEXAGRAM_NAME_TO_PAIR[hexagram_name]
    palace_name = PALACE_BY_HEXAGRAM[hexagram_name]
    palace_wuxing = TRIGRAM_META[palace_name]["wuxing"]
    stage_index = PALACE_STAGE_INDEX_BY_HEXAGRAM[hexagram_name]
    shi_line = SHI_LINE_BY_STAGE_INDEX[stage_index]
    ying_line = get_opposite_line(shi_line)

    lines = build_main_lines(down_trigram, up_trigram, palace_wuxing)
    palace_head_name = PALACE_HEXAGRAMS[palace_name][0]
    palace_head_up, palace_head_down = HEXAGRAM_NAME_TO_PAIR[palace_head_name]
    palace_head_lines = build_main_lines(palace_head_down, palace_head_up, palace_wuxing)
    lines = attach_fushen(lines, palace_head_lines)

    for line in lines:
        line["is_shi"] = line["index"] == shi_line
        line["is_ying"] = line["index"] == ying_line

    return {
        "name": hexagram_name,
        "number": HEXAGRAM_NUMBER_BY_NAME[hexagram_name],
        "symbol": HEXAGRAM_SYMBOL_BY_NAME[hexagram_name],
        "up_trigram": up_trigram,
        "up_trigram_symbol": TRIGRAM_META[up_trigram]["symbol"],
        "down_trigram": down_trigram,
        "down_trigram_symbol": TRIGRAM_META[down_trigram]["symbol"],
        "gong": palace_name,
        "gong_wuxing": palace_wuxing,
        "gong_stage": PALACE_STAGE_NAMES[stage_index],
        "shi_line": shi_line,
        "shi_line_name": LINE_LABELS[shi_line],
        "ying_line": ying_line,
        "ying_line_name": LINE_LABELS[ying_line],
        "gua_shen": build_gua_shen(lines, shi_line),
        "is_six_chong": hexagram_name in SIX_CHONG_DETAIL,
        "is_six_he": hexagram_name in SIX_HE_DETAIL,
        "six_chong_pairs": list(SIX_CHONG_DETAIL.get(hexagram_name, ())),
        "six_he_pairs": list(SIX_HE_DETAIL.get(hexagram_name, ())),
        "lines": lines,
    }


def build_all_64gua_table():
    """Build the full 64-hexagram static table in King Wen order."""

    return {
        hexagram_name: build_hexagram_record(hexagram_name)
        for hexagram_name in KING_WEN_NAMES
    }
