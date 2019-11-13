# -*- coding: utf-8 -*-
# @Time    : 2019-11-13 18:34
# @Author  : RichardoMu
# @File    : difference_of_score.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

def img_plot(diffi_note):
    plt.plot(np.arange(len(diffi_note)),diffi_note)
    plt.show()

def main():
    data_path = 'E:\debug\pyCharmdeBug\\alignment_cal\\alignment'
    data_name = []
    error_rate = 0.
    normal_rate = 0.
    lenth = 0.
    eval_df = pd.DataFrame([],columns=['error','normal'])
    for name in os.listdir(data_path):
        data_name.append(name)
    for i in range(len(data_name)):
        data = pd.read_csv(os.path.join(data_path,data_name[i]))
        data_array = np.array(data)
        data_list = []
        for data in data_array:
            temp = ''.join(data).split()
            data_list.append(temp)
        real_data = np.array(data_list)
        ground_note = real_data[:,0]
        score_note = real_data[:,1]
        diffi_note = np.array([float(score_note[i]) - float(ground_note[i] ) for i in range(len(score_note)) ])

        # evaluate
        error = diffi_note[abs(diffi_note)>0.5]
        normal = diffi_note[abs(diffi_note)<=0.5]
        lenth += len(diffi_note)
        error_rate += len(error)
        normal_rate += len(normal)

        df2 = pd.DataFrame([[len(error)/len(diffi_note),len(normal)/len(diffi_note)]],columns=['error','normal'])
        # print(df2)

        df = pd.DataFrame({'diffirence':diffi_note})
        eval_df = pd.concat([eval_df,df2])
        # print(df.loc[df['diffirence']>0.5])
        df.to_csv("%s\\%s.csv"%('E:\debug\pyCharmdeBug\\alignment_cal\\csvlist',data_name[i][0:-4]))
        # 画图
        # img_plot(diffi_note)
    error_rate/=lenth
    normal_rate/=lenth
    df3 = pd.DataFrame([[error_rate,normal_rate]],columns=['error','normal'])
    eval_df = pd.concat([eval_df,df3])
    eval_df.to_csv("%s\\%s.csv"%('E:\debug\pyCharmdeBug\\alignment_cal\\csvlist','avg'))
if __name__ == '__main__':
    main()