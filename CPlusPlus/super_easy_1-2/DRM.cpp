#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    string s;
    getline(cin, s);

    //get half
    string first = s.substr(0, s.size() / 2);
    string second = s.substr(s.size()/2);
    ///cout << first << " " << second << endl;
    string f[s.size() / 2];
    string sec[s.size() / 2];
    int rotv =0;
    for(auto c: first){
        rotv += (int) c - 'A';
    }
    string frot = "";
    for (auto c: first){
        char newc = (((c - 'A') + rotv) % 26) + 'A';
        frot += newc;
    }

    //cout << rotv << endl;
    //cout << frot << endl;

    //rotate second string
    rotv =0;
    string srot = "";
    for(auto c: second){
        rotv += (int) c - 'A';
    }

    for (auto c: second){
        char newc = (((c - 'A') + rotv) % 26) + 'A';
        srot += newc;
    }
    //cout << srot << endl;

    string out = "";
    for (int i = 0; i < s.size() / 2; i ++){
        char newc = (((frot[i] - 'A') + (srot[i] - 'A')) % 26) + 'A';
        out += newc;
    }
    cout << out;


}