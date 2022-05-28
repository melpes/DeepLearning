# import
import pandas as pd
import matplotlib.pyplot as plt

# 학습 데이터 불러오기
df_Train = pd.read_csv("DeepLearning/Train.csv")

print(df_Train.count()) # Train 데이터 개수
print(df_Train.isnull().sum()) #Train 데이터 중 NAN 데이터의 개수