//solution to https://codeforces.com/contest/1901/problem/A
#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    int n, x;
    cin >> n >> x;
    vector<int> gas(n, 0);
    for (int i = 0; i < n; i++){
        cin >> gas[i];
    }
    int bst = 0;
    for (int i = 0; i < n-1; i++){
        bst = max(bst, gas[i+1] - gas[i]);
    }
    bst = max(bst, gas[0]);
    bst = max(bst, 2 * (x - gas.back()));
    cout << bst << endl;
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