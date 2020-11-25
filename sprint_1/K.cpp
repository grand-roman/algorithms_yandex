#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string qer(int x){
    string k="";
    string t = "";
    while (x!=1){
        if (x%2==1){
            t='1';
        }
        else{
            t='0';
        }
        k= t + k;
        x/=2;
    }
    return ('1'+k);
}

int main()
{
    int a;
    cin >> a;
    string b = qer(a);
    cout << count (b.begin(), b.end(), '1');

    return 0;
}
