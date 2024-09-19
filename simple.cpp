
// simple.cpp
#include <iostream>

struct Point {
    int x;
    int y;
};

int main() {
    Point p = {10, 20};
    std::cout << "Point: (" << p.x << ", " << p.y << ")" << std::endl;
    return 0;
}
