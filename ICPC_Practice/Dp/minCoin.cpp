#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair



int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int coins, targ;
    cin >> coins >> targ;
    vector<int> dp(targ+ 1, 1e9);
    vector<int> c;
    int a;
    while (coins--){
        cin >> a;
        c.push_back(a);
    }
    dp[0] = 0;
    for (int i = 0; i < targ; i++){
        for (auto x: c){
            if (i+ x <= targ){
                dp[i+x] = min(dp[i+x], dp[i] + 1);
            }
        }
    }
    if (dp[targ] == 1e9){
        cout << -1;
    }else{
        cout << dp[targ];
    }
    
    return 0;
}