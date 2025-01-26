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



bool used[8] = {false};
int maxlen;
string usage;
unordered_set<string> seen;


void dfs(string cur){
    if ((int) cur.length() == maxlen){
        if (seen.insert(cur).second){
            cout << cur << endl;
        }
        return;
    }
    for (int i = 0; i < maxlen; i ++){
        if (used[i] == false){
            cur.push_back(usage[i]);
            used[i] = true;
            dfs(cur);
            cur.pop_back();
            used[i] = false;
        }
    }
    return;

}

ll fact(int n){
    ll out = 1;
    for (ll i = 1; i <= n; i++){
        out *= i;
    }
    return out;
}

void solve() {
    cin >> usage;
    sort(all(usage));
    maxlen = usage.length();
    //what is the most efficient way to do this?
    //can use some memory to keep track of seen? then do sort of a facotrial type of thing
    //sort of a depth first serach, dp?
    //
    unordered_map<char, int> cnt;
    for (char& c : usage){
        cnt[c]++;
    }
    //calculate permutations
    ll combs = fact(maxlen);
    for (auto& [character, count] : cnt){
        combs /= fact(count);
    }
    cout << (int) combs << endl;
    
    dfs("");
    return;
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}

