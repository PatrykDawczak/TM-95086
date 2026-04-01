import xml.etree.ElementTree as ET
import json

def discover_caps():
    # Pobieramy plik rozpakowany w Artefakcie 02
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    try:
        tree = ET.parse(manifest_path)
    except FileNotFoundError:
        print("BŁĄD: Nie znaleziono pliku Manifestu. Upewnij się, że Artefakt 02 został wykonany.")
        return

    root = tree.getroot()
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    package = root.attrib.get('package')
    main_activity = ""
    
    # Szukamy aktywności, która ma filtr MAIN i LAUNCHER
    for activity in root.findall('.//activity', ns):
        intent = activity.find('.//intent-filter', ns)
        if intent is not None:
            action = intent.find('.//action[@android:name="android.intent.action.MAIN"]', ns)
            if action is not None:
                main_activity = activity.attrib.get(f"{{{ns['android']}}}name")
                break
    
    capabilities = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "appPackage": package,
        "appActivity": main_activity,
        "deviceName": "emulator-5554",
        "noReset": True
    }
    
    with open('51_caps.json', 'w') as f:
        json.dump(capabilities, f, indent=4)
        
    print(f"Sukces! Wykryto: {package} / {main_activity}")

discover_caps()