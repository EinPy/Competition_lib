#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

void solve() {
    
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int board[4][4];
    bool hasjoined[4][4];
    for (int r = 0; r < 4; r++){
        for (int c = 0; c < 4; c++){
            cin >> board[r][c];
            hasjoined[r][c] = false;
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
        //test movign from right to the left
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
                    if (board[r][nc] == mv && !hasjoined[r][nc]){
                        board[r][nc] = 2 * mv;
                        posjoin = true;
                        posmv = false;
                        hasjoined[r][nc] = true;
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
    if (dir == 1){
        for (int c = 0; c < 4; c++){
            for (int r = 0; r < 4; r++){
                // for each row, iterate upwards and check to join
                int mv = board[r][c];
                bool posjoin = false;
                bool posmv = false;
                int last0 = 0;
                for (int nr = r - 1; nr >= 0; nr --){
                    if (board[nr][c] == 0){
                        posmv = true;
                        last0 = nr;
                    }
                    if (board[nr][c] == mv  &&!hasjoined[nr][c]){
                        board[nr][c] = 2 * mv;
                        posjoin = true;
                        posmv = false;
                        hasjoined[nr][c] = true;
                        break;
                    }else if (board[nr][c] != 0 ){
                        break;
                    }
                }
                if (posjoin){
                    board[r][c] = 0;
                }
                if (posmv){
                    board[last0][c] = board[r][c];
                    board[r][c] = 0; 
                }
            }   
        }
    }
    if (dir == 2){
        //test from left to right
        for (int r = 0; r < 4; r++){
            for (int c = 3; c >= 0; c--){
                // for each col, iterate forwards to check if join possible
                int mv = board[r][c];
                bool posjoin = false;
                bool posmv = false;
                int last0 = 0;
                for (int nc = c + 1; nc <  4; nc++){
                    if (board[r][nc] == 0){
                        posmv = true;
                        last0 = nc;
                    }
                    if (board[r][nc] == mv &&!hasjoined[r][nc]){
                        board[r][nc] = 2 * mv;
                        posjoin = true;
                        posmv = false;
                        hasjoined[r][nc] = true;
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
    if (dir == 3){
        // move down
        for (int c = 0; c < 4; c++){
            for (int r = 3; r >= 0; r--){
                // for each row, iterate donw and check to join
                int mv = board[r][c];
                bool posjoin = false;
                bool posmv = false;
                int last0 = 0;
                for (int nr = r + 1; nr < 4; nr ++){
                    if (board[nr][c] == 0){
                        posmv = true;
                        last0 = nr;
                    }
                    if (board[nr][c] == mv  &&!hasjoined[nr][c]){
                        board[nr][c] = 2 * mv;
                        posjoin = true;
                        posmv = false;
                        hasjoined[nr][c] = true;
                        break;
                    }else if (board[nr][c] != 0 ){
                        break;
                    }
                }
                if (posjoin){
                    board[r][c] = 0;
                }
                if (posmv){
                    board[last0][c] = board[r][c];
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