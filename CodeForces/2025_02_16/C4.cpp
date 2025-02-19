#include <bits/stdc++.h>
#include <ios>
#include <vector>

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

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    //positve sum will go from right to left,
    //negative sum will go from left to right
    //next_pos and rightmost_ne
    vector<ll> pos_sum(n, 0);
    vector<ll> neg_sum(n, 0);
    vector<ll> leftmost_pos(n, 100000000);
    vector<int> rightmost_neg(n, -1);
    ll cursum = 0;
    int next_neg = -1;
    
    int first_pos = -1;
    for (int i = n - 1; i >= 0; i--){
        if (arr[i] >= 0){
            cursum += arr[i];
        }
        pos_sum[i] = cursum;
        

        leftmost_pos[i] = first_pos;
        if (arr[i] > 0){
            first_pos = i;
        }
    }
    
    cursum = 0;
    for (int i = 0; i < n; i++){
        if (arr[i] < 0){
            cursum += abs(arr[i]);
        }


        rightmost_neg[i] = next_neg;
        if (arr[i] < 0){
            next_neg = i;
        }
        neg_sum[i] = cursum;

    }

    cursum = 0;
    int l, r;
    l = 0;
    r = n - 1;
    while (l <= r){
        //check if there is a an option that does not need computation
        if (arr[l] >= 0){
            cursum += arr[l];
            l ++;
        }else if (arr[r] < 0){
            cursum += abs(arr[r]);
            r --;
        }else{
            //check if the remaining positive sum or the remaining negative sum is larger
            ll rempos;
            rempos = pos_sum[l];
            if (r != n-1){
                rempos -= pos_sum[r+1];
            }
            ll remneg;
            remneg = neg_sum[r];
            if (l != 0){
                remneg -= neg_sum[l-1];
            }
            if (rempos >= remneg){
                l = leftmost_pos[l];
                cursum += arr[l];
                l++;
            }else{
                r = rightmost_neg[r];
                cursum += abs(arr[r]);
                r--;
            }
        }
    }
    cout << cursum << endl;

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

