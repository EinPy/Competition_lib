#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;



void solve() {
    int n;
    cin >> n;
    string A, B;
    cin >> A >> B;
    //split each string eas each pair of 1 and 0 can be allocated directly iwth a score of 2

    vector<string> AA;
    vector<string> BB;

    //falsg
    int on = 0;
    int ze = 0;
    int score = 0;
    string cA = "";
    for (int i = 0; i < n; i++){
        on = 0;
        ze = 0;

        if (A[i] == '1' || B[i] == '1'){
            on = 1;
        }
        if (A[i] == '0' || B[i] == '0'){
            ze = 1;
        }
        if (ze && on){
            score += 2;
            if (!cA.empty()){
                AA.push_back(cA);
                //cout << cA << endl;
                cA = "";
            }
        } else{
            cA.push_back(A[i]);
        }
    }
    if (!cA.empty()){
        AA.push_back(cA);
    }
    for (int i = 0; i < AA.size(); i++){
        string cur = AA[i];
        bool on, ze;
        on = false;
        ze = false;
        for (int j = 0; j < cur.size(); j++){
            if (cur[j] == '1'){
                on = true;
            }
            if (cur[j] == '0'){
                ze = true;
                score++;
            }
            if (ze && on){
                score++;
                ze = false;
                on = false;
            }
        }
    }
    cout << score << endl;

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

