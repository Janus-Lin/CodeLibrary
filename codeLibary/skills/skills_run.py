"""
CodeLibrary.skills_run
~~~~~~~~~~~~~~~~~~~~~~

Function: Python实用技巧和工具

Crater: lin
CreateDate: 2022-01-11
"""
# 交换变量
x = 6
y = 5
x, y = y, x
print(x, y)

# .if 语句在行内
print("Hello" if False else "World")

# 数字技巧
print(f'除后向下取整： {5.0 // 2}')
print(f'2的5次方： {2 ** 5}')

# 数值比较
x = 2
if 3 > x > 1:
    print(x)

if 1 < x > 0:
    print(x)

# 同时迭代两个列表
nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for teama, teamb in zip(nfc, afc):
    print(teama + " vs. " + teamb)

# 带索引的列表迭代
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print(index, team)

# 列表推导式：已知一个列表，我们可以刷选出偶数列表方法
numbers = [1, 2, 3, 4, 5, 6]
even = [number for number in numbers if number % 2 == 0]
print(f'even: {even}')

# 字典推导式
teams = ["Packers", "49ers", "Ravens", "Patriots"]
print({key: value for key, value in enumerate(teams)})

# 我承认try/except代码并不雅致，不过这里有一种简单方法，尝试在字典中查找key，如果没有找到对应的alue将用第二个参数设为其变量值。
data = {'user': 1, 'name': 'Max', 'three': 4}
try:
    is_admin = data['admin']
except KeyError:
    is_admin = False

# 优雅
data = {'user': 1, 'name': 'Max', 'three': 4}
is_admin = data.get('admin', False)

# 获取列表的子集
x = [1, 2, 3, 4, 5, 6]
# 前3个
print(f'原始数据: {x}')
print(f'前3个: x[:3]= {x[:3]}')
print(f'中间4个: x[1:5]= {x[1:5]}')
print(f'最后3个: x[-3:]= {x[-3:]}')
print(f'奇数项:  x[::2]= {x[::2]}')
print(f'偶数项:  x[1::2]= {x[1::2]}')
