import xml.etree.ElementTree as ET
import glob
import json

def mine_selectors(path):
    results = []
    ns = {'android': 'http://schemas.android.com/apk/res/android'}
    
    for file in glob.glob(path + "/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                res_id = elem.get('{http://schemas.android.com/apk/res/android}id')
                if res_id:
                    clean_id = res_id.split('/')[-1]
                    clean_file = file.split('/')[-1]
                    tag = elem.tag
                    results.append({"file": clean_file, "id": clean_id, "tag": tag})
        except ET.ParseError:
            pass
            
    with open('miner_report.json', 'w') as f:
        json.dump(results, f, indent=4)
    print(f"[OK] Extracted {len(results)} IDs and saved to miner_report.json")

mine_selectors("../Artefakt02/decompiled_apk/res/layout")