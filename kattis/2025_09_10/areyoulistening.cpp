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


bool ok (vector<vector<int>> & stations, int & cx, int & cy, int rad)
{
    int lap = 0;
    for (int i = 0; i < stations.size(); i++)
    {
        float diff = sqrt((cx - stations[i][0])* (cx - stations[i][0]) + (cy - stations[i][1]) * (cy - stations[i][1]));
        if (rad + stations[i][2] > diff)
        {
            lap ++ ;
        }
        if (lap >= 3)
        {
            return false;
        }
    }
    return true;
}

void solve() {
    
    int cx, cy, n;
    cin >> cx >> cy >> n;
    vector<int> a;
    vector<vector<int>> stations (n, a);
    int aa, b, c;
    for (int i = 0;i <n;i++)
    {
        cin >>aa>>b>>c;
        stations[i].push_back(aa);
        stations[i].push_back(b);
        stations[i].push_back(c);
    }

    int ans = 0;
    int l = 0;
    int r = 30000;
    
    int mid;
    while (l < r)
    {
        mid = (l + r) / 2;
        if (ok(stations,cx, cy,mid))
        {
            ans = mid;
            l = mid + 1;
        }else
        {
            r = mid;
        }
            
    }
    cout << ans;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

