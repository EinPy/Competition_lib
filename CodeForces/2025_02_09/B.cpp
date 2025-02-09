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
    string s;
    cin >> s;
    //if there is any matching, the length is 1?
    if (s.size() == 1){
        cout << "1" << endl; 
        return;
    }
    for (int i = 0; i < s.size() - 1; i ++){
        if (s[i] == s[i+1]){
            cout << "1" << endl;
            return;
        }
    }
    cout << s.size() << endl;
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

