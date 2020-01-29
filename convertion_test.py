from convertion import *
def test():
    assert convertion(0) == 'Range Fault'
    assert convertion(1) == 'I'
    assert convertion(4) == 'IV'
    assert convertion(5) == 'V'
    assert convertion(10) == 'X'
    assert convertion(14) == 'XIV'
    assert convertion(15) == 'XV'
    assert convertion(19) == 'XIX'
    assert convertion(45) == 'XLV'
    assert convertion(56) == 'LVI'
    assert convertion(89) == 'LXXXIX'
    assert convertion(99) == 'XCIX'
    assert convertion(100) == 'C'
    assert convertion(296) == 'CCXCVI'
    assert convertion(1024) == 'MXXIV'
    assert convertion(3999) == 'MMMCMXCIX'
    assert convertion(5000) == 'Range Fault'
    

