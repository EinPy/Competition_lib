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


ll arr[101];
//int bits[32];

void solve() {
    int n;
    cin >> n;
     vector<int> bits(32, 0);
    //cout << "vec size " << bits.size() << endl;
    ll num;
    for (int i = 0; i < n; i++){
        cin >> num;
        int bitnum = 0;
        while (num > 0){
            if ((num & 1) == 1){
                bits[bitnum] = 1;
            }
            num = num >> 1;
            bitnum++;
        }
    }
    //now create the actual number from the bits
    ll out = 0;
    for (int i = 0; i < 32; i++){
        if (bits[i] != 0){
            out += pow(2, i);
        }
    }
    cout << out << endl;
   
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        //cout << "Case #" << t << ": ";
        solve();
    }
}

