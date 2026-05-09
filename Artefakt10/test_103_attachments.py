import allure
import pytest

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("10.3: Dowody wizualne (Załączniki)")
def test_screenshot_on_fail():
    with allure.step("Krok 1: Próba kliknięcia w przycisk 'Zapisz'"):
        try:
            # Symulujemy błąd szukania elementu
            raise Exception("ElementNotVisibleException")
        except Exception as e:
            # Tworzymy atrapę zrzutu ekranu i logu API by zaliczyć zadanie
            allure.attach(b"fake_image_data", name="Screenshot_Error_01", attachment_type=allure.attachment_type.PNG)
            allure.attach("Błąd 500: Timeout", name="API_Response", attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Test padł, ale mamy dowody! Log: {str(e)}")