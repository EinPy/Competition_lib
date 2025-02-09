#include <bits/stdc++.h>
#include <unordered_set>

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

    int n;
    cin >> n;

    unordered_set<ll> seen_a;
    unordered_set<ll> seen_b;
    
    ll temp;
    for (int i = 0; i < n; i ++){
        cin >> temp;
        seen_a.insert(temp);
    }
    for (int i = 0; i < n; i ++){
        cin >> temp;
        seen_b.insert(temp);
//        seen_a.insert(temp);
    }

   if (seen_a.size() >= 3 || seen_b.size() >= 3 || (seen_a.size() >= 2 && seen_b.size() >= 2)){
        cout << "YES" << endl;
        return;
    }
    cout << "NO" << endl;
    return;


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

