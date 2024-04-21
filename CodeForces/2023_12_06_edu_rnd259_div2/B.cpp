#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;


ll n, P, l, t;

bool ok(ll days){
    ll cred = days * l;
    //can never do more than all tasks;
    cred += min(days * 2, 1 + (n -1) / 7) * t;
    if (cred >= P){
        return true;
    }
    return false;
}

void solve() {
    cin >> n >> P >> l >> t;

    //bns over days he has to go to school 
    ll lo, hi;
    lo = 0;
    hi = n;
    ll ans;
    while (lo < hi) {
        ll mid = lo + (hi - lo) / 2; // avoid overflow
        //cout << " checking " << mid;
        if (ok(mid)){// f should be false, then true
            hi = mid;
        } 
        else
            lo = mid + 1;
    }
    //lo is now the first index where f is true
    cout << n - lo << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int i = 1;i <=tc;i++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}