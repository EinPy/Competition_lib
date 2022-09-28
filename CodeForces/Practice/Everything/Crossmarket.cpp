//https://codeforces.com/contest/1715/problem/A
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
    while (t--)
    {
        int n, m;
        cin >> n >> m;
        //cout <<n << " " << m << endl;
        if (n == 1 && m == 1){
            cout << 0 << "\n";
        }
        else if (min(n, m ) == 1){
            cout << max(n,m) << endl;
        }
        else{
            cout << n - 1 + m - 1 + min(n,m) << endl;
        }
    }
    return 0;
}