#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9 + 5;
const ld EPS = 1e-9;



void solve() {
    ll n, k;
    cin >> n >> k;
    ll binlim = pow(2, k);
    if (k >= 36){
        binlim = INF;
    }
    if (binlim <= n + 1){
        cout << binlim << endl;
        return;
    }
    cout << n + 1<< endl;
    return;
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

