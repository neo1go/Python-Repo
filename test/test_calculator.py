from calculator import square  # dies dient der Verbindung zu der zu testenden Datei.
import pytest    # hier werden Funktionen von pytest implementiert.

 

def test_positive():
    assert square(2) == 4
    assert square(3) == 9   
    

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9 

    
def test_zero():
    assert square(0) == 0  
    

def test_str():
    with pytest.raises(TypeError):
        square("cat")