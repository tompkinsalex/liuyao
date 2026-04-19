import os

from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from config import role_prompt
from liuyao_roller import LiuYao
from qigua_time import get_qigua_time_info
from zhuanggua import ZhuangGua




deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

model = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    api_key = deepseek_api_key,
    temperature=0.0)

prompt = ChatPromptTemplate(
    [
        ("system",role_prompt),
        ("human","用户提问：{query}")
    ]
)

chain = prompt | model | StrOutputParser()


if __name__ == '__main__':

    query = input("请输入你要咨询的问题:")
    qigua_time_info = get_qigua_time_info()
    yang_time = qigua_time_info['qigua_time']
    richen_ganzhi = qigua_time_info['richen_ganzhi']
    xunkong = qigua_time_info['xunkong']
    liushen = qigua_time_info['liushen']
    liuyao = LiuYao()


    result = liuyao.run()

    gua = ZhuangGua().load_yaos(result)
    ben_gua_info = gua.get_detail_info_of_ben_gua()
    bian_gua_info = gua.get_detail_info_of_bian_gua()

    print(f"你要咨询的问题是:{query}")
    print(f"本次卦象如下\n{gua}")
    print(f"本卦详细信息\n{ben_gua_info}")
    print(f"变卦详细信息\n{bian_gua_info}")
    print("大模型解读中...")
    res = chain.invoke({"qigua_time":yang_time,"richen_ganzhi":richen_ganzhi,
                        "xunkong":xunkong,"liushen":liushen,"query":query,"ben_gua_data":ben_gua_info,
                        "bian_gua_data":bian_gua_info})

    print(res,flush=True)

