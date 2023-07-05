'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from math import floor

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net_int = 0
    net_float = 0.0
    
    for item in order.items:
        item_int = floor(item.amount)
        item_float = item.amount - item_int
        if item.type == 'payment':
            net_int += item_int
            net_float += item_float
        elif item.type == 'product':
            net_int -= item_int * item.quantity
            net_float -= item_float * item.quantity
        else:
            return("Invalid item type: %s" % item.type)
    item
    net = net_int + round(net_float,2)
    if net != 0.0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
