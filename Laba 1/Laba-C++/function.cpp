#include "function.h"

void Createfile(long long int n)
{
	ofstream A("Files/bin/A.bin", ios::binary);
	
	/* Seed */
	random_device rd;

	/* Random number generator */
	default_random_engine generator(rd());

	/* Distribution on which to apply the generator */
	uniform_int_distribution<unsigned long long int> distribution(1, 18000000000000000000);

	unsigned long long int number;
	for (long long int i = 0; i < n; i++)
	{
		number = distribution(generator);
		A.write((char*)&number, 8);
	}
	A.close();
}

// Перевірка, чи не пустий файл
bool Checkfile(ifstream& file)
{
	bool flag = true;
	if (file.peek() == ifstream::traits_type::eof())
	{
		flag = false;
	}
	return flag;
}

// Початок програми
void Start(long long int n)
{
	time_t t1 = time(NULL);
	Write_from_A_to_B(n); // Write from file A to files B
	time_t t2 = time(NULL);
	cout << "Write from A to B: " << t2 - t1 << "s" << endl;

	t1 = time(NULL);
	Write_from_B_to_C(n); // Write from files B to file C
	t2 = time(NULL);
	cout << "Write from B to C: " << t2 - t1 << "s" << endl;
	
	cout << "The answer has saved in the file C1.txt";
}


// Перестановка двох елементів
void swap(unsigned long long int* a, unsigned long long int* b)
{
	unsigned long long int t = *a;
	*a = *b;
	*b = t;
}

// Визначення індексу опорного елемента і порівняння елементів з опорним
long long int partition(unsigned long long int* arr, long long int low, long long int high)
{
	unsigned long long int number = arr[high]; // Опорний елемент
	long long int i = low - 1; // Індекс найлівішого елемента

	// Проходимо по заданому проміжку
	for (long long int j = low; j <= high - 1; j++)
	{
		// Якщо поточний елемент менший за опорний
		if (arr[j] < number)
		{
			// Збільшуємо індекс найлівішого елемента та міняємо його з поточним
			i++;
			swap(&arr[i], &arr[j]);
		}
	}

	swap(&arr[i + 1], &arr[high]); // Міняємо найлівіший елемент і опорний
	return (i + 1); // Повернаємо індекс опорного елемента
}

// Швидке сортування
void quickSort(unsigned long long int* arr, long long int low, long long int high)
{
	// Якщо low < high, то виконуємо:
	if (low < high) {
		// Знаходимо індекс опорного елемента
		long long int n = partition(arr, low, high);

		// Сортуємо елементи до і після опорного
		quickSort(arr, low, n - 1);
		quickSort(arr, n + 1, high);
	}
}

// Запис з файлу А у файли В
void Write_from_A_to_B(long long int n)
{
	ifstream A("Files/bin/A.bin", ios::binary);
	ofstream B[16] = { ofstream("Files/bin/B1.bin", ios::binary), ofstream("Files/bin/B2.bin", ios::binary), ofstream("Files/bin/B3.bin", ios::binary),
					   ofstream("Files/bin/B4.bin", ios::binary), ofstream("Files/bin/B5.bin", ios::binary), ofstream("Files/bin/B6.bin", ios::binary),
					   ofstream("Files/bin/B7.bin", ios::binary), ofstream("Files/bin/B8.bin", ios::binary), ofstream("Files/bin/B9.bin", ios::binary),
					   ofstream("Files/bin/B10.bin", ios::binary), ofstream("Files/bin/B11.bin", ios::binary), ofstream("Files/bin/B12.bin", ios::binary),
					   ofstream("Files/bin/B13.bin", ios::binary), ofstream("Files/bin/B14.bin", ios::binary),
					   ofstream("Files/bin/B15.bin", ios::binary), ofstream("Files/bin/B16.bin", ios::binary) };

	unsigned long long int number; // Зчитуване число
	long long int sizes[16]; // Кількість чисел у файлах

	// Знаходимо кількість чисел, які будуть у файлах В
	for (int i = 0; i < 16; i++)
	{
		sizes[i] = n / 16;
	}
	for (int i = 0; i < n % 16; i++)
	{
		sizes[i]++;
	}

	// Проходимо по файлах
	for (int i = 0; i < 16; i++)
	{
		// Якщо кількість чисел більша за 0
		if (sizes[i] > 0)
		{
			unsigned long long int* arr = new unsigned long long int[sizes[i]]; // Масив чисел
			A.read((char*)arr, 8 * sizes[i]); // Зчитуємо масив чисел
			quickSort(arr, 0, sizes[i] - 1); // Сортуємо масив
			B[i].write((char*)arr, 8 * sizes[i]); // Записуємо масив у файл B[i]
			delete[] arr; // Очищуємо пам'ять
		}
	}

	A.close();
	for (int i = 0; i < 16; i++)
	{
		B[i].close();
	}
}

