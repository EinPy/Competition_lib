#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    string a_num, s_num, t_lan;
    cin >> a_num >> s_num >> t_lan;
    //translate to normal number;
    //x number system
    int sys = s_num.size();
    // create a mapping from char to int
    unordered_map<char,int> dct;
    unordered_map<int,char> dctrev;
    for (int i = 0; i < s_num.size();i++){
        dct[s_num[i]] = i;      
    }
    for ( int i = 0; i < t_lan.size();i++){
        dctrev[i] = t_lan[i];
    }


    int power = 0;
    int actual = 0;
    for (int i = a_num.size()-1; i >= 0; i --){
        actual += dct[a_num[i]] * pow(sys, power);
        power ++;
    }
    
    //convert actual number to new system
    //divide by nymbersystem and set bit to remainder
    int outsys = t_lan.size();
    string out="";
   // cout << "got here" << endl;
    while (actual){
        int rem = actual % outsys;
        out += dctrev[rem];
        //cout << actual << " / " << sys << " rem: " << rem << endl;
        actual = actual / outsys;
        
    }
    reverse(out.begin(), out.end());
    cout << out;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }
}