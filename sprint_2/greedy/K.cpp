#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
  int a;
  int p;
  vector <int> b;
  int temp;
  int res=0;
  cin>>a;
  cin>>p;
  for(int i=0; i<a; i++){
    cin>>temp;
    b.push_back(temp);
  }
  sort(b.begin(),b.end());
  for(int i=0; i<a; i++){
    if(p-b[i]>=0){
      res++;
      p=p-b[i];
    }
  }
  cout<<res;
}
