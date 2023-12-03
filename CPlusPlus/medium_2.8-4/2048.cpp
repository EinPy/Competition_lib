#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int board[4][4];
    for (int r = 0; r < 4; r++){
        for (int c = 0; c < 4; c++){
            cin >> board[r][c];
        }
    }
    int dir;
    cin >> dir;
    vector<pair<int, int> > state;
    state.push_back(make_pair(-1, 0)); // 0 left
    state.push_back(make_pair(0, 1)); // 1 up
    state.push_back(make_pair(1, 0)); // 2 right
    state.push_back(make_pair(0, -1)); // down

    if (dir == 0){
        //test from left to rigth
        for (int r = 0; r < 4; r++){
            for (int c = 0; c < 4; c++){
                // for each col, iterate backwards to check if join possible
                int mv = board[r][c];
                bool posjoin = false;
                bool posmv = false;
                int last0 = 0;
                for (int nc = c-1; nc >=0; nc--){
                    if (board[r][nc] == 0){
                        posmv = true;
                        last0 = nc;
                    }
                    if (board[r][nc] == mv){
                        board[r][nc] = 2 * mv;
                        posjoin = true;
                        posmv = false;
                        break;
                    }else if (board[r][nc] != 0 ){
                        break;
                    }
                }

                if (posjoin){
                    board[r][c] = 0;
                }
                if (posmv){
                    board[r][last0] = board[r][c];
                    board[r][c] = 0; 
                }
            }
        }
    }


    for (int r = 0; r < 4; r++){
        for (int c = 0; c < 4; c++){
            cout <<  board[r][c] << " ";
        }
        cout << endl;
    }

}