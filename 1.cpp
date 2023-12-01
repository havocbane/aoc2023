// g++ -Wall -o 1.x 1.cpp

#include <iostream>
#include <fstream>
#include <string>

int main(int argc, char *argv[])
{
    // std::string filename = "1.test.txt";
    std::string filename = "1.txt";

    std::fstream fd(filename, std::ios::in);
    if (!fd.is_open())
    {
        std::cerr << "Failed to open file " << filename << std::endl;
        return 1;
    }
    std::cout << "Opened " << filename << " successfully" << std::endl
              << std::endl;

    int sum = 0;
    for (std::string line; std::getline(fd, line);)
    {
        std::string first, last = "";
        std::cout << line;
        for (std::string::const_iterator it = line.cbegin(); it != line.cend(); it++)
        {
            if (std::isdigit(*it))
            {
                if (first.empty())
                {
                    first = *it;
                }
                last = *it;
            }
        }
        int combined = std::stoul(first + last);
        std::cout << "; value = " << combined << std::endl;
        sum += combined;
    }
    std::cout << std::endl
              << "Sum = " << sum << std::endl
              << std::endl;

    fd.close();
    std::cout << "Closed " << filename << std::endl;
    std::cout << "Done" << std::endl;
    return 0;
}
