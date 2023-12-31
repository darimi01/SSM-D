#확률적 경사 하강법에서 훈련세트를 한번 모두 사용하는 과정 = 에포크
#여러개의 샘플을 사용해 경사 하강법을 수행하는 방식 =미니배치 경사 하강법
#전체 샘플을 사용하는 방식 = 배치 경사 하강법
#확률적 경사 하강법에서 사용하는 알고리즘은 신경망 알고리즘이다.
#손실함수 = 머신러닝 알고리즘이 얼마나 엉터리인지 측정하는 기준, 값이 적을수록 좋지만 어떤 값이 최솟값인지 알지 못함.
#비용함수 != 손실함수, 비용함수 = 모든 샘플에 대한 손실 함수의 합, 하지만 보통 둘을 엄격히 구분하지 않고 섞어서 사용
#로지스틱 손실 함수 = 이진 크로스엔트로피 손실 함수

import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(
    fish_input, fish_target, random_state =42
)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled=ss.transform(test_input)

from sklearn.linear_model import SGDClassifier

sc = SGDClassifier(loss='log',max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

sc.partial_fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

#에포크와 과대/과소적합

import numpy as np
sc=SGDClassifier(loss='log',random_state=42)
train_score = []
test_score = []
classes = np.unique(train_target)

for _ in range(0,300):
  sc.partial_fit(train_scaled, train_target, classes=classes)
  train_score.append(sc.score(train_scaled, train_target))
  test_score.append(sc.score(test_scaled, test_target))

import matplotlib.pyplot as plt
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()

sc = SGDClassifier(loss='log', max_iter=100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)

print(sc.score(train_scaled,train_target))
print(sc.score(test_scaled, test_target))

sc = SGDClassifier(loss='log', max_iter = 100, tol=None, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))
