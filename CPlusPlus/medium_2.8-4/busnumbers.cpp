#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
#define srtarr(x) x, x + sizeof(x) / sizeof(x[0])

using namespace std;

using ll = long long;
using ull = unsigned long long;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int n;
    cin >> n;
    //we iterate downwards from a fixed c, starting at n
    // we iterate over all values of a up to sqrt(n)
    // check if there exists solution, if solution, store it
    // keep going until we find another unique solution
    // if not found  output none
    while (n > 0){
        
        int firsta = -1, firstb = -1;
        bool found = false;
        for (int a = 0; a <= ceil(cbrt(n)) + 5; a++){
            if (n - a * a * a > 0 && (pow (a, 3) + pow(floor(cbrt(n - a * a* a)), 3) == n ||pow (a, 3) + pow(ceil(cbrt(n - a * a* a)), 3) == n) ){
                if (a >= 1 && cbrt(n - a * a* a) >= 1){
                    int b;
                    if (pow (a, 3) + pow(floor(cbrt(n - a * a* a)), 3) == n){
                        b =floor( cbrt(n - a * a* a));
                    }if (pow (a, 3) + pow(ceil(cbrt(n - a * a* a)), 3) == n ){
                        b = ceil(cbrt(n - a * a* a));
                    }
                    // we have a valid solution
                    if (found && b != firsta){
                        //cout << firsta << " " << firstb << endl;
                        //cout << n <<" " <<  a << " " << b;
                        cout << n;
                        return 0;
                    }
                    firsta = a;
                    firstb = b;
                    found = true;
                }
                
            }
        }
        n--;
    }
    cout << "none";
}