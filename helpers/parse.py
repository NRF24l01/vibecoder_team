from lxml import etree as ET
import re

def remove_markdown_wrapper(xml_str: str) -> str:
    # Удаляет markdown обертку ```xml ... ```
    pattern = r"^```xml\s*(.*?)\s*```$"
    match = re.match(pattern, xml_str, re.DOTALL)
    if match:
        return match.group(1).strip()
    return xml_str.strip()

def extract_result(xml_response: str):
    xml_response = remove_markdown_wrapper(xml_response)
    print(xml_response)

    parser = ET.XMLParser(recover=True)
    tree = ET.fromstring(xml_response.encode('utf-8'), parser=parser)

    if tree.tag != "response":
        tree = tree.find("response")

    if tree is None:
        raise ValueError("No <response> element found in XML")

    summary_node = tree.find("summary")
    result_node = tree.find("result")

    summary = summary_node.text.strip() if summary_node is not None and summary_node.text else ""
    result = ET.tostring(result_node, encoding='unicode', pretty_print=True) if result_node is not None else ""

    return summary, result