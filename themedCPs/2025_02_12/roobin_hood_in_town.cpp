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




bool ok(ll tot, ll add, unordered_map<int,int>& seen, int n){
    //new_avg
    long double avg = (tot + add) / (2.0L * n);
    ll below = 0;
    for (const auto& [key, value] : seen){
        if (key < avg){
            below += value;
        }
    }
    if (below > n / 2){
        return true;
    }
    return false;
}

void solve() {
    int n;
    cin >> n;
    ll tot = 0;
    int max_n = 0;
    unordered_map<int,int> seen;
    int num;
    for (int i = 0; i < n;i++){
        cin >> num;
        tot += num;
        max_n = max(max_n, num);
        seen[num] += 1;
    }
    seen[max_n] --;
    
    //cout << endl;
    //for (const auto& [key, value] : seen){
    //    cout << key << " : " << value << endl;
    //}
    //cout << endl;

    if (n < 3){
        cout << -1 << endl;
        return;
    }
    ll low, high;
    low = 0;
    high = 1e13;
    ll ans = -1;
    ll mid;
    while (low <= high){
        mid = (low + high) / 2;
        if (ok(tot, mid, seen, n)){
            ans = mid;
            high = mid - 1;
        }else{
            low = mid + 1;
        }
    }
    //cout << "with average: " << (tot + ans) / (2 * n) << endl;
    cout << ans << endl;
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

