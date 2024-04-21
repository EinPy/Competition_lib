#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

ll fact(ll n){
    ll out = 1;
    for (int i = 2; i <= n; i++){
        out *= i;
    }
    return out;
}

ll binomialCoefficient(int n, int k) {
    if (k > n - k) 
        k = n - k;

    ll result = 1;
    for (int i = 0; i < k; ++i) {
        result *= (n - i);
        result /= (i + 1);
    }

    return result;
}

void solve() {
    ll casenum, steps;
    cin >> casenum >>  steps;
    ll total = 0;

    //iterate from 0 onesteps to steps / 2 onesteps per leg
    for (int one = 0; one <= steps /2; one++){
        if ((steps - 2 * one) % 4 == 0){
            //the equation has a solution
            ll two = (steps - 2 * one) / 4;
            if (two  >= one){
                ll leftone = one;
                ll lefttwo = two;
                ll perm = binomialCoefficient(one + two, one);
                ll ways = perm * perm;
                total += ways;
            }
        }
    }
    cout << casenum << " " << total << endl;
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