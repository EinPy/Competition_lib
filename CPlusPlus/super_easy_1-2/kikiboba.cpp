#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {

}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    string s;
    cin >> s;

    int k_cnt = count(s.begin(), s.end(), 'k');
    int b_cnt = count(s.begin(), s.end(), 'b');

    if (k_cnt >   b_cnt){
        cout << "kiki" << endl;
    }else if (b_cnt > k_cnt)
    {
        cout << "boba" << endl;
    }else if(b_cnt == k_cnt && b_cnt != 0){
        cout << "boki"<<endl;
    }else{
        cout << "none" << endl;
    }
    
}   