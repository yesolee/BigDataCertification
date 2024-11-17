import pandas as pd

# Q1 데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고,
# 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후,
# 'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기
df = pd.read_csv('basic1.csv')

df = df.sort_values('f5',ascending=False)
df.iloc[:10,-1] = df.head(10)['f5'].min()
df['f5']
df[df['age']>=80]['f5'].mean()
df['age>=80']

# Q2. 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서,
# 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고
# 두 표준편차 차이 계산하기

df2 = pd.read_csv('basic1.csv')
df2 = df2.iloc[:int(len(df2)*0.7)]
std1 = df2['f1'].std()
df2['f1'] = df2['f1'].fillna(df2['f1'].median())
std2 = df2['f1'].std()

std1-std2

#Q3. 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오!
# 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함

df3 = pd.read_csv('basic1.csv')
out_range = df3['age'].std() * 1.5
outdata = df3[(df3['age']<df3['age'].mean()-out_range)|(df3['age']>df3['age'].mean()+out_range)]
sum(outdata['age'])

df4 = pd.read_csv('basic1.csv')
import numpy as np
data70, data30 = np.split(df4, [int(0.7*len(df))])