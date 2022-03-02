"""
CodeLibrary.base
~~~~~~~~~~~~~~~~

Function: pandas基础操作

Crater: lin
CreateDate: 2022-01-11
"""
import pandas as pd
import numpy as np

# 目标df
df = pd.DataFrame({"name": ['A', 'B', 'C', np.nan],
                   "age": [np.nan, 22, 25, np.nan],
                   "gender": ['male', 'female', 'male', 'female'],
                   })

# 删除name、age列中,【任意一列】的值为空的行；
df.dropna(subset=['name', 'age'],
          axis=0,  # axis=0表示删除行；
          how='any',  # how=any表示若列name、age中，任意一个出现空值，就删掉该行
          inplace=True  # inplace=True表示在原df上进行修改；
          )

# 删除name、age列中,二者都为空的行。
# 删除都为空的行，还是删除任意一列值为空的行，使用参数how来控制
df.dropna(subset=['name', 'age'],
          axis=0,
          how='all',  # how='all'表示若指定列的值都为空，就删掉该行
          inplace=True)
