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
    string s;
    cin >> n;
    cin >> s;
    //a segment 1111, is only one move
    //a segment 11000, is two moves, move it with zeroes, then move zeroes back
    //what if 11001100
    //
    //1100, 1100
    //110000, 11
    // -, 11110000
    // 0000, 1111
    // Can it be done faster?
    // this was 4 moves
    // - , 11001100
    // 1100, 1100
    bool is1 = false;
    int moves = 0;
    for (int i = s.size() - 1; i>=0; i--){
        //if on a 1 segment, fine, if not on a one segment, add two moves
        if (!is1 && s[i] == '1'){
            moves += 2;
            is1 = true;
        }
        if (s[i] == '0'){
            is1 = false;
        }
    }
    if (s[s.size() - 1] == '1'){
        moves --;
    }
    cout << moves << endl;
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

