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



void solve() {
    ll N, P;
    cin >> N >> P;

    vector<ll> names (N, 0);
    ll tot = 0;
    for (int i = 0; i < N; i ++)
    {
        cin >> names[i];
        tot += names[i];
    }
    ll pairs = 0;
    for (int i = 0; i < N; i ++)
    {
        pairs += names[i] * (tot - names[i]);
    }
    pairs /= 2;
    cout << (pairs + P - 1) / P;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

