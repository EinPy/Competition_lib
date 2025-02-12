#include <bits/stdc++.h>
#include <cmath>

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
    string num;
    cin >> num;
    int two, thre;
    two = 0;
    thre = 0;
    ll sum = 0;
    int n;
    for (int i = 0; i < num.size(); i ++){
        if (num[i] == '2'){
            two++;
        }
        if (num[i] == '3'){
            thre++;
        }
        n = num[i] - '0';
        sum += n;
    }
    //cout << "digsum: " << sum << endl;
    sum += 9;
    int rem = 9 - ( sum % 9 ); // whats left to create
    if (sum % 9 == 0){
        cout << "YES" << endl;
        return;
    }
    //figurte out if we can create the remainder as a linear combination of 2 * two + 6 * thre
    
    for (int x = 0; x <= min(two, 10); x++){
        for (int y = 0; y <= min(thre, 10); y++){
            if ((x * 2 + y * 6) % 9 == rem){
                cout << "YES" << endl;
                return;
            }
        }
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

