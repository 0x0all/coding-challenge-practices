#!/usr/bin/env python

from optparse import OptionParser
from collections import namedtuple
import os.path


Order = namedtuple('Order', ['MessageType', 'OrderID', 'Shares', 'StockSymbol'])

def file_to_str(filename):
    """Returns the contents of filename as a list."""
    with open(filename, 'r') as f:
        return f.read().splitlines()

def get_top_volume(contents):
    """Returns a dictionary of symbols sorted by largest traded shares."""
    def make_add_order_tuple(line):
        """Example: S28800011AAK27GA0000DTS000100SH    0000619200Y"""
        return Order(
            MessageType=line[8:8 + 1],
            OrderID=line[9:9 + 12],
            Shares=int(line[22:22 + 6]),
            StockSymbol=line[28:28 + 6].strip(),
            )

    def make_order_executed_tuple(line):
    	"""Example: S28954344E1K27GA0000D8000005000N1AQ00006"""
    	return Order(
            MessageType=line[8:8 + 1],
            OrderID=line[9:9 + 12],
            Shares=int(line[21:21 + 6]),
            StockSymbol='',
            )

    def make_order_cancel_tuple(line):
    	"""Example: S28800168X1K27GA00000Y000100"""
    	return Order(
            MessageType=line[8:8 + 1],
            OrderID=line[9:9 + 12],
            Shares=int(line[21:21 + 6]),
            StockSymbol='',
            )

    def make_trade_tuple(line):
        """Example: S28954324P4K27GA0000K4B000100DRYS    0001070100000N4AQ0000F"""
        return Order(
            MessageType=line[8:8 + 1],
            OrderID=line[9:9 + 12],
            Shares=int(line[22:22 + 6]),
            StockSymbol=line[28:28 + 6].strip(),
            )
    
    # Dictionary to store executed orders, key: StockSymbol, value: Shares
    traded = {}

    # Dictionary to store added orders, key: OrderID, value: (StockSymbol, Shares)
    queue = {}

    for item in contents:
        try:
            if item[9] == 'A':
            	newtuple = make_add_order_tuple(item[1:])
                queue[newtuple.OrderID] = (newtuple.StockSymbol, newtuple.Shares,)
            
            elif item[9] == 'X':
                newtuple = make_order_cancel_tuple(item[1:])
            	if newtuple.OrderID in queue:
            		if newtuple.Shares < queue[newtuple.OrderID][1]:
            			queue[newtuple.OrderID] = (queue[newtuple.OrderID][0], queue[newtuple.OrderID][1] - newtuple.Shares)
            		elif newtuple.Shares == queue[newtuple.OrderID][1]:
            			del queue[newtuple.OrderID]
            
            elif item[9] == 'E':
                newtuple = make_order_executed_tuple(item[1:])
                if newtuple.OrderID in queue:
                    if queue[newtuple.OrderID][0] in traded:
                        traded[queue[newtuple.OrderID][0]] += newtuple.Shares
                    else:
                        traded[queue[newtuple.OrderID][0]] = newtuple.Shares
                    if newtuple.Shares < queue[newtuple.OrderID][1]:
                        queue[newtuple.OrderID] = (queue[newtuple.OrderID][0], queue[newtuple.OrderID][1] - newtuple.Shares)
                    elif newtuple.Shares == queue[newtuple.OrderID][1]:
                        del queue[newtuple.OrderID]
            
            elif item[9] == 'P':
                newtuple = make_trade_tuple(item[1:])
                if newtuple.StockSymbol in traded:
                    traded[newtuple.StockSymbol] += newtuple.Shares
                else:
                    traded[newtuple.StockSymbol] = newtuple.Shares
            
            else:
                continue

    	except Exception, e:
    		print e

    return sorted(traded.items(), key=lambda x: x[1], reverse=True)



if __name__ == '__main__':
    parser = OptionParser(usage="Usage: python %prog [FILE]...")
    
    options, args = parser.parse_args()

    if not args:
        parser.print_usage()
        exit(1)

    for arg in args:
        if os.path.isfile(arg):
            sorted_tuples = get_top_volume(file_to_str(arg))
            for k, v in sorted_tuples[:10]:
                print k, v
        else:
            print '"{}" is not a file.'.format(arg)
            parser.print_usage()