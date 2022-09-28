#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


bool ok (vector<ll> arr, ll k, ll mid){
    ll zero = 0;
    ll ops = 0;
    //cout << mid << " " << k << endl;
    for (ll i = (arr.size()-1) / 2; i <= arr.size()-1; i++){
        ll m = max(zero, mid - arr[i]);
        ops += m;
        //cout << m << endl;
    }
    //cout << ops << endl;
    if (ops <= k){ return true;}
    else{
        return false;
    }
}

int last_true(vector<ll> arr, ll k){
    ll lo = 1, hi = 3e9, mid;
    lo --;
	while (lo < hi) {
		int mid = lo + (hi - lo + 1) / 2;
		if (ok(arr, k, mid)) {
			lo = mid;
		} else {
			hi = mid - 1;
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
    ll t, k;
    cin >> t >> k;
    ll mid = t / 2;
    vector<ll> arr;
    ll tC = t;
    while (t--)
    {
        ll x;
        cin >> x;
        arr.push_back(x);
    }
    if (tC == 1){
        cout << arr[0] + k << endl;
        return 0;
    }
    
    sort(arr.begin(),arr.end());
    ll lo = last_true(arr,k);
    cout << lo;
    
    

    

    return 0;
}