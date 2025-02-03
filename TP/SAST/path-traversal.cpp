#include <iostream>
#include <string>

std::string readFile(const std::string& filename) {
    std::ifstream file(filename);
    std::string contents((std::istreambuf_iterator<char>(file)), (std::istreambuf_iterator<char>()));
    return contents;
}

int main() {
    std::string userInput;
    std::cout << "Enter the file name: ";
    std::cin >> userInput;
    std::cout << readFile(userInput) << std::endl;
    return 0;
}