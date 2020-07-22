# python3.7
# encoding: utf-8
"""
@author: Chenjin.Qian
@email:  chenjin.qian@xquant.com
@file:   connect_models.py
@time:   2020-06-30 15:56
"""

import os



class ConnectOracle(object):
    def __init__(self, host=None, instance=None, user=None, password=None, port=1521):
        self.host = host if host else os.getenv("ORACLE_HOST")
        self.instance = instance if instance else os.getenv("ORACLE_INSTANCE")
        self.user = user if user else os.getenv("ORACLE_USER")
        self.pwd = password if password else os.getenv("ORACLE_PASSWORD")
        self.port = port if port != 1521 else os.getenv("ORACLE_PORT", 1521)
        import cx_Oracle
        self.conn = cx_Oracle.connect(f"{self.user}/{self.pwd}@{self.host}:{self.port}/{self.instance}")

    def commit(self):
        self.conn.commit()

    def ping(self):
        self.conn.ping()

    def reconnect(self):
        try:
            self.ping()
            flag = 1
        except (cx_Oracle.InterfaceError, cx_Oracle.OperationalError) as e:
            print(e)
            try:
                self.conn = cx_Oracle.connect(f"{self.user}/{self.pwd}@{self.host}:{self.port}/{self.instance}")
                flag = 1
            except (cx_Oracle.InterfaceError, cx_Oracle.OperationalError) as e:
                print(e)
                flag = 0
        finally:
            return flag

    def create_cursor(self):
        return self.conn.cursor()

    def __del__(self):
        self.conn.close()
