#include "Func.h"

// Генерація файлу
void createfile()
{
	ofstream A("Files/txt/A.txt");

	/* Seed */
	random_device rd;

	/* Random number generator */
	default_random_engine generator(rd());

	/* Distribution on which to apply the generator */
	uniform_int_distribution<unsigned int> distribution(1, 4000000000);

	for (int i = 0; i < 1000000; i++)
	{
		A << " " << distribution(generator);
	}
	A.close();
}

// Перевірка, чи не пустий файл
bool checkfile(ifstream& file)
{
	bool flag = true;
	if (file.peek() == ifstream::traits_type::eof())
	{
		flag = false;
	}
	return flag;
}

// Початок програми
void start()
{
	// Paths to the files
	filesystem::path a("Files/txt/A.txt");
	filesystem::path b("Files/txt/B1.txt");
	filesystem::path c("Files/txt/C1.txt");

	unsigned long long int size_a = filesystem::file_size(a); // The size of the file A.txt

	bool flag = true; // To changing files

	int t1 = time(NULL);
	write_from_A_to_B(); // Write from file A to files B
	int t2 = time(NULL);
	cout << "Write from A to B: " << t2 - t1 << "s" << endl;

	// While file A != B1 and A != C
	while (size_a != filesystem::file_size(b) && size_a != filesystem::file_size(c))
	{
		if (flag)
		{
			t1 = time(NULL);
			write_from_files1_to_files2("B", "C");
			t2 = time(NULL);
			cout << "Write from B to C: " << t2 - t1 << "s" << endl;
		}
		else
		{
			t1 = time(NULL);
			write_from_files1_to_files2("C", "B");
			t2 = time(NULL);
			cout << "Write from C to B: " << t2 - t1 << "s" << endl;
		}
		flag = !flag;
	}

	if (size_a == filesystem::file_size(b))
	{
		cout << "The answer has saved in the file B1.txt";
	}
	else
	{
		cout << "The answer has saved in the file C1.txt";
	}
}

// Запис серій з файлу А у файли В1-В8
void write_from_A_to_B()
{
	ifstream A("Files/txt/A.txt");
	ofstream B[8] = { ofstream("Files/txt/B1.txt"), ofstream("Files/txt/B2.txt"), ofstream("Files/txt/B3.txt"),
					  ofstream("Files/txt/B4.txt"), ofstream("Files/txt/B5.txt"), ofstream("Files/txt/B6.txt"),
					  ofstream("Files/txt/B7.txt"), ofstream("Files/txt/B8.txt") };

	unsigned int first = 0, second; // The numbers
	unsigned int i = 0; // The index of the file

	// Read the numbers from the file A.txt and write these ones to the files B1-B8.txt
	while (!A.eof())
	{
		A >> second;
		if (first > second)
		{
			i++;
		}
		B[i % 8] << " " << second;
		first = second;
	}

	A.close();
	for (int i = 0; i < 8; i++)
	{
		B[i].close();
	}
}

// Запис з файлів В у файли С (і навпаки)
void write_from_files1_to_files2(string file1, string file2)
{
	ifstream files1[8] = { ifstream("Files/txt/" + file1 + "1.txt"), ifstream("Files/txt/" + file1 + "2.txt"), ifstream("Files/txt/" + file1 + "3.txt"),
						   ifstream("Files/txt/" + file1 + "4.txt"), ifstream("Files/txt/" + file1 + "5.txt"), ifstream("Files/txt/" + file1 + "6.txt"),
						   ifstream("Files/txt/" + file1 + "7.txt"), ifstream("Files/txt/" + file1 + "8.txt") };
	ofstream files2[8] = { ofstream("Files/txt/" + file2 + "1.txt"), ofstream("Files/txt/" + file2 + "2.txt"), ofstream("Files/txt/" + file2 + "3.txt"),
						   ofstream("Files/txt/" + file2 + "4.txt"), ofstream("Files/txt/" + file2 + "5.txt"), ofstream("Files/txt/" + file2 + "6.txt"),
						   ofstream("Files/txt/" + file2 + "7.txt"), ofstream("Files/txt/" + file2 + "8.txt") };

	int n = 0; // Індекс файлу files2, в який треба записати серію
	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 }, // Попереднє число у файлі files1
		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX }; // Наступне число у файлі files1
	bool flags[8]; // Закінчення серії у файлі files1
	bool flags_not_empty[8]; // Перевірка на пустий файл files1

	// Перевірка, які файли files1 пусті
	for (int i = 0; i < 8; i++)
	{
		flags_not_empty[i] = checkfile(files1[i]);
		flags[i] = flags_not_empty[i];
	}

	// Прохід по файлах files1, поки хоча б в одному з них є числа
	while (flags[0] || flags[1] || flags[2] || flags[3] || flags[4] || flags[5] || flags[6] || flags[7])
	{
		bool flag = true; // Для завершення наступного циклу

		// Проходимо по файлах files1 та записуємо серію у файл files2[n % 8]
		while (flag)
		{
			// Проходимо по файлах files1 та зчитуємо з них по одному числу(якщо потрібно)
			for (int i = 0; i < 8; i++)
			{
				// Якщо потрібно зчитати число, то зчитуємо
				if (flags[i])
				{
					int pointer = files1[i].tellg(); // Запам'ятовуємо позицію зчитування
					files1[i] >> second[i];

					// Якщо кінець серії, то ставимо початкові значення для змінних і не більше його не зчитуємо до закінчення внутрішнього циклу while
					if (first[i] > second[i])
					{
						files1[i].seekg(pointer, ios::beg);
						flags[i] = false;
						second[i] = UINT32_MAX;
					}
				}
			}

			// Знаходимо мінімальне число та запам'ятовуємо індекс файлу
			unsigned int min = UINT32_MAX;
			int index = -1;
			for (int i = 0; i < 8; i++)
			{
				if (min > second[i])
				{
					min = second[i];
					index = i;
				}
			}

			// Якщо знайшли мінімальне число, то записуємо його у файл files2, інакше виходимо з внутрішнього циклу while
			if (index != -1)
			{
				int index_file2 = n % 8; // Індекс файл, у який треба записати число
				files2[index_file2] << " " << min;

				// Позначаємо файли files1, з яких не треба зчитувати
				for (int i = 0; i < 8; i++)
				{
					if (i != index)
					{
						flags[i] = false;
					}
				}

				// Позначаємо файл files1, з якого треба зчитати число на наступній ітерації
				flags[index] = true;
				first[index] = second[index];
				second[index] = UINT32_MAX;
			}
			else
			{
				// Виходимо з внутрішнього циклу while
				flag = false;

				// Знаходимо файли files1, які уже повністю зчитані або пусті і далі пропускаємо ці файли
				for (int i = 0; i < 8; i++)
				{
					first[i] = 0;
					if (!flags_not_empty[i] || files1[i].eof())
					{
						flags[i] = false;
					}
					else
					{
						flags[i] = true;
					}
				}
			}
		}
		n++; // Збільшуємо індекс файлу
	}

	for (int i = 0; i < 8; i++)
	{
		files1[i].close();
		files2[i].close();
	}
}