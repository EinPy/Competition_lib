#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair



int main()
{
#ifndef ONLINE_JUDGE
    freopen("i.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int mod = 1e9 + 7;
    int n, target;
    cin >> n >> target;
    vector<int> x(n);
    for (int i = 0; i < n; i++){
        cin >> x[i];
    }

    vector<vector<int>> dp(n+1, vector<int>(target +1, 0));
    dp[0][0] = 1;

    for (int c = 1; c <= n; c++){
        for (int i = 0; i<= target; i++){
            dp[c][i] = dp[c-1][i];
            int left = i -x[c-1];
            if (left >= 0){
                dp[c][i] += dp[c][left];
                dp[c][i] = dp[c][i] % mod;
            }
        }
    }
    cout << dp[n][target] << endl;
    return 0;
}