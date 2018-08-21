    
import cherrypy
import sys
sys.path.append("..") 

import message_pb2
import response_pb2
import time

import mysql.connector

config = {
  'user': 'ctin',
  'password': 'ctin',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'ctin',
  'raise_on_warnings': True,
}

current_milli_time = lambda: int(round(time.time() * 1000))

link = mysql.connector.connect(**config)
class HelloWorld(object):
    @cherrypy.expose
    def my_handler(self):
        try:
            body = cherrypy.request.body.read()
            p = message_pb2.Packet()
            p.ParseFromString(body)

            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()

            add_record = ("INSERT INTO ctin "
                  "(id, phrase, timestamp) "
                  "VALUES (%s, %s, %s)")
            cursor.execute(add_record, (p.id, p.phrase, current_milli_time()))

            # Make sure data is committed to the database
            cnx.commit()

            cursor.close()
            cnx.close()
        except Exception as e:
            print("exception", e.message)
            resp = response_pb2.Response()
            resp.type = response_pb2.Response.ERROR
            resp.text = e.message
            return resp.SerializeToString()

        resp = response_pb2.Response()
        resp.type = response_pb2.Response.SUCCESS
        resp.text = "success"
 
        return resp.SerializeToString()


if __name__ == '__main__':
    #cherrypy.config.update({'log.screen': False})

    cherrypy.quickstart(HelloWorld())