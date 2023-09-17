import config.config as constant 
from config.log import logger

import pymssql 
import pandas
import traceback
import warnings

warnings.filterwarnings('ignore')

def connect_pymssql(server, data_base, query=None, type=None):
    logger(f'[{constant.SERVER_GESTION}]-[{constant.BD_INTEGRA}] Iniciando conexión a la base de datos.')
    conn= None
    df= None
    estado = True

    try:
        conn = pymssql.connect(server, constant.UID, constant.PWD, data_base)
        df = pandas.read_sql_query(query, conn) 
        logger(f'OK "{str(len(df))}" Registros obtenidos.')
        conn.close()
    except Exception as e:
        logger("EXCEPTION_DB_PYMSSQL: " + str(e) + str(traceback.format_exc(limit=1)))
        estado = False
    finally:
        return df, estado

def conexion_bd_datos(server, base_datos, consulta, type=None, execute=None):

    try:
        cnxn = pymssql.connect(server, constant.UID, constant.PWD, base_datos)

        if type == "retorna_valor":
            resultado = []
            cursor = cnxn.cursor()
            cursor.execute(consulta)
            for row in cursor:
                resultado.append(row)
            cnxn.close()
            cursor.close()

            return resultado

        elif type == "sin_retorno":
            cursor = cnxn.cursor()
            cursor.executemany(consulta) if execute is None else cursor.execute(consulta)
            cnxn.commit()
            cnxn.close()
            cursor.close()
        else:
            cursor = cnxn.cursor()
            cursor.execute(consulta)

            resultado = cursor.fetchone()

            cnxn.commit()
            cnxn.close()
            cursor.close()

            return resultado[0]
    except Exception as e:
        logger("EXCEPTION_conexion_bd_datos: " + str(e) + str(traceback.format_exc(limit=1)))