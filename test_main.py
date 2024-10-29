# test_main.py
import pytest
from main import addition

#---- Test Paramétrique ----
@pytest.mark.parametrize("a, b, result", [
    (2, 3, 5)
])
def test_addition(a, b, result):
     a, b = 2,3
     assert addition(a, b) == result
