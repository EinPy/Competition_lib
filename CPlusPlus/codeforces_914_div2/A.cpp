#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    ll a, b;
    cin >> a >> b;
    ll xk, yk, xq, yq;
    cin >> xk >> yk >> xq >> yq;
    //find all possible attacking squares for both
    set<pair<ll,ll> > ka;
    for (int i = -1; i <= 1; i+=2){
        for (int j = -1; j <=1; j+= 2){
            ka.insert(make_pair(xk + i * a, yk + j * b));
            ka.insert(make_pair(xk + i * b, yk + j * a));
        }
    }
    //cout << ka.size() << endl;
    int out = 0;
    set<pair<ll,ll> > used;
    for (int i = -1; i <= 1; i+=2){
        for (int j = -1; j <=1; j+= 2){
            pair<ll,ll> pos1 = make_pair(xq + i * a, yq + j * b);
            pair<ll,ll> pos2 = make_pair(xq + i * b, yq + j * a);
            if (ka.count(pos1) > 0 && used.count(pos1) == 0){
                out ++;
                used.insert(pos1);
            }
            if (ka.count(pos2) > 0 && used.count(pos2) == 0){
                out ++;
                used.insert(pos2);
            }
        }
    }
    cout << out << endl;
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