from sci_calc import SciCalc
#from unittest import TestCase

#class myCalctest(unittest.testcase):

my_sci_calc = SciCalc()

def test_find_sqrt():
    assert my_sci_calc.find_sqrt(4) == 2

def test_find_ceil():
    assert my_sci_calc.find_ceil(22.7) == 23
