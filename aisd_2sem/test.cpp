#include <iostream>
#include <list>
#include "screen.h"
#include "shape.h"
using std::list;

// Определение класса точки
class Point {
public:
    int x, y;
    Point(int a = 0, int b = 0) : x(a), y(b) {}
};

// Определение класса Parallelogram, наследующего класс Rectangle
class Parallelogram : public rectangle, public reflectable {
public:
    Parallelogram(Point a, Point b) : rectangle(a, b) {}
    
    // Функция для рисования параллелограмма
    void draw() override {
        // Реализация рисования параллелограмма
    }

    // Пустая функция для отражения горизонтально
    void flip_horizontally() {}

    // Пустая функция для поворота вправо
    void rotate_right() {}

    // Пустая функция для поворота влево
    void rotate_left() {}
};

int main() {
    // Пример использования класса Parallelogram
    Point a(0, 0);
    Point b(5, 0);
    Parallelogram parallelogram(a, b);
    parallelogram.draw();
    
    return 0;
}