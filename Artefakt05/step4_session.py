import json

def check_readiness():
    with open('51_caps.json', 'r') as f:
        caps_data = json.load(f)
    with open('53_selectors.json', 'r') as f:
        ui_map = json.load(f)
        
    app_pkg = caps_data.get("appPackage") or caps_data.get("appium:appPackage")
    app_act = caps_data.get("appActivity") or caps_data.get("appium:appActivity")
    dev_name = caps_data.get("deviceName") or caps_data.get("appium:deviceName")
    
    if not app_pkg or not app_act:
        status_msg = "FAILED: Missing appPackage or appActivity in JSON!"
        color = "\033[91m" # Red
    else:
        status_msg = "READY TO CONNECT"
        color = "\033[92m" # Green
        
    report = ">>> ZADANIE 5.4: INTEGRACJA ARTEFAKTÓW (STABLE BUILD) <<<\n"
    report += "=== ARTEFAKT 5.4: SESSION READINESS REPORT ===\n"
    report += f"Target App     : {app_pkg}\n"
    report += f"Main Activity  : {app_act}\n"
    report += f"Device         : {dev_name}\n"
    report += f"UI Elements    : {len(ui_map.get('selectors', {}))} loaded\n"
    report += f"Status         : {status_msg}\n"
    
    print(report.replace("READY TO CONNECT", f"{color}READY TO CONNECT\033[0m"))
    
    with open('54_session.log', 'w') as f:
        f.write(report)

check_readiness()