#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    string enc;
    getline(cin, enc);
    //convert string to array, thing, then shift array. 
    int const dim = sqrt(enc.size());
    if (dim == 1){
        cout << enc <<endl;
        return;
    }
    char arr[dim][dim];
    int a = 0;
    for (int r =0;r<dim;r++){
        for (int c=0;c<dim;c++){
            arr[r][c] = enc[a];
            a ++;
        }
    }
    for (int c = dim -1; c>=0;c--){
        for (int r = 0; r<dim;r++){
            cout << arr[r][c];
        }
    }
    cout << endl;

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    cin >> tc;
    cin.ignore();
    while (tc--) {
        // cout << "Case #" << t << ": ";
        string s;
        getline(cin, s);
        int const dim = sqrt(s.size());
        char arr[dim][dim];
        int a = 0;
        for(int i = 0; i< dim; i ++){
            for (int j = 0; j<dim; j++){
                arr[i][j] = s[a];
                a++;
            }
        }
        for(int j=dim-1;j>=0;j--){
            for (int i = 0;i<dim;i++){
                cout << arr[i][j];
            }
        }
        cout << endl;
    }
    return 0;
}