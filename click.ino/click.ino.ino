#include <Mouse.h>

void setup() {
  Serial.begin(9600);
  Mouse.begin();
}

void loop() {
  if (Serial.available()) {
    // читаем первый байт
    char byte1 = Serial.read();
    if (byte1 == 'C') {
      // если первый байт 'C', то ждем следующего байта и выполняем действие в зависимости от его значения
      while (!Serial.available()) {
        // ждем появления следующего байта
      }
      char byte2 = Serial.read();
      if (byte2 == '1') {
        // выполняем действие 1
        // ...

        // клик левой кнопкой мыши
        Mouse.click(MOUSE_LEFT);

        // отпускаем левую кнопку мыши
        Mouse.release();
      } else if (byte2 == '2') {
        // выполняем действие 2
        // ...

        // клик правой кнопкой мыши
        Mouse.click(MOUSE_RIGHT);

        // отпускаем правую кнопку мыши
        Mouse.release();
      } else {
        // обработка ошибки
        // ...
      }
    }
  }
}