#pragma once
#include <iostream>
#include <fstream>
#include <random>
#include <ctime>

using namespace std;

void Createfile(long long int);
void Start(long long int);
void Write_from_A_to_B(long long int);
void Write_from_B_to_C(long long int);
bool Checkfile(ifstream&);
void readfile(const char*);
void quickSort(unsigned long long int*, long long int, long long int);
long long int partition(unsigned long long int*, long long int, long long int);
void swap(unsigned long long int*, unsigned long long int*);