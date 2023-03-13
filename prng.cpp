#include<iostream>
#include<ctime>
using namespace std;

int main()
{
	srand(time(NULL));
	int res[128];
	for (int i = 0; i < 128; i++)
	{
		res[i] = rand() % 2;
		cout << res[i];
	}
	return 0;
}


//11111110011111101110011010101001111110101110101000101100010110011110000111100111110100010011101010011010110000110111011001111110