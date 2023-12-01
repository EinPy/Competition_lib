#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

double dist(pair<double,double> a, pair<double,double> b){
    return sqrt( pow(b.first - a.first, 2) + pow(b.second - a.second, 2));
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int numlines;
    while (true){
        cin >> numlines;
        if (numlines == 0){
            break;
        }
        cin.ignore();
        //compute average end
        double x_tot, y_tot;
        x_tot = 0;
        y_tot = 0;
        vector<pair<double, double> > ends;
        for (int i = 0; i < numlines; i ++){
            string line;
            getline(cin, line);
            istringstream iss(line);


            //cin.ignore();
            double x, y;
            iss >> x >> y;
            //cout << x << " " << y << endl;
            double curangle = 0;

            string command;
            while (iss >> command){
                if (command == "start" || command == "turn"){
                    double theta;
                    iss >> theta;
                    curangle += theta;
                }else{
                    //command is walk
                    double w;
                    iss >> w;
                    x += w * cos(curangle * 2*3.14159265359 / 360 );
                    y += w * sin(curangle *2* 3.14159265359 / 360);
                }
            }
            ends.push_back(make_pair(x, y));
            x_tot += x;
            y_tot += y;
        }
        
        x_tot = x_tot / (numlines);
        y_tot = y_tot / (numlines);
        //find point with greates distance to average
        double greatest = 0;
        for (auto p : ends){
            greatest = max(greatest, dist(make_pair(x_tot, y_tot),p));
        }
        cout << fixed << setprecision(3)<< x_tot << " " << y_tot << " " << greatest << endl;

    }
}
