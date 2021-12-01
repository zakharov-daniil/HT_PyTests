# HT_PyTests
## Issue-1: DocTest
Файл morse.py
1. Запуск без ошибок (для проверки работы флага) с командной строки: </br>
$ python -m doctest -v -o NORMALIZE_WHITESPACE morse.py
2. Запуск с ошибкой (без флага): </br>
$ python -m doctest -v morse.py
3. Или можно запустить файл в pycharm (и получить ошибку из-за отсутствия флага)

## Issue-2: Parametric Pytest
Файл morse.py
1. Запуск с командной строки </br>
$ python -m pytest morse.py

## Issue-3: Unittest
Файлы one_hot_encoder.py с функцией fit_tramsform и test_u_fit.py с тестами
1. Запуск с командной строки: </br>
$ python -m unittest -v test_u_fit.py
2. Запуск в pycharm

## Issue-4: Pytest
Файлы one_hot_encoder.py с функцией fit_tramsform и test_py_fit.py с тестами </br>
1. Запуск с командной строки</br>
$ python -m pytest -v test_py_fit.py

## Issue-5: WorldClock
