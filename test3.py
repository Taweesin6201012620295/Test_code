'''import csv
import pandas as pd
from datetime import datetime

def abc(time):
    a = time.split(" ")
    time1 = a[1]
    time2 = a[2]
    time2 = datetime.strftime("%m", time2)
    time3 = a[3]
    post = str(time3) + '-' + str(time2) + '-'+ str(time1)
    return post

pan = pd.read_csv('google.csv')
time = pan["Posted"].apply(abc)

pan["Posted"] = time

print(pan["Posted"])'''


from datetime import datetime

date_time_str = '2021-Feb-22'
date_time_obj = datetime.strptime(date_time_str, '%Y-%b-%d')

print(date_time_obj)

