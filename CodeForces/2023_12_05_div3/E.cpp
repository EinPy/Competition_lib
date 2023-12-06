#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

int digsum(int n){
    int dig = 0;
    while (n){
        dig += n  % 10;
        n = n / 10;
    }
}

void solve() {
    int n;
    cin >> n;
    for (int a = 0; a < n+1; a++){
        
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