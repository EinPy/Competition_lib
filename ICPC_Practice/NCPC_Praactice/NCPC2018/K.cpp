// C++ Implementation of above approach
#include <bits/stdc++.h>
using namespace std;
const int maxx = 1e5;
vector<int> tree[maxx];
int degree_of_node[maxx], parent_of_node[maxx],
    child_of_node[maxx], flag = -1;
 
// Function to calculate number of children
// of every node in a tree with root 1
void dfs(int current, int parent)
{
    parent_of_node[current] = parent;
    for (int& child : tree[current]) {
 
        // If current and parent are same we have
        // already visited it, so no need to visit again
        if (child == parent)
            return;
        dfs(child, current);
    }
 
    // If the current node is a leaf node
    if (degree_of_node[current] == 1 && current != 1) {
 
        // For leaf nodes there will be no child.
        child_of_node[current] = 0;
        return;
    }
 
    // Gives the total child of current node
    int total_child = 0;
    for (auto& child : tree[current]) {
        if (child == parent)
            return;
        else
            ++total_child;
    }
    child_of_node[current] = total_child;
    return;
}
 
// Function to calculate permutations ( nPr )
int find_nPr(int N, int R)
{
    if (R > N) {
        flag = 0;
        return 0;
    }
    int total = 1;
    for (int i = N - R + 1; i <= N; ++i) {
        total = total * i;
    }
    return total;
}
 
// Function to calculate the number of ways
// to paint the tree according to given conditions
int NoOfWays(int Nodes, int colors)
{
 
    // Do dfs to find parent and child of a node,
    // we root the tree at node 1.
    dfs(1, -1);
 
    // Now start iterating for all nodes of
    // the tree and count the number of ways to
    // paint its children and node itself
    int ways = 0;
    for (int i = 1; i <= Nodes; ++i) {
 
        // If the current node is root node, then
        // we have total of K ways to paint it and
        // (k-1)P(x) to paint its child
        if (i == 1) {
            ways = ways + colors *
                   find_nPr(colors - 1, child_of_node[1]);
        }
        else {
 
            // For other remaining nodes which are not
            // leaf nodes we have (k-2)P(x) to paint
            // its children, we will not take into
            // consideration of current node
            // since we already painted it.
            if (degree_of_node[i] == 1) {
                continue;
            }
            else {
                ways = ways *
                find_nPr(colors - 2, child_of_node[i]);
            }
        }
    }
    return ways;
}
 
// Function to build the tree
void MakeTree()
{
 
    tree[2].push_back(1);
    tree[1].push_back(2);
    tree[3].push_back(2);
    tree[2].push_back(3);
    degree_of_node[2]++;
    degree_of_node[1]++;
    degree_of_node[3]++;
    degree_of_node[2]++;
}
 
int main()
{
#ifndef ONLINE_JUDGE
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, k;
    cin >> n >> k;
    for (int i = 1; i <= n; i++)
    {
        int a; 
        cin >> a;
        tree[a].push_back(i);
        tree[i].push_back(a);
        degree_of_node[i]++;
        degree_of_node[a]++;
        
    }
    int Count = NoOfWays(n, k);
    cout << Count << "tee";
    return 0;
}