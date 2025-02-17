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


ll N;
int arr[MAX_N];


void solve() {
    cin >> N;
    unordered_map<int,int> seen;
    for (int i = 0; i < N; i++){
        cin >> arr[i];
        seen[arr[i]]++;
    }
    //N**2 possible subarrays
    //only worth to delete duplicates, deleting one number is never worth it, as
    //it at most increases score by 1 if duplicate is removed but also de3creases by 1
    //01233 has score 5 - 4 = 1
    //012 has score 3 - 3 = 0
    //33 has score 2 - 1 = 1
    //233 has score 3 - 2 = 1
    //
    //can do prefix and postfix array?
    //find the contigues subarray where more unique elements are deleted than the range of the indicies?
    //also minimize the legnth with that score?
    //
    //so deleting duplicates are never worth it because then score is decreased,
    //after that we want to delete the longest contigues sequence of unique numbers
    int best_len = 0;
    int bl, br;
    bl = 0;
    br = 0;
    int l, r;
    l = 0;
    r = 0;
    int curlen = 0;
    //iterate over array
    int i = 0;
    while (i < N){
        while (i < N && seen[arr[i]] == 1){
            i++;
            curlen++;
        }
        if (curlen > best_len){
            best_len = i - l;
            bl = l;
            br = i;
        }
        l = i + 1;
        curlen = 0;
        i++;
    }
    if (best_len == 0){
        cout << 0 << endl;
        return;
    }
    cout << bl + 1 << " " << br << endl;
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

