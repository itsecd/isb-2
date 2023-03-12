#include <iostream>
#include <random>
#include <ctime>

int main()
{
	//вихрь Мерсенна со случайным начальным значением на основе часов
	std::mt19937 mersenne{ static_cast<std::mt19937::result_type>(std::time(nullptr)) };
	std::uniform_int_distribution<> die{ 0, 1 };
	for (int count{ 1 }; count <= 128; ++count) std::cout << die(mersenne);
	return 0;
}
//11110010110111000101111001000101101001101001000100100001001011101011011100111011110110000001000111100110000111111001010010001110