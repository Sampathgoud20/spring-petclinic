import json
import xml.etree.ElementTree as ET

with open("reports/trivy-result.json") as f:
    data = json.load(f)

root = ET.Element("TrivyScan")

for result in data.get("Results", []):
    target = ET.SubElement(root, "Target", name=str(result.get("Target")))

    for vuln in result.get("Vulnerabilities", []) or []:
        v = ET.SubElement(target, "Vulnerability")
        ET.SubElement(v, "ID").text = str(vuln.get("VulnerabilityID"))
        ET.SubElement(v, "Severity").text = str(vuln.get("Severity"))

tree = ET.ElementTree(root)
tree.write("reports/trivy-result.xml")

print("XML generated")