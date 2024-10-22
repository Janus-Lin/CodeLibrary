"""
CodeLibrary.chrt
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2023-03-30
"""
import matplotlib.pyplot as plt
import numpy as np

# # 生成数据
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.exp(x)
#
# # 创建图形和子图对象
# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(8, 8))
#
# # 绘制第一个折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
# ax1.plot(x, y1, color='blue', linewidth=2, linestyle='-', label='sin(x)', alpha=0.7, dashes=[6, 2])
#
# # 绘制第二个折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
# ax2.plot(x, y2, color='red', linewidth=2, linestyle='--', label='exp(x)', alpha=0.7, dashes=[2, 2])
#
# # 添加标题和坐标轴标签，设置字体大小和颜色
# fig.suptitle('Two complex plots sharing the same x-axis', fontsize=18, color='green')
# ax1.set_ylabel('sin(x)', fontsize=14, color='blue')
# ax2.set_ylabel('exp(x)', fontsize=14, color='blue')
# ax2.set_xlabel('x', fontsize=14, color='blue')
#
# # 设置坐标轴范围和刻度
# ax1.set_xlim(0, 10)
# ax1.set_xticks(np.linspace(0, 10, 11))
# ax2.set_ylim(0, 22000)
# ax2.set_yticks(np.linspace(0, 20000, 5))
#
# # 添加网格线，设置颜色、样式和透明度
# ax1.grid(color='gray', linestyle='--', alpha=0.5)
# ax2.grid(color='gray', linestyle='--', alpha=0.5)
#
# # 添加图例，设置位置和字体大小
# ax1.legend(loc='upper right', fontsize=12)
# ax2.legend(loc='upper right', fontsize=12)
#
# # 显示图形
# plt.show()


# 生成数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.exp(x)

# 创建图形对象
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制第一个折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
ax.plot(x, y1, color='blue', linewidth=2, linestyle='-', label='sin(x)', alpha=0.7, dashes=[6, 2])

# 绘制第二个折线图，设置线条颜色、宽度、样式、标签、透明度和虚线
ax2 = ax.twinx()  # 创建第二个y轴
ax2.plot(x, y2, color='red', linewidth=2, linestyle='--', label='exp(x)', alpha=0.7, dashes=[2, 2])

# 添加标题和坐标轴标签，设置字体大小和颜色
ax.set_title('Two complex plots in one figure', fontsize=18, color='green')
ax.set_xlabel('x', fontsize=14, color='blue')
ax.set_ylabel('sin(x)', fontsize=14, color='blue')
ax2.set_ylabel('exp(x)', fontsize=14, color='blue')

# 设置坐标轴范围和刻度
ax.set_xlim(0, 10)
ax.set_xticks(np.linspace(0, 10, 11))
ax2.set_ylim(0, 22000)
ax2.set_yticks(np.linspace(0, 20000, 5))

# 添加网格线，设置颜色、样式和透明度
ax.grid(color='gray', linestyle='--', alpha=0.5)
ax2.grid(color='gray', linestyle='--', alpha=0.5)

# 添加图例，设置位置和字体大小
lines = [ax.get_lines()[0], ax2.get_lines()[0]]
ax.legend(lines, [line.get_label() for line in lines], loc='upper right', fontsize=12)

# 显示图形
plt.show()
