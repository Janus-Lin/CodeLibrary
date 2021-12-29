"""
CodeLibrary.time_datetime
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-29
"""
'''
时间相关的操作，时间有三种表示方式：

    时间戳            1970年1月1日之后的秒，即：time.time()
    格式化的字符串    　2014-11-11 11:11，    即：time.strftime('%Y-%m-%d')
    结构化时间         元组包含了：年、日、星期等... time.struct_time    即：time.localtime()

'''
import time

print(time.time())  # 返回当前系统时间戳（1970年1月1日0时0分0秒开始）
print(time.ctime())  # 输出Tue May 17 16:07:11 2016，当前系统时间
print(time.ctime(time.time() - 86400))  # 将时间戳转换为字符串格式
print(time.gmtime(time.time() - 86400))  # 将时间戳转换为struct_time格式
print(time.localtime(time.time() - 86400))  # 将时间戳转换为struct_time格式，返回本地时间
print(time.mktime(time.localtime()))  # 与time.localtime()功能相反，将struct_time格式转回成时间戳格式
# time.sleep(5)  　　　　　　　　　　　　　　　　             # sleep停顿
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))  # 将struct_time格式转成指定的字符串格式

print("----------------------------------------------------------------")
from datetime import datetime, timedelta, date

# 获取当前时间, 2021-12-29 14:31:13.150093 <class 'datetime.datetime'>
current_time = datetime.now()
print(current_time, type(current_time))

# 世界时间
shijie_time = datetime.utcnow()
print(shijie_time, type(shijie_time))

# 输出2008-08-08 16:21:34.798203,返回当前时间,但指定的值将被替换
print(current_time.replace(2008, 8, 8))

# 获取当前日期，2021-12-29 <class 'datetime.date'>
today = date.today()

# 获取前60天日期，2021-10-30 <class 'datetime.date'>
today_60 = (datetime.today() - timedelta(60)).date()

# date --> str，2021-12-29 <class 'str'> # 快捷: strftime('%F')
today_str = today.strftime('%Y-%m-%d')

# str --> date
today_date = datetime.strptime("2016-05-17", '%Y-%m-%d').date()

# 时间字符串格式转化，2001-07-04 --> 20010704 <class 'str'>
start_date = time.strftime('%Y%m%d', time.strptime('2001-07-04', '%Y-%m-%d'))


def get_yesterday():
    """
    获取昨日日期
    :return: str
    """
    yesterday = datetime.today() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


def get_one_date(input_date):
    """获取当前日期上一个月一号和最后一号日期"""

    time_tuple = time.strptime(input_date, '%Y%m%d')
    year, month, day = time_tuple[:3]

    # 当前时间
    time_now = date(year, month, day)

    # 当前月份1号
    first_day = date(time_now.year, time_now.month, 1)

    # 上个月最后一天
    pre_month = first_day - timedelta(days=1)

    # 上个月第一天
    first_day_of_pre_month = date(pre_month.year, pre_month.month, 1)

    return pre_month.strftime('%Y%m%d'), first_day_of_pre_month.strftime('%Y%m%d')


if __name__ == '__main__':
    a = get_one_date('20211229')
    print(a)
