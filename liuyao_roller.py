# 六爻钱卦，每次扔三枚铜钱，扔六次
# 古钱币：背面（花面、满文）为阳，正面（汉字面）为阴
# 现代五毛钱：反面阳，正面阴
import random


# 一个阳面：          少阳 ——
# 两个阳面(一个阴面)：  少阴 --
# 全是阳面：          老阳 ——o(变阴)
# 全是阴面：          老阴 --o(变阳)
class LiuYao(object):
    def __init__(self):
        self.count_of_YANG = []
        self.YANG_to_YAO ={0:"老阴",1:"少阳",2:"少阴",3:"老阳"}
        self.count = 0


    def _roll(self):
        '''
        程序模拟扔一次，返回三个硬币的结果，解读交给上一层方法
        '''
        coin1 = random.randint(0,1)
        coin2 = random.randint(0,1)
        coin3 = random.randint(0,1)

        return coin1,coin2,coin3

    def clear_result(self):
        self.count = 0
        self.count_of_YANG = []

    def get_single_result(self):
        '''
            把赛博抛硬币roll得到的结果进行记录
        '''
        result = self._roll()
        self.count +=1
        self.count_of_YANG.append(result.count(1))

        return {
            'status': 'success',
            'info': f'第{self.count}次结果:{self.count_of_YANG[self.count - 1]}个阳,{3-self.count_of_YANG[self.count - 1]}个阴'
        }

    def fill_single_result(self):

        '''
            手动填写抛硬币结果
        '''
        coin1= input("第一枚硬币阴阳：0阴1阳，只输入数字:")
        coin2= input("第二枚硬币阴阳：0阴1阳，只输入数字:")
        coin3= input("第三枚硬币阴阳：0阴1阳，只输入数字:")

        self.count_of_YANG.append((coin1,coin2,coin3).count("1"))
        self.count += 1
        return {
            'status': 'success',
            'info': f'第{self.count}次结果:{self.count_of_YANG[self.count - 1]}个阳,{3-self.count_of_YANG[self.count - 1]}个阴'
        }
    def finish_this_round(self):

        '''
            结算结果
        '''

        result = [self.YANG_to_YAO[yang] for yang in self.count_of_YANG]

        self.clear_result()
        return result

    def run(self):
        self.count = 0
        while self.count<6:
            msg = ""
            user_input = input("输入roll电子抛硬币，输入fill手动填写结果:")
            if user_input == 'roll':
                msg = self.get_single_result()
                print(msg)
            elif user_input == 'fill':
                msg = self.fill_single_result()
                print(msg)
            else:
                print("去你吗的，好好输")

        result = self.finish_this_round()

        print(result)
        return result

if __name__ == '__main__':
    liuyao = LiuYao()

    liuyao.run()
