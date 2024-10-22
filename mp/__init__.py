# """
# CodeLibrary.__init__.py
# ~~~~~~~~~~~~~~~~~~~~~~~
#
# Function:
#
# Crater: lin
# CreateDate: 2023-03-27
# """
import matplotlib.pyplot as plt
import numpy as np

# 创建数据
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# 绘制图形
fig, ax = plt.subplots()
ax.plot(x, y, label='sin(x)')

# 设置x轴和y轴交叉点的刻度展示
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))

# 设置x轴和y轴的标签
ax.set_xlabel('x')
ax.set_ylabel('y')

# 设置标题
ax.set_title('Sine Curve')

# 添加图例
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1)

# 显示图形
plt.show()








