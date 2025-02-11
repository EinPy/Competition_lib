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

const int L = 1e4 + 5;
string A;
string B;
int N;


int dp[MAX_N][2][2]; // Correctly include ze and on in memoization

ll best(int idx, int ze, int on) {
    if (idx == N) {
        return 0;
    }
    if (dp[idx][ze][on] != -1) { // Correctly check memoization
        return dp[idx][ze][on];
    }

    // Update `ze` and `on` based on current characters
    if (A[idx] == '1' || B[idx] == '1') {
        on = 1;
    }
    if (A[idx] == '0' || B[idx] == '0') {
        ze = 1;
    }
    ll score = 0;
    if (ze == 1){
        score = 1;
    }
    if (ze == 1 && on == 1){
        score = 2;
    }

    ll ans;
    if (score == 2) {
        ans = score + best(idx + 1, 0, 0);
    } else if (score == 0) {
        ans = best(idx + 1, ze, on);
    } else {
        ans = max(score + best(idx + 1, 0, 0), best(idx + 1, ze, on));
    }
    dp[idx][ze][on] = ans;
    return ans; // Correctly store in dp
}
void solve() {
    cin >> N;
    cin >> A >> B;

    memset(dp, -1, sizeof(dp));

    cout << best(0, 0, 0) << endl;

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