// Запис з файлів В у файл С
void Write_from_B_to_C(long long int n)
{

	ifstream B[16] = { ifstream("Files/bin/B1.bin", ios::binary), ifstream("Files/bin/B2.bin", ios::binary), ifstream("Files/bin/B3.bin", ios::binary),
					   ifstream("Files/bin/B4.bin", ios::binary), ifstream("Files/bin/B5.bin", ios::binary), ifstream("Files/bin/B6.bin", ios::binary),
					   ifstream("Files/bin/B7.bin", ios::binary), ifstream("Files/bin/B8.bin", ios::binary),
					   ifstream("Files/bin/B9.bin", ios::binary), ifstream("Files/bin/B10.bin", ios::binary), ifstream("Files/bin/B11.bin", ios::binary),
					   ifstream("Files/bin/B12.bin", ios::binary), ifstream("Files/bin/B13.bin", ios::binary), ifstream("Files/bin/B14.bin", ios::binary),
					   ifstream("Files/bin/B15.bin", ios::binary), ifstream("Files/bin/B16.bin", ios::binary) };
	ofstream C("Files/bin/C1.bin", ios::binary);

	bool flag[16]; // Для перевірки, чи треба зчитати число з файлу В
	unsigned long long int number[16]; // Зчитані числа

	// Встановлюємо початкові значення
	for (int i = 0; i < 16; i++)
	{
		number[i] = ULLONG_MAX;
	}

	// Перевірка, чи не пусті файли В
	for (int i = 0; i < 16; i++)
	{
		flag[i] = Checkfile(B[i]);
	}

	// Проходимо по кількості чисел у файлах В
	for (long long int i = 0; i < n; i++)
	{
		// Проходимо по файлах В
		for (int j = 0; j < 16; j++)
		{
			// Якщо треба зчитати число з файлу В[j], то зчитуємо його
			if (flag[j])
			{
				// Якщо число не можна зчитати, то встановлюємо файл В[j] як прочитаний
				if (!B[j].read((char*)&number[j], 8))
				{
					flag[j] = false;
				}
			}
		}

		// Знаходимо мінімальне число
		unsigned long long int min = ULLONG_MAX;
		int index = -1;
		for (int k = 0; k < 16; k++)
		{
			if (min > number[k])
			{
				min = number[k];
				index = k;
			}
		}

		C.write((char*)&min, 8); // Записуємо мінімальне число у файл С

		// Проходимо по файлах та встанолюємо на них flag = false
		for (int k = 0; k < 16; k++)
		{
			if (k != index)
			{
				flag[k] = false;
			}
		}

		// Позначаємо файл, як той, з якого потрібно зчитати число і присвоюємо числу початкове значення
		flag[index] = true;
		number[index] = ULLONG_MAX;
	}

	for (int i = 0; i < 16; i++)
	{
		B[i].close();
	}
	C.close();
}

// Зчитуємо файл і виводимо його в консоль
void readfile(const char* path)
{
	unsigned long long int number;
	ifstream file(path, ios::binary);
	cout << "\nFile: " << path << endl;
	while (file.read((char*)&number, 8))
	{
		cout << "\n" << number;
	}
	cout << endl;
}