#include <iostream>
 
int main(int argc, char *argv[])
{
 
    srand(time(0));
    int x = std::rand() % 12347;
 
    int N = 128;
    bool b;
 
 
    for(int i = 0; i < N; i++)
    {
        x = (x * 222 + 4) % 12347;
        b = x % 2;
        std::cout << b;
    }
 
    return 0;
}

//11111110110011100100110000001100000001010101011101100101010110100000000100010011010000100001110001010110110101000111101010100111
