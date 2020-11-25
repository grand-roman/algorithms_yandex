#include <iostream>

using namespace std;

int func(int x){
    if (x==0 || x==1){
        return 1;
    }
    return func(x-1)+func(x-2);
}

int main()
{
    int a;
    cin>>a;
    cout<<func(a);

    return 0;
}
