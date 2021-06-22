#include <iostream>
 
using namespace std;
 
int main()
{
    int N;
    cin >> N;
    for (int I = 0; I < N; I++) {
        float a, b;
        cin >> a >> b;
        if (b / a >= 2)
            cout << "NO\n";
        else
            cout << "YES\n";
    }
}
 