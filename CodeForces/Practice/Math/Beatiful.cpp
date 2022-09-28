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
    while (t--){
        ll n, k, b, s;
        cin >> n >> k >> b >> s;
        // lengt = n, divide by k, beauty b, and sum s
        if (s / k < b){
            cout << -1 << endl;
        }
        else if (s / k == b){
            for (int i = 0; i <n -1; i++){
                cout << 0 << " ";
            }
            cout << s << endl;
        }
        else{
            vector<ll> myvector;
            ll must = k * b;
            if (must > s){
                cout << -1 << endl;
            }
            else{
                must += min(k-1, s - must);
                myvector.push_back(must);
                s -= must;
                for (int i = 0; i < n-1; i++){
                    ll el = min(k-1, s);
                    myvector.push_back(el);
                    s -= el;
                }
                if (s != 0){
                    cout << -1 << endl;
                }
                else{
                    for (auto x: myvector){
                    cout << x << " ";
                    }
                    cout << endl;
                }
                
            }
            
        }
    }

    return 0;
}

