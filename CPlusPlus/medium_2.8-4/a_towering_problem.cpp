#include <bits/stdc++.h>
#define all(x) begin(x),end(x)
using namespace std;
using ll = long long;

void solve() {
    
}
//this is just 3sum, unoptimized version is N3 which is ok for small input
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int h[6];
    for (int i = 0; i<6;i++){
        cin >> h[i];
    }
    int a , b;
    cin >> a >> b;
    set<int> used;
    vector<int> first;
    vector<int> second;
    for (int i = 0; i < 6; i++){
        for (int j = i+1; j < 6; j++){
            for (int k = j + 1; k < 6; k++){
                if (h[i] + h[j] + h[k] == a){
                    first.push_back(h[i]);
                    first.push_back(h[j]);
                    first.push_back(h[k]);
                    for (int idx = 0; idx < 6; idx++){
                        if (idx != i && idx != j && idx != k){
                            second.push_back(h[idx]);
                        }
                    }
                    sort(all(first), greater<int>());
                    sort(second.begin(),second.end(), greater<int>());
                    for (auto x : first){
                        cout << x << " ";
                    }
                    for (auto x : second){
                        cout << x  << " ";
                    }
                    return 0;
                }
            }
        }
    }
}