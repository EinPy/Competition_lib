#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 5;
    // cin >> tc;
    int best=0;
    int bestidx;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        int cur = 0;
        for (int j =0;j<4;j++){
            int a;
            cin >> a;
            cur +=a;
        }
        if (cur > best){
            best = cur;
            bestidx = t;
        }
    }
    cout << bestidx << " " << best;
}