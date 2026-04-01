import xml.etree.ElementTree as ET
import os
import json

def build_ui_map():
    layout_dir = "../Artefakt02/decompiled_apk/res/layout/"
    ui_map = {"selectors": {}}
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    count = 0

    for file_name in os.listdir(layout_dir):
        if file_name.endswith(".xml"):
            try:
                tree = ET.parse(os.path.join(layout_dir, file_name))
                root = tree.getroot()
                
                for element in root.iter():
                    res_id = element.attrib.get(f"{{{ns['android']}}}id")
                    if res_id:
                        clean_id = res_id.split('/')[-1]
                        business_name = clean_id.upper()
                        
                        if business_name not in ui_map["selectors"]:
                            ui_map["selectors"][business_name] = clean_id
                            count += 1
            except:
                continue
                
    with open('53_selectors.json', 'w') as f:
        json.dump(ui_map, f, indent=4)
        
    print(">>> ZADANIE 5.3: BUDOWA MAPY SELEKTORÓW (UI MAPPING) <<<")
    print(f"[OK] Zmapowano {count} unikalnych elementów UI.")
    print("Artefakt zapisany: 53_selectors.json")

build_ui_map()