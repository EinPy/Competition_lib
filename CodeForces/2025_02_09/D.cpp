#include <bits/stdc++.h>
#include <utility>

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
    ll n, m;
    vector<vector<ll>> arrays;
    vector<tuple<ll,ll, ll>> scores; //pair of score, totalvalue and array, then sort based on score and concat arrays
    cin >> n >> m;
    for (ll i = 0; i < n; i ++){
        //read in a vector of length m;
        vector<ll> tmp(m);
        ll total = 0;
        ll score = 0;

        for (ll idx = 0; idx < m; idx++){
            cin >> tmp[idx];
            total += tmp[idx];
            score += (m - idx) *  tmp[idx];
        }
        arrays.push_back(tmp);
        //inside same loop I can create the score of the array
        tuple<ll, ll, ll> tp = {total, score, i};
        scores.push_back(tp);
    }
    sort(all(scores));
    //compute the toal score
    ll out = 0;
    for (int i = 0; i < n; i ++){
        //for the first "pass" use the score, for all other passes, use the total
        auto [tt, ss, id] = scores[i];
        //cout << "score: " << ss << endl;
        out += ss;
        //then the worst scores will have zero multiples of sum, the others
        //will have i - 1 multiples of sum
        out += (i * m) * tt;
        //cout << "total " << tt << endl;
        //cout << "tadd " << (i * m) * tt << endl;
        
    }
    cout << out << endl;


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

