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


void rec(int num_disk, int source, int aux, int dest)
{
    if (num_disk == 1){
        //there is only one disk, move it from the source to the destination
        cout << source << " " << dest << endl;
        return;
    }else
    {
        //move n-1 disks from the source to the auxillary
        rec(num_disk - 1, source, dest, aux);  // move n - 1 disks from the source, now with the destination used as the auxillary
        //move a disk from the source to the destimation, this is the bottom disk
        cout << source << " " << dest << endl;
        //now move the rest of the dists from the auxillary, now using the source as auxillary, to the actual destination
        rec(num_disk - 1, aux, source, dest);
    }
    return;
}

void solve() {
    int n;
    cin >> n;

    if (n == 1){
        cout << 1 << endl;
        cout << "1 3" << endl;
        return;
    }
    if (n == 2)
    {
        cout << 3 << endl;
        cout << "1 2" << endl;
        cout << "1 3" << endl;
        cout << "2 3" << endl;
        return;
    }
    cout << pow(2, n) - 1<< endl;
    rec(n, 1, 2, 3);
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

