import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#다운로드 받은 파일 train.csv, test.csv 두 개의 파일을 읽는다.
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

#두 개의 파일의 내용을 하나로 병합한다.
merge = pd.concat([train, test], axis=0, ignore_index=True)

#전체 데이터 수량을 파악한다.
print("전체 데이터 수량:",len(merge))

'''
사람들이 다른 차원으로 전송되었는지 여부를 나타내는 Transported 항목과
가장 관련성이 높은 항목을 찾는다.
'''
analysis = merge.copy()

#True False를 0과 1로 바꿔야 관련성을 계산 가능
analysis['Transported'] = analysis['Transported'].astype(float)
analysis['CryoSleep'] = analysis['CryoSleep'].astype(float)
analysis['VIP'] = analysis['VIP'].astype(float)

#Transported와 모든 항목 간의 관련성을 계산
correlations = analysis.corr(numeric_only=True)['Transported']

#그 중에서 가장 관련성이 높은 항목
print("가장 관련성이 높은 항목:",correlations.sort_values(ascending=False).iloc[1:2])

'''
나이를 기준으로 10대, 20대, 30대, 40대, 50대, 60대, 70대 별로
Transported 여부를 하나의 그래프에서 출력해 본다.
'''
bins = [10, 20, 30, 40, 50, 60, 70,80]
labels = ['10s', '20s', '30s', '40s', '50s', '60s', '70s',]
merge['AgeGroup'] = pd.cut(merge['Age'], bins=bins, labels=labels, right=False)

# 그래프 그리기
plt.figure(figsize=(12, 6))
sns.countplot(data=merge, x='AgeGroup', hue='Transported', palette='coolwarm')
plt.title('Transported Status by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()


