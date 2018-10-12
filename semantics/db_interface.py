# Tested on python2.7

import psycopg2
import psycopg2.extras
import logging
import os


class DbInterface:

    db_dict = {'local':['OB_LOCAL_HOSTNAME','OB_LOCAL_USERNAME','OB_LOCAL_PASSWORD'],'remote_1':['OB_REMOTE_1_HOSTNAME','OB_REMOTE_1_USERNAME','OB_REMOTE_1_PASSWORD']}

    def __init__(self,db):


        self.db = 0
        self.connect(db)


    def __del__(self):

        # Close sql connection

        try:
            self.conn.close()
            print('Connection to postgresql closed.')
        except Exception as e:
            logging.exception("message")
            print('Error closing connection to postgresql.')

    def connect(self,db):

        # Create a connection object

        hostname = os.environ[self.db_dict[db][0]]
        username = os.environ[self.db_dict[db][1]]
        password = os.environ[self.db_dict[db][2]]

        database = os.environ['OB_ALL_DATABASE']
        port = os.environ['OB_ALL_PORT']

        try:
            self.conn = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)
            print('Connection to postgresql opened.')

        except Exception as e:
            logging.exception("message")

        self.conn.autocommit = True
        self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


    def test(self):

        try:
            self.cursor.execute("""SELECT * from channel""")
            rows = self.cursor.fetchall()
            rows_len = len(rows)
            for row in rows:
                print(row)
            print(type(rows))
            print(type(rows[0]))
            print(rows[0]['id'])
            print("rows_len,",rows_len)
        except Exception as e:
            logging.exception("message")




def run_test():

    # d = DbInterface('remote_1')
    d = DbInterface('local')
    d.test()



__end__ = '__end__'


if __name__ == '__main__':

    run_test()

    pass