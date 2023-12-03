#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    double w, h;
    cin >> tc >> w >> h;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        int n;
        cin >> n;
        if (n <= sqrt(w *w + h * h)){
            cout<< "DA";
        }else{
            cout << "NE";
        }
        cout << endl;
    }
}