#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool isprime(ll n){
    if (n < 2){
        return false;
    }
    if (n % 2 == 0){
        if (n == 2){
            return true;
        }
        return false;
    }
    ll mx = min(ceil(sqrt(n)) + 2, N);
    for (ll i = 0; i < mx; i += 2){
        if (n % i == 0){
            return false;
        }
    }
    return true;

}