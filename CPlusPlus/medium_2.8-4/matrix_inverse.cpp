//solution to https://open.kattis.com/problems/matrix
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
    // cin >> tc;]
    int a, b, c, d;
    while (cin >> a >> b >> c >> d){
        cout << "Case " << tc << ":" << endl;
        int div = 1 / (a * d - b * c);
        cout << div * d << " " << div * -1 * b << endl;
        cout << div * -1 * c << " " << div * a << endl;
        tc++;
    }
    return 0;
}