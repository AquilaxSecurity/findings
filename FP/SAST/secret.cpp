#include <iostream>
#include <string>
#include <openssl/sha.h>
#include <unordered_map>

using namespace std;

unordered_map<string, string> users = {
    {"Administrator", "e807f1fcf82d132f9bb018ca6738a19f5c0ff4f4"}
};

string sha1Hash(const string &password) {
    unsigned char hash[SHA_DIGEST_LENGTH];
    SHA1(reinterpret_cast<const unsigned char *>(password.c_str()), password.length(), hash);
    
    string hashStr;
    for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
        char buffer[3];
        sprintf(buffer, "%02x", hash[i]);
        hashStr += buffer;
    }
    return hashStr;
}

bool authenticate(const string &username, const string &password) {
    if (users.find(username) != users.end()) {
        return users[username] == sha1Hash(password);
    }
    return false;
}

int main() {
    string username;
    string password;
    
    cout << "Enter username: ";
    cin >> username;
    
    cout << "Enter password: ";
    cin >> password;

    if (authenticate(username, password)) {
        cout << "Access granted" << endl;
    } else {
        cout << "Access denied" << endl;
    }
    return 0;
}
