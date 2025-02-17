#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 2e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e9;
const ld EPS = 1e-9;


ll arr[MAX_N];
//ll prev_neg[MAX_N];
//ll next_pos[MAX_N];
ll N;
unordered_map<int, unordered_map<int ,int>> dp;
//vector<vector<ll>> dp;


ll rec(int l, int r){
    //always delete l if negative and always delete right if negative
    //
    //cout << "checking: "<< l << " " << r << endl;
    if (l > r){
        return 0;
    }
    if (l == r){
        return abs(arr[l]);
    }
    if (dp.find(l) != dp.end() && dp[l].find(r) != dp[l].end()){
        return dp[l][r];
    }
    //if (dp[l][r] != -1){
        //cout << "hashed value \n";
      //  return dp[l][r];
    //}
    //
    if (arr[l] >= 0){
        return arr[l] + rec(l+1, r);
    } else if (arr[r] < 0){
        return -1 * arr[r] + rec(l, r-1);
    }

    //now try all different possible choices?
    //actually only need to check the first positive from the left
    //and the first negative from the right!, there is never a point
    //in choosing a negative number that is to the left of a negative number
    //because then you could always choose both
    ll best = 0;
    for (int i = l; i <= r; i++){
        if (arr[i] >= 0){
            best = max(best, arr[i] + rec(i+1, r));
            break;
        }
        
        //else{
          //  best = max(best, -1 * arr[i] + rec(l, i-1));
        //}
    }
    for (int i = r; i >= l; i --){
        if (arr[i] < 0){
            best = max(best, -1 * arr[i] + rec(l, i-1));
            break;
        }
    }
    dp[l][r] = best;
    return best;
}

ll greedy(int l,int r){
    ll score = 0;
    while (arr[l] >= 0&& l < N){
        score += arr[l];
        l++;
    }
    while (arr[r] < 0 && r >= l){
        score += -1 * arr[r];
        r --;
    }

}

void solve() {
    cin >> N;
    int neg_idx = -1;

    for (int i = 0; i < N;i++){
        cin >> arr[i];
        if (arr[i] > 0){
            neg_idx = i;
        }
        prev_neg = neg_idx;
        
    }
    //allocate next and prev arrays
        


    //dp.assign(N, vector<ll>(N, -1));
    dp.clear();
    cout << rec(0, N-1) << endl;
    return;

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

