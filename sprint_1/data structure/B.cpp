#include <iostream>

using namespace std;

int main()
{
    int m;
    int n;
    int temp;
    
    cin >> m >> n;
    
    int matr [n][m];
    
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin>>temp;
            matr[j][i] = temp;
        }

    }
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cout<<matr[i][j]<<' ';
        }
        cout<<endl;
    }

    return 0;
}

