# zhuanggua.py

from data.gua_table import (YAO_TO_BEN_LINE,YAO_TO_BIAN_LINE,TRIGRAM_BY_LINES,HEXAGRAM_BY_TRIGRAMS)
from liuyao_roller import LiuYao
from data.all_64gua_table import to_string

class ZhuangGua(object):
    def __init__(self):
        self.yaos = []
        self.ben_gua_up = ""
        self.ben_gua_down = ""
        self.ben_gua = ""
        self.bian_gua_up = ""
        self.bian_gua_down = ""
        self.bian_gua = ""
        self.query = ""

    def load_yaos(self,yaos):
        self.yaos = yaos
        self.ben_gua_down,self.ben_gua_up,self.ben_gua = self.get_gua_by_yao(self.yaos,YAO_TO_BEN_LINE)
        self.bian_gua_down,self.bian_gua_up,self.bian_gua = self.get_gua_by_yao(self.yaos,YAO_TO_BIAN_LINE)
        return self

    def get_gua_by_yao(self,yaos,line_maps):
        lines = [line_maps[yao] for yao in yaos] # 先把["少阴", "少阴", "老阴", "老阳", "少阳", "少阳"]转化成阴阳，对卦

        down_gua = TRIGRAM_BY_LINES[tuple(lines[:3])] #取下卦，列表不能当字典key
        up_gua = TRIGRAM_BY_LINES[tuple(lines[3:])] #取上卦

        gua_name = HEXAGRAM_BY_TRIGRAMS[(up_gua,down_gua)] #打表的时候是(上卦，下卦)

        return down_gua,up_gua,gua_name

    def __str__(self):
        return (
            f"本卦：{self.ben_gua}（上{self.ben_gua_up} 下{self.ben_gua_down}）\n"
            f"变卦：{self.bian_gua}（上{self.bian_gua_up} 下{self.bian_gua_down}）"
        )

    def get_detail_info_of_ben_gua(self):
        return to_string(self.ben_gua)
    def get_detail_info_of_bian_gua(self):
        return to_string(self.bian_gua)

if __name__ == '__main__':
    query = input("请输入你要咨询的问题:")
    liuyao = LiuYao()

    result = liuyao.run()

    gua = ZhuangGua().load_yaos(result)

    print(f"你要咨询的问题是:{query}")
    print(f"本次卦象如下\n{gua}")
    print(f"本卦详细信息\n{gua.get_detail_info_of_ben_gua()}")
    print(f"变卦详细信息\n{gua.get_detail_info_of_bian_gua()}")

