
// example.cpp
#include <iostream>

#include <vector>

#include <Eigen/Dense>

using namespace std;
using namespace Eigen;

struct Point {
    int x;
    int y;
};

int main() {
    Point p = {10, 20};

    int C = 7;

    int Z = 42;

    std::vector<int> test(10,1);

    // Define a square matrix (3x3 for this example)
    Matrix3d A = Matrix3d::Identity();
    
    cout << "Original Matrix:" << endl;
    cout << A << endl;
    
    std::cout << "Point: (" << p.x << ", " << p.y << ")" << std::endl;
    return 0;
}
