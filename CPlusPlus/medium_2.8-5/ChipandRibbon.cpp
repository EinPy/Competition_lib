//solution to https://codeforces.com/contest/1901/problem/B

#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    ll n;
    cin >> n;
    vector<ll> arr(n, 0);
    for (ll t = 0; t < n; t++) {
        // cout << "Case #" << t << ": ";
        cin >> arr[t];
    }
    ll curc = 1;
    //for each chip that is created
    ll creat=0;
    for (ll i = 0; i < n; i ++){
        if (arr[i] > curc){
            creat += arr[i] - curc;
            curc = arr[i];
        }
        else if (arr[i] < curc){
            curc = arr[i];
        }
    }
    cout << creat << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll tc = 1;
    cin >> tc;
    for (ll t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}