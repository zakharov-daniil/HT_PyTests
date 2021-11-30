
# Issue-1:
## 1. $ python -m doctest -v -o NORMALIZE_WHITESPACE morse.py:
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
