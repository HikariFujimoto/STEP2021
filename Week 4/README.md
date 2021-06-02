# Week 4 Assignment Graph Algorithms

## 課題内容
与えられたWikipediaのページとリンク集を使い、'Google'から'渋谷'までの最短ルートを探す。


## 準備
以下のようなディレクトリ構成で実行してください。
```
FILE_NAME
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
└── wikipedia_path_finder.py
```

## 使用言語
python 3.9.5

実行方法
`python3 .\wikipedia_path_finder.py`

## アルゴリズム
最短ルートを探さなければいけないため、探しているnodeを初めて見つけた場合、それが最短ルートになる幅優先探索を行う。

入力：links, 探索開始ページID (root node), 探索目標ページID (target node)

出力： 最短ルートで通ったnodeのリスト 

初期化としてroot nodeをキューと探索済みかを確認するために使う辞書のvisitedに追加する。
whileループを使い以下のプロセスをキューの最初の要素(node)がtarget nodeになるまで行う：
- キューの最初のnodeがtarget nodeかチェックする
- ちがう場合、visitedに入っていない隣接しているnodeをキューとvisitedに最初のnode(親ID)をkey、隣接しているnode(子ID)をvalueとして追加する。
- 全ての隣接しているnodeを追加し終わったら、nodeをキューからpopする。

最初のnodeがtarget nodeの場合、visitedに入っている親IDと子IDのペアを使い、子IDからルートを逆引きし、リストにして返す。
最後にルートで通ったページの名前を表示する。

ただし、このアルゴリズムの場合、もし複数の最短ルートがあっても一番最初に到達したものしか認識・表示しない。

## 確認したルート 
`Google (ID: 457783 ) フジテレビジョン (ID: 189152 ) 渋谷 (ID: 22557 )`

`Google (ID: 457783 ) セグウェイ (ID: 154009 ) 渋谷 (ID: 22557 )`

`Google (ID: 457783 ) フレッシュアイ (ID: 579364 ) 渋谷 (ID: 22557 )`

`Google (ID: 457783 ) スターバックス (ID: 22188 ) 渋谷 (ID: 22557 )`

***

## Assignment
Using the given pages and link (found at [this link](https://drive.google.com/file/d/1zqtjSb-ZoR4rzVUWZrjNSES5GKJhYmmH/view)) find the shortest path from 'Google' to '渋谷'

## Preparation
Please execute the program with the following directory structure:
```
FILE_NAME
├── data
│   ├── graph_small.png
│   ├── links_small.txt
│   ├── links.txt
│   ├── pages_small.txt
│   └── pages.txt
└── wikipedia_path_finder.py
```

## Algorithm 
#### Reading Data (Sample program provided)
Read content of pages.txt and links.txt. 

For pages.txt, store values in a dictionary where the key is the ID and value is the title of the page. 

For links.txt, store values in a dictionary where the key is the ID and value contains set of all ID adjacent to key.

#### Path finding using BFS
In order to find the shortest path from a node to another node, BFS is optimal; therefore used to solve this problem. 

Input: links, root ID, target ID

Output: list containing the IDs of the path taken

Initialize with inputting the root node into queue and the dictionary visited.
Use while loop to repeat the following process until the target node is reached:
- Check if the first node in queue is not the target node.
- If not, add all neighboring nodes that is not yet visited into the queue. Add the parent ID and child ID as a key-value pair to visited (used to track the path later).
- Once all neighboring nodes are added, pop node from queue.

When first node is the target node, return the list containing the path; created by using the child-parent ID pair in visited.
Finally, print the page title of the links in the path.

This algorithm will stop whenever the target node is reached by the smallest number of steps, therefore if there are multiple shortest paths, other possibilities are disregarded. 