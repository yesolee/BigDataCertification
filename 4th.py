import pandas as pd

df = pd.read_csv('../2회기출/basic1.csv')
df.info()

# 1-1. age 컬럼의 3사분위수와 1사분위수의 차를 절대값으로 구하고, 소수점 버려서, 정수로 출력¶
df['age'].isna().sum()
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3-Q1
print(int(abs(Q3-Q1)))

#1-2. (loves반응+wows반응)/(reactions반응) 비율이 0.4보다 크고 0.5보다 작으면서, type 컬럼이 'video'인 데이터의 갯수 
fb = pd.read_csv('fb.csv')
fb.info()

fb.head()
fb.query('((loves+wows)/reactions>0.4) & (loves+wows)/reactions<0.5)')
target = (fb['loves'] + fb['wows'])/fb['reactions']
len(fb[(target>0.4) & (target<0.5)].query('type=="video"'))

# 1-3. date_added가 2018년 1월 이면서 country가 United Kingdom 단독 제작인 데이터의 갯수
nf = pd.read_csv('nf.csv')
nf.info()
nf.head()
nf['date_added'] = pd.to_datetime(nf['date_added'])
len(nf.query('(date_added>="2018-01") & (date_added<"2018-02")&(country=="United Kingdom")'))