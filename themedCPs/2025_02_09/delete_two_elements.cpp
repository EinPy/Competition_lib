#include <bits/stdc++.h>
#include <unordered_map>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 2e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;



void solve() {
    bool debug = false;
    int n;
    cin >> n;
    ld tot = 0;
    vector<ll> arr(n);
    for (int i = 0; i < n; i ++){
        cin >> arr[i];
        tot += arr[i];
    }
    long double mean = tot / n;
    if (debug){cout << "mean "<< mean << endl;}
    long double targg = mean* 2;
    if (debug){cout << "targ: " << targg << endl;}
    ll targ = (ll) targg;
    if ((ll) targg != targg){
        cout << 0 << endl;
        return;
    }
    unordered_map<ll,int> seen;
    ll out = 0;
    for (int i = 0; i < n; i ++){
        //check if a number an equal distance from the mean already exists
        ll need = targ - arr[i];
        if (seen.find(need) != seen.end()){
            out += seen[need];
        }else{
            seen[need] = 0;
        }
        seen[arr[i]]++;
    }
    cout << out << endl;
    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        //cout << "Case #" << t << ": ";
        solve();
    }
}

