#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair



int main()
{
#ifndef ONLINE_JUDGE
    freopen("i.txt", "r", stdin);
    freopen("o.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    vector<int> w;
    int totalWeight = 0;
    int a;
    while (t--)
    {
        cin >> a;
        totalWeight += a;
        w.push_back(a);
    }
    //cout << totalWeight << endl;
    int possible[3000] = {};
    possible[0] = 1;
    int best = -1;
    for (int k = 0; k < w.size(); k++){
        for (int x = totalWeight; x>= 0; x--){
            if (possible[x] == 1 && x + w[k] <3000){
                possible[x+w[k]] = 1;
                if (abs(1000 - x+w[k]) <= abs(best-1000)){
                    best = x+w[k];
                }
            }
        }
    }
    cout << best;
}