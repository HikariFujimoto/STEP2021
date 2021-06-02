# Week 4 Assignment Graph Algorithms

## 課題内容
与えられたWikipediaのページとリンク集を使い、'Google'から'渋谷'までの最短ルートを探す。

## 使用言語
python 3.9.5
実行方法
`python3 .\wikipedia_path_finder.py`

## アルゴリズム

## Assignment
Using the given pages and link (found at [this link](https://github.com/yukidmy/step_wikipedia-graph)) look for the shortest path from 'Google' to '渋谷'

## Algorithm 
#### Reading Data (Sample program provided)
Read content of pages.txt and links.txt. 
For pages.txt, store values in a dictionary where the key is the ID and value is the title of the page. 
For links.txt, store values in a dictionary where the key is the ID and value contains set of all ID adjacent to key.

#### Path finding using BFS
In order to find the shortest path from a node to another node, BFS is optimal; therefore used to solve this problem. 

Input: links, root ID, target ID
Output: list containing the IDs of the path taken

Initialize with inputting the root node into queue and the visited dictionary.
Use while loop to repeat the following process until the target node is reached:
  - Check if the first node in queue is not the target node.
  - If not, add all neighboring nodes that is not yet visited into the queue. Store the parent ID and child ID in connection to track the path later.
  - Once all neighboring nodes are added, pop node from queue.
When first node is the target node, return the list containing the path; created by using the child-parent ID pair in connection.
Finally, print the page title of the links in the path.