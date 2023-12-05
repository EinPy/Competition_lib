#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

long long MOD = pow(10, 9) + 7;

struct matrix {
    long long mat[2][2];
    matrix friend operator *(const matrix &a, const matrix &b){
        matrix c;
        for (int i = 0; i < 2; i++) {
          for (int j = 0; j < 2; j++) {
              c.mat[i][j] = 0;
              for (int k = 0; k < 2; k++) {
                  c.mat[i][j] += a.mat[i][k] * b.mat[k][j];
                  c.mat[i][j] %=  MOD;
              }
          }
        }
        return c;
    }
};


matrix matpow(matrix base, long long n) {
    matrix ans{ {
      {1, 0},
      {0, 1}
    } };
    while (n) {
        if(n&1)
            ans = ans*base;
        base = base*base;
        n >>= 1;
    }
    return ans;
}

long long fib(ll n) {
    if (n == 0){
        return 0;
    }
    matrix base{ {
      {1, 1},
      {1, 0}
    } };
    return matpow(base, n).mat[0][1];
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    ll a ,b;
    ll n;
    
    cin >> a >> b >> n;

    if (n == 0){
        cout << a << " " << b << endl;
        return 0;
    }

    
    ll aa, bb, cc;
    aa = fib(2 * (n) - 1);
    bb = fib(2 * (n));
    cc = fib(2 * n + 1);
    //cout << aa <<" " <<bb<<" " << cc << endl;
    cout << (aa * a + bb* b) % MOD << " " << (bb * a + cc * b) % MOD; 
    

}