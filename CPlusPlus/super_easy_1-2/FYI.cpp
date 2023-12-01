#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int arr[2];
    cin >> arr[0] >> arr[1];
    int l = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr + l);
    cout << arr[0] << " " << arr[1];
}