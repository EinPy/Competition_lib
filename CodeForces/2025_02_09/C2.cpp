#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 2e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

ll A[MAX_N];
ll B[MAX_N];


ll lb (int up,ll nm, ll targ){
    ll l, r;
    ll mid;
    l = 0;
    r = up;
    ll ans = -1;
    while (l <= r){
        mid = (l + r) / 2;
        if (B[mid] - nm  >= targ){
            ans = mid;
            r = mid - 1;
        }else{
            l = mid + 1;
        }
    }
    return ans;
}
void parr(int n){
    for (int i = 0; i < n; i++){
        cout << A[i] << " ";
    }
    cout << endl;
    return;
}

void solve() {
    
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++){
        cin >> A[i];
    }
    for (int i = 0; i < m; i++){
        cin >> B[i];
    }

    ll mi, ma;
    
    sort(B, B + m);
    //now, for each number, make it as small as possible
    for (int i = 0; i < n; i ++){
        if (i == 0){
            A[i] = min(A[i], B[0] - A[i]);
        }else{
            //find the smallest number where B[num] - arr[i] >= arr[i-1]
            ll idx = lb(m - 1, A[i], A[i-1]);
            if (idx != -1){
                if (A[i] >= A[i-1]){
                    A[i] = min(A[i], B[idx] - A[i]);
                }else{
                    A[i] = B[idx] - A[i];
                    if (A[i] < A[i-1]){
                        cout << "NO\n";
                        return;
                    }
                }
            }else{
                if (A[i] < A[i-1]){
                    cout << "NO\n";
                    //parr(n);
                    return;
                }
            }
        }
    }
    cout << "YES\n";
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

