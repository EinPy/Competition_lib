#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll c;

    cin >> c;
    ll n = c;
    vector<ll> arr;
    vector<ll> pref(n+2,0);
    ll sum = 0;
    for (int i = 1; i <= c; i ++){
        ll x;
        cin >> x;
        arr.push_back(x);
        sum += x;
        pref[i] = sum;
    }
    ll s, f;
    cin >> s >> f;
    //cout << c <<" " << n << endl;;
    // always wants to wait at least to the first timezone
    // bearly can participate
    // we do a sliding window approahc

    // literally not that hard, it's a sliding window
    // of length d
    ll d = f - s - 1;
    ll p = 0, best = 0, h= 1;
    for (ll i = 1; i <= n; i ++){
        ll r = i + d;
        if (r <= n){
            p = pref[r] - pref[i - 1];
        }
        else{
            p = pref[n] - pref[i -1] + pref[r % n];
        }
        
        if (p >= best){
            
            //cout << i << endl;
            //i is s, count backwards to find time in zone 0
            ll start = s;
            for (int back = 0; back < i -1; back++){
                start -= 1;
                if (start == 0){
                    start = c;
                }
            }
            if (p > best){
                h = start;
            }
            else{
                h = min(h,start);
            }
            best = p;
        }
        
    }
    cout << h;
    return 0;
}