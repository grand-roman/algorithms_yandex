#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int kol_c;
    vector <int> children;
    int kol_p;
    vector <int> cook;
    int temp;
    
    cin >> kol_c;
    for(int i = 0; i<kol_c; i++){
        cin>>temp;
        children.push_back(temp);
    }

    cin >> kol_p;
    for(int i = 0; i<kol_p; i++){
        cin>>temp;
        cook.push_back(temp);
    }
    sort(children.begin(),children.end());
    reverse(children.begin(),children.end());
    sort(cook.begin(),cook.end());
    reverse(cook.begin(),cook.end());
    int k = 0;
    temp = 0;
    for(int i = 0; i<kol_c; i++){
        for(int j = temp; j<kol_p; j++){
            if(cook[j]>=children[i]){
                k++;
                temp = j+1;
                break;
            }
        }
    }
    cout<<k;

    return 0;
}

