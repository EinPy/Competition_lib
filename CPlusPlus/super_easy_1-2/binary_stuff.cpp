#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int num;
    cin >> num;
    string bin="";
    for (int i = 31; i >=0; i--){
        bin += (num & (1 << i)) ? "1" : "0";
    }
    //create normal number again
    //go from the first 1;
    int cnt = 0;
    int out = 0;
    for (int i = 0; i < bin.size(); i++){
        //starrt count on the first one
        if (bin[i] == '1'){
            out += pow(2, cnt);
            cnt +=1;
        }else{
            if (cnt != 0){
                cnt++;
            }
        }
    }
    cout << out;

}