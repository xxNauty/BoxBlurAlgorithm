from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

def write_xml(filename: str, data: dict) -> None:
    # Convert dict to XML bytes
    xml_bytes = dicttoxml(data, custom_root='root', attr_type=False)
    # Parse bytes to XML DOM
    dom = parseString(xml_bytes)
    # Pretty print as string
    pretty_xml = dom.toprettyxml(indent="  ")

    # Write to file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)