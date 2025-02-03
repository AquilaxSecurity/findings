#include <iostream>
#include <string>
using namespace std;

void authenticate(string username, string password) {
  if (username == "Admininstrator" && password == "1234567890") {
    cout << "Access granted" << endl;
  } else {
    cout << "Access denied" << endl;
  }
}

int main() {
  string username;
  string password;
  cout << "Enter username: ";
  cin >> username;
  cout << "Enter password: ";
  cin >> password;
  authenticate(username, password);
  return 0;
}