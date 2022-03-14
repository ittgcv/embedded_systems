from cfdiclient import Autenticacion,  DescargaMasiva
from cfdiclient import Fiel
import datetime
from cfdiclient import SolicitaDescarga
from cfdiclient import VerificaSolicitudDescarga
import base64
import time

def getToken():
    auth = Autenticacion(fiel)
    token = auth.obtener_token()
    return token
def solicitaDescarga():
    descarga = SolicitaDescarga(fiel)
    # Emitidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_emisor=rfc_emisor)
    print(result)
    # Recibidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_receptor=rfc_receptor)
    print(result)
    # {'mensaje': 'Solicitud Aceptada', 'cod_estatus': '5000', 'id_solicitud': 'be2a3e76-684f-416a-afdf-0f9378c346be'}
    return result['id_solicitud']
def verificaSolicitud(id_solicitud):    
    v_descarga = VerificaSolicitudDescarga(fiel)
    result = v_descarga.verificar_descarga(token, rfc_solicitante, id_solicitud)
    print(result)
    return result['paquetes']
def descargaCfdi(id_paquete):
    descarga = DescargaMasiva(fiel)
    result = descarga.descargar_paquete(token, rfc_solicitante, id_paquete)
    print(result)
    decoded_string = base64.b64decode(result[ 'paquete_b64'])
    with open("cfdis.zip", "wb") as cfdis_file2:
        cfdis_file2.write(decoded_string);

FIEL_KEY = 'Claveprivada_FIEL_PEPM710624PY5_20171108_112525.key'
FIEL_CER = 'pepm710624py5.cer'
FIEL_PAS = 'sdjazmin'
cer_der = open(FIEL_CER, 'rb').read()
key_der = open(FIEL_KEY, 'rb').read() 
fiel = Fiel(cer_der, key_der, FIEL_PAS)
rfc_solicitante = 'PEPM710624PY5'
fecha_inicial = datetime.datetime(2020, 1, 1)
fecha_final = datetime.datetime(2020, 5,28)
rfc_emisor = 'OOTJ881128JS1'
rfc_receptor = 'PEPM710624PY5'

token=getToken()
idSolicitud=solicitaDescarga()
print(idSolicitud)
for i in range(20):
    paquetes=verificaSolicitud(idSolicitud)
    print(paquetes, len(paquetes))
    for items in paquetes:
        descargaCfdi(items)
    time.sleep(300)
