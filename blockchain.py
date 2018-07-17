blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]


def add_value(txn_amount,last_tranx = [1]):
    blockchain.append([last_tranx,txn_amount])

def get_user_input():
    return float(input('Your Transation value : '))


txn_amount = get_user_input()
add_value(txn_amount)
txn_amount =get_user_input()
add_value(txn_amount,get_last_blockchain_value())
txn_amount = get_user_input()
add_value(txn_amount,get_last_blockchain_value())
print(blockchain)