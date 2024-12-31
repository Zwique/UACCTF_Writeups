#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream infile("output.txt");
    if (!infile) {
        cerr << "Error opening file for reading!" << endl;
        return 1;
    }

    string encrypted;
    if (!getline(infile, encrypted)) { // Read the encrypted line and check for failure
        cerr << "Error reading from file!" << endl;
        infile.close();
        return 1;
    }

    char xorkey = 'X';
    for (size_t i = 0; i < encrypted.size(); ++i) {
        encrypted[i] = encrypted[i] ^ xorkey; // XOR again with the key to decrypt
    }

    cout << "Decrypted flag: " << encrypted << endl;

    infile.close();
    return 0;
}