---
title: 算法
layout: cs
---

## 动态规划

### 回文

- 5 最长的回文substring, 遍历n,以每个字符为中心，向首尾展开。 O(n^2)
- 516 最长的回文Subsequence，步长s递增，data[i][i+s] = max(a,b,c)
- 131 切成回文substring有哪几种切法，dfs(i:0->n) { check(i->n)回文，substr  }
- 132 切成回文substring最少切几刀，向后传递，dp[i]=max(dp[i],dp[i-1]+1); dp[i+j]=min(dp[i+j],dp[i-1]+1)


### 数组

- 53 连续子数组的最大和 sum = data[i]+max(sum, 0); res = max(res, sum);
- 152 连续子数组的最大积， \_max=...; _min=...; res=max(res,_max);
- 689 3个子数组总和最小，先求1个，然后2个，再3个。dp[0][i]一个的情况下从i到endl要选哪个开始
- 718 共同出现的最长连续子数组，A[i]从右到左，B[j]从左到右，O(n^2), dp[j] = 1 + dp[j+1];
- 898 所有子数组内部“或”运算会有几个结果。unordered_set容器存结果，遍历数组内元素与容器“或”
- 368 两两互余的子数组。排序，遍历nums, 后推j，if(nums[j]%nums[i]==0 && dp[i] >= dp[j]) { dp[j]=dp[i]+1; prev[j]=i   }   最后找到dp[i]最大值往前推


### 矩阵

- 63 左上角到右下角走法，有障碍 dp[i][j] = (左+上)\*isPass
- 64 左上角到右下角最短路径。 dp[i][j] = nums[i][j] + min(左，上) 。dp可以与nums同大小，边缘for
- 576 踢出界，由外向内
- 174 左上角到右下角，加减血，逆行。dp[i][j]=min(下，右)-data[i][j]; dp[i][j]=max(1,dp[i][j])
- 221 矩阵内最大的矩形 dp[i][j] = min(上左斜)+1; res=max(res,dp[i][j])
- 304 多次求和2d, data[i][j] 存储（0,0）到 （i,j）的和

### 买卖

- 121 股票一次买卖 res = max(res, pices[i]-MIN); MIN = min(min,pices[i]);
- 122 股票多次买卖 sell=max(sell,buy+pices[i]) buy=max(buy,sell-pices[i])
- 309 股票多次买卖，停一天。buy[i+2] = max(buy[i+1], sell[i]-prices[i]); sell[i+2] = max(sell[i+1], buy[i+1]+prices[i]); prices[i]对应buysell的i+2
- 123 股票两次买卖  
sell1=max(sell1,buy1+pices[i])  
buy1=max(buy1,sell0-pices[i])  
sell0=max(sell0,buy0+pices[i])  
buy0=max(buy0,-pices[i]) // 不累计营利  
- 124 股票K次买卖 sell1和buy1展开k

### 背包

- 279 最少需要几个平方数组成 data[i] = min(data[i], data[i-j\*j]+1);     j = 1->sqrt(i);
- 322 最少需要几张零钱组成，完全背包最小值。dp={0, Max ...} dp[i] = min(dp[i], dp[i-coins[j]] + 1);
- 416 能否分成sum相同的两组，01背包。price和weight都等于nums, 容量C为和一半
- 377 组成某个数的排列有几种。完全背包计数, dp[i] += dp[i-nums[j]];

### 排列组合  

- 排列 sort(data.begin(), data.end()); prev_permutation(data.begin(), date.end());  
- 组合 m选n。data={0,,1}; prev_permutation() 1选0不选。  

### 其他

- 32 最长的有效括号, statck存index, 匹配到()，先pop (, 再l = i-top)
- 91 1-26 —> A-Z 解码，“00”+S dp[i+2] = dp[i+1] + dp[i]， dp[i+1]要考虑0边界, dp[i]要考虑26边界
- 96 n个结点的BST有几种组合，遍历nums[i], for(j=i->0) dp[j] = dp[j+1] + dp[j-1], sum(dp)
- 95 n个结点的BST有哪几种组合，遍历nums[i]，(1)nums[i]当head; (2)nums[i]插入右侧.
- 139 句子能否有那几个单词组成。遍历每个字母确定其步长，能否从头走到尾巴，可以从尾逆推到头。
- 198 偷盗相邻报警，dp[i+3] = nums[i] + max(dp[i],dp[i+1]); 空间O(n).  
temp=rob;rob = nums[i]+pass; pass=max(pass,temp); 空间O(1)
- 213 房子环形，max(rob(0,n-1),rob(1,n)), rob是上面函数
- 264 丑数 data[i] = min(data[k2]\*2, data[k3]\*3, data[k5]\*5 );  k++
- 削掉一个数，左中右积。dp[i][j] = max(dp[i][j], 左中右积+data[i][中]+data[中][i])
- 338 连续n个数中1出现的次数，ret[i] = ret[i&(i-1)] + 1;
- 343 将一个数拆成几个数相乘，最大乘积。dp[i] = max(dp[i-3]\*3, dp[i-2]\*2)
- 354 套信封。长从小到大，同长比宽从大到小。回朔j至0, if(j宽小于i宽) data[i] = max(data[i],data[j]); res=max(res,data[i])
- 376 波动Subsequence，flag记录上下趋势，res根据flag和num[i和i-1] 进行++

## 贪心

