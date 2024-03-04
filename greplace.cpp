#include <iostream>
#include <fstream>
#include <filesystem>
#include <string>
#include <regex>

namespace fs = std::filesystem;

void replaceInFile(const std::string& filePath, const std::string& searchText, const std::string& replaceText) {
    std::ifstream inputFile(filePath);
    std::string fileContents((std::istreambuf_iterator<char>(inputFile)), std::istreambuf_iterator<char>());
    inputFile.close();

    size_t pos = fileContents.find(searchText);
    while (pos != std::string::npos) {
        fileContents.replace(pos, searchText.length(), replaceText);
        pos = fileContents.find(searchText, pos + replaceText.length());
    }

    std::ofstream outputFile(filePath);
    outputFile << fileContents;
    outputFile.close();
}

void processFiles(const std::string& pathPattern, const std::string& searchText, const std::string& replaceText, bool includeSubdirectories) {
    std::regex filePattern(pathPattern);

    if (includeSubdirectories) {
        for (const auto& entry : fs::recursive_directory_iterator(fs::path("."))) {
            if (entry.is_regular_file() && std::regex_match(entry.path().filename().string(), filePattern)) {
                replaceInFile(entry.path().string(), searchText, replaceText);
                std::cout << "Processed file: " << entry.path() << std::endl;
            }
        }
    } else {
        for (const auto& entry : fs::directory_iterator(fs::path("."))) {
            if (entry.is_regular_file() && std::regex_match(entry.path().filename().string(), filePattern)) {
                replaceInFile(entry.path().string(), searchText, replaceText);
                std::cout << "Processed file: " << entry.path() << std::endl;
            }
        }
    }
}

int main(int argc, char* argv[]) {
    if (argc < 4 || argc > 5) {
        std::cerr << "Usage: " << argv[0] << " [-s] <path-pattern> <search-text> <replace-text>" << std::endl;
        return 1;
    }

    bool includeSubdirectories = false;
    int argIndex = 1;

    // Check if the first argument is "-s"
    if (argc == 5 && std::string(argv[1]) == "-s") {
        includeSubdirectories = true;
        argIndex = 2;
    }

    std::string pathPattern = argv[argIndex];
    std::string searchText = argv[argIndex + 1];
    std::string replaceText = argv[argIndex + 2];

    try {
        processFiles(pathPattern, searchText, replaceText, includeSubdirectories);
        std::cout << "Replacement complete." << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
