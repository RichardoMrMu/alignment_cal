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
    data_path = 'F:\debug\cal_alignment\\alignment'
    data_name = []
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
        error = diffi_note[abs(diffi_note)>0.5]
        normal = diffi_note[abs(diffi_note)<=0.5]
        df = pd.DataFrame({'diffirence':diffi_note,'normal':normal,'error':error,'sum':diffi_note.shape,'error_rate':(len(error) * 1.)/len(diffi_note)})
        # print(df.loc[df['diffirence']>0.5])
        df.to_csv("%s\\%s.csv"%('F:\debug\cal_alignment\\csvlist',data_name[i][0:-4]))
        # 画图
        img_plot(diffi_note)

if __name__ == '__main__':
    main()