### 会议
- 252 一间能否满足所有会议。按start排序后比较。
- 253 这些会议需要几间？最小堆存储end。遍历剩余会议，如果start小于堆顶只能新开房，也就是push end; 否则就先pop再push。
- 一间最多安排几个会议，按start排序，依次遍历，不能参加时如果结束时间还要早，替换上一场

- 134 加油站 Station: 从0到n-1累加，当小于0时另起并记录当前位置，欠的后面要还上

- 135 分蛋糕: 左扫一遍，高分比低分多1，右扫一遍，高分到少多1, 即data[i]=max(data[i], data[i+1]+1)

- 402 数中删掉k位后变最小。for(num: nums) 回朔并pop str，直到遇到比num小的，push num to str
- 316 删掉重复的字母，变最小。同上，遇到大的删掉再push自己，除非它后续没有了，所以要个计算器。

- 358 间隔K问题，<int,char>推入大堆，以k为一周期，连pop k次，pop完后再推回

- 502 n个项目利润，n个成本，从中选k个投资，本金w。先把能投资的先推入堆，赚钱后再推，每次都是从堆顶选

- 3个连续的分一组，tail记录已分的组的尾数，if tail[num[i-1]], return false; else check num[i+1,+2].

- 870 田忌赛马 sort(A) by multiset, B[i]比A最大rbegin还要大则选最小，或者选upper_bound
p = B[i]>=\*data.rbegin()? data.begin() : data.upper_bound(B[i]);

## 树  

### 遍历  
- 非递归inorder\_order 出栈后推右及右的所有左子孙  
- 非递归pre\_order  出栈后先推右后推左  
- 非递归post_oder 出栈后先把内容存入res, 先左后右推。reverse res。  
- 层次遍历(涉及分行)。递归pre\_order,带行号。if(ret.size() == depth) 新加一行。
- 宽度。同上，多带编号，子点编号为2n和2n+1

### 验证  
- BST 递归函数第2个参数prev等于先驱val，引用。先递归左，再验val, 若val大于prev则fail, 否则prev=val,验递归左。  
- 对称，左右两子树同时进行层次遍历。  

## 经典

### LRU  
{% highlight C++ %}
list<int> lru;
unordered_map<int, pair<int, list<int>::iterator>> data;
void change(int key){
    lru.erase(data[key].second);
    lru.push_front(key);                 
    data[key].second = lru.begin();
}
int get(int key) {
    if(check(key)){
       change(key);
       return data[key].first;
    }
    return -1;
}
int put(int key, int val){
    if(!check(key)){
        if(data.size()==_capacity){
            data.erase(lru.back());
            lru.pop_back();
        }
        lru.push_front(key);
        data[key] = {value, lru.begin()}
    }else{
        data[key].first = value;
        change(key);
    }
}
{% endhighlight %}

### 背包
{% highlight C++ %}
// 完全
vector<int> dp(container+1);
for(int j=0; j<weights.size(); j++){
    for(int i=weights[j]; i<=container; i++){
        if(i-weights[j]>=0)
            dp[i] = max(dp[i], dp[i-weights[j]]+prices[j]);
    }
}
{% endhighlight %}
{% highlight C++ %}
// 01
vector<int> dp(container+1);
for(int j=0; j<weights.size(); j++){
    for(int i=container; i>=weights[j]; i--){
        if(i-weights[j]>=0)
            dp[i] = max(dp[i], dp[i-weights[j]]+prices[j]);
    }
}
{% endhighlight %}
{% highlight C++ %}
// 最小
int Max = container+1;
vector<int> dp(container+1,Max);
dp[0] = 0;
int n = weights.size();
for(int i=0; i<n; i++){
    for(int j=weights[i]; j<=container; j++){
        dp[j] = min(dp[j], dp[j-weights[i]]+1);
    }
}
{% endhighlight %}

### Dijkstra
最短路径  O(n^2)
{% highlight C++ %}
vector<vector<int>> data; // 邻接矩阵
vector<int> D(N+1); // 与src的距离
for(int i=1; i<=N; i++) D[i] = data[src][i];
for(int k=0; k<N-1; k++){
    int next = 0;
    for(int i=1; i<=N; i++){
        if(visited[i])
            continue;
        if(D[i]<D[next])
            next = i;
    }
    for(int i=1; i<=N; i++)
        if(data[next][i]!=INT_MAX)
            D[i] = min(D[i], D[next]+data[next][i]);
    visited[next] = 1;
}
{% endhighlight %}

### Prim
最小生成树 O(n^2)  
{% highlight C++ %}
vector<vector<int>> data; // 邻接矩阵
vector<int> D(N+1); // 与集体的距离
for(int i=1; i<=N; i++) D[i] = data[src][i];
for(int k=0; k<N-1; k++){
    int next = 0;
    for(int i=1; i<=N; i++){
        if(visited[i])
            continue;
        if(D[i]<D[next])
            next = i;
    }
    for(int i=1; i<=N; i++)
        if(!visited[i])
            D[i] = min(D[i], data[next][i]);
    visited[next] = 1;
}
{% endhighlight %}

###  Kruskal
最小生成树  O(eloge)
{% highlight C++ %}
    sort(edges...);
    for(auto edge: edges){
        int a = find(edge[0]);
        int b = find(edge[1]);
        if(a!=b){
            prev[a] = b;
            res += edge[2];
        }
    }
{% endhighlight %}
