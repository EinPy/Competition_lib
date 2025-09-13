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
    int n, m;
    cin >> n >> m;
    vector<vector<int>> A(n, vector<int> (m, 0));
    for (int r = 0;r<n;r++){
        for(int c=0;c<m;c++){
            cin >> A[r][c];
        }
    }
    //takes at most two operations to turn all of one colour into another
    //is it ever wort to turn something into an intermediary colour?
    //count the number of colours and the operations for them?
    unordered_map<int,int> seen;
    int mx = 0;
    for (int r = 0; r<n;r++){
        for(int c =0;c<m;c++){
            //check all surrounding cells to the right and down
            if (seen.find(A[r][c]) == seen.end()){
                seen[A[r][c]] = 1;
            }
            if (r + 1 < n){
                if (A[r+1][c] == A[r][c]){
                    seen[A[r][c]] = 2;
                }
            }
            if (c+1 < m && A[r][c+1] == A[r][c]){
                seen[A[r][c]] = 2;
            }
            mx = max(mx, seen[A[r][c]]);
        }
    }
    ll out = 0;
    for (auto& [k, v] : seen){
        out += v;
    }
    out -= mx;
    cout << out << endl;
    return;
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

