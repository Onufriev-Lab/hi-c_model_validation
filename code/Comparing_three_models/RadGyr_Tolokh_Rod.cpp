#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cmath>

class TadLocation {
public:
    int num;
    double x;
    double y;
    double z;

    void init(int _num, double _x, double _y, double _z) {
        num = _num;
        x = _x;
        y = _y;
        z = _z;
    }
};

class TTMatrix {
public:
    double distance(TadLocation a);
    void processData(const std::string& fileName);
};


double TTMatrix::distance(TadLocation a) {
    return sqrt((pow(a.x, 2) + pow(a.y, 2) + pow(a.z -12.74, 2)));
}

void TTMatrix::processData(const std::string& fileName) {
    std::ifstream inFile(fileName);
    if (!inFile) {
        std::cout << "Error opening file!" << std::endl;
        return;
    }

    std::vector<TadLocation> tadLocationVector;

    std::string line;
    while (getline(inFile, line)) {
        std::stringstream ss(line);
        double x, y, z;
        if (ss >> x >> y >> z) {
            TadLocation location;
            location.init(0, x, y, z); // You might need to assign a proper 'num' value
            tadLocationVector.push_back(location);
        }
    }

    double sigma = 0.0;
    for (size_t i = 0; i < 185; i++) {
        sigma += distance(tadLocationVector[i]) * distance(tadLocationVector[i]);
        
    }

    double finalRg = sqrt(sigma / 184);
    std::cout << "Rg: " << finalRg << std::endl;

    inFile.close();
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cout << "Usage: ./program_name input_file.csv" << std::endl;
        return 1;
    }

    std::string fileName = argv[1];

    TTMatrix ttMatrix;
    ttMatrix.processData(fileName);

    return 0;
}
