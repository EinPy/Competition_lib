#include <bits/stdc++.h>
#include <vector>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


void pvec(vector<int> v){
    for (int i = 0;i < v.size(); i++){
        cout << v[i] << " ";
    }
    cout << endl;
    return;
}

void solve() {
    int n;
    cin >> n;
    vector<int> A(n);
    vector<int> B(n);
    for (int i = 0; i < n; i++){
        cin >> A[i];
    }
    for (int i = 0; i < n; i++){
        cin >> B[i];
    }
    int diff = 0;
    for (int i = 0; i < n - 1;i++){
        if(A[i] > B[i+1]){
            //cout << "adding " << A[i] - B[i+1] << endl;
            diff += A[i] - B[i+1];
        }
    }
    diff += A[n-1];
    //pvec(A);
    //pvec(B);
    //cout << "last char of A: " << A[n - 1] << endl;
    cout << diff << endl;
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

