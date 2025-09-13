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
    int g[n][m];
    string s;
    for ( int i = 0; i < n; i ++)
    {
        cin >> s;
        for (int j = 0; j < m; j++)
        {
            g[i][j] = s[j] - '0';
        }
    }

    int dist[n][m];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            dist[i][j] = -1;
        }
    }

    vector<pair<int, int>> q;
    q.push_back(make_pair(0,0));
    dist[0][0] = 0;
    while (q.size() > 0)
    {
        vector<pair<int,int>> q2;
        for (auto [r, c] : q)
        {
            int el = g[r][c];
            vector<pair<int,int>> next = {{r + el, c}, {r - el, c}, {r, c - el}, {r, c + el}};

            for (auto [nr, nc] : next)
            {
                if (nr < n && nr >= 0 && nc < m && nc >= 0 && dist[nr][nc] == -1)
                {
                    dist[nr][nc] = dist[r][c] + 1;
                    q2.push_back(make_pair(nr, nc));
                }
            }
        }
        q = q2;
    }

    cout << dist[n - 1][m - 1];
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

