#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


bool ok(vector<pair<ll,ll>> rd, ll rad){
    vector<bool> vis (rd.size(), false);
    ll cnt = 0;
    for (int i = 0; i < rd.size(); i ++){
        if (rd[i].second == 1){
            vis[i] = true;
            cnt += 1;

            ll p = i;
            while(p + 1 < rd.size() && rd[p+1].second != 1 && rd[p+1].first - rd[i].first <= rad){
                p ++;
                vis[p] = true;
                cnt += 1;
            }
            p = i;
            while(p - 1 >= 0 && !vis[p-1] && rd[i].first - rd[p-1].first <= rad){
                p--;
                vis[p] = true;
                cnt += 1; 
                }
            
        }
    }
    for (auto x : vis){
        if (!x){
            return false;
        }
    }
    return true;
}


ll first_true(vector<pair<ll,ll>> rd){
    ll lo = 0, hi = 3e9, mid;
    hi ++;
    while (lo < hi){
        mid = lo + (hi-lo) / 2;
        if (ok(rd, mid)){
            hi = mid;
        }
        else{
            lo = mid + 1;
        }
        
    }
    return lo;
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
    int t, m;
    cin >> t >> m;
    vector<pair<ll,ll>> road;
    for (int i = 0; i < t; i++)
    {
        ll city, type = 0;
        cin >> city;
        road.push_back(make_pair(city, type));
    }
    for (int i = 0; i< m; i++){
        ll tower, type = 1;
        cin >> tower;
        road.push_back(make_pair(tower, type));
    }
    sort(road.begin(), road.end());
    ll ans = first_true(road);

    cout << ans;

    return 0;
}