import csv
import pandas as pd

God = pd.read_csv("โควิด19_Data.csv")
God = God.sort_values(by="time")
print(God)