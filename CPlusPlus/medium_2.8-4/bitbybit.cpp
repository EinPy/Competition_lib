//solution to https://open.kattis.com/problems/bitbybit
#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    while (cin >> tc){
        vector<int> out (tc, -1);
        string command;
        int a, b;

        for (int i = 0; i < tc; i ++){
            cin >> command >> a;
            if (command == "AND" || command = "OR"){
                cin >> b;
            }
            if (command == "CLEAR"){
                out[a] = 0;
            }
            if (command == "SET"){
                out[a] = 1;
            }
            if (command == "OR"){
                if (out[a] != -1){
                    if (out[b] != -1){
                        out[a] = out[a] | out[b];
                    }
                }
                if (out[b] == 1){
                    out[a] = 1;
                }
            }
            if (command == "AND"){
                
            }

        }
    }
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}