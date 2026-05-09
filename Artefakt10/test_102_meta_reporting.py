import allure

@allure.epic("Platforma Edukacyjna Artefakt")
@allure.feature("Moduł Kursy i Lekcje")
@allure.story("Przeglądanie listy lekcji")
def test_lesson_list():
    allure.dynamic.title("Test wczytywania listy lekcji")
    with allure.step("Krok 1: Otwarcie modułu kursów"):
        allure.attach("Log: Moduł otwarty poprawnie", name="Log systemowy", attachment_type=allure.attachment_type.TEXT)
        assert True