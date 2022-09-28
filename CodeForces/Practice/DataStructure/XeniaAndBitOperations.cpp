#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair

const int MAXN = 131072;
int t[4 * MAXN];
int arr[MAXN];

//a = input array, v = current vertex
// tl and tr is left and right boundry
//in a program this is calle with first v = 1
// tl = 0 and tr = n-1
void build(int v, int tl, int tr, int depth){
    if (tl == tr){
        t[v] = arr[tl];
    }else{
        int tm = (tl + tr) / 2;
        build(v*2, tl, tm, depth -1);
        build(v*2 + 1, tm + 1, tr, depth - 1);
        if (depth % 2 == 0){
            t[v] = t[v*2] | t[v*2+1];
        }else{
            t[v] = t[v*2] ^ t[v*2 + 1];
        }
    }
}

// tl and tr is left and right boundry
void update(int v, int tl, int tr, int pos, int new_val, int depth){
    if (tl == tr){
        t[v] = new_val;
    }else{
        int tm = (tl + tr) / 2;
        if (pos <= tm){
            update(v*2, tl, tm, pos, new_val, depth -1 );
        }else{
            update(v*2 + 1, tm +1, tr, pos, new_val, depth -1);
        }
        if (depth % 2 == 0){
            t[v] = t[v*2] | t[v*2+1];
        }else{
            t[v] = t[v*2] ^ t[v*2 + 1];
        }
    }
}


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < pow(2,n); i++){
        cin >>arr[i];
    }
    //compute the segment tree of the array
    build(1, 0, pow(2,n) -1 , n-1 );
    int a, b;
    //for (int i = 0; i< 10; i++){
    //    cout << t[i] << " ";
    //}
    //cout << "\n";
    while (m--){
        cin >> a >> b;
        update(1, 0, pow(2,n) - 1, a -1,b, n-1);
        cout << t[1] << "\n";
    }
    return 0;   
}