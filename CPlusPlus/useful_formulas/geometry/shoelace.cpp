#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

struct Point {
    double x, y;
};

//if counterclockwise, area is positive, otherwise it is negative
double computeSignedArea(vector<Point> points) {
    double area = 0.0;
    int n = points.size();

    for (int i = 0; i < n; i++) {
        int j = (i + 1) % n; // Next vertex, wrapping around
        area += (points[i].x * points[j].y) - (points[j].x * points[i].y);
    }

    return area / 2.0;
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