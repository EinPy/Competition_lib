#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    string s;
    cin >> s;
    size_t a = s.size();
    string out;
    out += "h";
    for (size_t i = 0; i < (a - 2)  * 2 ; i++){
        out += "e";
    }
    out += "y";
    cout << out;

}