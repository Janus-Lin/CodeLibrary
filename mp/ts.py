"""
CodeLibrary.ts
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2023-03-27
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['font.family'] = ['SimHei']  #mac用'Heiti TC'，windows用'SimHei'
#  注意：%matplotlib inline 是 Jupyter 提供的魔法命令，它可以把输出图显示在笔记本内部，否则会以查看器的形式单独显示。
# from matplotlib.font_manager import *  # 如果想在图上显示中文，需导入这个包
# 支持中文
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.rcParams['font.sans-serif']=['SimHei']解决缺失字体
# 排除警告信息
# import warnings
# warnings.filterwarnings("ignore")
# matplotlib画图常见参数设置
# mpl.rcParams["font.family"] = "SimHei" # 设置字体
# mpl.rcParams["axes.unicode_minus"]=False # 用来正常显示负号
# plt.rcParams['font.sans-serif']=['SimHei'] # 用来正常显示中文标签

x = np.linspace(-2*np.pi,2*np.pi,100)
y1 = x**2
y2 = 20*np.sin(x)
y3 = 20*np.cos(3*x)
fig, ax = plt.subplots(figsize=(13,6)) # Create a figure and an axes.
ax.plot(x, y1, linestyle='--',linewidth=3,c='plum',label='Quadratic') # Plot some data on the axes.
ax.plot(x,y2,marker='o',label='20Sin(x)',markerfacecolor='gold',markeredgecolor='firebrick') # Plot more data on the axes...
ax.plot(x, y3, marker='x',label='20Cos(3x)')
plt.show()