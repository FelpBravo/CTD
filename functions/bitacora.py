from config.config import SERVER_GESTION, BD_INTEGRA, ID_PROCESO
from config.log import logger
from functions.db import conexion_bd_datos


spUPD_Control_Procesos_Gestion = '''exec [cuadre].[*************] {id_instancia},{estado},'{resultado}',{cant_total},{cant_ok},{cant_err},NULL'''
spINS_Control_Procesos_Gestion = "DECLARE @RC bigint; exec [cuadre].[****************] {id_proceso},{bloque_proceso},@RC output,NULL; SELECT @RC AS rc;"


def insertar_bitacora(id_proceso, bloque_proceso="0"):
    try:
        id_instancia = conexion_bd_datos(
            SERVER_GESTION,
            BD_INTEGRA,
            spINS_Control_Procesos_Gestion.format(id_proceso=id_proceso, bloque_proceso=bloque_proceso)
        )
        return id_instancia
    except Exception as e:
        logger(str(e))


def actualizar_bitacora(id_instancia, id_proceso, xml="", estado=True, cant_total='NULL', cant_ok='NULL', cant_err='NULL'):
    try:
        if id_proceso == ID_PROCESO:
            xml = "<Result>\n"
            xml += "<InformaciónProceso>\n"
            xml += "<NombreProceso>CTD Cuprum</NombreProceso>\n"
            xml += "<Version>1</Version>\n"
            xml += "</InformaciónProceso>\n"
            xml += "</Result>\n"

        conexion_bd_datos(
            SERVER_GESTION,
            BD_INTEGRA,
            spUPD_Control_Procesos_Gestion.format(
                id_instancia=str(id_instancia),
                estado="1" if estado else "0",
                resultado=str(xml).replace("'", '''"'''),
                cant_total=str(cant_total),
                cant_ok=str(cant_ok),
                cant_err=str(cant_err)
            ),
            "sin_retorno", "Si"
        )
    except Exception as e:
        logger(str(e))
