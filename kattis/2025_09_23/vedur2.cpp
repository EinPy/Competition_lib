
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

vector<ll> parent;
vector<ll> depth;

void make_set(ll v)
{
    parent[v] = v;
    depth[v] = 1;

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
        if (depth[a] < depth[b])
        {
            swap(a, b);
        }
        parent[b] = a;
        if (depth[a] == depth[b])
        {
            depth[a]++;
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
    parent.resize(n*m);
    depth.resize(n*m);

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
    for (int r = 0; r < n; r++)
    {
        for (int c = 0; c < m; c++)
        {
            id1 = id(r, c);
            id2 = id(r+1, c);
            if (r+1 < n)
            {
                w = max(vals[id1], vals[id2]);
                edges.push_back(Edge{w, id1,id2}); 
            }
            if (c+1 < m)
            {
                id2 = id(r, c+1);
                w = max(vals[id1], vals[id2]);
                edges.push_back(Edge{w, id1, id2});
            }
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


    vector<Edge> result;

    for (Edge e : edges)
    {
        if (find_set(e.fr) == find_set(e.to))
        {
            continue;
        }
        result.push_back(e);
        union_sets(e.fr, e.to);
    }
    for (Edge e : result)
    {
        mst[e.fr].push_back(make_pair(e.w, e.to));
        mst[e.to].push_back(make_pair(e.w, e.fr));
    }

    int power = 1;
    while ((1 << power) <= n * m)
    {
        power++;
    }
    //dpeth from the root
    vector<ll> branch_len(n*m, -1);
    //up[k][v] = up[k-1][up[k-1][v]]
    vector<vector<ll>> up(power, vector<ll> (n*m, -1)); //up[i][j] is 2**i parent of node j
    vector<vector<ll>> mx (power, vector<ll> (n*m, 0)); // mx[i][j] maximum edge weight encounted on upwards path to parent 2**i from node j 

    //rooting the MST and finding the level 0 ancestors

    deque<ll> dq;
    ll N = n*m;
    for (ll s = 0; s < N; s++)
    {
        if (branch_len[s] != -1)
        {
            //we have already processed
            continue;
        }
        branch_len[s] = 0;
        up[0][s] = -1;
        mx[0][s] = 0;
        dq.push_back(s);
        while (!dq.empty())
        {
            ll u = dq.front();
            dq.pop_front();
            for (auto [w, v] : mst[u])
            {
                if (branch_len[v] == -1)
                {
                    branch_len[v] = branch_len[u] + 1;
                    up[0][v] = u;
                    mx[0][v] = w;
                    dq.push_back(v);
                }
            }
        }
    }

    //now, how to build the binary lifitng tables. 
    for (int k = 1; k < power; k++)
    {
        for (int v = 0; v < N; v++)
        {
            //so for every binary lifting power, iterate over every node
            ll a = up[k-1][v]; //the 2**(k-1) ancestor of v
            if (a == -1)
            {
                up[k][v] = -1;
                mx[k][v] = mx[k-1][v]; //cannot go higher, keep the current max
            }else{
                up[k][v] = up[k-1][a]; // don't really understand this one
                // or yes to the 2**k ancestor a a is the the 2 * 2**(k-1) of the root, so if we find the intermediary, we take one step from that one as well
                mx[k][v] = max(mx[k-1][v], mx[k-1][a]);

            }
        }
    }

    auto lift_max = [&](ll u, ll steps) -> pair<ll, ll> {
        ll max_on_path = 0;
        ll bit = 0;

        //decompose steps in binary
        //jump of 2**bit steps and mrge wbottleneck
        while (steps > 0 && u!= -1)
        {
            if (steps & 1)
            {
                max_on_path = max(max_on_path, mx[bit][u]);
                u = up[bit][u];
            }
            steps >>= 1; //move the the next bit?
            bit++; //consider the next power of 2 jump
        }
        return {u, max_on_path};
    };


    auto query = [&] (ll u, ll v)->ll{
        if (u == v)
        {
            return vals [u];
        }
        if (branch_len[u]<branch_len[v])
        {
            swap(u,v);
        }
        //lift deeper node to same level as others
        auto [uu, acc1] = lift_max(u, branch_len[u] - branch_len[v]);
        //lift both nodes up together
        u = uu;
        ll ans = acc1;
        if (u == v)
        {
            return ans;
        }
        
        for (int k = power - 1; k >= 0; k--)
        {
            if (up[k][u] != up[k][v])
            {
                ans = max(ans, mx[k][u]);
                ans = max(ans, mx[k][v]);
                u = up[k][u];
                v = up[k][v];
            }
        }
        //now u and v are children of lca, one more jump
        ans = max(ans, mx[0][u]);
        ans = max(ans, mx[0][v]);
        return ans;
    };

    int q; cin >> q;
    while (q--) {
        int sr, sc, er, ec; cin >> sr >> sc >> er >> ec;
        --sr; --sc; --er; --ec;
        int a = id(sr, sc), b = id(er, ec);
        cout << query(a, b) << '\n';
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

