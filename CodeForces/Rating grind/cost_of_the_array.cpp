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
    ll n, k;
    vector<ll> arr(n);
    cin >> n >> k;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());

    //greedy strategy, grow the array as long as you can while score is bad, that is
    //hopefully until the first 2, is there ever better to included a one?
    //
    //do not think greedy work necessaryli
    //too tired RN, finish later
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

