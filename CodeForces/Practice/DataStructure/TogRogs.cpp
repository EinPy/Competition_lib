#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair

int n, m;
const int MAXN = 3e5 + 10; 
int a[MAXN];
int b[MAXN];
int t[4 * MAXN];

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++){
        cin >>a[i];
    }
    for (int i = 0; i < n; i++){
        cin >>b[i];
    }
    int q;
    cin >> q;
    while (q--){
        int id,  i, c;
        cin >> id >> i >> c;
        //change price of dish
        if (id == 1){

        }
        //change money of student
        if (id == 2){

        }
    }
}