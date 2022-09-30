"""
0-1ナップサック問題Ⅱ

問題
価値が vi 重さが wi であるような N 個の品物と、容量が W のナップザックがあります。次の条件を満たすように、品物を選んでナップザックに入れます

選んだ品物の価値の合計をできるだけ高くする。
選んだ品物の重さの総和は W を超えない。

価値の合計の最大値を求めてください。

制約
1 ≤ N ≤ 100
1 ≤ vi ≤ 100
1 ≤ wi ≤ 10,000,000
1 ≤ W ≤ 1,000,000,000

※普通の0-1ナップサック問題と違い、重さwiと容量Wの値の範囲が大きい
"""


N,W=map(int,input().split())

# jを容量とすると計算量がすさまじいことになる(dp表の列を最大1,000,000,000まで作らなきゃいけなくなる)
# なので、jを価値の取りうる値として考える(品物の個数Nの最大値=100、一品物の価値の最大値=100なので、全部の価値の最大値は100×100=10000)
inf = float("inf")
dp=[[inf for j in range(10000+1)] for i in range(N+1)]
dp[0][0]=0

# 「dp[i][j]=i番目までの品物を使ってjの価値を出すための最小の重さ」を要素としてdp表を埋めていく
for i in range(1,N+1):
  v,w=map(int,input().split())
  for j in range(10000+1):
    # i番目の品物の価値vと価値の最大値jを比べる
    if j<v:
      dp[i][j]=dp[i-1][j]
    else:
      dp[i][j]=min(dp[i-1][j],dp[i-1][j-v]+w)

# 「dp[i][j]=i番目までの品物を使ってjの価値を出すための最小の重さ」なので、
# j(価値)について逆から回し、dpの要素が容量W以下に初めてなった時のjが求めたい値となる
for j in range(10000,0,-1):
  if dp[N][j]<=W:
    print(j)
    exit()
print(0)