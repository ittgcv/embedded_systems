import xml.dom.minidom
import xml.etree.ElementTree as ET
tree=ET.parse('facturarotoplas1.xml')
for node in tree.iter():
    print('node', node.tag)
    for subnode in node:
        print('subnode', subnode.tag)
root=tree.getroot()
print(root.tag, len(root))
for element in root:
    print(element)
print(root.attrib)
print(root[2].attrib)
node=tree.findall('{http://www.sat.gob.mx/cfd/3}Conceptos')
print(len(node))
articulos=node[0].findall('{http://www.sat.gob.mx/cfd/3}Concepto')
print(len(articulos))
for name in node:
    print('concepto', name)

doc=xml.dom.minidom.parse('facturarotoplas1.xml')
print(doc.nodeName)
print(doc.firstChild.tagName)
items=doc.getElementsByTagName('cfdi:Emisor')
for i in items:
    print(i.getAttribute('Nombre'))
items=doc.getElementsByTagName('cfdi:Receptor')
for i in items:
    print(i.getAttribute('Nombre'))
items=doc.getElementsByTagName('cfdi:Conceptos')
print('elementos de conceptos ', len(items))
concepto=items[0].getAttribute('cfdi:Concepto')
print('concepto por atributo', (concepto))
items=doc.getElementsByTagName('cfdi:Concepto')
print(len(items))
for i in items:
    print(i.getAttribute('Descripcion'))
