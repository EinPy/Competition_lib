#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair



int n, t[4*1000];

//a = input array, v = current vertex
// tl and tr is left and right boundry
//in a program this is calle with first v = 1
// tl = 0 and tr = n-1
void build(int a[] ,int v, int tl, int tr){
    if (tl == tr){
        t[v] = a[tl];
    }else{
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2 + 1, tm + 1, tr);
        t[v] = t[v*2] + t[v*2 + 1];
    }
}

int sum(int v, int tl, int tr,  int l, int r){
    if (l > r){
        return 0;
    }
    if (l == tl && r == tr){
        return t[v];
    }

    int tm = (l + r) / 2;
    return sum(v * 2, tl, tm, l, min(r, tm))
        + sum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r);
}

void update(int v, int tl, int tr, int pos, int new_val){
    if (tl == tr){
        t[v] = new_val;
    }else{
        int tm = (tl + tr) / 2;
        if (pos <= tm){
            update(v*2, tl, tm, pos, new_val);
        }else{
            update(v*2 + 1, tm +1, tr, pos, new_val);
        }
        t[v] = t[v*2] + t[v*2+1];
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
    int t;
    cin >> t;
    while (t--)
    {
        //write code here
        cout << "yeetsky";
    }
    return 0;
}