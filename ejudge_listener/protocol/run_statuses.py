"""Статусы посылок задач.

0  => 'OK'
99 => 'Перетестировать'
8  => 'Зачтено/Принято'
14 => 'Ошибка оформлени кода'
9  => 'Проигнорировано'
1  => 'Ошибка компиляции'
10 => 'Дисквалифицировано
7  => 'Частичное решение
11 => 'Ожидает проверки'
2  => 'Ошибка во время выполнения программы
3  => 'Превышено максимальное врем работы'
4  => 'Неправильный формат вывода'
5  => 'Неправильный ответ'
6  => 'Ошибка проверки, обратитесь к администраторам'
12 => 'Превышение лимиа памяти'
13 => 'Security error'
96 => 'Тестирование...'
98 => 'Компилирование...'
"""
TERMINAL_RUN_STATUSES = {0, 99, 8, 14, 9, 1, 10, 7, 11, 2, 3, 4, 5, 6, 12, 13}
NON_TERMINAL_RUN_STATUSES = {96, 98}
