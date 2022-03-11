import tkinter as tk
from know_all_exceptEl import window_exceptEL
from eco_con import MoneyElasticity
from eco_con import IncomeElasticity
from eco_con import CrossPriceElasticity
from window_choice import MainWindow
import numpy as np


def open_window_price():
    win_price= window_exceptEL()
    win_price.start_window()



    def command1():
        now_need=int(win_price.E_nowneed.get())
        past_need=int(win_price.E_pastneed.get())
        now_price=int(win_price.E_np.get())
        past_price=int(win_price.E_pp.get())
        format_H=win_price.LB.get(win_price.LB.curselection())
        ELasticity=MoneyElasticity(now_need,now_price,past_need,past_price,format_H)
        elasticity=ELasticity.get_price_elasticity()
        #TODO 进一步提出建议，根据弹性
        win_price.E_tell.insert('0.0',elasticity)
        if np.abs(elasticity)>1:
            win_price.E_tell.insert('end','富有弹性\n 价格下降时，收益将增加')
        if np.abs(elasticity)<1:
            win_price.E_tell.insert('end','缺乏弹性\n 价格下降时，收益下降')
        if np.abs(elasticity)==1:
            win_price.E_tell.insert('end','单位弹性\n 价格下降时，收益不变')

    def add_Button():
        B=tk.Button(win_price.window_getEL,text='开始',command=command1,height=1,width=10,bg='red')
        B_quit=tk.Button(win_price.window_getEL,text='退出',command=quit,height=1,width=10,bg='red')
        B.place(x=90,y=130)
        B_quit.place(x=90,y=160)




    add_Button()
    win_price.window_getEL.mainloop()


def open_window_income():
    win_income=window_exceptEL()
    win_income.start_window()



    def command1():
        now_need=int(win_income.E_nowneed.get())
        past_need=int(win_income.E_pastneed.get())
        now_price=int(win_income.E_np.get())
        past_price=int(win_income.E_pp.get())
        format_H=win_income.LB.get(win_income.LB.curselection())
        ELasticity=IncomeElasticity(now_need,now_price,past_need,past_price,format_H)
        elasticity=ELasticity.get_income_elasticity()
        #TODO 进一步提出建议，根据弹性
        win_income.E_tell.insert('0.0',elasticity)
        if np.abs(elasticity) > 1:
            win_price.E_tell.insert('end', '富有弹性\n 收入下降时，收益将增加')
        if np.abs(elasticity) < 1:
            win_price.E_tell.insert('end', '缺乏弹性\n 收入下降时，收益下降')
        if np.abs(elasticity) == 1:
            win_price.E_tell.insert('end', '单位弹性\n 收入下降时，收益不变')


    def add_Button():
        B=tk.Button(win_income.window_getEL,text='开始',command=command1,height=1,width=10,bg='red')
        B_quit=tk.Button(win_income.window_getEL,text='退出',command=quit,height=1,width=10,bg='red')
        B.place(x=90,y=130)
        B_quit.place(x=90,y=160)



    add_Button()
    win_income.window_getEL.mainloop()



def open_window_cross():
    win_cross=window_exceptEL()
    win_cross.start_window()

    def command1():
        now_need=int(win_cross.E_nowneed.get())
        past_need=int(win_cross.E_pastneed.get())
        now_price=int(win_cross.E_np.get())
        past_price=int(win_cross.E_pp.get())
        format_H=win_cross.LB.get(win_cross.LB.curselection())
        ELasticity=CrossPriceElasticity(now_need,now_price,past_need,past_price,format_H)
        elasticity=ELasticity.get_CrossPrice_Elastictiy()
        #TODO 进一步提出建议，根据弹性
        win_cross.E_tell.insert('0.0',elasticity)
        if elasticity > 0:
            win_price.E_tell.insert('end', '1价格与2的需求同方向变动，两种运输见有可替代性')
        if elasticity< 0:
            win_price.E_tell.insert('end', '1价格与2的需求反方向变动，两种运输之间存在互补关系')


    def add_Button():
        B=tk.Button(win_cross.window_getEL,text='开始',command=command1,height=1,width=10,bg='red')
        B_quit=tk.Button(win_cross.window_getEL,text='退出',command=quit,height=1,width=10,bg='red')
        B.place(x=90,y=130)
        B_quit.place(x=90,y=160)



    add_Button()
    win_cross.window_getEL.mainloop()


def startpro():
    mainwin=MainWindow()
    mainwin.choicemenu.add_command(label='价格',command=open_window_price)
    mainwin.choicemenu.add_command(label='收入',command=open_window_income)
    mainwin.choicemenu.add_command(label='交叉',command=open_window_cross)
    mainwin.choicemenu.add_separator()
    mainwin.choicemenu.add_command(label='退出',command=quit)
    mainwin.mainwindow.config(menu=mainwin.menu)

    mainwin.mainwindow.mainloop()

if __name__=='__main__':
    startpro()


# self.choicemenu.add_cascade(label='价格',command=open_window_price)
# self.choicemenu.add_cascade(label='价格',command=open_window_income)
# self.choicemenu.add_cascade(label='交叉',command=open_window_cross)

