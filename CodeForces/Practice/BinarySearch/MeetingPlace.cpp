#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


bool ok (vector<ll> f, vector<ll> s, long double t){
    long double sho = 3e9, lon = 0;
    vector<ll> pref(f.size(),0);
    long double L = 0, R = 3e9;
    vector<pair<long double,long double>> segs;
    for (int i = 0; i < f.size(); i++){
        segs.push_back(make_pair(f[i] - s[i]*t, f[i] + s[i]*t));
        L = max(f[i] - s[i]*t, L);
        R = min(f[i] + s[i]*t, R);
    }
    if (L <= R){
        return true;
    }
    return false;

}


long double first_true(vector<ll> f, vector<ll> s) {
	long double lo = 0, hi = 3e9, mid;
    long double ans= -1;

	while (lo <= hi) {
		mid = (hi + lo) / 2;
		if (ok(f,s,mid)) {
            ans = mid;
			hi = mid - 0.0000001;
		} else {
			lo = mid + 0.0000001;
		}
	}
	return ans;
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
    vector<ll> f;
    vector<ll> s;
    for (int i = 0; i < t; i ++)
    {
        ll x;
        cin >> x;
        f.push_back(x);
    }
        for (int i = 0; i < t; i ++)
    {
        ll x;
        cin >> x;
        s.push_back(x);
    }
    long double ans = first_true(f, s);
    cout.precision(12);
    cout << ans;
    return 0;
}