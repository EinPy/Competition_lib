#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 2e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


ll arr[MAX_N];
void solve() {
    // do not need to think too much, can just do it greedy, always make the smallest
    //  possible
    ll n, m;
    cin >> n >> m;
    
    for (ll i = 0; i < n; i++){
        cin >> arr[i];
    }
    ll num;
    cin >> num;
    if (n == 1){
        cout << "YES" << endl;
        return;
    }
    //always make each number as small as possible
    ll mi, ma;
    for (ll i = 0; i < n; i ++){
        if (i == 0){
            arr[i] = min(arr[i], num - arr[i]);
        }else{
            mi =  min(arr[i], num - arr[i]);
            ma = max(arr[i], num - arr[i]);
            if (mi >= arr[i-1]){
                arr[i] = mi;
            }else{
                arr[i] = ma;
            }
            if (arr[i] < arr[i-1]){
                cout << "NO" << endl;
                return;
            }
        }
    }
    cout << "YES" << endl;
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

