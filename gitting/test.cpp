#include <iostream>

int calculation(int x, int y){
    int sum;
    sum = x % y;
    return sum;
}

using namespace std;

int main(){
    int x,y;
    cin >> x >> y;
    cout << calculation(x,y);
    return 0;

}