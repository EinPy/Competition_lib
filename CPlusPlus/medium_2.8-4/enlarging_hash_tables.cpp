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
    ll mx = min((ll)ceil(sqrt(n)) + 2, n);
    for (ll i = 3; i < mx; i += 2){
        if (n % i == 0){
            return false;
        }
    }
    return true;

}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll n;
    while (cin >> n){
        if (n == 0){
            break;
        }
        ll check = 2 * n + 1;
        //i guess i only need to check odd numbers;
        while (!isprime(check)){
            check += 2;
        }
        cout << check;
        if (!isprime(n)){
            cout << " (" << n << " is not prime)";
        }
        cout << endl;
        

    }
}