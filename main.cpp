#include <iostream>
#include <random>
#include <bitset>
using namespace std;
int main()
{
    //генератор Мерсенна-Твистера
    random_device rd;
    mt19937_64 gen(rd());

    bitset<128> random_number(gen());

    cout << "Random number: " << random_number << std::endl;

    return 0;
}
//00000000000000000000000000000000000000000000000000000000000000000000000111000010011010110000111110010111000100100110100011100011