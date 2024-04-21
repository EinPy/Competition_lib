#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    string s;
    cin >> s;
    int cnt['z' - 'a'+1] = {0};
    for (auto c: s){
        //cout << c << " "<< (int) c - 'a' << endl;
        cnt[c - 'a'] += 1;
    }
    // for (auto c: cnt){
    //     cout << c << " ";
    // }
    cout << endl;
    sort(srtarr(cnt));
    int out = 0;
    for (int i = 0; i < 'z' - 'a' - 2+1; i++){
        out += cnt[i];
    }
    cout << out;
}