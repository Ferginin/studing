#include <iostream>
#include <conio.h>

void gotoxy(int x, int y) {
    printf("\x1b[%d;%df", y, x);
}

int main() {
    int x = 15, y = 5;
    const int x1 = 15, y1 = 5, x2 = 60, y2 = 15;

    // Очистим экран
    system("cls");

    // Нарисуем окно
    for (int i = x1; i <= x2; ++i) {
        gotoxy(i, y1);
        std::cout << "-";
        gotoxy(i, y2);
        std::cout << "-";
    }

    for (int i = y1; i <= y2; ++i) {
        gotoxy(x1, i);
        std::cout << "|";
        gotoxy(x2, i);
        std::cout << "|";
    }

    // Поставим символ в начальную позицию
    gotoxy(x, y);
    std::cout << "*";

    char key;
    while (true) {
        if (_kbhit()) {
            key = _getch();
            // F1 - влево
            if (key == 0 && _kbhit()) {
                key = _getch();
                if (key == 59) {
                    if (x > x1) {
                        gotoxy(x, y);
                        std::cout << " ";  // Стереть предыдущий символ
                        --x;
                        gotoxy(x, y);
                        std::cout << "*";
                    }
                }
            }
            // F2 - вправо
            else if (key == 0 && _kbhit()) {
                key = _getch();
                if (key == 60) {
                    if (x < x2) {
                        gotoxy(x, y);
                        std::cout << " ";  // Стереть предыдущий символ
                        ++x;
                        gotoxy(x, y);
                        std::cout << "*";
                    }
                }
            }
        }
    }

    return 0;
}