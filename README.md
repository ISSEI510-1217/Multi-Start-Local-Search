# Multi-Start-Local-Search
多スタート局所探索法
1. 初期解 S1,S2,S3,・・・,Sn をランダムに生成する
2. 全ての初期解に局所探索法を適用し, 得られた暫定解を全て保持する
3. 終了条件を満たせば探索を終了し, その時点で得られた暫定解の中で最良の解を最終解とする

終了条件:「暫定解の更新回数は P 回まで」「計算時間は T 分まで」等

# Question statement
４人の院生A,B,C,Dが、英語、数学、物理、化学の試験問題作成を分担する
4人それぞれ, 問題作成に作業時間が必要である
English=1, Math=2, Physics=3, Chemistry=4

最短の作成時間とその組み合わせを求める

# program_code
## Multi-Start-Local-Search.py
P個の初期解を与えて実行できる多スタート局所探索法(Multi-Start Local Search)のプログラム
摂動 : 隣り合う要素を入れ替える
終了条件 : 初期解の入れ替え (p×3 回) の暫定解を導くまで
[実行方法] python Multi-Start-Local-Search.py
[出力]最短時間, 組み合わせ
