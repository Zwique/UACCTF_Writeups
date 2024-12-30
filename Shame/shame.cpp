#include <iostream>
#include <cstring>
#include <fstream> 
using namespace std;

void vuln(char flag[], char key, ofstream &outfile) {
    int len = strlen(flag); 

    for (int i = 0; i < len; i++) {
        flag[i] = flag[i] ^ key;
    }

    for (int i = 0; i < len; i++) {  
        outfile << flag[i];
    }
    outfile << endl;
}

int main() {
    char flag[] = "Find ME";
    char xorkey = 'X';
    
    ofstream outfile("output.txt");
    if (!outfile) {
        cerr << "Error opening file for writing!" << endl;
        return 1;
    }

    vuln(flag, xorkey, outfile);

    outfile.close();
    
    return 0;
}