//////////////////////////////////////////////////////////////////////////////////
// TAD-TAD contact matrix generator						//
// Use the Makefile to compile!							//
// To run on "something.vtf", "rad_list" and tolerance 0.1 use:  		//
// ./tad_tad /path/to/something.vtf /path/to/rad_list  tolerance   skip#frames	//
// Output is dumped to stdout, pipe into the file of your choice.		//
//////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <iomanip>
#include <fstream>
#include <boost/algorithm/string.hpp>
#include <vector>
#include <math.h>
#include <map>
#include <algorithm>

/////////////
// Classes //
/////////////

/*
The TAD Location class represents a TAD's location in a snapshot. It contains the TAD's ID and location in xyz space. 
*/
class TadLocation
{
public:
    int num;
    double x;
    double y;
    double z;
    /*  Constructor for TAD Location class */ 
    void init(int _num, double _x, double _y, double _z)
    {
        num = _num; //Which TAD the location is associated with
        x = _x; //The x location
        y = _y; //The y location
        z = _z; //The z location
    }
};

/*
TAD TAD Interaction Matrix
*/
class TTMatrix
{
    std::vector<double> tadVector; //Vector of all the TADs, used to determine radius.
    std::map<int,double> tadMap; //Map of tads to their radius. I do not use unordered_map because it's not supported by GCC 4.4. Thus it's O(log(n)) for all regular operations.
    std::vector<std::vector<double> > finalMat;
    std::vector<std::vector<double> > finalDis;
    std::vector<double> genomicDis;
    //std::vector<double> mss = {664950355, 232228355, 101036355, 284863855, 1243676355, 369239355, 66651355, 166367855, 48400855, 93894855, 391457355, 515507855, 576871855, 111351855, 274548355, 126957355, 179857355, 280367355, 372148855, 131453855, 282747855, 1034192355, 107913355, 812541355, 502547355, 701186855, 85695355, 359452855, 573962355, 549892855, 66651355, 343847355, 595386855, 458111355, 543015855, 348608355, 509424355, 139917855, 189908355, 71147855, 297295355, 111351855, 306552855, 500166855, 203926855, 121931855, 71676855, 391721855, 351782355, 109764855, 120080355, 162400355, 190172855, 365536355, 223499855, 34911355, 464194855, 1036837355, 164516355, 403624355, 104210355, 93101355, 236460355, 318455355, 578987855, 109764855, 207365355, 151026855, 43375355, 231170355, 116377355, 483767855, 481651855, 56600355, 128015355, 335383355, 712560355, 65064355, 285657355, 1059319855, 329035355, 657544355, 49987855, 706741355, 56335855, 52368355, 975208855, 450176355, 78289355, 37820855, 225086855, 438273855, 157639355, 39672355, 54219855, 201017355, 164251855, 417907355, 1132321855, 297030855, 96010855, 118493355, 275341855, 406798355, 783446355, 121931855, 78289355, 40465855, 90191855, 95481855, 39143355, 576871855, 51574855, 304701355, 111087355, 1106400855, 1002187855, 650931855, 39672355, 307081855, 335647855, 146265855, 404153355, 74850855, 340408855, 384580355, 277457855, 278251355, 482445355, 50516855, 141240355, 122989855, 437744855, 35440355, 363420355, 71147855, 263439355, 234873355, 305230355, 87017855, 246246855, 171657855, 67709355, 287244355, 78289355, 471600855, 46549355, 856712855, 178799355, 41259355, 74321855, 38349855, 184353855, 215829355, 885278855, 217151855, 123254355, 400185855, 309197855, 54484355, 324803355, 167161355, 151026855, 997955855, 532171355, 46549355, 548041355, 113203355, 49194355, 227202855, 241485855, 534022855, 43639855, 505456855, 314487855, 43639855, 617075855, 712295855, 70089855, 708063855, 133305355, 605966855, 978118355, 122989855};
    
    //std::vector<double> finalDis;
public:
    void init() {};
    int timeStepCount = 0; //The number of timestep within the vtf
    int startFrame;
    int endFrame;
    double finalRg;
    bool contact(TadLocation a, TadLocation b, double tolerance);
    double distance(TadLocation a); 
    void printMatrix();
    void printMatrix2();
    void parseVTF(std::ifstream& inFile, std::ifstream& radFile, double tolerance);
    void parseRadius(std::ifstream& radFile);
};


///////////////
// Functions //
///////////////

