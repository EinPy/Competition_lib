#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int x, y;
    cin >> x >> y;
    if (x > 0){
        if (y > 0){
            cout << 1;
            return 0;
        }
        cout << 4;
    }else{
        if (y > 0){
            cout << 2;
            return 0;
        }
        cout << 3;

    }
}