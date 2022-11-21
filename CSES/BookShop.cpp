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

    
    int n, x;
    cin >> n >> x;
    vector<int> price(n), pages(n);
    for (int i = 0; i < n; i ++){
        cin >> price[i];
    }
    for (int i = 0; i<n; i++){
        cin >> pages[i];
    }
    vector<vector<int>> dp(n+1, vector<int> (x+1, 0));

    for (int book = 1; book <= n; book++){
        for (int cost = 0; cost <= x; cost++){
            dp[book][cost] = dp[book-1][cost];
            int left = cost - price[book-1];
            if (left >= 0){
                dp[book][cost] = max(dp[book][cost], dp[book-1][left] + pages[book-1]);
            }
        }
    }
    cout << dp[n][x] << endl;
    return 0;
}