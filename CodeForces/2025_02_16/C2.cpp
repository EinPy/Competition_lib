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

const ll NEG_INF = -1e18; // “negative infinity”
 
void solve() {
    int n;
    cin >> n;
    vector<ll> arr(n);
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // next_pos[i]: index of the first positive number at or after index i
    vector<int> next_pos(n + 1, n);
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] > 0) {
            next_pos[i] = i;
        } else {
            next_pos[i] = next_pos[i + 1];
        }
    }

    // prev_neg[i]: index of the last negative number at or before index i
    vector<int> prev_neg(n, -1);
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            prev_neg[i] = i;
        } else if (i > 0) {
            prev_neg[i] = prev_neg[i - 1];
        }
    }

    // max_negative[i]: maximum coins from subarray arr[0..i] if only negative moves are made
    vector<ll> max_negative(n, 0);
    for (int i = 0; i < n; i++) {
        max_negative[i] = max_negative[max(0, i - 1)];
        if (arr[i] < 0) {
            ll new_value = -arr[i] + (i > 0 ? max_negative[i - 1] : 0);
            max_negative[i] = max(max_negative[i], new_value);
        }
    }

    // best_switch[i]: best option to switch to negative moves from arr[i..n-1]
    vector<ll> best_switch(n + 1, NEG_INF);
    for (int i = n - 1; i >= 0; i--) {
        best_switch[i] = best_switch[i + 1];
        if (arr[i] < 0) {
            ll new_value = -arr[i] + (i > 0 ? max_negative[i - 1] : 0);
            best_switch[i] = max(best_switch[i], new_value);
        }
    }

    // max_coins[i]: max coins from arr[i..n-1] when choosing moves optimally
    vector<ll> max_coins(n + 1, 0);
    for (int i = n - 1; i >= 0; i--) {
        ll best_choice = NEG_INF;
        if (next_pos[i] < n) { 
            best_choice = arr[next_pos[i]] + max_coins[next_pos[i] + 1];
        }
        max_coins[i] = max(best_choice, best_switch[i]);
    }

    ll result = max(max_coins[0], max_negative[n - 1]);
    cout << result << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int test_cases;
    cin >> test_cases;
    
    while (test_cases--) {
        solve();
    }
    
    return 0;
}
