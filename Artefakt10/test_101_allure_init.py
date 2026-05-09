import allure
import pytest

@allure.feature("10.1: Inicjalizacja Allure")
def test_success_example():
    with allure.step("Krok 1: Wykonanie operacji, która się powiedzie"):
        assert True

@allure.feature("10.1: Inicjalizacja Allure")
def test_failure_example():
    with allure.step("Krok 1: Wykonanie operacji, która ma błąd"):
        assert 1 == 2, "Wymuszony błąd do raportu"