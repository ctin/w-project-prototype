import time

import argparse
import requests
import sys
sys.path.append("..") 

import message_pb2
import response_pb2

def do_it(id):

    phrase = id
    while True:
        try:
            p = message_pb2.Packet()
            p.id = id
            phrase = phrase + 1
            p.phrase = str(phrase)
            
            r = requests.post('http://127.0.0.1:8080/my_handler', p.SerializeToString())
            retText = r.content
            resp = response_pb2.Response()
            resp.ParseFromString(retText)
            if resp.type != response_pb2.Response.SUCCESS:
                print(resp)
        except Exception as e:
            print("exception", e.message)
        time.sleep(1)

if __name__ == '__main__':
#	parser = argparse.ArgumentParser(description='Wierdo client. Require id and phrase.')
#    parser.add_argument('id', type=int,
#                        help='unique id')
#    parser.add_argument('phrase', type=string, help='unique phrase')#
#
#    args = parser.parse_args()

#    do_it(args.id, args.phrase)
 	print ("main")   