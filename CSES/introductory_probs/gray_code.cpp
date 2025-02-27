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
    int n;
    cin >> n;
    int curnum = 0;
    int bit = 0;
    for (int it = 0; it < pow(2, n); it++){
        //determine the gray number
        curnum = it ^ (it >> 1);
        //print the curnum in a correct way
        for (int i = n - 1; i >= 0; i --){
            bit = (curnum >>  i) & 1;
            cout << bit;
        }   
        cout << endl;
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

