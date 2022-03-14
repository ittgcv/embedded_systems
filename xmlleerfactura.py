import xml.dom.minidom
import xmltodict
import json
#mydict=xmltodict.parse()
#import xml.etree.ElementTree as ET
doc=xml.dom.minidom.parse('facturarotoplas3.xml')
items=doc.getElementsByTagName('cfdi:Receptor')
cliente=items[0].getAttribute('Nombre')
print(cliente)
items=doc.getElementsByTagName('cfdi:Concepto')
print(len(items))
for i in items:
    print(i.getAttribute('Descripcion'))
    print(i.getAttribute('Cantidad'))
