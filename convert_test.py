from conversion import convertion as c
def test():
    assert c.convertion(0) == 'Range Fault'
    assert c.convertion(1) == 'I'
    assert c.convertion(4) == 'IV'
    assert c.convertion(5) == 'V'
    assert c.convertion(10) == 'X'
    assert c.convertion(14) == 'XIV'
    assert c.convertion(15) == 'XV'
    assert c.convertion(19) == 'XIX'
    assert c.convertion(45) == 'XLV'
    assert c.convertion(56) == 'LVI'
    assert c.convertion(89) == 'LXXXIX'
    assert c.convertion(99) == 'XCIX'
    assert c.convertion(100) == 'C'
    assert c.convertion(296) == 'CCXCVI'
    assert c.convertion(1024) == 'MXXIV'
    assert c.convertion(3999) == 'MMMCMXCIX'
    assert c.convertion(5000) == 'Range Fault'
    

