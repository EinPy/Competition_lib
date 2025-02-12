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



void solve() {
    int l, r, L, R;
    cin >> l >> r >> L >> R;
    r ++;
    R ++;
    //lock all doors that are in an overlapping range
    //if zero overlap
    //two overlapping segemnts are between the smallest upper bound and the greatest lower bound
    int top = min(r, R);
    int bot = max(l, L);

    if (bot > top){
        cout << 1 << endl;
        return;
    }
    int score = top - bot - 1;
    if (min(l, L) < bot){
        score ++;
    }
    if (max(r, R) > top){
        score ++;
    }
    cout << score << endl;
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

