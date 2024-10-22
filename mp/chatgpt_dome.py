"""
CodeLibrary.chatgpt_dome
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2023-03-30
"""
import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图形和子图对象
fig, ax = plt.subplots()

# 绘制折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
ax.plot(x, y1, color='blue', linewidth=2, linestyle='-', label='sin(x)', alpha=0.7, dashes=[6, 2])

# 绘制第二条折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
ax.plot(x, y2, color='red', linewidth=2, linestyle='--', label='cos(x)', alpha=0.7, dashes=[2, 2])

# 添加标题和坐标轴标签，设置字体大小和颜色
ax.set_title('A complex plot', fontsize=18, color='green')
ax.set_xlabel('x', fontsize=14, color='blue')
ax.set_ylabel('y', fontsize=14, color='blue')

# 设置坐标轴范围和刻度
ax.set_xlim(0, 10)
ax.set_xticks(np.linspace(0, 10, 11))
ax.set_ylim(-1, 1)
ax.set_yticks([-1, 0, 1])

# 添加网格线，设置颜色、样式和透明度
ax.grid(color='gray', linestyle='--', alpha=0.5)

# 添加图例，设置位置和字体大小
ax.legend(loc='upper right', fontsize=12)

# 添加注释，设置文本内容、箭头样式、颜色和字体大小
ax.annotate('Max', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=7),
            color='blue', fontsize=12)

# 显示图形
plt.show()
