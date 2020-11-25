#include <iostream>
#include <string>

using namespace std;

string func(){
    int i = 0;
    int j = 0;
    string s;
    string t;
    
    getline(cin,s);
    getline(cin,t);

    if (s.size() == 0)
        return "True";

    while (j != t.size()){
        if (s[i] == t[j]){
            i++;
        }
    
        j++;

        if (i == s.size())
          return "True";
    }
    return "False";
}

int main()
{
    cout<<func();

    return 0;
}

