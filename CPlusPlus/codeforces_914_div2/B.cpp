//solution to https://codeforces.com/contest/1904/problem/B
#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    ll n;
    cin >> n;

    ll a;
    vector<pair<ll,int> > arr;
    vector<ll> org;
    for (int i = 0; i < n; i ++){
        cin >> a;
        arr.push_back(make_pair(a, i));
        org.push_back(a);
    }
    sort(all(arr));
    //create prefix array
    vector<ll> pref;
    ll cur = 0;
    for (int i = 0; i < n; i++){
        cur += arr[i].first;
        pref.push_back(cur);
    }
    // iterate backwards and check the next doubling if any
    vector<int> nxtDoub(n, -1);
    int nxt = -1;
    for (int i = n - 1; i > 0; i --){
        if (pref[i-1] < org[i]){
            nxt = i;
        }
        nxtDoub[i] = nxt;
    }
    vector<int> out(n);
    for (int )

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