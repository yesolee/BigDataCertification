import pandas as pd

#Q1. 2022년 데이터 중 2022년 중앙값보다 큰 값의 데이터 수
df = pd.read_csv('t1-data2.csv', index_col='year')
df
df.info()

df.iloc[0].median()
sum(df.iloc[0]>df.iloc[0].median())

#Q2. 결측치 데이터(행)을 제거하고, 앞에서부터 60% 데이터만 활용해, 'f1' 컬럼 3사분위 값을 구하시오
df2 = pd.read_csv('t1-data1.csv')
df2.isna().sum()
df2 = df2.dropna()
df2.iloc[:int(len(df2)*0.6)]['f1'].quantile(0.75)

#Q3. 결측치가 제일 큰 값의 컬럼명을 구하시오
df3 = pd.read_csv('t1-data1.csv')
df4 = pd.DataFrame(df3.isna().sum(), columns=['cnt_null'])
df4.sort_values('cnt_null',ascending=False).index[0]