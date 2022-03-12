# TODO 获取弹性（价格弹性）
import numpy as np


class MoneyElasticity():

    def __init__(self, nowneed, nowmoney, pastneed, pastmoney, H_format):



        self.nowneed = nowneed
        self.nowmoney = nowmoney
        self.pastmoney = pastmoney
        self.pastneed = pastneed
        self.H_formart = H_format
        self.elasticity = (self.nowneed - self.pastneed) / (self.nowmoney - self.pastmoney)
        self.point_elasticity = self.elasticity * (self.pastmoney / self.pastneed)

    # def what_type(self):
    #
    #     if self.H_formart=='线性':
    #         return True
    #     if self.H_formart=='对数':
    #         return False
    #
    def get_price_elasticity(self):
        # self.pro_money=(self.nowmoney-self.pastmoney)/self.pastmoney
        # self.pro_need=(self.nowneed-self.pastneed)/self.pastneed
        if self.H_formart == '线性':
            return self.point_elasticity
        if self.H_formart == '对数':
            return np.log(self.nowneed / self.pastneed) / np.log(self.nowmoney / self.pastmoney)


# TODO 获取弹性（收入弹性）
class IncomeElasticity:

    def __init__(self, nowneed, nowincome, pastneed, pastincom,H_formart):
        self.H_formart = H_formart
        self.nowneed = nowneed
        self.nowincome = nowincome
        self.pastneed = pastneed
        self.pastincome = pastincom
        self.elasticity = (self.nowneed - self.pastneed) / (self.nowincome - self.pastincome)
        self.point_elasticity = self.elasticity * (self.pastincome / self.pastneed)

    def get_income_elasticity(self):
        if self.H_formart == '线性':
            return self.point_elasticity
        if self.H_formart == '对数':
            return np.log(self.nowneed / self.pastneed) / np.log(self.nowincome / self.pastincome)


# TODO 获取弹性（交叉弹性）
class CrossPriceElasticity:

    def __init__(self, needone, priceone, needtwo, pricetwo,H_formart):  # 两个需求，两个价格


        self.H_formart = H_formart
        self.needone = needone
        self.needtwo = needtwo
        self.priceone = priceone
        self.pricetwo = pricetwo
        self.elasticity = (self.needone - self.needtwo) / (self.priceone - self.pricetwo)
        self.point_elasticity = self.elasticity * (self.pricetwo / self.needtwo)

    def get_CrossPrice_Elastictiy(self):

        if self.H_formart == '线性':
            return self.point_elasticity
        if self.H_formart == '对数':
            return np.log(self.needone / self.needtwo) / np.log(self.priceone / self.pricetwo)
