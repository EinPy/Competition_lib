#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll n, m;
    cin >> n >> m;
    ll x;
    vector<ll> arr(n+2, 0);
    for (int i = 1; i <= n; i++){
        cin >> arr[i];
    }
    ll tot = 0;
    for (int i = 0; i < n; i ++){
        tot += (arr[i] != arr[i+1]) * (n - (i+1) + 1) * i;
    }
    ll i;
    while (m--){
        cin >> i >> x;
        if (arr[i] != arr[i+1]){
            tot -= (n - (i+1) + 1) * i;
        }
        if (arr[i] != arr[i-1]){
            tot -= (n - i + 1) * (i - 1);
        }
        arr[i] = x;
        if (arr[i] != arr[i+1]){
            tot += (n - (i+1) + 1) * i;
        }
        if (arr[i] != arr[i-1]){
            tot += (n - i + 1) * (i - 1);
        }
        cout << tot + (n * (n + 1)) / 2 << "\n";
    }


    return 0;
}
