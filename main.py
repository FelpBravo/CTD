#!/usr/bin/python3.9
from datetime import datetime
import zipfile
import os
import traceback

import config.config as constant
import functions.db as db
import functions.mail as mail
from config.log import logger
import functions.sftp as sftp
import functions.bitacora as bitacora


estado_proceso=True

try:
    logger("Inicio del proceso para Reporte CTD Cuprum")
    ID_PADRE= bitacora.insertar_bitacora(id_proceso=constant.ID_PROCESO)

    #Variables
    fecha_maestra = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #... Ejemplo: 2023-08-30 16:54:53.020
    date = datetime.today().strftime('%Y%m%d') #... Ejemplo 20230904 
    hour = datetime.today().strftime('%H%M')   #... Ejemplo 1320
    file_name = f"ATD_RESPAG_{datetime.today().strftime('%Y%m%d')}_{datetime.today().strftime('%H%M')}_1003.csv"
    sp_maestro = constant.spLST_Cuprum_Afiliado_Traspasado_Diario.format(fecha_maestra=fecha_maestra)

    logger('EJECUTANDO Procedimiento almacenado...' + str(sp_maestro))
    ID_10611= bitacora.insertar_bitacora(id_proceso="10611")
    df, estado = db.connect_pymssql(constant.SERVER_GESTION, constant.BD_INTEGRA, sp_maestro)
    bitacora.actualizar_bitacora(ID_10611, "10611", estado=estado)

    logger(f'GENERANDO Archivo de salida en ruta local {constant.LOCAL_OUTPUT_DIR}')
    df.to_csv(constant.LOCAL_OUTPUT_DIR + file_name, index=False, header=False)

    logger(f'COMPRIMIENDO Archivo de salida en ruta local  {constant.LOCAL_OUTPUT_DIR}')
    ID_10612= bitacora.insertar_bitacora(id_proceso="10612")
    fantasy_zip = zipfile.ZipFile(constant.LOCAL_OUTPUT_DIR + file_name.split('.')[0] + '.zip', 'w')
    fantasy_zip.write(
        os.path.join(constant.LOCAL_OUTPUT_DIR, file_name), 
        os.path.relpath(os.path.join(constant.LOCAL_OUTPUT_DIR, file_name), constant.LOCAL_OUTPUT_DIR), 
        compress_type=zipfile.ZIP_DEFLATED
        )
    fantasy_zip.close()

    logger('TRANSFIRIENDO Archivo zip a casilla SFTP.')
    estado = sftp.connect(
        rutaLocal =constant.LOCAL_OUTPUT_DIR  + file_name.split('.')[0] + '.zip', 
        rutaRemota=constant.REMOTE_OUTPUT_DIR + file_name.split('.')[0] + '.zip'
        )
    bitacora.actualizar_bitacora(ID_10612, "10612", estado=estado)
    
except Exception as e:
    logger("EXCEPTION_GENERAL: " + str(e) + str(traceback.format_exc(limit=1)))
    mail.enviar_mail_con_error("EXCEPTION_GENERAL: " + str(e) + str(traceback.format_exc(limit=1)))
    estado_proceso=False
finally:
    cant_registros = '0' if df is None else str(len(df))
    bitacora.actualizar_bitacora(ID_PADRE, constant.ID_PROCESO, estado=estado_proceso, cant_total=cant_registros, cant_ok=cant_registros )
    logger('FIN del proceso.')


