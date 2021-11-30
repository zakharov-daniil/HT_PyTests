<pre>
# Issue-1:
## 1. $ python -m doctest -v -o NORMALIZE_WHITESPACE morse.py:
Trying: </br>
    encode('SOS') </br>
Expecting:</br>
    '...  --- ...'</br>
ok</br>
Trying:</br>
    encode('0 THIS IS A TEST FOR NUMBER 0') # doctest: +ELLIPSIS</br>
Expecting:</br>
    '----- ... -----'</br>
ok</br>
Trying:</br>
    encode('sos')</br>
Expecting:</br>
    Traceback (most recent call last):</br>
    ...</br>
    KeyError: 's'</br>
ok</br>
2 items had no tests:</br>
    morse</br>
    morse.decode</br>
1 items passed all tests:</br>
   3 tests in morse.encode</br>
3 tests in 3 items.</br>
3 passed and 0 failed. </br>
Test passed. </br>
## 2. $ python -m doctest -v morse.py </br>
Trying: </br>
    encode('SOS') </br>
Expecting: </br>
    '...  --- ...' </br>
********************************************************************** 
File "/.../morse.py", line 34, in morse.encode </br>
Failed example: </br>
    encode('SOS') </br>
Expected: </br>
    '...  --- ...' </br>
Got:</br>
    '... --- ...' </br>
Trying: </br>
    encode('0 THIS IS A TEST FOR NUMBER 0') # doctest: +ELLIPSIS </br>
Expecting: </br>
    '----- ... -----' </br>
ok </br>
Trying: </br>
    encode('sos') </br>
Expecting: </br>
    Traceback (most recent call last): </br>
    ... </br>
    KeyError: 's' </br>
ok </br>
2 items had no tests: </br>
    morse </br>
    morse.decode </br>
**********************************************************************
1 items had failures: </br>
   1 of   3 in morse.encode </br>
3 tests in 3 items. </br>
2 passed and 1 failed. </br>
***Test Failed*** 1 failures. </br>
</pre>
