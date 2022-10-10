#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mp make_pair


int fix(int a, int w){
    if(a < 0){
        return w +a;
    }
    return a;
}


int main()
{

    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int n, k;
    cin >> n >> k;

    vector<float> prob;
    for (int i = 0; i < n ; i++){
        float in = 0;
        cin >> in;
        prob.push_back(in);

    }

    sort(prob.begin(), prob.end());
    reverse(prob.begin(), prob.end());

    float dp[n+2][(n+3) * 2] = {0};
    float best = 0;
    for (int i = 0; i < n+2; i++){
        for (int j = 0; j <(n+3)*2; j++){
            dp[i][j] = 0;
        }
    }



    dp[0][0] = 1;
    int width = ((n+3) * 2);


    for (int r = 0; r < n+1; r++){
        dp[r][fix(-r,width)] = 1;
    }
    for (int i = 0; i < width; i ++){
        dp[0][i] = 0;
    }
    dp[0][0] = 1;



    for (int i = 1; i< n+1; i++){
        for (int j = -1 + 1; j < i+1; j++){
            dp[i][fix(j, width)] = prob[i-1] * dp[i-1][fix(j-1, width)] + (1 - prob[i-1]) * dp[i-1][fix(j+1, width)];
            if (j >= k){
                best = max(best, dp[i][fix(j, width)]);
            }
        }
    }

    cout << best << endl;

    return 0;
}