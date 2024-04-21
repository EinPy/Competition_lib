#include <bits/stdc++.h>
#define all(x) begin(x),end(x)

using namespace std;

using ll = long long;
using ull = unsigned long long;

//fast modulo operations
ull modmul(ull a, ull b, ull M) {
	ll ret = a * b - M * ull(1.L / M * a * b);
	return ret + M * (ret < 0) - M * (ret >= (ll)M);
}
ull modpow(ull b, ull e, ull mod) {
	ull ans = 1;
	for (; e; b = modmul(b, b, mod), e /= 2)
		if (e & 1) ans = modmul(ans, b, mod);
	return ans;
}

//miller rabin is prime
//probabilistic approach
//guaranteed to work for numbers up to 7 * 10**18, for larger numbers use python
bool isPrime(ull n) {
	if (n < 2 || n % 6 % 4 != 1)
		return (n | 1) == 3;
	ull s = __builtin_ctzll(n-1);
	for (ull a : {2, 325, 9375, 28178, 450775, 9780504, 1795265022}) {
		ull p = modpow(a % n, n >> s, n), i = s;
		while (p != 1 && p != n - 1 && a % n && i--)
			p = modmul(p, p, n);
		if (p != n-1 && i != s) return 0;
	}
	return 1;
}


//pollard-rho prime factorization
//returns prime factos in arbitrary order 
ull pollard(ull n) {
	auto f = [n](ull x) {return modmul(x, x, n)+1;};
	ull x = 0, y = 0, t = 30, prd = 2, i = 1;
	while (t++ % 40 || gcd(prd, n) == 1) {
		if (x == y) x = ++i, y = f(x);
		ull q = modmul(prd, max(x,y)-min(x,y), n);
		if (q) prd = q;
		x = f(x), y = f(f(y));
	}
	return gcd(prd, n);
}
vector<ull> factor(ull n) {
	if (n == 1) return {};
	if (isPrime(n)) return {n};
	ull x = pollard(n);
	auto l = factor(x), r = factor(n / x);
	l.insert(l.end(), all(r));
	return l;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    while (true){
        ull n;
        cin >> n;
        if (n == 4){
            return 0;
        }
        int cnt  = 1;
        while (!isPrime(n)){
            cnt++;
            vector<ull> f = factor(n);
            n = 0;
            for (auto x :f){
                n += x;
            }
        }
        cout << n << " " << cnt << endl;

    }
}