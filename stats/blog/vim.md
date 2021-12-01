# Использование окон и вкладок Vim

Основная система у меня без GUI. Я использую дистрибутив CalmiraLinux 1.1 на постоянной основе. Да, исключительно в консоли, никакой графики. Чаще всего работаю, конечно же, в Vim. Собственно, в нём писал эту статью. Мне нужно часто переключаться между файлами, либо держать открытыми на одном экране сразу несколько. Сначала я просто прибегал к помощи нескольких TTY, но есть способ проще - использовать стандартные возможности Vim. Это - окна и вкладки.

## Окна

То, что в Vim называется окнами, очень удобная вещь, позволяющая одновременно просматривать сразу несколько документов. Эдакий тайлинг. Для создания нового окна нажмите сочетание клавиш <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>N</kbd> (важен регистр). Для закрытия, соответственно, <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>Q</kbd>.

Переключение между окнами осуществляется комбинацией <kbd>Ctrl</kbd>+<kbd>W</kbd>+Вверх/Вниз/Влево/Вправо.

Для перемещения окон используются следующие сочетания:

- **Вверх:** <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>K</kbd>;
- **Вниз:** <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>J</kbd>;
- **Влево:** <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>H</kbd>;
- **Вправо:** <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>L</kbd>

Для перемещения открытого активного окна в новую вкладку используется сочетание <kbd>Ctrl</kbd>+<kbd>W</kbd>+<kbd>T</kbd>

## Вкладки

Что такое вкладки, думаю, пояснять не нужно:

<!-- Тут должно быть фото вкладок -->

Ctrl + W + gf - открыть новую вкладку;

gT - переключиться между вкладками.