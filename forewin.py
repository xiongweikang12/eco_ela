import tkinter as tk
import numpy as np
from know_all_exceptEl import foreWindow
import time


def fore_1():
    # time.sleep(1)
    # mainwin.mainwindow.destroy()

    win_forecast_price = foreWindow()

    def fore_result1():  # 预测需求，要求其价格 #np,pp,pq,el
        input_getq = win_forecast_price.E_forecast.get()
        input_getq = input_getq.split('，')
        print(input_getq)
        if len(input_getq) == 4 and np.abs(float(input_getq[0])) > 1:  # nq,pq,pp,el
            pro_q = (float(input_getq[0]) - float(input_getq[1])) / float(input_getq[1])
            now_p = ((pro_q * float(input_getq[-1])) + 1) * float(input_getq[2])
            win_forecast_price.E_tell_result_forecast.insert('end', '现价：{} 过价：{} 过需：{} 弹性：{} 预测需求:{:.2f}\n'
                                                             .format(input_getq[0], input_getq[1], input_getq[2],
                                                                     input_getq[-1], now_p))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益:{}'.format(now_p * float(input_getq[0])))

        if len(input_getq) == 3 and np.abs(float(input_getq[0])) < 1:  # pro,pp,el
            now_p_2 = ((float(input_getq[0]) * float(input_getq[-1])) + 1) * float(input_getq[1])
            win_forecast_price.E_tell_result_forecast.insert('end', '价变：{} 过需：{} 弹性：{} 预测需求:{:.2f}\n'
                                                             .format(input_getq[0], input_getq[1], input_getq[2],
                                                                     now_p_2))

        if len(input_getq) == 4 and np.abs(float(input_getq[0])) < 1:  # pro,pp,pq,el
            now_p_2 = ((float(input_getq[0]) * float(input_getq[-1])) + 1) * float(input_getq[1])
            win_forecast_price.E_tell_result_forecast.insert('end', '价变：{} 过需：{} 弹性：{} 预测需求:{:.2f}\n'
                                                             .format(input_getq[0], input_getq[1], input_getq[-1],
                                                                     now_p_2))
            win_forecast_price.E_tell_result_forecast.insert('end', '收益:{}\n'.format(
                now_p_2 * (float(input_getq[0]) + 1) * float(input_getq[2])))

    def fore_result2():  # 预测价格,要求需求
        input_getp = win_forecast_price.E_forecast.get()
        input_getp = input_getp.split('，')
        print(input_getp)

        if len(input_getp) == 4 and float(input_getp[0])>1:  # nq,pq,pp,el
            pro_q = (float(input_getp[0]) - float(input_getp[1])) / float(input_getp[1])
            now_q = ((pro_q / float(input_getp[-1])) + 1) * float(input_getp[2])
            win_forecast_price.E_tell_result_forecast.insert('end', '现需：{} 过需：{} 过价：{} 弹性：{} 预测价格:{:.2f}\n'
                                                             .format(input_getp[0], input_getp[1], input_getp[2],
                                                                     input_getp[-1], now_q))
            win_forecast_price.E_tell_result_forecast.insert('end','收益:{}\n'.format(now_q*float(input_getp[0])))

        if len(input_getp) == 3 and np.abs(float(input_getp[0])) < 1:  # pro,pp,pn,el
            now_p_1 = ((float(input_getp[0]) / float(input_getp[-1])) + 1) * float(input_getp[1])
            win_forecast_price.E_tell_result_forecast.insert('end', '需变：{} 过价：{} 弹性：{} 预测价格:{:.2f}\n'
                                                             .format(input_getp[0], input_getp[1], input_getp[2],
                                                                     now_p_1))
        if len(input_getp) == 4 and np.abs(float(input_getp[0])) < 1:  # pro,pp,pq,el
            now_p_2 = ((float(input_getp[0]) * float(input_getp[-1])) + 1) * float(input_getp[1])
            win_forecast_price.E_tell_result_forecast.insert('end', '价变：{} 过需：{} 弹性：{} 预测需求:{:.2f}\n'
                                                                .format(input_getp[0], input_getp[1], input_getp[-1],
                                                                     now_p_2))

            win_forecast_price.E_tell_result_forecast.insert('end', '收益:{}\n'.format(
                now_p_2 * (float(input_getp[0]) + 1) * float(input_getp[2])))

        time.sleep(3)
        win_forecast_price.E_forecast.delete(0, tk.END)

    def quit_window():
        win_forecast_price.fore.destroy()

    RB_N = tk.Radiobutton(win_forecast_price.fore, text='需求', command=fore_result1)
    RB_N.place(x=70, y=30)
    RB_p = tk.Radiobutton(win_forecast_price.fore, text='价格/收入/其他', command=fore_result2)
    RB_p.place(x=120, y=30)
    B_Q = tk.Button(win_forecast_price.fore, text='退出', command=quit_window)
    B_Q.place(x=220, y=75)
    win_forecast_price.start_forecast()
    win_forecast_price.fore.mainloop()

