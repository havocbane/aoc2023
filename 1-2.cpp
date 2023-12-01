// g++ -Wall -std=c++11 -o 1-2.x 1-2.cpp

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

const std::string ONE = "one";
const std::string TWO = "two";
const std::string THREE = "three";
const std::string FOUR = "four";
const std::string FIVE = "five";
const std::string SIX = "six";
const std::string SEVEN = "seven";
const std::string EIGHT = "eight";
const std::string NINE = "nine";

std::string convert(std::string val)
{
    if (val.compare(ONE) == 0)
        return "1";
    if (val.compare(TWO) == 0)
        return "2";
    if (val.compare(THREE) == 0)
        return "3";
    if (val.compare(FOUR) == 0)
        return "4";
    if (val.compare(FIVE) == 0)
        return "5";
    if (val.compare(SIX) == 0)
        return "6";
    if (val.compare(SEVEN) == 0)
        return "7";
    if (val.compare(EIGHT) == 0)
        return "8";
    if (val.compare(NINE) == 0)
        return "9";
    return val;
}

int main(int argc, char *argv[])
{
    // std::string filename = "1-2.test.txt";
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

        size_t min = line.length();
        size_t max = 0;

        std::vector<std::string> v{ONE, "1", TWO, "2", THREE, "3", FOUR, "4", FIVE, "5", SIX, "6", SEVEN, "7", EIGHT, "8", NINE, "9"};

        for (std::vector<std::string>::const_iterator it = v.cbegin(); it != v.cend(); it++)
        {
            std::string::size_type n = line.find(*it);
            if (n != std::string::npos && n < min)
            {
                min = n;
                first = convert(*it);
            }
            n = line.rfind(*it);
            if (n != std::string::npos && n >= max)
            {
                max = n;
                last = convert(*it);
            }
        }

        std::string number = first + last;
        std::cout << "; value = " << number << std::endl;
        int combined = std::stoul(number);
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