/*
Determines if two TADs are in contact with each other. The passed TAD locations are uses to determine the distance between the two TADs.
We then grab the radius from the TAD vector. 
*/
bool TTMatrix::contact(TadLocation a, TadLocation b, double tolerance)
{
    double dist = sqrt(pow(b.x - a.x, 2)+pow(b.y - a.y, 2)+pow(b.z - a.z, 2)); //Distance formula
    double rad1 = tadVector[a.num]; //Get radius of tad a
    double rad2 = tadVector[b.num]; //Get radius of tad b
    if (dist < rad1+rad2+tolerance) {
        return true;
    }
    return false;
}



double TTMatrix::distance(TadLocation a, TadLocation b)
{
    double dist =  (pow(a.x, b.x)+pow(a.y, b.y)+pow(a.z, b.z)); //Distance formula
    //std::cout <<  " a.x " << a.x  <<  " a.y " << a.y  <<  " a.z " << a.z << " dist " << dist << " \n  ";
    return dist;
}


/*
Prints the heatmap matrix, should be piped to file to plot upon using gnuplot or etc.
*/
void TTMatrix::printMatrix()
{
    //C++11 ver
    // for (auto& row:finalMat) {
    // 	for(auto& col:row) {
    // 	    if (&col == &row.front()) {
    // 		std::cout << col;
    // 		continue;
    // 	    }
    // 	    std::cout << ", " << col; //Print out element in each row
    // 	}
    // 	std::cout << std::endl;
    // }
    // legacy version
    std::vector<int> nonTads{225,226,227,662,663,664,972,973,1177,1178,1179,1180};
    for (size_t i = 0; i != finalMat.size(); ++i) {
        if (std::binary_search(nonTads.begin(), nonTads.end(), i)) {
            continue;
        }
        for(size_t j = 0; j != finalMat[i].size(); j++) {
            if (std::binary_search(nonTads.begin(), nonTads.end(), j)) {
                continue;
            }
            if (j == 0) {
                std::cout << finalMat[i][j];
                continue;
            }
            //std::cout << ", " << finalMat[i][j]; //Print out element in each row
            std::cout << ", " << finalDis[i][j];
        }
        std::cout << std::endl;
    }
}

void TTMatrix::printMatrix2()
{
    int gsize = 184;//TadCount;//change it for X chomosome
    //for (size_t i = 1; i != gsize; ++i) {
    for (size_t i = 0; i != gsize - 1; ++i) {
        //std::cout << ", " << genomicDis[i]/((gsize-i)*(endFrame - startFrame + 1)); //Print out element in each row
        //std::cout <<  i*118.02 << " " <<  genomicDis[i]/((gsize-i)*(endFrame - startFrame + 1))<< "\n";
        // std::cout <<  i*118.02 << " " <<  genomicDis[i]/((gsize-i-1)*(endFrame - startFrame + 1))<< "\n";
        std::cout << ", " << genomicDis[i]/((gsize-i)*(endFrame - startFrame +1));
    }
}

void TTMatrix::parseRadius(std::ifstream& radiusFile) {
    for (std::string line; getline(radiusFile, line);) {
        std::vector<std::string> sLine;
        boost::split(sLine, line, boost::is_any_of(" \t"));
        if (sLine[0] == "" or sLine[0] == "bID") { //skip empty lines and the header
            continue;
        }
        int beadID = std::stoi(sLine[0]);
        double radius = std::stod(sLine[1]);
        tadVector[beadID] = radius;
    }
}

