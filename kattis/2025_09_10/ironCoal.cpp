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


void bfs(vector<int> &dist, vector<int> & starts, vector<vector<int>> & graph)
{
    vector<int> q = starts;
    
    for (auto u : starts)
    {
        dist[u] = 0;
    }

    while (q.size() > 0)
    {
        vector<int> q2;
        for (auto u : q)
        {
            for (auto v : graph[u]){
                if (dist[v] == -1)
                {
                    dist[v] = dist[u] + 1;
                    q2.push_back(v);
                }
            }
        }
        q = q2;
    }
}

void solve() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<int> iron;
    vector<int> coal;
    int a;
    for (int i = 0; i < m; i++)
    {
        cin >> a;
        iron.push_back(a-1);
    }
    for (int i = 0; i < k; i++)
    {
        cin >> a;
        coal.push_back(a-1);
    }

    vector<int> b;
    vector<vector<int>> adj(n, b);
    vector<vector<int>> rev_adj(n, b);

    for (int i = 0; i < n; i++)
    {
        int b;
        cin >> b;
        for (int j = 0; j<b ;j++)
        {
            int c;
            cin >> c;
            adj[i].push_back(c-1);
            rev_adj[c-1].push_back(i);
        }
    }

    vector<int> d_org (n, -1);
    vector<int> d_iron (n, -1);
    vector<int> d_coal (n, -1);

    vector<int> org = {0};
    bfs(d_org, org, adj);
    bfs(d_iron, iron, rev_adj);
    bfs(d_coal, coal, rev_adj);

    bool pos = false;

    int best = 10000000;

    for (int i = 0; i < n; i ++)
    {
        if (d_org[i] != -1 && d_iron[i] != -1 && d_coal[i] != -1)
        {
            pos = true;
            best = min(best, d_org[i] + d_iron[i] + d_coal[i]);
        }
    }
    if (pos)
    {
        cout << best;
    }
    else
    {
        cout <<"impossible";
    }


    

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

