#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    map<int, string> d;
    int a, b, c;
    cin >> a >> b >> c;
    d[a] = "Monnei";
    d[b] = "Fjee";
    d[c] = "Dolladollabilljoll";

    int key = min(a,b);
    //cout << a << b << c;
    key = min(key, c);
    //cout << key << endl;
    cout << d[key] << endl;
}