# python3.7
# encoding: utf-8
"""
@author: Chenjin.Qian
@email:  chenjin.qian@xquant.com
@file:   operate.py
@time:   2020-06-30 16:29
"""



class DatabaseOperate(object):
    def __init__(self, current_conn):
        self.conn = current_conn
        self.cursor = self.conn.create_cursor()

    def check_connection(self):
        flag = self.conn.reconnect()
        return flag

    def get_all(self, sql, **kwargs):
        if not self.check_connection():
            return None
        self.cursor.execute(sql, kwargs)
        out = self.cursor.fetchall()
        return out

    def get_one(self, sql, **kwargs):
        if not self.check_connection():
            return None
        self.cursor.execute(sql, kwargs)
        out = self.cursor.fetchone()
        return out

    def one_column_list(self, sql, **kwargs):
        if not self.check_connection():
            return None
        self.cursor.execute(sql, kwargs)
        rows = self.cursor.fetchall()
        out = [i[0] for i in rows]
        return out

    def get_df(self, sql, index_name=None, **kwargs):
        import pandas as pd
        if not self.check_connection():
            return None
        self.cursor.execute(sql, kwargs)
        rows = self.cursor.fetchall()
        col_name = [i[0] for i in self.cursor.description]
        data = [list(i) for i in rows]
        df = pd.DataFrame(data, columns=col_name)
        table = df if not index_name else df.set_index(index_name)
        return table

    def insert_data(self, sql, data=[]):
        if not self.check_connection():
            return None
        self.cursor.prepare(sql)
        self.cursor.execute(None, data)
        self.conn.commit()

    def execute_sql(self, sql, **kwargs):
        if not self.check_connection():
            return None
        try:
            self.cursor.execute(sql, kwargs)
            self.conn.commit()
            flag = 1
        except Exception as e:
            flag = 0
        finally:
            return flag

    def close_cursor(self):
        self.cursor.close()
