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
    int t;
    cin >> t;
    vector<ll> arr(t,0);
    for (int ii = 0; ii < t;ii++){
        cin >> arr[ii];;
    }
    ll sum = -1e10, best = -1e10;
    for (int i = 0; i < t; i++){
        sum = max(arr[i], sum + arr[i]);
        best = max(sum, best);
    }
    cout << best;
    return 0;
}