
# Issue-1
## 1. $ python -m doctest -v -o NORMALIZE_WHITESPACE morse.py
```python
Trying: 
    encode('SOS') 
Expecting:
    '...  --- ...'
ok
Trying:
    encode('0 THIS IS A TEST FOR NUMBER 0') # doctest: +ELLIPSIS
Expecting:
    '----- ... -----'
ok
Trying:
    encode('sos')
Expecting:
    Traceback (most recent call last):
    ...
    KeyError: 's'
ok
2 items had no tests:
    morse
    morse.decode
1 items passed all tests:
   3 tests in morse.encode
3 tests in 3 items.
3 passed and 0 failed. 
Test passed. 
```
## 2. $ python -m doctest -v morse.py 
```python
Trying: 
    encode('SOS') 
Expecting: 
    '...  --- ...' 
********************************************************************** 
File "/.../morse.py", line 34, in morse.encode 
Failed example: 
    encode('SOS') 
Expected: 
    '...  --- ...' 
Got:
    '... --- ...' 
Trying: 
    encode('0 THIS IS A TEST FOR NUMBER 0') # doctest: +ELLIPSIS 
Expecting: 
    '----- ... -----' 
ok 
Trying: 
    encode('sos') 
Expecting: 
    Traceback (most recent call last): 
    ... 
    KeyError: 's' 
ok 
2 items had no tests: 
    morse 
    morse.decode 
**********************************************************************
1 items had failures: 
   1 of   3 in morse.encode 
3 tests in 3 items. 
2 passed and 1 failed. 
***Test Failed*** 1 failures. 
```
## 3. Запуск через pycharm
```python
**********************************************************************
File "/Users/daniilzakharov/Documents/Avito_Analitics/1.Python/10.Классы/Домашка/main.py", line 34, in __main__.encode
Failed example:
    encode('SOS')
Expected:
    '...  --- ...'
Got:
    '... --- ...'
**********************************************************************
1 items had failures:
   1 of   3 in __main__.encode
***Test Failed*** 1 failures.
```
# Issue-2
## $ python -m pytest morse.py
```python
collected 3 items                                                                                                                                                             

main.py .FF                                                                                                                                                             [100%]

================================================================================== FAILURES ===================================================================================
_______________________________________________ test_decode[- . ... -   ..-. --- .-.   .-.. . - - . .-.   ---TEST FOR LETTER M] _______________________________________________

test_input = '- . ... -   ..-. --- .-.   .-.. . - - . .-.   --', expected = 'TEST FOR LETTER M'

    @pytest.mark.parametrize('test_input, expected', [
        ('... --- ...', 'SOS'),
        ('- . ... -   ..-. --- .-.   .-.. . - - . .-.   --', 'TEST FOR LETTER M'),
        ('..-. ..- -. -. -.--   .-- --- .-. -..', 'FUNNY WORD')
        ])
    def test_decode(test_input, expected):
>       assert decode(test_input) == expected
E       AssertionError: assert 'TESTFORLETTERM' == 'TEST FOR LETTER M'
E         - TEST FOR LETTER M
E         ?     -   -      -
E         + TESTFORLETTERM

main.py:70: AssertionError
________________________________________________________ test_decode[..-. ..- -. -. -.--   .-- --- .-. -..-FUNNY WORD] ________________________________________________________

test_input = '..-. ..- -. -. -.--   .-- --- .-. -..', expected = 'FUNNY WORD'

    @pytest.mark.parametrize('test_input, expected', [
        ('... --- ...', 'SOS'),
        ('- . ... -   ..-. --- .-.   .-.. . - - . .-.   --', 'TEST FOR LETTER M'),
        ('..-. ..- -. -. -.--   .-- --- .-. -..', 'FUNNY WORD')
        ])
    def test_decode(test_input, expected):
>       assert decode(test_input) == expected
E       AssertionError: assert 'FUNNYWORD' == 'FUNNY WORD'
E         - FUNNY WORD
E         ?      -
E         + FUNNYWORD

main.py:70: AssertionError
=========================================================================== short test summary info ===========================================================================
FAILED main.py::test_decode[- . ... -   ..-. --- .-.   .-.. . - - . .-.   ---TEST FOR LETTER M] - AssertionError: assert 'TESTFORLETTERM' == 'TEST FOR LETTER M'
FAILED main.py::test_decode[..-. ..- -. -. -.--   .-- --- .-. -..-FUNNY WORD] - AssertionError: assert 'FUNNYWORD' == 'FUNNY WORD'
========================================================================= 2 failed, 1 passed in 0.50s =========================================================================
```
# Issue-3
## 1. $ python -m unittest -v test_u_fit.py
```python
test_empty (main.TestFitTransform) ... ok
test_none (main.TestFitTransform) ... ok
test_texts (main.TestFitTransform) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK

```
## 2. Запуск через pycharm
```python
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
# Issue-4
## $ python -m pytest -v test_py_fit.py
```python
collected 6 items                                                                                                                                                             

main.py::test_none PASSED                                                                                                                                               [ 16%]
main.py::test_empty PASSED                                                                                                                                              [ 33%]
main.py::test_fit_texts[text0-expected0] PASSED                                                                                                                         [ 50%]
main.py::test_fit_texts[text1-expected1] PASSED                                                                                                                         [ 66%]
main.py::test_fit_texts[text2-expected2] PASSED                                                                                                                         [ 83%]
main.py::test_fit_texts[text3-expected3] PASSED                                                                                                                         [100%]

============================================================================== 6 passed in 0.08s ==============================================================================
```
