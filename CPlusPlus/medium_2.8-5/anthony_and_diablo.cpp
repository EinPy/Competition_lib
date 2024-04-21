//solution to https://open.kattis.com/problems/anthonyanddiablo
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
    double a, n;
    cin >> a >> n;
    // maximum area with some fence is circle i think?
    if (M_PI * pow(n / (M_PI * 2), 2) >= a){
        cout <<  "Diablo is happy!";
    }else{
        cout << "Need more materials!";
    }
}