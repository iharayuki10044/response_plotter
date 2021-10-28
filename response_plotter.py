#!/usr/bin/python3

import numpy as np
import matplotlib 
from matplotlib import pyplot

file_name = "./data.txt"
#data.txtを自分の読み込ませたいファイル名にする


try:
    file = open(file_name)
    data_list = file.read().split("\n")
except Exception as e:
    print(e)
finally:
    file.close()

x = []
y1 = []
y2 = []
index_num = 0
#表示させたい変数が増えたらy3のように増やしてfor loopの中にも書き加えてください

for index in range(len(data_list)):
    splited_data = data_list[index].split(", ")
    x += [float(splited_data[0])]
    y1 += [float(splited_data[1])]
    y2 += [float(splited_data[2])]
    index_num = index

pyplot.plot(x,y1, label="MVn")
pyplot.plot(x,y2, label="PVn")
pyplot.xlabel("time[sec]")
pyplot.ylabel("response[rpm]")
pyplot.show()
