import json
import xml.etree.ElementTree as ET

def generate_report():
    with open('51_caps.json', 'r') as f:
        caps = json.load(f)
    with open('53_selectors.json', 'r') as f:
        ui_map = json.load(f)
        
    current_pkg = caps.get("appPackage", "")
    feedback_report = []
    
    # 1. Weryfikacja Pakietu
    if current_pkg == "io.appium.android.apis":
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji", "status": "ZGODNY",
            "message": f"Pakiet {current_pkg} poprawnie zmapowany."
        })
    else:
        feedback_report.append({
            "feature": "Identyfikacja Aplikacji", "status": "DO POPRAWY",
            "message": f"Niezgodność pakietu. Wykryto {current_pkg}."
        })
        
    # 2. Weryfikacja Dostępności Elementów
    target_element = "ACCESSIBILITY"
    if target_element in ui_map.get("selectors", {}):
        feedback_report.append({
            "feature": "Dostępność UI", "status": "ZGODNY",
            "message": f"Element {target_element} jest dostępny w layoutach."
        })
    else:
        sample_keys = list(ui_map.get('selectors', {}).keys())[:3]
        feedback_report.append({
            "feature": "Dostępność UI", "status": "INFORMACJA",
            "message": f"Nie odnaleziono ID '{target_element}'. Sugestia: Zweryfikuj czy element nie zmienił nazwy na jedną z dostępnych: {sample_keys}."
        })
        
    # Terminal output
    print(">>> ZADANIE 5.5: GENEROWANIE RAPORTU FEEDBACKU DLA DEWELOPERA <<<")
    print("--- FEEDBACK DLA TWÓRCÓW APLIKACJI ---")
    for item in feedback_report:
        print(f"[{item['status']}] {item['feature']}: {item['message']}")
    print("\n[INFO] Blok 5 zakończony. Raport opisowy gotowy: 55_result.xml")
    
    # Generowanie pliku JUnit XML
    testsuites = ET.Element("testsuites")
    testsuite = ET.SubElement(testsuites, "testsuite", name="ConsistencyTest", tests=str(len(feedback_report)))
    
    for item in feedback_report:
        testcase = ET.SubElement(testsuite, "testcase", classname="Validation", name=item["feature"])
        if item["status"] != "ZGODNY":
            failure = ET.SubElement(testcase, "failure", message=item["message"])
            failure.text = item["status"]
            
    tree = ET.ElementTree(testsuites)
    ET.indent(tree, space="    ")
    tree.write("55_result.xml", encoding="utf-8", xml_declaration=True)

generate_report()