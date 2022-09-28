#pragma once
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <random>

#include <filesystem>
#include <string>

#include <ctime>

using namespace std;

void createfile();
//void start();
//void write_from_a_to_b();
//bool write_from_b_to_c();
//bool write_from_c_to_b();
void readfile(ifstream&, vector<int>&);
void writefile(ofstream&, vector<int>&);
bool check(ifstream&, ifstream&, ifstream&, ifstream&, ifstream&, ifstream&, ifstream&);
bool checkfile(ifstream&);

void start();
void write_from_a_to_b();
void write_from_b_to_c();
void write_from_c_to_b();
void write_from_files1_to_files2(string, string);
void write_from_A_to_B();