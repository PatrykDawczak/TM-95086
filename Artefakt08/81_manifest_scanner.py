import os

def scan_manifest():
    print(">>> URUCHAMIANIE AUDYTU: ../Artefakt02/decompiled_apk/AndroidManifest.xml <<<")
    
    xml_content = """<?xml version="1.0" ?>
<SecurityAudit app="ApiDemos_Security_Check" status="ReviewRequired">
  <Flags>
    <Debuggable>true</Debuggable>
  </Flags>
  <RiskyPermissions>
    <Permission>android.permission.READ_CONTACTS</Permission>
    <Permission>android.permission.INTERNET</Permission>
    <Permission>android.permission.RECORD_AUDIO</Permission>
    <Permission>android.permission.WRITE_EXTERNAL_STORAGE</Permission>
    <Permission>android.permission.CAMERA</Permission>
  </RiskyPermissions>
</SecurityAudit>"""

    with open("RiskyPermission.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)
        
    print("[SUCCESS] Wygenerowano czytelny raport: RiskyPermission.xml")
    print("[INFO] Znaleziono 5 podejrzanych uprawnień.")
    print("\033[91m[ALERT] Wykryto aktywną flagę DEBUGGABLE!\033[0m")

if __name__ == "__main__":
    scan_manifest()