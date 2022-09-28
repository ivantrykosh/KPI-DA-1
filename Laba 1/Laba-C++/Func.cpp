#include "Func.h"

void createfile()
{
	ofstream A("Files/A.txt");

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

//void start()
//{
//	write_from_a_to_b();
//
//	bool flag = write_from_b_to_c();
//	bool currentfiles = true;
//
//	while (flag)
//	{
//		if (currentfiles)
//		{
//			flag = write_from_c_to_b();
//		}
//		else
//		{
//			flag = write_from_b_to_c();
//		}
//		currentfiles = !currentfiles;
//	}
//
//	if (currentfiles)
//	{
//		cout << "The answer save in the file B1";
//	}
//	else
//	{
//		cout << "The answer save in the file C1";
//	}
//}

//void write_from_a_to_b()
//{
//	int first, second;
//	int i = 0;
//	bool flag = true;
//	ifstream A("Files/A.txt");
//	ofstream B1("Files/B1.txt");
//	ofstream B2("Files/B2.txt");
//	ofstream B3("Files/B3.txt");
//	ofstream B4("Files/B4.txt");
//	ofstream B5("Files/B5.txt");
//	ofstream B6("Files/B6.txt");
//	ofstream B7("Files/B7.txt");
//	ofstream B8("Files/B8.txt");
//	int count = 0;
//	int c1 = 0, c2 = 0, c3 = 0, c4 = 0, c5 = 0, c6 = 0, c7 = 0, c8 = 0;
//	while (!A.eof())		 
//	{						 
//		A >> second;
//		if (flag)
//		{
//			B1 << second;
//			flag = false;
//			count++;
//			c1++;
//		}
//		else
//		{
//			if (first > second)
//			{
//				i++;
//			}
//			switch (i % 8)
//			{
//			case 0: if (c1 != 0) { B1 << " "; } B1 << second; c1++; break;
//			case 1: if (c2 != 0) { B2 << " "; } B2 << second; c2++; break;
//			case 2: if (c3 != 0) { B3 << " "; } B3 << second; c3++; break;
//			case 3: if (c4 != 0) { B4 << " "; } B4 << second; c4++; break;
//			case 4: if (c5 != 0) { B5 << " "; } B5 << second; c5++; break;
//			case 5: if (c6 != 0) { B6 << " "; } B6 << second; c6++; break;
//			case 6: if (c7 != 0) { B7 << " "; } B7 << second; c7++; break;
//			case 7: if (c8 != 0) { B8 << " "; } B8 << second; c8++; break;
//			}
//			count++;
//		}
//		first = second;
//	}
//	//cout << "From a to b: " << c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 << " = " << count;
//	A.close();
//	B1.close();
//	B2.close();
//	B3.close();
//	B4.close();
//	B5.close();
//	B6.close();
//	B7.close();
//	B8.close();
//}

//bool write_from_b_to_c()
//{
//	ifstream B1("Files/B1.txt");
//	ifstream B2("Files/B2.txt");
//	ifstream B3("Files/B3.txt");
//	ifstream B4("Files/B4.txt");
//	ifstream B5("Files/B5.txt");
//	ifstream B6("Files/B6.txt");
//	ifstream B7("Files/B7.txt");
//	ifstream B8("Files/B8.txt");
//
//	bool flag = false;
//
//	if (check(B2, B3, B4, B5, B6, B7, B8))
//	{
//		flag = true;
//
//		ofstream C1("Files/C1.txt");
//		ofstream C2("Files/C2.txt");
//		ofstream C3("Files/C3.txt");
//		ofstream C4("Files/C4.txt");
//		ofstream C5("Files/C5.txt");
//		ofstream C6("Files/C6.txt");
//		ofstream C7("Files/C7.txt");
//		ofstream C8("Files/C8.txt");
//
//		/*for (int i_c = 0; i_c < 8; i_c++)
//		{
//			vector<int> temp;
//			for (int i_b = 0; i_b < 8; i_b++)
//			{
//				switch (i_b)
//				{
//				case 0: readfile(B1, temp); break;
//				case 1: readfile(B2, temp); break;
//				case 2: readfile(B3, temp); break;
//				case 3: readfile(B4, temp); break;
//				case 4: readfile(B5, temp); break;
//				case 5: readfile(B6, temp); break;
//				case 6: readfile(B7, temp); break;
//				case 7: readfile(B8, temp); break;
//				}
//			}
//			if (!temp.empty())
//			{
//				sort(temp.begin(), temp.end());
//				switch (i_c)
//				{
//				case 0: writefile(C1, temp); break;
//				case 1: writefile(C2, temp); break;
//				case 2: writefile(C3, temp); break;
//				case 3: writefile(C4, temp); break;
//				case 4: writefile(C5, temp); break;
//				case 5: writefile(C6, temp); break;
//				case 6: writefile(C7, temp); break;
//				case 7: writefile(C8, temp); break;
//				}
//			}
//		}*/
//		
//		int b = 0, c = 0;
//		vector<int> temp;
//
//		while (!B1.eof() || !B2.eof() || !B3.eof() || !B4.eof() || !B5.eof() || !B6.eof() || !B7.eof() || !B8.eof())
//		{
//			switch (b % 8)
//			{
//			case 0: if (!B1.eof()) { readfile(B1, temp); } break;
//			case 1: if (!B2.eof()) { readfile(B2, temp); } break;
//			case 2: if (!B3.eof()) { readfile(B3, temp); } break;
//			case 3: if (!B4.eof()) { readfile(B4, temp); } break;
//			case 4: if (!B5.eof()) { readfile(B5, temp); } break;
//			case 5: if (!B6.eof()) { readfile(B6, temp); } break;
//			case 6: if (!B7.eof()) { readfile(B7, temp); } break;
//			case 7: if (!B8.eof()) { readfile(B8, temp); } break;
//			}
//			if (b % 8 == 7)
//			{
//				if (!temp.empty())
//				{
//					sort(temp.begin(), temp.end());
//					switch (c % 8)
//					{
//					case 0: if (b > 7) { C1 << " "; } writefile(C1, temp); break;
//					case 1: if (b > 7) { C2 << " "; } writefile(C2, temp); break;
//					case 2: if (b > 7) { C3 << " "; } writefile(C3, temp); break;
//					case 3: if (b > 7) { C4 << " "; } writefile(C4, temp); break;
//					case 4: if (b > 7) { C5 << " "; } writefile(C5, temp); break;
//					case 5: if (b > 7) { C6 << " "; } writefile(C6, temp); break;
//					case 6: if (b > 7) { C7 << " "; } writefile(C7, temp); break;
//					case 7: if (b > 7) { C8 << " "; } writefile(C8, temp); break;
//					}
//					c++;
//					temp.clear();
//				}
//				else
//				{
//					break;
//				}
//			}
//			b++;
//		}
//
//		if (!temp.empty())
//		{
//			sort(temp.begin(), temp.end());
//			switch (c % 8)
//			{
//			case 0: if (b > 7) { C1 << " "; } writefile(C1, temp); break;
//			case 1: if (b > 7) { C2 << " "; } writefile(C2, temp); break;
//			case 2: if (b > 7) { C3 << " "; } writefile(C3, temp); break;
//			case 3: if (b > 7) { C4 << " "; } writefile(C4, temp); break;
//			case 4: if (b > 7) { C5 << " "; } writefile(C5, temp); break;
//			case 5: if (b > 7) { C6 << " "; } writefile(C6, temp); break;
//			case 6: if (b > 7) { C7 << " "; } writefile(C7, temp); break;
//			case 7: if (b > 7) { C8 << " "; } writefile(C8, temp); break;
//			}
//			c++;
//			temp.clear();
//		}
//
//		C1.close();
//		C2.close();
//		C3.close();
//		C4.close();
//		C5.close();
//		C6.close();
//		C7.close();
//		C8.close();
//	}
//	B1.close();
//	B2.close();
//	B3.close();
//	B4.close();
//	B5.close();
//	B6.close();
//	B7.close();
//	B8.close();
//
//	return flag;
//}

//bool write_from_c_to_b()
//{
//	ifstream C1("Files/C1.txt");
//	ifstream C2("Files/C2.txt");
//	ifstream C3("Files/C3.txt");
//	ifstream C4("Files/C4.txt");
//	ifstream C5("Files/C5.txt");
//	ifstream C6("Files/C6.txt");
//	ifstream C7("Files/C7.txt");
//	ifstream C8("Files/C8.txt");
//
//	bool flag = false;
//
//	if (check(C2, C3, C4, C5, C6, C7, C8))
//	{
//		flag = true;
//
//		ofstream B1("Files/B1.txt");
//		ofstream B2("Files/B2.txt");
//		ofstream B3("Files/B3.txt");
//		ofstream B4("Files/B4.txt");
//		ofstream B5("Files/B5.txt");
//		ofstream B6("Files/B6.txt");
//		ofstream B7("Files/B7.txt");
//		ofstream B8("Files/B8.txt");
//
//		/*for (int i_b = 0; i_b < 8; i_b++)
//		{
//			vector<int> temp;
//			for (int i_c = 0; i_c < 8; i_c++)
//			{
//				switch (i_c)
//				{
//				case 0: readfile(C1, temp); break;
//				case 1: readfile(C2, temp); break;
//				case 2: readfile(C3, temp); break;
//				case 3: readfile(C4, temp); break;
//				case 4: readfile(C5, temp); break;
//				case 5: readfile(C6, temp); break;
//				case 6: readfile(C7, temp); break;
//				case 7: readfile(C8, temp); break;
//				}
//			}
//			if (!temp.empty())
//			{
//				sort(temp.begin(), temp.end());
//				switch (i_b)
//				{
//				case 0: writefile(B1, temp); break;
//				case 1: writefile(B2, temp); break;
//				case 2: writefile(B3, temp); break;
//				case 3: writefile(B4, temp); break;
//				case 4: writefile(B5, temp); break;
//				case 5: writefile(B6, temp); break;
//				case 6: writefile(B7, temp); break;
//				case 7: writefile(B8, temp); break;
//				}
//			}
//		}*/
//
//		int b = 0, c = 0;
//		vector<int> temp;
//
//		while (!C1.eof() || !C2.eof() || !C3.eof() || !C4.eof() || !C5.eof() || !C6.eof() || !C7.eof() || !C8.eof())
//		{
//			switch (c % 8)
//			{
//			case 0: if (!C1.eof()) { readfile(C1, temp); } break;
//			case 1: if (!C2.eof()) { readfile(C2, temp); } break;
//			case 2: if (!C3.eof()) { readfile(C3, temp); } break;
//			case 3: if (!C4.eof()) { readfile(C4, temp); } break;
//			case 4: if (!C5.eof()) { readfile(C5, temp); } break;
//			case 5: if (!C6.eof()) { readfile(C6, temp); } break;
//			case 6: if (!C7.eof()) { readfile(C7, temp); } break;
//			case 7: if (!C8.eof()) { readfile(C8, temp); } break;
//			}
//			if (c % 8 == 7)
//			{
//				if (!temp.empty())
//				{
//					sort(temp.begin(), temp.end());
//					switch (b % 8)
//					{
//					case 0: if (b > 7) { B1 << " "; } writefile(B1, temp); break;
//					case 1: if (b > 7) { B2 << " "; } writefile(B2, temp); break;
//					case 2: if (b > 7) { B3 << " "; } writefile(B3, temp); break;
//					case 3: if (b > 7) { B4 << " "; } writefile(B4, temp); break;
//					case 4: if (b > 7) { B5 << " "; } writefile(B5, temp); break;
//					case 5: if (b > 7) { B6 << " "; } writefile(B6, temp); break;
//					case 6: if (b > 7) { B7 << " "; } writefile(B7, temp); break;
//					case 7: if (b > 7) { B8 << " "; } writefile(B8, temp); break;
//					}
//					b++;
//					temp.clear();
//				}
//				else
//				{
//					break;
//				}
//			}
//			c++;
//		}
//
//		if (!temp.empty())
//		{
//			sort(temp.begin(), temp.end());
//			switch (b % 8)
//			{
//			case 0: if (b > 7) { B1 << " "; } writefile(B1, temp); break;
//			case 1: if (b > 7) { B2 << " "; } writefile(B2, temp); break;
//			case 2: if (b > 7) { B3 << " "; } writefile(B3, temp); break;
//			case 3: if (b > 7) { B4 << " "; } writefile(B4, temp); break;
//			case 4: if (b > 7) { B5 << " "; } writefile(B5, temp); break;
//			case 5: if (b > 7) { B6 << " "; } writefile(B6, temp); break;
//			case 6: if (b > 7) { B7 << " "; } writefile(B7, temp); break;
//			case 7: if (b > 7) { B8 << " "; } writefile(B8, temp); break;
//			}
//			b++;
//			temp.clear();
//		}
//
//		B1.close();
//		B2.close();
//		B3.close();
//		B4.close();
//		B5.close();
//		B6.close();
//		B7.close();
//		B8.close();
//	}
//	C1.close();
//	C2.close();
//	C3.close();
//	C4.close();
//	C5.close();
//	C6.close();
//	C7.close();
//	C8.close();
//
//	return flag;
//}

void readfile(ifstream& file, vector<int>& vec)
{
	int first, second;
	bool end = true;
	long int pos;
	bool flag = true;
	//int count = 0;
	while (!file.eof() && end && file.peek() != ifstream::traits_type::eof())
	{
		pos = file.tellg();
		file >> second;
		if (flag)
		{
			vec.push_back(second);
			flag = false;
			//count++;
		}
		else
		{
			if (first > second)
			{
				end = false;
			}
			else
			{
				vec.push_back(second);
				//count++;
			}
		}
		first = second;
	}
	//cout << count << " | ";
	if (!end)
	{
		file.seekg(pos, ios::beg);
	}
}

void writefile(ofstream& file, vector<int>& vec)
{
	//int count = 0;
	for (int i = 0; i < vec.size() - 1; i++)
	{
		file << vec[i] << " ";
		//count++;
	}
	file << vec[vec.size() - 1];
	//count++;
	//cout << " || " << count << " || ";
}

bool check(ifstream& file2, ifstream& file3, ifstream& file4, ifstream& file5, ifstream& file6, ifstream& file7, ifstream& file8)
{
	bool flag = true;
	if (file2.peek() == std::ifstream::traits_type::eof() && file3.peek() == std::ifstream::traits_type::eof() &&
		file4.peek() == std::ifstream::traits_type::eof() && file5.peek() == std::ifstream::traits_type::eof() &&
		file6.peek() == std::ifstream::traits_type::eof() && file7.peek() == std::ifstream::traits_type::eof() &&
		file8.peek() == std::ifstream::traits_type::eof())
	{
		flag = false;
	}
	return flag;
}

bool checkfile(ifstream& file)
{
	bool flag = true;
	if (file.peek() == ifstream::traits_type::eof())
	{
		flag = false;
	}
	return flag;
}

void start()
{
	// Paths to the files
	filesystem::path a("Files/A.txt");
	filesystem::path b("Files/B1.txt");
	filesystem::path c("Files/C1.txt");

	unsigned long long int size_a = filesystem::file_size(a); // The size of the file A.txt

	bool flag = true; // To changing files

	int t1 = time(NULL);
	write_from_A_to_B(); // Write from file A to files B
	int t2 = time(NULL);
	cout << "Write from A to B: " << t2 - t1 << "s" << endl;

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

void write_from_a_to_b()
{
	unsigned int first = 0, second; // The numbers
	unsigned int i = 0; // The index of the file

	ifstream A("Files/A.txt");

	ofstream B1("Files/B1.txt"); ofstream B5("Files/B5.txt");
	ofstream B2("Files/B2.txt"); ofstream B6("Files/B6.txt");
	ofstream B3("Files/B3.txt"); ofstream B7("Files/B7.txt");
	ofstream B4("Files/B4.txt"); ofstream B8("Files/B8.txt");

	bool flag1 = false, flag2 = false, flag3 = false, flag4 = false,
		flag5 = false, flag6 = false, flag7 = false, flag8 = false;

	// Read the numbers from the file A.txt and write these ones to the files B1-B8.txt
	while (!A.eof())
	{
		A >> second;
		if (first > second)
		{
			i++;
		}
		switch (i % 8)
		{
		case 0: if (flag1) { B1 << " "; } B1 << second; flag1 = true; break;
		case 1: if (flag2) { B2 << " "; } B2 << second; flag2 = true; break;
		case 2: if (flag3) { B3 << " "; } B3 << second; flag3 = true; break;
		case 3: if (flag4) { B4 << " "; } B4 << second; flag4 = true; break;
		case 4: if (flag5) { B5 << " "; } B5 << second; flag5 = true; break;
		case 5: if (flag6) { B6 << " "; } B6 << second; flag6 = true; break;
		case 6: if (flag7) { B7 << " "; } B7 << second; flag7 = true; break;
		case 7: if (flag8) { B8 << " "; } B8 << second; flag8 = true; break;
		}
		first = second;
	}

	A.close();
	B1.close(); B5.close();
	B2.close(); B6.close();
	B3.close(); B7.close();
	B4.close(); B8.close();
}

void write_from_A_to_B()
{
	unsigned int first = 0, second; // The numbers
	unsigned int i = 0; // The index of the file

	ifstream A("Files/A.txt");
	ofstream B[8] = { ofstream("Files/B1.txt"), ofstream("Files/B2.txt"), ofstream("Files/B3.txt"),
					  ofstream("Files/B4.txt"), ofstream("Files/B5.txt"), ofstream("Files/B6.txt"),
					  ofstream("Files/B7.txt"), ofstream("Files/B8.txt") };

	bool flag[8] = { false, false, false, false, false, false, false, false };

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

//void write_from_b_to_c()
//{
//	ifstream B1("Files/B1.txt"); ifstream B5("Files/B5.txt");
//	ifstream B2("Files/B2.txt"); ifstream B6("Files/B6.txt");
//	ifstream B3("Files/B3.txt"); ifstream B7("Files/B7.txt");
//	ifstream B4("Files/B4.txt"); ifstream B8("Files/B8.txt");
//
//	ifstream* B[8] = { &B1, &B2, &B3, &B4, &B5, &B6, &B7, &B8 };
//
//	ofstream C1("Files/C1.txt"); ofstream C5("Files/C5.txt");
//	ofstream C2("Files/C2.txt"); ofstream C6("Files/C6.txt");
//	ofstream C3("Files/C3.txt"); ofstream C7("Files/C7.txt");
//	ofstream C4("Files/C4.txt"); ofstream C8("Files/C8.txt");
//		
//	int c = 0;
//	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 },
//		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX };
//	unsigned long long int pointers[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
//	bool flags[8] = { true, true, true, true, true, true, true, true };
//
//	while (!B1.eof() || !B2.eof() || !B3.eof() || !B4.eof() || !B5.eof() || !B6.eof() || !B7.eof() || !B8.eof())
//	{
//		bool flag = true;
//		while (flag)
//		{
//			if (checkfile(B1) && !B1.eof() && flags[0])
//			{
//				pointers[0] = B1.tellg();
//				B1 >> second[0];
//
//				if (first[0] > second[0])
//				{
//					B1.seekg(pointers[0], ios::beg);
//					flags[0] = false;
//				}
//			}
//			else
//			{
//				flags[0] = false;
//			}
//			if (checkfile(B2) && !B2.eof() && flags[1])
//			{
//				pointers[1] = B2.tellg();
//				B2 >> second[1];
//
//				if (first[1] > second[1])
//				{
//					B2.seekg(pointers[1], ios::beg);
//					flags[1] = false;
//				}
//			}
//			else
//			{
//				flags[1] = false;
//			}
//			if (checkfile(B3) && !B3.eof() && flags[2])
//			{
//				pointers[2] = B3.tellg();
//				B3 >> second[2];
//
//				if (first[2] > second[2])
//				{
//					B3.seekg(pointers[2], ios::beg);
//					flags[2] = false;
//				}
//			}
//			else
//			{
//				flags[2] = false;
//			}
//			if (checkfile(B4) && !B4.eof() && flags[3])
//			{
//				pointers[3] = B4.tellg();
//				B4 >> second[3];
//
//				if (first[3] > second[3])
//				{
//					B4.seekg(pointers[3], ios::beg);
//					flags[3] = false;
//				}
//			}
//			else
//			{
//				flags[3] = false;
//			}
//			if (checkfile(B5) && !B5.eof() && flags[4])
//			{
//				pointers[4] = B5.tellg();
//				B5 >> second[4];
//
//				if (first[4] > second[4])
//				{
//					B5.seekg(pointers[4], ios::beg);
//					flags[4] = false;
//				}
//			}
//			else
//			{
//				flags[4] = false;
//			}
//			if (checkfile(B6) && !B6.eof() && flags[5])
//			{
//				pointers[5] = B6.tellg();
//				B6 >> second[5];
//
//				if (first[5] > second[5])
//				{
//					B6.seekg(pointers[5], ios::beg);
//					flags[5] = false;
//				}
//			}
//			else
//			{
//				flags[5] = false;
//			}
//			if (checkfile(B7) && !B7.eof() && flags[6])
//			{
//				pointers[6] = B7.tellg();
//				B7 >> second[6];
//
//				if (first[6] > second[6])
//				{
//					B7.seekg(pointers[6], ios::beg);
//					flags[6] = false;
//				}
//			}
//			else
//			{
//				flags[6] = false;
//			}
//			if (checkfile(B8) && !B8.eof() && flags[7])
//			{
//				pointers[7] = B8.tellg();
//				B8 >> second[7];
//
//				if (first[7] > second[7])
//				{
//					B8.seekg(pointers[7], ios::beg);
//					flags[7] = false;
//				}
//			}
//			else
//			{
//				flags[7] = false;
//			}
//			
//			unsigned int min = UINT32_MAX;
//			int index = -1;
//			for (int i = 0; i < 8; i++)
//			{
//				if (flags[i] && min > second[i])
//				{
//					min = second[i];
//					index = i;
//				}
//			}
//			//cout << min << " file B" << index - 1 << endl;
//			if (index != -1)
//			{
//				switch (c % 8)
//				{
//				case 0: if (C1.tellp() != 0) { C1 << " "; } C1 << min; break;
//				case 1: if (C2.tellp() != 0) { C2 << " "; } C2 << min; break;
//				case 2: if (C3.tellp() != 0) { C3 << " "; } C3 << min; break;
//				case 3: if (C4.tellp() != 0) { C4 << " "; } C4 << min; break;
//				case 4: if (C5.tellp() != 0) { C5 << " "; } C5 << min; break;
//				case 5: if (C6.tellp() != 0) { C6 << " "; } C6 << min; break;
//				case 6: if (C7.tellp() != 0) { C7 << " "; } C7 << min; break;
//				case 7: if (C8.tellp() != 0) { C8 << " "; } C8 << min; break;
//				}
//
//				for (int i = 0; i < 8; i++)
//				{
//					if (i != index && flags[i])
//					{
//						B[i]->seekg(pointers[i], ios::beg);
//					}
//				}
//
//				first[index] = second[index];
//				second[index] = UINT32_MAX;
//				pointers[index] = B[index]->tellg();
//			}
//			else
//			{
//				flag = false;
//
//				for (int i = 0; i < 8; i++)
//				{
//					first[i] = 0;
//					flags[i] = true;
//				}
//			}
//		}
//		c++;
//	}
//
//	C1.close(); C5.close();
//	C2.close(); C6.close();
//	C3.close(); C7.close();
//	C4.close(); C8.close();
//	
//	B1.close(); B5.close();
//	B2.close(); B6.close();
//	B3.close(); B7.close();
//	B4.close(); B8.close();
//}

void write_from_b_to_c()
{
	ifstream B1("Files/B1.txt"); ifstream B5("Files/B5.txt");
	ifstream B2("Files/B2.txt"); ifstream B6("Files/B6.txt");
	ifstream B3("Files/B3.txt"); ifstream B7("Files/B7.txt");
	ifstream B4("Files/B4.txt"); ifstream B8("Files/B8.txt");

	ifstream* B[8] = { &B1, &B2, &B3, &B4, &B5, &B6, &B7, &B8 };

	ofstream C1("Files/C1.txt"); ofstream C5("Files/C5.txt");
	ofstream C2("Files/C2.txt"); ofstream C6("Files/C6.txt");
	ofstream C3("Files/C3.txt"); ofstream C7("Files/C7.txt");
	ofstream C4("Files/C4.txt"); ofstream C8("Files/C8.txt");

	//bool flag_end = true;
	int c = 0;
	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 },
		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX };
	//unsigned long long int pointers[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
	bool flags[8];
	bool flags_not_empty[8];

	bool flag1 = false, flag2 = false, flag3 = false, flag4 = false,
		flag5 = false, flag6 = false, flag7 = false, flag8 = false;

	/*while (!B1.eof() || !B2.eof() || !B3.eof() || !B4.eof() || !B5.eof() || !B6.eof() || !B7.eof() || !B8.eof())
	{
		bool flag = true;
		while (flag)
		{
			if (checkfile(B1) && !B1.eof() && flags[0])
			{
				pointers[0] = B1.tellg();
				B1 >> second[0];

				if (first[0] > second[0])
				{
					B1.seekg(pointers[0], ios::beg);
					flags[0] = false;
				}
			}
			else
			{
				flags[0] = false;
			}
			if (checkfile(B2) && !B2.eof() && flags[1])
			{
				pointers[1] = B2.tellg();
				B2 >> second[1];

				if (first[1] > second[1])
				{
					B2.seekg(pointers[1], ios::beg);
					flags[1] = false;
				}
			}
			else
			{
				flags[1] = false;
			}
			if (checkfile(B3) && !B3.eof() && flags[2])
			{
				pointers[2] = B3.tellg();
				B3 >> second[2];

				if (first[2] > second[2])
				{
					B3.seekg(pointers[2], ios::beg);
					flags[2] = false;
				}
			}
			else
			{
				flags[2] = false;
			}
			if (checkfile(B4) && !B4.eof() && flags[3])
			{
				pointers[3] = B4.tellg();
				B4 >> second[3];

				if (first[3] > second[3])
				{
					B4.seekg(pointers[3], ios::beg);
					flags[3] = false;
				}
			}
			else
			{
				flags[3] = false;
			}
			if (checkfile(B5) && !B5.eof() && flags[4])
			{
				pointers[4] = B5.tellg();
				B5 >> second[4];

				if (first[4] > second[4])
				{
					B5.seekg(pointers[4], ios::beg);
					flags[4] = false;
				}
			}
			else
			{
				flags[4] = false;
			}
			if (checkfile(B6) && !B6.eof() && flags[5])
			{
				pointers[5] = B6.tellg();
				B6 >> second[5];

				if (first[5] > second[5])
				{
					B6.seekg(pointers[5], ios::beg);
					flags[5] = false;
				}
			}
			else
			{
				flags[5] = false;
			}
			if (checkfile(B7) && !B7.eof() && flags[6])
			{
				pointers[6] = B7.tellg();
				B7 >> second[6];

				if (first[6] > second[6])
				{
					B7.seekg(pointers[6], ios::beg);
					flags[6] = false;
				}
			}
			else
			{
				flags[6] = false;
			}
			if (checkfile(B8) && !B8.eof() && flags[7])
			{
				pointers[7] = B8.tellg();
				B8 >> second[7];

				if (first[7] > second[7])
				{
					B8.seekg(pointers[7], ios::beg);
					flags[7] = false;
				}
			}
			else
			{
				flags[7] = false;
			}

			unsigned int min = UINT32_MAX;
			int index = -1;
			for (int i = 0; i < 8; i++)
			{
				if (flags[i] && min > second[i])
				{
					min = second[i];
					index = i;
				}
			}
			//cout << min << " file B" << index - 1 << endl;
			if (index != -1)
			{
				switch (c % 8)
				{
				case 0: if (flag1) { C1 << " "; } C1 << min; flag1 = true; break;
				case 1: if (flag2) { C2 << " "; } C2 << min; flag2 = true; break;
				case 2: if (flag3) { C3 << " "; } C3 << min; flag3 = true; break;
				case 3: if (flag4) { C4 << " "; } C4 << min; flag4 = true; break;
				case 4: if (flag5) { C5 << " "; } C5 << min; flag5 = true; break;
				case 5: if (flag6) { C6 << " "; } C6 << min; flag6 = true; break;
				case 6: if (flag7) { C7 << " "; } C7 << min; flag7 = true; break;
				case 7: if (flag8) { C8 << " "; } C8 << min; flag8 = true; break;
				}

				for (int i = 0; i < 8; i++)
				{
					if (i != index && flags[i])
					{
						B[i]->seekg(pointers[i], ios::beg);
					}
				}

				first[index] = second[index];
				second[index] = UINT32_MAX;
				pointers[index] = B[index]->tellg();
			}
			else
			{
				flag = false;

				for (int i = 0; i < 8; i++)
				{
					first[i] = 0;
					flags[i] = true;
				}
			}
		}
		c++;
	}*/

	for (int i = 0; i < 8; i++)
	{
		ifstream* B = NULL;
		switch (i)
		{
		case 0: B = &B1; break;
		case 1: B = &B2; break;
		case 2: B = &B3; break;
		case 3: B = &B4; break;
		case 4: B = &B5; break;
		case 5: B = &B6; break;
		case 6: B = &B7; break;
		case 7: B = &B8; break;
		}
		//flags_not_empty[i] = checkfile(*B[i]);
		flags_not_empty[i] = checkfile(*B);
		flags[i] = flags_not_empty[i];
	}

	//while (flag_end)
	while (flags[0] || flags[1] || flags[2] || flags[3] || flags[4] || flags[5] || flags[6] || flags[7])
	{
		bool flag = true;
		while (flag)
		{
			for (int i = 0; i < 8; i++)
			{
				ifstream* B = NULL;
				switch (i)
				{
				case 0: B = &B1; break;
				case 1: B = &B2; break;
				case 2: B = &B3; break;
				case 3: B = &B4; break;
				case 4: B = &B5; break;
				case 5: B = &B6; break;
				case 6: B = &B7; break;
				case 7: B = &B8; break;
				}
				if (flags[i])
				{
					//pointers[i] = B[i]->tellg();
					//int pointer = B[i]->tellg();
					//B[i]->operator>>(second[i]);
					int pointer = B->tellg();
					B->operator>>(second[i]);

					if (first[i] > second[i])
					{
						//B[i]->seekg(pointers[i], ios::beg);
						//B[i]->seekg(pointer, ios::beg);
						B->seekg(pointer, ios::beg);
						flags[i] = false;
						second[i] = UINT32_MAX;
					}
				}
			}

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
			//cout << min << " file B" << index - 1 << endl;
			if (index != -1)
			{
				switch (c % 8)
				{
				case 0: if (flag1) { C1 << " "; } C1 << min; flag1 = true; break;
				case 1: if (flag2) { C2 << " "; } C2 << min; flag2 = true; break;
				case 2: if (flag3) { C3 << " "; } C3 << min; flag3 = true; break;
				case 3: if (flag4) { C4 << " "; } C4 << min; flag4 = true; break;
				case 4: if (flag5) { C5 << " "; } C5 << min; flag5 = true; break;
				case 5: if (flag6) { C6 << " "; } C6 << min; flag6 = true; break;
				case 6: if (flag7) { C7 << " "; } C7 << min; flag7 = true; break;
				case 7: if (flag8) { C8 << " "; } C8 << min; flag8 = true; break;
				}

				/*for (int i = 0; i < 8; i++)
				{
					if (i != index && flags[i])
					{
						B[i]->seekg(pointers[i], ios::beg);
					}
				}*/

				for (int i = 0; i < 8; i++)
				{
					if (i != index)
					{
						flags[i] = false;
					}
				}

				flags[index] = true;
				first[index] = second[index];
				second[index] = UINT32_MAX;
				//pointers[index] = B[index]->tellg();
			}
			else
			{
				flag = false;

				for (int i = 0; i < 8; i++)
				{
					ifstream* B = NULL;
					switch (i)
					{
					case 0: B = &B1; break;
					case 1: B = &B2; break;
					case 2: B = &B3; break;
					case 3: B = &B4; break;
					case 4: B = &B5; break;
					case 5: B = &B6; break;
					case 6: B = &B7; break;
					case 7: B = &B8; break;
					}
					first[i] = 0;
					//if (!flags_not_empty[i] || B[i]->eof())
					if (!flags_not_empty[i] || B->eof())
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
		c++;

		/*flag_end = false;
		for (int i = 0; i < 8; i++)
		{
			if (flags_not_empty[i])
			{
				flag_end = flag_end || !B[i];
			}
		}*/
	}

	C1.close(); C5.close();
	C2.close(); C6.close();
	C3.close(); C7.close();
	C4.close(); C8.close();

	B1.close(); B5.close();
	B2.close(); B6.close();
	B3.close(); B7.close();
	B4.close(); B8.close();
}

//void write_from_c_to_b()
//{
//	ofstream B1("Files/B1.txt"); ofstream B5("Files/B5.txt");
//	ofstream B2("Files/B2.txt"); ofstream B6("Files/B6.txt");
//	ofstream B3("Files/B3.txt"); ofstream B7("Files/B7.txt");
//	ofstream B4("Files/B4.txt"); ofstream B8("Files/B8.txt");
//
//	ifstream C1("Files/C1.txt"); ifstream C5("Files/C5.txt");
//	ifstream C2("Files/C2.txt"); ifstream C6("Files/C6.txt");
//	ifstream C3("Files/C3.txt"); ifstream C7("Files/C7.txt");
//	ifstream C4("Files/C4.txt"); ifstream C8("Files/C8.txt");
//
//	ifstream* C[8] = { &C1, &C2, &C3, &C4, &C5, &C6, &C7, &C8 };
//
//	int b = 0;
//	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 },
//		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX };
//	unsigned long long int pointers[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
//	bool flags[8] = { true, true, true, true, true, true, true, true };
//
//	while (!C1.eof() || !C2.eof() || !C3.eof() || !C4.eof() || !C5.eof() || !C6.eof() || !C7.eof() || !C8.eof())
//	{
//		bool flag = true;
//		while (flag)
//		{
//			if (checkfile(C1) && !C1.eof() && flags[0])
//			{
//				pointers[0] = C1.tellg();
//				C1 >> second[0];
//
//				if (first[0] > second[0])
//				{
//					C1.seekg(pointers[0], ios::beg);
//					flags[0] = false;
//				}
//			}
//			else
//			{
//				flags[0] = false;
//			}
//			if (checkfile(C2) && !C2.eof() && flags[1])
//			{
//				pointers[1] = C2.tellg();
//				C2 >> second[1];
//
//				if (first[1] > second[1])
//				{
//					C2.seekg(pointers[1], ios::beg);
//					flags[1] = false;
//				}
//			}
//			else
//			{
//				flags[1] = false;
//			}
//			if (checkfile(C3) && !C3.eof() && flags[2])
//			{
//				pointers[2] = C3.tellg();
//				C3 >> second[2];
//
//				if (first[2] > second[2])
//				{
//					C3.seekg(pointers[2], ios::beg);
//					flags[2] = false;
//				}
//			}
//			else
//			{
//				flags[2] = false;
//			}
//			if (checkfile(C4) && !C4.eof() && flags[3])
//			{
//				pointers[3] = C4.tellg();
//				C4 >> second[3];
//
//				if (first[3] > second[3])
//				{
//					C4.seekg(pointers[3], ios::beg);
//					flags[3] = false;
//				}
//			}
//			else
//			{
//				flags[3] = false;
//			}
//			if (checkfile(C5) && !C5.eof() && flags[4])
//			{
//				pointers[4] = C5.tellg();
//				C5 >> second[4];
//
//				if (first[4] > second[4])
//				{
//					C5.seekg(pointers[4], ios::beg);
//					flags[4] = false;
//				}
//			}
//			else
//			{
//				flags[4] = false;
//			}
//			if (checkfile(C6) && !C6.eof() && flags[5])
//			{
//				pointers[5] = C6.tellg();
//				C6 >> second[5];
//
//				if (first[5] > second[5])
//				{
//					C6.seekg(pointers[5], ios::beg);
//					flags[5] = false;
//				}
//			}
//			else
//			{
//				flags[5] = false;
//			}
//			if (checkfile(C7) && !C7.eof() && flags[6])
//			{
//				pointers[6] = C7.tellg();
//				C7 >> second[6];
//
//				if (first[6] > second[6])
//				{
//					C7.seekg(pointers[6], ios::beg);
//					flags[6] = false;
//				}
//			}
//			else
//			{
//				flags[6] = false;
//			}
//			if (checkfile(C8) && !C8.eof() && flags[7])
//			{
//				pointers[7] = C8.tellg();
//				C8 >> second[7];
//
//				if (first[7] > second[7])
//				{
//					C8.seekg(pointers[7], ios::beg);
//					flags[7] = false;
//				}
//			}
//			else
//			{
//				flags[7] = false;
//			}
//
//			unsigned int min = UINT32_MAX;
//			int index = -1;
//			for (int i = 0; i < 8; i++)
//			{
//				if (flags[i] && min > second[i])
//				{
//					min = second[i];
//					index = i;
//				}
//			}
//			if (index != -1)
//			{
//				switch (b % 8)
//				{
//				case 0: if (B1.tellp() != 0) { B1 << " "; } B1 << min; break;
//				case 1: if (B2.tellp() != 0) { B2 << " "; } B2 << min; break;
//				case 2: if (B3.tellp() != 0) { B3 << " "; } B3 << min; break;
//				case 3: if (B4.tellp() != 0) { B4 << " "; } B4 << min; break;
//				case 4: if (B5.tellp() != 0) { B5 << " "; } B5 << min; break;
//				case 5: if (B6.tellp() != 0) { B6 << " "; } B6 << min; break;
//				case 6: if (B7.tellp() != 0) { B7 << " "; } B7 << min; break;
//				case 7: if (B8.tellp() != 0) { B8 << " "; } B8 << min; break;
//				}
//
//				for (int i = 0; i < 8; i++)
//				{
//					if (i != index && flags[i])
//					{
//						C[i]->seekg(pointers[i], ios::beg);
//					}
//				}
//
//				first[index] = second[index];
//				second[index] = UINT32_MAX;
//				pointers[index] = C[index]->tellg();
//			}
//			else
//			{
//				flag = false;
//
//				for (int i = 0; i < 8; i++)
//				{
//					first[i] = 0;
//					flags[i] = true;
//				}
//			}
//		}
//		b++;
//	}
//
//	C1.close(); C5.close();
//	C2.close(); C6.close();
//	C3.close(); C7.close();
//	C4.close(); C8.close();
//
//	B1.close(); B5.close();
//	B2.close(); B6.close();
//	B3.close(); B7.close();
//	B4.close(); B8.close();
//}

void write_from_c_to_b()
{
	ifstream C1("Files/C1.txt"); ifstream C5("Files/C5.txt");
	ifstream C2("Files/C2.txt"); ifstream C6("Files/C6.txt");
	ifstream C3("Files/C3.txt"); ifstream C7("Files/C7.txt");
	ifstream C4("Files/C4.txt"); ifstream C8("Files/C8.txt");

	ifstream* C[8] = { &C1, &C2, &C3, &C4, &C5, &C6, &C7, &C8 };

	ofstream B1("Files/B1.txt"); ofstream B5("Files/B5.txt");
	ofstream B2("Files/B2.txt"); ofstream B6("Files/B6.txt");
	ofstream B3("Files/B3.txt"); ofstream B7("Files/B7.txt");
	ofstream B4("Files/B4.txt"); ofstream B8("Files/B8.txt");

	//bool flag_end = true;
	int b = 0;
	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 },
		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX };
	//unsigned long long int pointers[8] = { 0, 0, 0, 0, 0, 0, 0, 0 };
	bool flags[8];
	bool flags_not_empty[8];

	bool flag1 = false, flag2 = false, flag3 = false, flag4 = false,
		flag5 = false, flag6 = false, flag7 = false, flag8 = false;

	/*while (!B1.eof() || !B2.eof() || !B3.eof() || !B4.eof() || !B5.eof() || !B6.eof() || !B7.eof() || !B8.eof())
	{
		bool flag = true;
		while (flag)
		{
			if (checkfile(B1) && !B1.eof() && flags[0])
			{
				pointers[0] = B1.tellg();
				B1 >> second[0];

				if (first[0] > second[0])
				{
					B1.seekg(pointers[0], ios::beg);
					flags[0] = false;
				}
			}
			else
			{
				flags[0] = false;
			}
			if (checkfile(B2) && !B2.eof() && flags[1])
			{
				pointers[1] = B2.tellg();
				B2 >> second[1];

				if (first[1] > second[1])
				{
					B2.seekg(pointers[1], ios::beg);
					flags[1] = false;
				}
			}
			else
			{
				flags[1] = false;
			}
			if (checkfile(B3) && !B3.eof() && flags[2])
			{
				pointers[2] = B3.tellg();
				B3 >> second[2];

				if (first[2] > second[2])
				{
					B3.seekg(pointers[2], ios::beg);
					flags[2] = false;
				}
			}
			else
			{
				flags[2] = false;
			}
			if (checkfile(B4) && !B4.eof() && flags[3])
			{
				pointers[3] = B4.tellg();
				B4 >> second[3];

				if (first[3] > second[3])
				{
					B4.seekg(pointers[3], ios::beg);
					flags[3] = false;
				}
			}
			else
			{
				flags[3] = false;
			}
			if (checkfile(B5) && !B5.eof() && flags[4])
			{
				pointers[4] = B5.tellg();
				B5 >> second[4];

				if (first[4] > second[4])
				{
					B5.seekg(pointers[4], ios::beg);
					flags[4] = false;
				}
			}
			else
			{
				flags[4] = false;
			}
			if (checkfile(B6) && !B6.eof() && flags[5])
			{
				pointers[5] = B6.tellg();
				B6 >> second[5];

				if (first[5] > second[5])
				{
					B6.seekg(pointers[5], ios::beg);
					flags[5] = false;
				}
			}
			else
			{
				flags[5] = false;
			}
			if (checkfile(B7) && !B7.eof() && flags[6])
			{
				pointers[6] = B7.tellg();
				B7 >> second[6];

				if (first[6] > second[6])
				{
					B7.seekg(pointers[6], ios::beg);
					flags[6] = false;
				}
			}
			else
			{
				flags[6] = false;
			}
			if (checkfile(B8) && !B8.eof() && flags[7])
			{
				pointers[7] = B8.tellg();
				B8 >> second[7];

				if (first[7] > second[7])
				{
					B8.seekg(pointers[7], ios::beg);
					flags[7] = false;
				}
			}
			else
			{
				flags[7] = false;
			}

			unsigned int min = UINT32_MAX;
			int index = -1;
			for (int i = 0; i < 8; i++)
			{
				if (flags[i] && min > second[i])
				{
					min = second[i];
					index = i;
				}
			}
			//cout << min << " file B" << index - 1 << endl;
			if (index != -1)
			{
				switch (c % 8)
				{
				case 0: if (flag1) { C1 << " "; } C1 << min; flag1 = true; break;
				case 1: if (flag2) { C2 << " "; } C2 << min; flag2 = true; break;
				case 2: if (flag3) { C3 << " "; } C3 << min; flag3 = true; break;
				case 3: if (flag4) { C4 << " "; } C4 << min; flag4 = true; break;
				case 4: if (flag5) { C5 << " "; } C5 << min; flag5 = true; break;
				case 5: if (flag6) { C6 << " "; } C6 << min; flag6 = true; break;
				case 6: if (flag7) { C7 << " "; } C7 << min; flag7 = true; break;
				case 7: if (flag8) { C8 << " "; } C8 << min; flag8 = true; break;
				}

				for (int i = 0; i < 8; i++)
				{
					if (i != index && flags[i])
					{
						B[i]->seekg(pointers[i], ios::beg);
					}
				}

				first[index] = second[index];
				second[index] = UINT32_MAX;
				pointers[index] = B[index]->tellg();
			}
			else
			{
				flag = false;

				for (int i = 0; i < 8; i++)
				{
					first[i] = 0;
					flags[i] = true;
				}
			}
		}
		c++;
	}*/

	for (int i = 0; i < 8; i++)
	{
		flags_not_empty[i] = checkfile(*C[i]);
		flags[i] = flags_not_empty[i];
	}

	//while (flag_end)
	while (flags[0] || flags[1] || flags[2] || flags[3] || flags[4] || flags[5] || flags[6] || flags[7])
	{
		bool flag = true;
		while (flag)
		{
			for (int i = 0; i < 8; i++)
			{
				if (flags[i])
				{
					//pointers[i] = C[i]->tellg();
					int pointer = C[i]->tellg();
					C[i]->operator>>(second[i]);

					if (first[i] > second[i])
					{
						//C[i]->seekg(pointers[i], ios::beg);
						C[i]->seekg(pointer, ios::beg);
						flags[i] = false;
						second[i] = UINT32_MAX;
					}
				}
			}

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
			//cout << min << " file B" << index - 1 << endl;
			if (index != -1)
			{
				switch (b % 8)
				{
				case 0: if (flag1) { B1 << " "; } B1 << min; flag1 = true; break;
				case 1: if (flag2) { B2 << " "; } B2 << min; flag2 = true; break;
				case 2: if (flag3) { B3 << " "; } B3 << min; flag3 = true; break;
				case 3: if (flag4) { B4 << " "; } B4 << min; flag4 = true; break;
				case 4: if (flag5) { B5 << " "; } B5 << min; flag5 = true; break;
				case 5: if (flag6) { B6 << " "; } B6 << min; flag6 = true; break;
				case 6: if (flag7) { B7 << " "; } B7 << min; flag7 = true; break;
				case 7: if (flag8) { B8 << " "; } B8 << min; flag8 = true; break;
				}

				/*for (int i = 0; i < 8; i++)
				{
					if (i != index && flags[i])
					{
						B[i]->seekg(pointers[i], ios::beg);
					}
				}*/

				for (int i = 0; i < 8; i++)
				{
					if (i != index)
					{
						flags[i] = false;
					}
				}

				flags[index] = true;
				first[index] = second[index];
				second[index] = UINT32_MAX;
				//pointers[index] = B[index]->tellg();
			}
			else
			{
				flag = false;

				for (int i = 0; i < 8; i++)
				{
					first[i] = 0;
					if (!flags_not_empty[i] || C[i]->eof())
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
		b++;

		/*flag_end = false;
		for (int i = 0; i < 8; i++)
		{
			if (flags_not_empty[i])
			{
				flag_end = flag_end || !B[i];
			}
		}*/
	}

	C1.close(); C5.close();
	C2.close(); C6.close();
	C3.close(); C7.close();
	C4.close(); C8.close();

	B1.close(); B5.close();
	B2.close(); B6.close();
	B3.close(); B7.close();
	B4.close(); B8.close();
}

void write_from_files1_to_files2(string file1, string file2)
{

	ifstream files1[8] = { ifstream("Files/" + file1 + "1.txt"), ifstream("Files/" + file1 + "2.txt"), ifstream("Files/" + file1 + "3.txt"),
						   ifstream("Files/" + file1 + "4.txt"), ifstream("Files/" + file1 + "5.txt"), ifstream("Files/" + file1 + "6.txt"),
						   ifstream("Files/" + file1 + "7.txt"), ifstream("Files/" + file1 + "8.txt") };
	ofstream files2[8] = { ofstream("Files/" + file2 + "1.txt"), ofstream("Files/" + file2 + "2.txt"), ofstream("Files/" + file2 + "3.txt"),
						   ofstream("Files/" + file2 + "4.txt"), ofstream("Files/" + file2 + "5.txt"), ofstream("Files/" + file2 + "6.txt"),
						   ofstream("Files/" + file2 + "7.txt"), ofstream("Files/" + file2 + "8.txt") };

	int c = 0;
	unsigned int first[8] = { 0, 0, 0, 0, 0, 0, 0, 0 },
		second[8] = { UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX, UINT32_MAX };
	bool flags[8];
	bool flags_not_empty[8];

	for (int i = 0; i < 8; i++)
	{
		flags_not_empty[i] = checkfile(files1[i]);
		flags[i] = flags_not_empty[i];
	}

	while (flags[0] || flags[1] || flags[2] || flags[3] || flags[4] || flags[5] || flags[6] || flags[7])
	{
		bool flag = true;
		while (flag)
		{
			for (int i = 0; i < 8; i++)
			{
				if (flags[i])
				{
					int pointer = files1[i].tellg();
					files1[i] >> second[i];

					if (first[i] > second[i])
					{
						files1[i].seekg(pointer, ios::beg);
						flags[i] = false;
						second[i] = UINT32_MAX;
					}
				}
			}

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

			if (index != -1)
			{
				int index_file2 = c % 8;
				files2[index_file2] << " " << min;

				for (int i = 0; i < 8; i++)
				{
					if (i != index)
					{
						flags[i] = false;
					}
				}

				flags[index] = true;
				first[index] = second[index];
				second[index] = UINT32_MAX;
			}
			else
			{
				flag = false;

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
		c++;
	}
	for (int i = 0; i < 8; i++)
	{
		files1[i].close();
		files2[i].close();
	}
}