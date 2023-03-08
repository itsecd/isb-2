#include <iostream>
#include <random>
#include <bitset>
using namespace std;
int main()
{
    //генератор Мерсенна-Твистера
    random_device rd;
    mt19937_64 generator(rd());
    
    bitset<128>  bits;
    for (int i = 0; i < 128; i++) {
        bits[i] = generator() & 1;
    }
    
    cout << "Random number: " <<  bits.to_string()  << std::endl;

    return 0;
}
//01111111111001001001101110110101010010110111001001000011100001100000001101111001110101100111110101111001100111110101100010110111