import pytest

def es_par(num):
    try:
        if num % 2 == 0:
            return True
    except:
        return False
    return False 

@pytest.mark.qaminds
def test_numero_par():
    numero = 4
    expected_result = True
    actual_result = es_par(numero)
    assert expected_result == actual_result , f'El numero ingresado no es par: {numero} se esperaba True y se obtuvo {actual_result}'

def test_numero_impar():
    numero = 7
    expected_result = False
    actual_result = es_par(numero)
    assert expected_result == actual_result , f'El numero ingresado no es impar: {numero} se esperaba False y se obtuvo {actual_result}'

def test_numero_cero():
    numero = 0
    expected_result = True
    actual_result = es_par(numero)
    assert expected_result == actual_result , f'El numero ingresado no es par: {numero} se esperaba True y se obtuvo {actual_result}'

def test_caracter():
    caracter = 'a'
    expected_result = False
    actual_result = es_par(caracter)
    assert expected_result == actual_result , f'El numero ingresado no es par: {caracter} se esperaba True y se obtuvo {actual_result}'