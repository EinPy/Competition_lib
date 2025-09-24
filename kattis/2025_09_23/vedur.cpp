#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const ll MAX_N = 1e10 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;

ll parent[MAX_N];
ll rnk[MAX_N];

void make_set(ll v)
{
    parent[v] = v;
    rnk[v] = 1;

}

ll find_set(ll v)
{
    if (v == parent[v])
    {
        return v;
    }
    parent[v] = find_set(parent[v]);
    return parent[v];
}

void union_sets (ll a, ll b)
{
    a = find_set(a);
    b = find_set(b);
    if (a != b)
    {
        if (rnk[a] < rnk[b])
        {
            swap(a, b);
        }
        parent[b] = a;
        if (rnk[a] == rnk[b])
        {
            rnk[a]++;
        }
    }
}

struct Node 
{
    ll key;
    ll r;
    ll c;
};

struct Edge
{
    ll w; //weight
    ll fr; //from
    ll to; //to
};



void solve() {
    
    ll n, m;
    cin >> n >> m;
    vector<ll> vals (n * m, 0);

    auto id = [&](ll r, ll c)
        {
            return r * m + c;
        };

    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            cin >> vals[id(r, c)];
        }
    }


    //create edges
    vector<Edge> edges;
    ll w;
    ll id1, id2;
    vector<vector<pair<ll,ll>>> mst(n*m);
    for (int r = 0; r < n - 1; r++)
    {
        for (int c = 0; c < m - 1; c++)
        {
            id1 = id(r, c);
            id2 = id(r+1, c);
            w = max(vals[id1], vals[id2]);
            edges.push_back(Edge{w, id1,id2}); 

            id2 = id(r, c+1);
            w = max(vals[id1], vals[id2]);
            edges.push_back(Edge{w, id1, id2});
        }
    }

    auto min_order = [] (const Edge & a, const Edge & b)
        {
            return a.w < b.w;
        };

    //kruskals minimum spanning tree
    sort(edges.begin(), edges.end(), min_order);
    ll added = 0;
    for (ll i = 0; i < n * m; i ++)
    {
        make_set(i);
    }

    ll cost;

    vector<Edge> result;

    for (Edge e : edges)
    {
        if (find_set(e.fr) == find_set(e.to))
        {
            continue;
        }
        cost += e.w;
        result.push_back(e);
        union_sets(e.fr, e.to);
    }
    for (Edge e : result)
    {
        mst[e.fr].push_back(make_pair(e.w, e.to));
        mst[e.to].push_back(make_pair(e.w, e.fr));
    }

    int power = 1;
    while ((1 << power) <= max(1, n * m))
    {
        power++;
    }

    ll q;
    cin >> q;
    ll sr, sc, er, ec, ans, mid;
    for (int i = 0; i < q; i++)
    {
        cin >> sr >> sc >> er >> ec;
        sr--;
        sc--;
        er--;
        ec--;
        if (sr == er && sc == ec)
        {
            cout << vals[id(sr, sc)] << "\n";
            continue;
        }
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

