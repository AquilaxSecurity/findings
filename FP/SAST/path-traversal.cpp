#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

bool isValidPath(const std::string& filename) {
 
    if (filename.find("..") != std::string::npos) {
        std::cerr << "Error: Invalid file path!" << std::endl;
        return false;
    }

    std::filesystem::path safeDir = "safe_files/";
    std::filesystem::path filePath = safeDir / filename;

    if (!std::filesystem::exists(filePath) || !std::filesystem::is_regular_file(filePath)) {
        std::cerr << "Error: File does not exist or is not allowed!" << std::endl;
        return false;
    }

    return true;
}

std::string readFile(const std::string& filename) {
    if (!isValidPath(filename)) {
        return "Error: Invalid request.";
    }

    std::ifstream file("safe_files/" + filename);
    if (!file) {
        return "Error: Could not open file.";
    }

    std::string contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return contents;
}

int main() {
    std::string userInput;
    std::cout << "Enter the file name (inside 'safe_files/' directory): ";
    std::cin >> userInput;

    std::cout << readFile(userInput) << std::endl;
    return 0;
}
