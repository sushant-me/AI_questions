import xml.etree.ElementTree as ET

def parse_xml_file(file_path):
    """ Parse XML file. """
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    for child in root:
        print(child.tag, child.attrib)

# Example usage
parse_xml_file('https://example.com/data.xml')