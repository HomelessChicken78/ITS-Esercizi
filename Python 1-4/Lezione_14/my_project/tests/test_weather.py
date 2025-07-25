# ...../Lezione_14$ pytest my_project/tests/test_weather.py

from my_project.weather import check_weather
'''
# passed
def test_check_weather1():
    assert check_weather(21.00) == "hot", "temperatures greater than 20 degree \
        must be considered as hot"
    
# failed
def test_check_weather2():
    assert check_weather(5.00) == "average", "temperatures between 10 and 20 degree" \
        "must be considered as average temperature"
    
def test_check_weather3():
    assert check_weather(5.00) == "cold", "temperatures between 10 and 20 degree" \
        "must be considered as cold temperature"

def test_check_weather4():
    assert check_weather(13.00) == "average", "temperatures between 10 and 20 degree" \
        "must be considered as average temperature"

# # NO -> Viene considerato come un unico test anche se ci stanno due assert
# def test_check_weather5():
#     assert check_weather(30.00) == "hot", "temperatures greater than 20 degree must be considered as hot"
#     assert check_weather(11.00) == "cold", "temperatures lower than 10 degree must be considered as cold"
'''

'''
import pytest
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected
'''

# Assertion Error custom
import pytest
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = "Errore 1"
    elif temperature <= 20:
        ae = "Errore 2"
    else:
        ae = "Errore 3"
    assert check_weather(temperature) == expected, ae