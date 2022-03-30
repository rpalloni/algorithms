# supply chain: manufacturer >> transportation >> retailer
# problem: fraud or damage

from hashlib import sha256
import json
from datetime import datetime

class Block:
    def __init__(self, index, previous_hash, current_transaction, timestamp, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.current_transaction = current_transaction
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        first_hash = sha256(block_string.encode()).hexdigest()
        second_hash = sha256(first_hash.encode()).hexdigest()
        return second_hash

    def __str__(self):
        return str(self.__dict__)


class BlockChain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.genesis_block()

    def __str__(self):
        return str(self.__dict__)

    def genesis_block(self):
        genesis_block = Block('Genesis',0x0,[3,4,5,6,7],'datetime.now().timestamp()',0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block.hash)
        self.transactions.append(str(genesis_block.__dict__))
        return genesis_block

    def getLastBlock(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        difficulty = 1
        block.nonce = 0
        computed_hash=block.compute_hash()
        while not (computed_hash.endswith('0' * difficulty) and ('55' * difficulty) in computed_hash):
            block.nonce +=1
            computed_hash = block.compute_hash()
            return computed_hash

    def add(self, data):
        block = Block(len(self.chain), self.chain[-1], data, 'datetime.now().timestamp()',0)
        block.hash = self.proof_of_work(block)
        self.chain.append(block.hash)
        self.transactions.append(block.__dict__)
        return json.loads(str(block.__dict__).replace('\'', '\"'))

    def getTransactions(self, id):
        labels = ['Manufacturer', 'Transportation', 'Retailer']
        if id == 'all':
            for i in range(len(self.transactions)-1):
                print('{}:\n{}\n'.format(labels[i], self.transactions[i+1]))
        elif type(id)==int:
            print(self.transactions[id])



def main():
    manufacturer = {
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial':500100,
                'name': 'blue jeans',
                'from': 'Manufacturer X',
                'to': 'Transporter Y',
                'message': 'product to deliver',
                'digital signature': 'approved',
                'flagged':'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500200,
                'name': 'red t-shirt',
                'from': 'Manufacturer X',
                'to': 'Transporter Y',
                'message': 'product to deliver',
                'digital signature': 'approved',
                'flagged':'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500201,
                'name': 'red t-shirt',
                'from': 'Manufacturer X',
                'to': 'Transporter Y',
                'message': 'product to deliver',
                'digital signature': 'approved',
                'flagged':'N'
                },
            ]
    }

    transportation = {
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial':500100,
                'name': 'blue jeans',
                'from': 'Transporter Y',
                'to': 'Retailer Z',
                'shipping_id':100,
                'message': 'product shipped to retailer. Accepted',
                'digital signature': 'approved',
                'flagged':'N'},
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500200,
                'name': 'red t-shirt',
                'from': 'Transporter Y',
                'to': 'Retailer Z',
                'shipping_id':101,
                'message': 'product shipped to retailer. Accepted',
                'digital signature': 'approved',
                'flagged':'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500201,
                'name': 'red t-shirt',
                'from': 'Transporter Y',
                'to': 'Retailer Z',
                'shipping_id':102,
                'message': 'product damaged. Rejected',
                'digital signature': 'retailer review',
                'flagged':'Y'
                },
            ]
    }

    retailer = {
        'transactions':
            [
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':1,
                'product_serial':500100,
                'name': 'blue jeans',
                'from': 'Retailer Z',
                'to': 'Shop',
                'receiving_id':400,
                'message': 'product OK',
                'digital signature': 'approved',
                'flagged':'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500200,
                'name': 'red t-shirt',
                'from': 'Retailer Z',
                'to': 'Shop',
                'receiving_id':401,
                'message': 'product OK',
                'digital signature': 'approved',
                'flagged':'N'
                },
                {
                'timestamp': datetime.now().timestamp(),
                'product_id':2,
                'product_serial':500201,
                'name': 'red t-shirt',
                'from': 'Retailer Z',
                'to': 'return-to-producer',
                'receiving_id':402,
                'message': 'product KO',
                'digital signature': 'rejected',
                'flagged':'Y'
                },
            ]
    }

    B=BlockChain()
    B.add(manufacturer)
    B.add(transportation)
    B.add(retailer)
    B.getTransactions('all')
    # print('------------------------------')
    # B.getTransactions(2)

if __name__ == '__main__':
    main()
