#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair

const int MAXI = 1e5 + 10;
bool isPossible, vis[MAXI + 2], group[MAXI];
vector<vector<int>> g(MAXI+2);
    

void dfs(int n = 1, bool c = 0){
    //cout << "visiting: " << n << endl;
    vis[n] = 1;
    group[n] = c;
    for (int v: g[n]){
        if (vis[v]){
            if (group[v] == c){
                isPossible = false;
            }
        }else{
            dfs(v, !c);
        }
    }
}


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
    {
        for (int i = 0; i <= MAXI +1; i ++){
            vis[i] = 0;
            g[i] = {};
        }
        isPossible = true;

        int n, m;
        cin >> n >> m;
        
        int a, b;
        while (m--){
            cin >> a >> b;
            g[a].push_back(b);
            g[b].push_back(a);
        }
        dfs();
        a = 0;
        b = 0;
        for (int i = 1; i <= n; i++){
            if (group[i] == 1){
                a ++;
            }
            else{
                b++;
            }
        }
        if (a < b){
            cout << a << "\n";
            for (int i = 1; i <= n; i++){
                if (group[i] == 1){
                    cout << i << " ";
                }
            }
        }
        else{
            cout << b << "\n";
            for (int i = 1; i <= n; i++){
                if (group[i] == 0){
                    cout << i << " ";
                }
            }
        }
        cout << "\n";

    }
    return 0;
}