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
    
    int N;
    cin >> N;
    string s;
    cin >> s;
    bool l = false;
    bool v = false;
    for (int i = 0; i < N-1; i ++)
    {
        if (s[i] == 'l')
        {
            l = true;
        }
        if (s[i] == 'v')
        {
            v = true;
        }
        if (s[i] == 'l' && s[i+1] == 'v')
        {
            cout << 0;
            return;
        }
    }
    if (s[N-1] == 'v')
    {
        v = true;
    }
    if (s[N-1] == 'l')
    {
        l = true;
    }
    if (v || l){
        cout << 1;
        return;
    }
    cout << 2;
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

