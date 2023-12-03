#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    ll pts = 4;
    ll outer = 0; // handle first case by itself, represents how many on one side
    ll sq = 0; //innersquaresnumber of square

    //all inner crosses will always share 4 of 5 pts
    //corners share 2, edges share 3
    for (int t = 0; t < tc; t++) {
        // cout << "Case #" << t << ": ";
        if (t == 0){
            pts = 9;
            sq = 4;
            outer = 2;
        }else{
            //for each corner, add 3 unique points
            //first calculate total outer squares
            ll totouter = 2 * outer + (2 * outer -2);
            pts += 4 * 4; // add all corners // shared dots are half
            pts += (totouter - 4) * (2 +0.5 + 0.5 + 0.5);

            //inner squares add 1 unique pt, 4 shares -> 2 tot 3
            ll totsqures = outer * outer;
            ll innersquares = totsqures - totouter;
            pts += innersquares * 3-1;

            outer = outer  * 2;

        }
    }
    cout << pts;
}