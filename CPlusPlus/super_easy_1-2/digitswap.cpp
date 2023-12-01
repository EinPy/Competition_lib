#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int col, row;
    cin >> col >> row;
    double cars = 0;
    for (int r = 0;r<row;r++){
        string s;
        cin >> s;
        for (int c =0;c<col;c++){
            if (s[c] == '#'){
                cars++;
            }
        }
    }
    cout << ((col * row) - cars) / (col * row);
}