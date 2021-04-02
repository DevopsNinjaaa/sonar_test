# pytest test_my_math.py
# pytest test_my_math.py -v 
# pytest test_my_math.py::test_addition
# pytest test_my_math.py::test_addition -v
from check import Person
import pytest

@pytest.mark.parametrize('name, age, year',[
	("Vegito", 22, 1998),
	("Neymar", 29, 1992),
	("Messi", 34, 1987),
])
def test_birth_year(name, age, year):
	p1 = Person(name, age)
	assert p1.get_birth_year() == year

@pytest.mark.parametrize('name, age, result, token',[
	("Vegito", 16, "No Access", None),
	("Neymar", 29, "Full Access", None),
	("Messi", 34, "Full Access", None),
	("De Brune", 14, "Limited Access", "e$23231"),
	("Sterling", 14, "No Access", "E$23231"),
])
def test_entry(name, age, result, token):
	p1 = Person(name, age, token)
	assert p1.check_access() == result

