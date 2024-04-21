#include <bits/stdc++.h>
#define all(x) x.begin(),x.end()
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

vector<ll> nll(ll n){
    vector<ll> vec(n,0);
    for (int i = 0; i < n; i ++){
        cin >> vec[i];
    }
    return vec;
}

vector<int> nint(int n){
    vector<int> vec(n,0);
    for (int i = 0; i < n; i ++){
        cin >> vec[i];
    }
    return vec;
}

void pll(vector<ll> vec){
    for (auto x: vec){
        cout << x << " ";
    }
    cout << endl;
}

void solve() {
    ll n;
    cin >> n;
    if (n == 1){
        cin >> n;
        cout << 1 << endl;
       
        return;
    }
    vector<ll> arr = nll(n);
    set<ll> exists;
    for (auto x : arr){
        exists.insert(x);
    }
    ll ma = *max_element(all(arr)); // returns iterator 
    //get gcd of all elemnts and max
    vector<ll> diff;
    for (auto x: arr){
        if (x != ma){
            diff.push_back(ma - x);
        }
    }
    // take gcd of alle elements in the diff array and the max
    ll cur = diff[0];
    for (auto x: diff){
        cur = gcd(cur, x);
    }
    ll ops = 0;
    for (auto x: diff){
        ops += abs(x / cur);
    }
    //pll(diff);
    //cout << " gcd" << cur << endl;
    ll add = ma;

    while (true){
        if (exists.count(add) == 0){
            break;
        }
        ops++;
        add -= cur;
    }
    cout << ops << endl;
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