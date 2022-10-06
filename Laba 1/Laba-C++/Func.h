#pragma once
#include <iostream>
#include <fstream>
#include <random>
#include <filesystem>
#include <string>
#include <ctime>

using namespace std;

void createfile();
void start();
void write_from_A_to_B();
void write_from_files1_to_files2(string, string);
bool checkfile(ifstream&);