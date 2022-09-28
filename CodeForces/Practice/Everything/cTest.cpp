#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair



int main()
{
#ifndef ONLINE_JUDGE
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll a, b, c;
    cin >>a>>b>>c;
    ll d = a / c;
    ll e = b / c;
    if (a % c != 0){
        d += 1;
    }
    if (b % c != 0){
        e += 1;
    }
    cout << e * d;
    return 0;
}