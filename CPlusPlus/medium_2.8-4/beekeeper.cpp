//https://open.kattis.com/problems/beekeeper
#include <bits/stdc++.h>
#define all(x) begin(x),end(x)

using namespace std;

using ll = long long;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    set<char> vow = {'a', 'e', 'i', 'o', 'u', 'y'};
    set<string> doub = {"aa", "ee", "ii", "oo", "uu", "yy"};
    while (true){
        int tc;
        cin >> tc;
        cin.ignore();
        if (tc == 0){
            return 0;
        }
        unordered_map<string,int> d;
        string bestwrd;
        int cnt = 0, bstcnt = 0;
        for (int i = 1; i <= tc; i++){
            cnt =0;
            string s;
            getline(cin, s);
            for (int j = 0; j < s.size()-1; j++){
                if (s[j] == s[j+1] && vow.count(s[j]) > 0){
                    cnt++;
                }
            }
            if (cnt >= bstcnt){
                bstcnt = cnt;
                bestwrd = s;
            }
        }
        cout << bestwrd << endl;

    }
}