import multiprocessing 
import argparse
import client
import time

if __name__ == '__main__':
    start = time.time()

    parser = argparse.ArgumentParser(description='Client pool.')
    parser.add_argument('clients_count', type=int,
                        help='count of clients')

    args = parser.parse_args() 
    for x in xrange(args.clients_count):
        p = multiprocessing.Process(target=client.do_it, args=(x,))
        p.start()


    #pool = Pool(processes=args.clients_count)    # start 4 worker processes

    #pool.map(client.do_it, range(args.clients_count)) 
    print(time.time() - start)

