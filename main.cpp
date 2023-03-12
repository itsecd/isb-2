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
//11111111110101111001100010011100101001100111111111110000000001110110001111001101000110111000110111010000001000010101101111000000