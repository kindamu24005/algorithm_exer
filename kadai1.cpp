#include <iostream>
#include <string>
using namespace std;
int main() {
    int A, B;
    string op;
    cin >> A >> op >> B;
    
    if (op == "+") {
        cout << A + B << endl;
    }
    // ここにプログラムを追記
    else if (op == "-"){
        cout << A - B << endl;
    }
    else if (op == "*"){
        cout << A * B << endl;
    }
    else if (op == "/" && B != 0){
        cout << A / B << endl;
    }
    else{
        cout << "error" << endl;
    }
    }

//atcoder1章計算問題
int main() {
  cout << 100 * (100+1) / 2 << endl;
}