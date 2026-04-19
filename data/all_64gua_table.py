"""六十四卦总表。

用法示例：
    from data.all_64gua_table import all_64gua_table, to_string
    gua = all_64gua_table["天山遁"]
    print(gua["fuhao"])
    print(gua["yaos"][0])
    print(to_string("天山遁"))
"""

from data.liushen_rule import shengcheng_all_64gua_table


all_64gua_table = shengcheng_all_64gua_table()


def _fushen_to_string(fushen):
    """把伏神信息转成一小段文字。"""

    if not fushen:
        return "无伏神"

    return (
        f"伏神：{fushen['liuqin']} {fushen['ganzhi']} "
        f"{fushen['wuxing']}"
    )


def _yao_to_string(yao):
    """把单爻信息转成一行文字。"""

    biaoji = []
    if yao["shifou_shiyao"]:
        biaoji.append("世")
    if yao["shifou_yingyao"]:
        biaoji.append("应")

    biaoji_text = f"（{'、'.join(biaoji)}）" if biaoji else ""

    return (
        f"{yao['yaoming']}{biaoji_text}："
        f"{yao['yinyang']}爻，"
        f"{yao['liuqin']}，"
        f"{yao['ganzhi']}，"
        f"五行{yao['wuxing']}，"
        f"{_fushen_to_string(yao['fushen'])}"
    )


def _guashen_to_string(guashen):
    """把卦身信息转成一小段文字。"""

    bengua_weizhi = "、".join(item["yaoming"] for item in guashen["bengua_weizhi"])
    fushen_weizhi = "、".join(item["yaoming"] for item in guashen["fushen_weizhi"])

    if not bengua_weizhi:
        bengua_weizhi = "未见于明爻"
    if not fushen_weizhi:
        fushen_weizhi = "未见于伏神"

    return (
        f"卦身地支{guashen['dizhi']}，五行{guashen['wuxing']}；"
        f"依据{guashen['genju_shiyao_ming']}{guashen['shiyao_yinyang']}世，"
        f"从{guashen['qishi_dizhi']}起；"
        f"明爻位置：{bengua_weizhi}；"
        f"伏神位置：{fushen_weizhi}"
    )


def to_string(guaming):
    """按卦名返回适合放进 prompt 的完整卦信息文本。

    参数：
        guaming：卦名，例如 "天山遁"。

    返回：
        一段字符串，包含卦名、符号、上下卦、宫位、世应、卦身、
        六冲六合、六爻纳甲和伏神信息。
    """

    gua = all_64gua_table[guaming]
    liuchong_text = "是" if gua["shifou_liuchong"] else "否"
    liuhe_text = "是" if gua["shifou_liuhe"] else "否"
    liuchong_dui = "、".join(gua["liuchong_dui"]) if gua["liuchong_dui"] else "无"
    liuhe_dui = "、".join(gua["liuhe_dui"]) if gua["liuhe_dui"] else "无"

    lines = [
        f"卦名：{gua['guaming']} {gua['fuhao']}，序号：{gua['xuhao']}",
        (
            f"上下卦：上卦{gua['shanggua']}{gua['shanggua_fuhao']}，"
            f"下卦{gua['xiagua']}{gua['xiagua_fuhao']}"
        ),
        (
            f"所属八宫：{gua['gong']}宫，宫位五行：{gua['gong_wuxing']}，"
            f"阶段：{gua['gong_jieduan']}"
        ),
        f"世应：世爻在{gua['shiyao_ming']}，应爻在{gua['yingyao_ming']}",
        f"卦身：{_guashen_to_string(gua['guashen'])}",
        f"六冲：{liuchong_text}，冲对：{liuchong_dui}",
        f"六合：{liuhe_text}，合对：{liuhe_dui}",
        "六爻明细如下，顺序为从初爻到上爻：",
    ]

    lines.extend(_yao_to_string(yao) for yao in gua["yaos"])

    return "\n".join(lines)

if __name__ == '__main__':
    print(all_64gua_table)
