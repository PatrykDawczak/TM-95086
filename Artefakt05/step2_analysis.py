import xml.etree.ElementTree as ET

def analyze_manifest():
    manifest_path = "../Artefakt02/decompiled_apk/AndroidManifest.xml"
    tree = ET.parse(manifest_path)
    root = tree.getroot()
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    package = root.attrib.get('package')
    permissions = [elem.attrib.get(f"{{{ns['android']}}}name") for elem in root.findall('.//uses-permission', ns)]
    activities = [elem.attrib.get(f"{{{ns['android']}}}name") for elem in root.findall('.//activity', ns)]
    
    log_content = "=== ARTEFAKT 5.2: RAPORT ANALIZY SYSTEMOWEJ ===\n"
    log_content += f"Pakiet główny: {package}\n"
    log_content += f"Liczba Activity: {len(activities)}\n\n"
    log_content += "Kluczowe Uprawnienia (Co aplikacja chce robić?):\n"
    
    for perm in permissions:
        if perm:
            log_content += f"- {perm}\n"
            
    print(">>> ZADANIE 5.2: ANALIZA MANIFESTU (POŁĄCZENIE Z ARTEFAKTEM 02) <<<")
    print(log_content)
    
    with open('52_inspection.log', 'w') as f:
        f.write(log_content)
        
    print("[OK] Sukces! Artefakt zapisany jako: 52_inspection.log")

analyze_manifest()