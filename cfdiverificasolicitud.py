from cfdiclient import Autenticacion
from cfdiclient import Fiel
from cfdiclient import VerificaSolicitudDescarga

import datetime
from cfdiclient import SolicitaDescarga

FIEL_KEY = 'Claveprivada_FIEL_PEPM710624PY5_20171108_112525.key'
FIEL_CER = 'pepm710624py5.cer'
FIEL_PAS = 'sdjazmin'
cer_der = open(FIEL_CER, 'rb').read()
key_der = open(FIEL_KEY, 'rb').read() 
fiel = Fiel(cer_der, key_der, FIEL_PAS)

auth = Autenticacion(fiel)

token = auth.obtener_token()
#token='eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE1ODg1NzIwMjcsImV4cCI6MTU4ODU3MjYyNywiaWF0IjoxNTg4NTcyMDI3LCJpc3MiOiJMb2FkU29saWNpdHVkRGVjYXJnYU1hc2l2YVRlcmNlcm9zIiwiYWN0b3J0IjoiMzAzMDMwMzAzMTMwMzAzMDMwMzAzMDM0MzAzODMwMzUzOTMxMzczNSJ9.dl0r1t7UQkWVM1UJVdWWpi0YuULC6ZXg83pzwpD2-pM%26wrap_subject%3d3030303031303030303030343038303539313735'
print(token)
id_solicitud='51ca6215-7f93-45dd-ad9f-ca61d4901819'
#descarga = SolicitaDescarga(fiel)
v_descarga = VerificaSolicitudDescarga(fiel)

#token = 'eyJh'
rfc_solicitante = 'PEPM710624PY5'
fecha_inicial = datetime.datetime(2020, 1, 1)
fecha_final = datetime.datetime(2020, 4, 30)
rfc_emisor = 'OOTJ881128JS1'
rfc_receptor = 'PEPM710624PY5'
result = v_descarga.verificar_descarga(token, rfc_solicitante, id_solicitud)
print(result)
