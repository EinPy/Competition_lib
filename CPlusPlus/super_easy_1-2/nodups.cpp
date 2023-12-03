#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int g, s, c;
    cin >>g>>s>>c;
    int money = 3 * g + 2 * s + c;
    if (money >= 8){
        cout << "Province or ";
    }else if (money >= 5){
        cout << "Duchy or ";
    }else if (money >= 2){
        cout << "Estate or ";
    }
    if(money >= 6){
        cout << "Gold";
    }else if (money >= 3){
        cout << "Silver";
    }else{
        cout << "Copper";
    }

}