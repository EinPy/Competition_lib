#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

int dp[MAX_N][2][2];

void solve() {
    int n;
    cin >> n;
    string A,B;
    cin >> A >> B;
    memset(dp, 0, sizeof(dp));
    int score = 0;
    int ze, on;
    ze = 0;
    on = 0;
    if (A[0] == '1' || B[0] == '1'){
        on = 1;
    }
    if (A[0] == '0' || B[0] == '0'){
        ze = 0;
    }
    score = 0;
    if (ze){
        score = 1;
    }
    if (ze && on){
        score = 2;
    }
    dp[0][ze][on] = score;
    for (int i = 1; i < n; i++){
        //for every i we can start by computing the score where 
        // so the max at 0, 0 will walways be the max of all the previous scores
        dp[i][0][0] = max({dp[i-1][0][0],
                           dp[i-1][0][1],
                           dp[i-1][1][0],
                           dp[i-1][1][1]});
         
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

