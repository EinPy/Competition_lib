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

void pll(vector<ll> vec){
    for (int i = 0; i < vec.size(); i++){
        cout << vec[i] << " ";
    }
    cout << endl;
    return;
}

bool solve() {
//think I need heuristic that is O(N), maybe O(nLog(N))
    //first I can find if the sum is dividible by 4, ortherwise it is not possible
    ll n, tot;
    tot = 0;
    cin >> n;
    vector<ll> nums(n,0);
    for (int i = 0; i < n; i++){
        cin >> nums[i];
        tot += nums[i];
    }
    //there is something with parity as well, I would think that you maybe have to do some sorting?
    //can actually propagate from first and last probably?
    //can make the first operation, and from then consider the positions where a[i] > 0
    if (nums[0] != 0){
        if (nums[1] >= 2 * nums[0] && nums[2] >= nums[0]){
            nums[1] -= 2 * nums[0];
            nums[2] -= nums[0];
            nums[0] = 0;
        }else{
            return false;
        }
    }
    for (int i = 0; i < n - 2;  i++){
        //consider nonzero elements
        //the first nonzero element can only be changed by applying the operation on the element to the right
        if (nums[i+1] >= nums[i] && nums[i+2] >= nums[i]){
            nums[i+1] -= 2 * nums[i];
            nums[i+2] -= nums[i];
            nums[i] = 0;
        }else{
            return false;
        }
    }
    if (nums[n-1] != 0 || nums[n-2] != 0){
        return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        if (solve()){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
}

