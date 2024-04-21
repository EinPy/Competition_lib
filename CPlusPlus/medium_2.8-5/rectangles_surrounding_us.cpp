#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void pg(int arr[505][505]){
    for (int r = 0; r < 20; r++){
        for ( int c = 0; c < 20; c++){
            cout << arr[r][c] << " ";
        }
        cout << endl;
    }
}


void solve(int tc) {
    int arr[505][505] = {0};
    //pg(arr);
    int a, b, c, d;
    // just to rows of prefix sums, this is easier
    int cnt = 0;
    for (int i = 0; i < tc; i++){
        cnt++;
        cin >> a >> b >> c >> d;
        for (int r = b; r < d; r++){
            for (int col = a; col < c; col++){
                arr[r][col]++;
            }
        }
    }
    //cout << "this ran" << cnt << endl;
    //pg(arr);
    int out = 0;
    for (int r = 0; r < 502; r ++){
        for (int cc = 0; cc < 502; cc++){
            if (arr[r][cc]){
                out ++;
            }
        }
    }
    cout << out << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc;
    while (true){
        cin >> tc;
        if (tc == 0){
            return 0;
            break;
        }
        solve(tc);
    }
}