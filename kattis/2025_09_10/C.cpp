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
    vector<int> a;
    vector<vector<int>> g(n, a);

    vector<int> dist(n, -1);

    int fr, to;
    for (int i = 0; i < m; i ++)
    {
        cin >> fr >> to;
        g[fr].push_back(to);
        g[to].push_back(fr);
    }

    int vis = 0;
    vector<int> dir(n, -1);
    bool pos = true;

    for (int i = 0; i < n; i ++)
    {
        if (dir[i] == -1)
        {
            dir[i] = 0;
            vector<int> q;
            q.push_back(i);

            while (q.size() > 0)
            {
                vector<int> q2;
                for (auto node : q)
                {
                    for (auto v : g[node])
                    {   
                        if (dir[v] == dir[node])
                        {
                            pos = false;
                        }
                        if (dir[v] == -1)
                        {
                            if (dir[node] == 0)
                            {
                                dir[v] = 1;
                            }else
                            {
                                dir[v] = 0;
                            }
                            q2.push_back(v);
                        }
                    }
                }
                q = q2;
            }
        }
    }
    if (pos)
    {
        cout << "attend here";
    }
    else{
        cout <<"no way";
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

