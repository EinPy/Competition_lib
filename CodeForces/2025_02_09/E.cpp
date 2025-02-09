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
    ll n, m, k;
    cin >> n >> m >> k;

    // If the absolute difference between zeros and ones is greater than k, it's impossible
    if (abs(n - m) > k) {
        cout << "-1\n";
        return;
    }

    // Now, let's try to construct the string.
    string out = "";
    
    // We need to start with the more abundant character to prevent large balance substrings.
    char first_char = n > m ? '0' : '1';
    char second_char = n > m ? '1' : '0';
    ll first_count = n > m ? n : m;
    ll second_count = n > m ? m : n;
    ll fadd = 0;
    ll sadd = 0;
    // If we have excess characters, add them first in a balanced manner
    while (first_count > 0 && second_count > 0 && out.size() < n + m) {
        // Ensure the balance doesn't exceed k
        if (fadd - sadd < k) {
            out.push_back(first_char);
            first_count--;
            fadd ++;
        } else {
            out.push_back(second_char);
            second_count--;
            sadd ++;
        }
    }
    
    // If any characters are left, append them at the end
    while (first_count > 0) {
        out.push_back(first_char);
        first_count--;
    }
    while (second_count > 0) {
        out.push_back(second_char);
        second_count--;
    }

    // Now, check if we have created a valid string with the required maximum balance k
    cout << out << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        solve();
    }
}

