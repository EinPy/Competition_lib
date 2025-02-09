#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


// This is a suggestion ok, that is fine

void solve() {
    int n, m , k;
    //keep track of min and max possible, will be a 2d array with each entry being cur_min and cur_max
    cin >> n >> m >> k;

    int totcost = n * m - 1;
   if (k == totcost){
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

