#include <bits/stdc++.h>
using namespace std;

typedef long long ll;


vector<int> outeven(vector<int> s){
    vector<int> out;
    for (int i = 0; i< s.size() / 2; i++){
        //add of left deck and then of right deck
        out.push_back(s[i]);
        out.push_back(s[i + s.size()/2]);
        
    }
    return out;
}

vector<int> ineven(vector<int> s){
    vector<int> out;
    for (int i = 0; i< s.size() / 2; i++){
        out.push_back(s[i + s.size()/2]);
        out.push_back(s[i]);
    }
    return out;
}

vector<int> outodd(vector<int> s){
    vector<int> out;
    for (int i = 0; i< s.size() / 2 + 1; i++){
        out.push_back(s[i]);
        if (i != s.size() / 2){
            out.push_back( s[i + s.size()/2 + 1]);
        }
    }
    return out;
}

vector<int> inodd(vector<int> s  ){
    vector<int> out;
    // for (auto x: s){
    //     cout << x << " ";
    // }
    // cout << endl;
    for (int i = 0; i< s.size() / 2; i++){
        out.push_back(s[i + s.size()/2]);
        out.push_back(s[i]);
    }
    out.push_back( s[s.size()-1]);
    // cout << "rotate to"<< endl;
    // for (auto x: out){
    //     cout << x << " ";
    // }
    // cout << endl << endl;
    return out;
}
//can probably simulate?
//can probably find a mathematical formula

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    string s;
    int a;
    cin >> a >> s;
    string copy = s;
    int parity = a % 2;
    int cnt = 1;
    vector<int> org;
    vector<int> check;
    for (int i = 0; i < a;i++){
        org.push_back(i);
        check.push_back(i);
    }
    if (parity){
        //odd
        if (s == "out"){
            check = outodd(check);
            while(check != org){
                check = outodd(check);
                cnt ++;
            }
        }else{
            //cout << " in odd";
            check = inodd(check);
            while(check != org){
                check = inodd(check);
                cnt ++;
            }
        }
    }else{
        //even
        if (s == "out"){
            check = outeven(check);
            while(check != org){
                check = outeven(check);
                cnt ++;
            }
        }else{
            check = ineven(check);
            while(check != org){
                check = ineven(check);
                cnt ++;
            }
        }
    }
    cout << cnt;
}