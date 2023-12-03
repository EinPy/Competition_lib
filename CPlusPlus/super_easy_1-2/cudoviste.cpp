#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

const int maxnum = 50;
char arr[maxnum][maxnum];
int row, col;

void solve() {
    //
    vector<pair<int,int> >  dir;
    dir.push_back(make_pair(0,0));
    dir.push_back(make_pair(1,0));
    dir.push_back(make_pair(1,1));
    dir.push_back(make_pair(0,1));
    //check all possible squares
    int crush[5]={};
    for(int r = 0;r < row -1; r++){
        for (int c=0;c<col-1;c++){
            //check all directions
            //cout << "checking " << r << " " << c << endl;
            bool pos = true;
            int sq = 0;
            for (auto x : dir){
                char find = arr[r + x.first][c + x.second];
                if (find == '#'){
                    pos = false;
                }else if(find == 'X'){
                    sq ++;
                }

            }
            if (pos){
                crush[sq]++;
            }
        }
    }
    for (auto x : crush){
        cout << x << endl;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    char ch;
    cin >> row >>col;
    for (int r =0; r<row;r++){
        for(int c=0;c<col;c++){
            cin >> ch;
            arr[r][c] =ch;
        }
    }
    // for (int r =0; r<row;r++){
    //     for(int c=0;c<col;c++){
    //         cout << arr[r][c];
    //     }
    //     cout << endl;
    // }

    solve();
    
}