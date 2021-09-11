/*
 * Проект, демонстрирующий работу с библиотекой fstream
 */
#include <iostream>
#include <fstream>
#include "str_switch.h"
using namespace std;

// Функция для открытия файла со справкой
void print_text(string text) {
	/***********************************************
	 * Объявление переменной line строкового типа, *
	 * в которой будет находиться содержимое файла *
	 **********************************************/
	string line;

	ifstream file(text);
    
	// Проверка на наличие файла
	if (file.is_open()) {
		while (getline(file, line)) {
			cout << line << endl; // Вывод информации из текста
		}
	} else {
		cout << "\a\e[1;31mОШИБКА: файл \e[0m\e[35m" << text << "\e[0m\e[1;31m не существует!\e[0m\n";
		exit(1); // Завершение программы с кодом ошибки 1
	}
	file.close(); // Закрытие файла
}

// Функция для записи информации в файл
void write_text(string text) {
	int i, num;
	string a;
	
	ofstream file(text, ios_base::app);
	
	cout << "Введите количество строк: ";
	cin >> num;
	
	for(i = 0; i < num; i++) {
		cin >> a;
		file << a << "\n"; // Запись числа в файл
	}
	
	file.close(); // Закрытие файла
}

int main(int argc, char* argv[]) {
	SWITCH(argv[1]) {
		CASE("print"): // Вывод содержимого файла
			print_text(argv[2]);
			break;
		CASE("write"): // Ввод в файл
			write_text(argv[2]);
			break;
		DEFAULT:
			cout << "ОШИБКА: неправильно введена опция " << argv[1] << endl;
			exit(1);
	}
	
	return 0;
}
