'''
Write a program to allocate orders to couriers in the Test Town of 10 mt square units.
Requirements:
*Distance is calculated only considering orthogonal moves
*An order may (or may not) be generated each unit of time
*Orders will have a pickup point and a delivery point
*Orders will only be assigned to idle couriers
*Couriers will only take one order at a time
*Couriers will move at the specified velocity when they have an assigned order (otherwise they will remain stopped)

Test scenario:
• Given couriers:
    ◦ A: position -3, 2; velocity: 3
    ◦ B: position 0, -2, velocity: 2
    ◦ C: position 4,-3, velocity: 2
• New orders at unit of time:
    ◦ Time 1: pickup: 3,-2, delivery: 3,-4
    ◦ Time 2: pickup: 3,-2, delivery: 2,-1
    ◦ Time 3: pickup: 3,-2, delivery: 4,-3
    ◦ Time 4: 
    ◦ Time 5: pickup: 1,3, delivery: 3,3
'''

from datetime import datetime

class Courier:

    def __init__(self, code, position_point, velocity, idle=True):
        self.code = code
        self.position_point = position_point
        self.velocity = velocity
        self.idle = idle

class Order:

    def __init__(self, code, pickup_point, delivery_point):
        self.code = code
        self.pickup_point = pickup_point
        self.delivery_point = delivery_point
        self.pickup_time = None
        self.delivery_time = None


def distance(courier, order):
    d = (
        abs(courier.position_point[0] - order.pickup_point[0])
        + abs(courier.position_point[1] - order.pickup_point[1])
        + abs(order.pickup_point[0] - order.delivery_point[0])
        + abs(order.pickup_point[1] - order.delivery_point[1])
    )

    '''
    this would be useful for computing the total distance, but is not necessary for the assignment
    Once the courier (regardless of which one is assigned to the order) gets to the pick-up point,
    the distance from pick-up to delivery is the same for any courier.
    Thus, the 3rd point is not really relevant.
    '''

    return d/courier.velocity


def assign_order(couriers, order):
    dist = {}
    if order:
        for courier in couriers:
            if courier.idle:
                d = distance(courier, order)
                dist[courier.code] = d
        print(dist)
        closer = min(dist, key=dist.get)
        for courier in couriers:
            if courier.code == closer:
                # courier.idle = False
                courier.position_point = order.delivery_point # assign new position to courier
                order.pickup_time = datetime.now()
        print(f'Order {order.code} assigned to courier {closer} at {order.pickup_time}')
        return
    print('<<< no order >>>')

def deliver_order(couriers, order):
    # delivery_time = abs(delivery_point-pickup_point) / velocity
    # order.pickup_time + delivery_time = order.delivery_time => idle True
    pass


a = Courier('A', (-3, 2), 3)
b = Courier('B', (0, -2), 2)
c = Courier('C', (4, -3), 2)

o1 = Order('001', (3, -2), (3, -4))
o2 = Order('002', (3, -2), (2, -1))
o3 = Order('003', (3, -2), (4, -3))
o4 = Order('004', (1, 3), (3, 3))

# distance(a, o1)

orders = [o1, o2, o3, None, o4]

for order in orders:
    assign_order([a, b, c], order)
