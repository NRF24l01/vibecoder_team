from lxml import etree as ET
import re

def remove_markdown_wrapper(xml_str: str) -> str:
    # Removes markdown wrapper ```xml ... ``` if present
    # Updated to allow leading whitespace before the markdown block
    pattern = r"^\s*```xml\s*(.*?)\s*```\s*$"
    match = re.match(pattern, xml_str, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # If input doesn't have markdown wrapper, check if it looks like XML
    if xml_str.strip().startswith('<') and xml_str.strip().endswith('>'):
        return xml_str.strip()
        
    raise ValueError("Invalid XML format: Expected markdown wrapper with ```xml ... ``` or plain XML content")

def extract_result(xml_response: str):
    if xml_response is None:
        return "Error: Empty response", ""
        
    xml_response = remove_markdown_wrapper(xml_response)

    parser = ET.XMLParser(recover=True)
    tree = ET.fromstring(xml_response.encode('utf-8'), parser=parser)

    if tree.tag != "response":
        tree = tree.find("response")

    if tree is None:
        raise ValueError("No <response> element found in XML")

    summary_node = tree.find("summary")
    result_node = tree.find("result")

    summary = summary_node.text.strip() if summary_node is not None and summary_node.text else ""
    if result_node is not None and result_node.text:
        result = result_node.text.strip()
    else:
        result = ""

    return summary, result