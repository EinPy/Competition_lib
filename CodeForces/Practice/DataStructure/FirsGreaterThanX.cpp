#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


const int MAXN = 200001;

int n;
int t[4 * MAXN], a[MAXN];

//a = input array, v = current vertex
// tl and tr is left and right boundry
//in a program this is calle with first v = 1
// tl = 0 and tr = n-1
void build(int l = 1, int r = n, int node = 1){
    if (l == r){
        t[node] = a[l];
    }else{
        int mid = (l + r) / 2;
        build(l, mid , node * 2);
        build(mid + 1, r, node * 2 + 1);
        t[node] = max(t[node*2] ,t[node*2 + 1]);
    }
}

void queryUpdate(int val, int l = 1, int r = n, int node = 1){
    if (l == r){
        t[node] -= val;
        cout << l << " ";
    }else{
        int mid = (l + r) / 2;
        if (t[node*2] < val){
            queryUpdate(val, mid + 1, r, node * 2 + 1);
        }else{
            queryUpdate(val, l, mid, node * 2);
        }
        t[node] = max(t[node*2], t[node*2 +1]);
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
    int q;
    cin >> n >> q;
    for (int i = 1; i<= n; i++){
        cin >> a[i];
    }
    build();
    while (q--)
    {
        int x;
        cin >> x;
        if (x > t[1]){
            cout << "0 ";
        }else{
            queryUpdate(x);
        }
    }
    return 0;
}