/*
Parses through the .vtf provided and ructs a matrix of size n x n where n is the number of TADS.
*/
void TTMatrix::parseVTF(std::ifstream& inFile, std::ifstream& radFile, double tolerance)
{
    std::string line; //line in file
    //Parse vtf and load all the TADs and their radii into tadVector
    for (line; getline(inFile,line);) //Iterate over lines in file
    {
        std::vector<std::string> sLine; //split line
        boost::split(sLine, line, boost::is_any_of(" ")); //split on spaces
        /*
    sLine is in format of atom tadnumValue:tadnumValue radius radiusValue name nameValue type typeValue q qValue
    Example: atom 676,839 radius 0.187813 name X type 38 q 2.0
    */
        if (!sLine[0].compare("pbc")) { //we want to skip the first line (pbc = periodic boundary conditions)
            continue;
        }
        //Let's store the atoms and their radii

        //Check if we are done parsing atoms, a split size of less than 8 means we have parsed through all the TADs and their radii in the vtf.
        if (sLine.size() < 8) {
            break;
        }
        else {
            std::string tadGrouping = sLine[1];
            std::vector<std::string> tads; //will split up tadnumValue into seperate TADs to be parsed
            boost::split(tads,tadGrouping,boost::is_any_of(","));
            //Go through each tad found within the line we are parsing
            for (size_t i = 0; i < tads.size(); i++)
            {
                //Two cases, when the tad is just singular like [483] vs when the tad is a range like [483:489]
                std::string currentTad = tads[i];
                size_t colonIndex = currentTad.find(':'); //Colon is the delimiter that lets us determine which case we are looking at
                if (colonIndex != std::string::npos) {
                    //A range of tads, not just a single tad!
                    int start     = std::atoi(currentTad.substr(0,colonIndex).c_str());
                    int end       = std::atoi(currentTad.substr(colonIndex+1).c_str());
                    double radius = std::stod(sLine[3]); //Precompute as it will be the same for the entire range
                    for (int i = start; i <= end; i++) {
                        tadMap[i] = radius;
                    }
                }
                else {
                    //Just a single tad
                    tadMap[std::atoi(currentTad.c_str())] = std::stod(sLine[3]);
                }
            }
        }
    }

    std::size_t tadCount = tadMap.size();
    tadVector.reserve(tadCount); //preallocate

    //convert tadMap to array so it is faster (by a large margin!)
    for (auto it = tadMap.begin(); it != tadMap.end(); ++it) {
        tadVector.emplace_back(it->second);
    }
    parseRadius(radFile); //replace radius
    
    std::vector<TadLocation> tadLocationVector; //Vector containing the xyz location of TADs in current snapshot
    finalMat.resize(tadCount, std::vector<double>(tadCount));
    finalDis.resize(tadCount, std::vector<double>(tadCount));
    genomicDis.resize(tadCount);
    //finalDis.resize(tadCount*(tadCount-1)/2);
    
    for (std::string line; getline(inFile,line);) {
        if (line.find("timestep") == std::string::npos) {
            //Keep going to skip over atom and bond information we don't need
            continue;
        }
        //At a snapshot segment in .vtf
        timeStepCount++;
        if (timeStepCount < startFrame) {
            continue;
        }
        if (timeStepCount > endFrame) {
            continue;
        }
        
        //Go over a snapshot and populate the tadLocationVector
        for (size_t i = 0; i < tadCount; i++) {
            std::string tempLine;
            getline(inFile,tempLine);
            std::vector<std::string> sLine;
            boost::split(sLine,tempLine,boost::is_any_of(" "));
            TadLocation tempTadLoc;
            tempTadLoc.init(i,std::stod(sLine[0]),std::stod(sLine[1]), std::stod(sLine[2]));
            tadLocationVector.push_back(tempTadLoc);
        }
        
        //Parse the tadLocationVector
        
        //for (size_t i = 0; i < tadCount; i++) {//uncomment for all chomosomes
        //for (size_t j = i; j < tadCount; j++) {//uncomment for all chromosomes
        double sumX = 0.0;
        double sumY = 0.0;
        double sumZ = 0.0;
        double sigma = 0;
        for (size_t i = 993; i < 1177; i++) {
            //for (size_t i = 993; i < 995; i++) {
            
            sumX += tadLocationVector[i].x;
            sumY += tadLocationVector[i].y;
            sumZ += tadLocationVector[i].z;
            //disCount++;
        
        }
        double avgX = sumX /184;
        double avgY = sumY /184;
        double avgZ = sumZ /184;
        
        for (size_t i = 993; i < 1177; i++) {
        
        sigma += TTMatrix::distance(tadLocationVector[i])* distance(tadLocationVector[i]);
        finalRg =  sqrt((sigma)/184);
        std::cout << "Average X: " << avgX << ", Average Y: " << avgY << ", Average Z: " << avgZ << std::endl;
       
        std::cout <<  " timeStepCount " << timeStepCount << " Rg " << finalRg << " \n  ";
        
        tadLocationVector.clear(); //clear every iteration and reuse (space allocated is not destroyed)
    }

}

int main(int argc, char* argv[])
{
    int c;
    std::string fileName = argv[1];
    std::string radiusFileName = argv[2];
    double tolerance = std::stod(argv[3]);
    // std::string line; //input line
    std::ifstream inFile; //input file
    inFile.open(fileName); //vtf file to parse
    std::ifstream radiusFile;
    radiusFile.open(radiusFileName);
    //Error checking
    if (!inFile) {
        std::cout << "Can't open the vtf!";
        exit(1);
    }
    if (!radiusFile) {
        std::cout << "Can't open the radius file!";
        exit(1);
    }
    
    TTMatrix ttMatrix;
    ttMatrix.startFrame = std::stoi(argv[4]);
    ttMatrix.endFrame = std::stoi(argv[5]);
    ttMatrix.parseVTF(inFile, radiusFile, tolerance);
    //ttMatrix.printMatrix2(); //prints to stdout, need to pipe to a file to make use of output
    //ttMatrix.printMatrix2(); //prints to stdout, need to pipe to a file to make use of output
}
