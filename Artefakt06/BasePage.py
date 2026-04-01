import json

class BasePage:
    def __init__(self, selectors_file="../Artefakt05/53_selectors.json"):
        try:
            with open(selectors_file, "r") as f:
                self.selectors = json.load(f)["selectors"]
            print(f"[BASE_PAGE] Pomyślnie zainicjalizowano mapę: {len(self.selectors)} elementów.")
        except FileNotFoundError:
            print(f"[BASE_PAGE] BŁĄD: Nie znaleziono pliku {selectors_file}")
            self.selectors = {}

    def get_selector(self, business_name):
        return self.selectors.get(business_name, None)

if __name__ == "__main__":
    page = BasePage()
    print(f"Weryfikacja klucza 'ADD': {page.get_selector('ADD')}")