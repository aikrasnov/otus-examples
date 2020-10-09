import xml.etree.ElementTree as ET

tree = ET.parse('foo.xml')
root = tree.getroot()

for child in root:
    print(dir(child))
    print(child.tag, child.attrib)
    for _child in child:
        print(_child.tag, _child.text)
    child.clear()
    print(child)