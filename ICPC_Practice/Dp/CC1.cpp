#include <bits/stdc++.h>
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
    int CC, targ;
    int mod = 1e9 + 7;
    cin >> CC >> targ;
    vector<int> dp (targ + 1, 0);
    dp[0] = 1;
    vector<int> coin;
    while (CC--){
        int a;
        cin >> a;
        coin.push_back(a);

    }

    for (int i = 0; i<targ; i++){
        for (int x : coin){
            if (i + x <= targ){
                dp[i + x] = (dp[i+x] + dp[i]) % mod;
            }
        }
    }
    cout << dp[targ];


    return 0;
}