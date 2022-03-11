#TODO 获取弹性（价格弹性）
import numpy as np

class MoneyElasticity():

    def __init__(self,nowneed,nowmoney,pastneed,pastmoney,H_format):
        self.nowneed=nowneed
        self.nowmoney=nowmoney
        self.pastmoney=pastmoney
        self.pastneed=pastneed
        self.H_formart=H_format

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
        self.elasticity=(self.nowneed-self.pastneed)/(self.nowmoney-self.pastmoney)
        self.point_elasticity=self.elasticity*(self.pastmoney/self.pastneed)
        if self.H_formart=='线性':
            return self.point_elasticity
        if self.H_formart=='对数':
            return np.log((self.nowneed/self.pastneed)-(self.nowmoney/self.pastmoney))



#TODO 获取弹性（收入弹性）
class IncomeElasticity():

    def __init__(self,nowneed,nowincome,pastneed,pastincom):
        self.nowneed=nowneed
        self.nowincome=nowincome
        self.pastneed=pastneed
        self.pastincome=pastincom


    def get_income_elasticity(self):
        self.elasticity = (self.nowneed - self.pastneed) / (self.nowincome - self.pastincome)
        self.point_elasticity = self.elasticity * (self.pastincome / self.pastneed)
        if self.H_formart == '线性':
            return self.point_elasticity
        if self.H_formart == '对数':
            return np.log((self.nowneed / self.pastneed) - (self.nowincome / self.pastincome))




#TODO 获取弹性（交叉弹性）
class CrossPriceElasticity():

    def __init__(self,needone,priceone,needtwo,pricetwo): #两个需求，两个价格
        self.needone=needone
        self.needtwo=needtwo
        self.priceone=priceone
        self.pricetwo=pricetwo


    def get_CrossPrice_Elastictiy(self):

        self.elasticity = (self.needone- self.needtwo) / (self.priceone - self.pricetwo)
        self.point_elasticity = self.elasticity * (self.pricetwo / self.needtwo)
        if self.H_formart == '线性':
            return self.point_elasticity
        if self.H_formart == '对数':
            return np.log((self.needone / self.needtwo) - (self.priceone/ self.pricetwo))

















