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


using State = array<char, 16>;

void left (State & s, int r)
{
    //AAAA
    //BBBB
    //rrrr
    //DDDD
    char org = s[4*r];
    s[4*r] = s[4*r + 1];
    s[4*r + 1] = s[4*r + 2];
    s[4*r + 2] = s[4*r + 3];
    s[4*r + 3] = org;
    
}

void right (State & s, int r)
{
    char org = s[4*r];
    s[4*r] = s[4*r + 3];
    s[4*r + 3] = s[4*r + 2];
    s[4*r + 2] = s[4*r + 1];
    s[4*r + 1] = org;
    
}

void down (State & s, int c)
{
    char org = s[c];
    s[c] = s[12 + c];
    s[12 + c] = s[8 + c];
    s[8+c] = s[4 + c];
    s[4+c] = org;
    
}

void up (State & s, int c)
{
    char org = s[c];
    s[c] = s[4 + c];
    s[4 + c] = s[8 + c];
    s[8 + c] = s[12 + c];
    s[12 + c] = org;
    
}

void solve() 
{
    string s1, s2, s3, s4;
    cin >> s1 >> s2 >> s3 >> s4;
    string inp = s1 + s2 + s3 + s4;

    State cur;
    for (int i = 0; i < inp.size(); i ++)
    {
        cur[i] = inp[i];
    }

    string gl = "RRRRGGGGBBBBYYYY";
    State goal;
    for (int i = 0; i < gl.size();i++)
    {
        goal[i] = gl[i];
    }

    if(cur == goal)
    {
        cout << 0;
        return;
    }

    unordered_map<string,vector<string>> g1, g2;

    unordered_map<string, int> d1, d2;

    d1[cur] = 0;
    d2[goal] = 0;
    
    vector<string> q1, q2;

    q1.push_back(cur);
    q2.push_back(goal);

    vector<string> dirs = {s1, s2, s3, s4};

    while (q1.size() > 0 || q2.size() > 0)
    {
        //do one layer in each bfs
        vector<string> q1_2;
        for (auto & u : q1)
        {
            //16 possible neighbours
            for(int i = 0; i < 4; i++)
            {
                dirs[0] = left(u, i);
                dirs[1] = up(u, i);
                dirs[2] = right(u, i);
                dirs[3] = down(u, i);

                for (auto dir : dirs)
                {
                    if (d1.find(dir) == d1.end())
                    {
                        d1[dir] = d1[u] + 1;
                        if (d2.find(dir) != d2.end())
                        {
                            cout << d1[dir] + d2[dir];
                            return;
                        }
                        q1_2.push_back(dir);
                        
                    }
                }
            }
            
        }
        q1 = q1_2;

        vector<string> q2_2;
        for (auto & u : q2)
        {
            //16 possible neighbours
            for(int i = 0; i < 4; i++)
            {
                dirs[0] = left(u, i);
                dirs[1] = up(u, i);
                dirs[2] = right(u, i);
                dirs[3] = down(u, i);

                for (auto dir : dirs)
                {
                    if (d2.find(dir) == d2.end())
                    {
                        d2[dir] = d2[u] + 1;
                        if (d1.find(dir) != d1.end())
                        {
                            cout << d1[dir] + d2[dir];
                            return;
                        }
                        q2_2.push_back(dir);
                        
                    }
                }
            }
        } 
        q2 = q2_2;
    }

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

