//solution to https://codeforces.com/contest/1907/problem/B
#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    string s;
    cin >> s;
    vector<pair<char, int> > l, u;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == 'b'){
            if (l.size() > 0){
                l.pop_back();
            }
        }else if (s[i] == 'B'){
            if(u.size() > 0){
                u.pop_back();
            }
        }else{
            if (tolower(s[i]) == s[i]){
                l.push_back(make_pair(s[i], i));
            }else{
                u.push_back(make_pair(s[i], i));
            }
        }
    }
    int ls, us;
    vector<char>out;
    reverse(all(l));
    reverse(all(u));
    while (l.size() > 0 || u.size() > 0){
        ls = 10000000;
        us = 10000000;
        if (l.size() > 0){
            ls = l.back().second;
        }
        if(u.size() > 0){
            us = u.back().second;
        }
        if (ls < us){
            out.push_back(l.back().first);
            l.pop_back();
        }else{
            out.push_back(u.back().first);
            u.pop_back();
        }
    }
    for (auto c: out){
        cout << c;
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}