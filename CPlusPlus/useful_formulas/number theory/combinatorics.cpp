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