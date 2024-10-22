"""
CodeLibrary.pandas_315
~~~~~~~~~~~~~~~~~~~~~~

Function: 计算每小时电费
link: https://blog.51cto.com/u_15155099/2817814

Crater: lin
CreateDate: 2023-04-11
"""
import timeit
import pandas as pd
import numpy as np


# 计时器
def clock(func):
    def clocked(*args):
        t0 = timeit.default_timer()
        result = func(*args)
        elapsed = timeit.default_timer() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s)' % (elapsed, name, arg_str))
        return result

    return clocked


# 分段计费函数
def apply_tariff(kwh, hour):
    """计算每个小时的电费"""
    if 0 <= hour < 7:
        rate = 12
    elif 7 <= hour < 17:
        rate = 20
    elif 17 <= hour < 24:
        rate = 28
    else:
        raise ValueError(f'Invalid hour: {hour}')
    return rate * kwh


def apply_tariff_loop(df):
    """用for循环计算enery cost，并添加到列表"""
    energy_cost_list = []
    for i in range(len(df)):
        # 获取用电量和时间（小时）
        energy_used = df.iloc[i]['energy_kwh']
        hour = df.iloc[i]['date_time'].hour
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
    df['cost_cents'] = energy_cost_list
    return df


def apply_tariff_iterrows(df):
    """使用 iterrows循环"""
    energy_cost_list = []
    for index, row in df.iterrows():
        # 获取用电量和时间（小时）
        energy_used = row['energy_kwh']
        hour = row['date_time'].hour
        # 添加cost列表
        energy_cost = apply_tariff(energy_used, hour)
        energy_cost_list.append(energy_cost)
    df['cost_cents'] = energy_cost_list


def apply_tariff_withapply(df):
    """pandas的apply方法"""
    df['cost_cents'] = df.apply(lambda row: apply_tariff(kwh=row['energy_kwh'], hour=row['date_time'].hour), axis=1)


def apply_tariff_isin(df):
    """矢量化操作：使用.isin选择数据"""
    # 定义小时范围Boolean数组
    peak_hours = df.index.hour.isin(range(17, 24))
    shoulder_hours = df.index.hour.isin(range(7, 17))
    off_peak_hours = df.index.hour.isin(range(0, 7))
    #
    # 使用上面apply_traffic函数中的定义
    df.loc[peak_hours, 'cost_cents'] = df.loc[peak_hours, 'energy_kwh'] * 28
    df.loc[shoulder_hours, 'cost_cents'] = df.loc[shoulder_hours, 'energy_kwh'] * 20
    df.loc[off_peak_hours, 'cost_cents'] = df.loc[off_peak_hours, 'energy_kwh'] * 12


def apply_tariff_cut(df):
    """使用pandas的pd.cut()函数来自动完成切割"""
    cents_per_kwh = pd.cut(x=df.index.hour,
                           bins=[0, 7, 17, 24],
                           include_lowest=True,
                           labels=[12, 20, 28]).astype(int)
    df['cost_cents'] = cents_per_kwh * df['energy_kwh']


def apply_tariff_digitize(df):
    """NumPy的digitize()函数"""
    prices = np.array([12, 20, 28])
    bins = np.digitize(df.index.hour.values, bins=[7, 17, 24])
    df['cost_cents'] = prices[bins] * df['energy_kwh'].values
    print(prices[bins])
    print(bins)


# 读取数据
df = pd.read_csv('./file/demand_profile.csv')
df['date_time'] = pd.to_datetime(df['date_time'])


@clock
def apply_tariff_loop_run():
    apply_tariff_loop(df)


@clock
def apply_tariff_iterrows_run():
    apply_tariff_iterrows(df)


@clock
def apply_tariff_withapply_run():
    apply_tariff_withapply(df)


@clock
def apply_tariff_isin_run():
    apply_tariff_isin(df)


@clock
def apply_tariff_cut_run():
    apply_tariff_cut(df)


@clock
def apply_tariff_digitize_run():
    apply_tariff_digitize(df)


apply_tariff_loop_run()
apply_tariff_iterrows_run()
apply_tariff_withapply_run()

# 将date_time列设置为DataFrame的索引
df.set_index('date_time', inplace=True)

apply_tariff_isin_run()
apply_tariff_cut_run()
apply_tariff_digitize_run()
