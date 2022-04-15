import json
import os
from eth_account import Account
from web3 import Web3
from web3.middleware import geth_poa_middleware
from factorys.ABIs.swappa_router_ABI import  swappa_router
import time


w3 = Web3(Web3.HTTPProvider('https://forno.celo.org'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)  # celo使用poa，必须用中间件，不然无法解析32位以上的数据。
block = w3.eth.getBlock('latest')
# timestamp = block.timestamp+1000
print(block)
# with open(f"{os.path.expanduser('~')}/.celokeys/first", 'rt') as f:
#     key = f.read().replace('\n', '').replace('\r', '')
#     f.close()
with open(f"{os.path.expanduser('~')}/.celokeys/first_store", 'rt') as f3:
    json_first = json.load(f3)
    print(json_first)
    print(type(json_first))
    f3.close()

password = input("put in your password\n")
key = Account.decrypt(json_first, password)
# print(key.hex())
my_address = Account.from_key(key).address
print("address is", my_address)

#=============================================授权===========================================================#
# # #Approve for mcusd

#=============================================合约交互===========================================================#
transaction = {
        'from': my_address,
        'gas' : 2201258,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.getTransactionCount(my_address),
        'chainId': 42220
    }


path_swap =[
        "0x918146359264c492bd6934071c6bd31c854edbc3",#//mcusd_address
        "0xe273ad7ee11dcfaa87383ad5977ee1504ac07568",#//mceur_address
        "0xd8763cba276a3738e6de85b4b3bf5fded6d6ca73" #//ceur_address
    ]
pair_swap = [
        "0x4ee9b81bde8ec6d3838e8f6967616ffcf460ab9c",#//uniswap_swappa_pair_address  mcusd -> mceur
        "0x0a96c96a4b791537a612312d8ff6073083d9e991" #//moola_swapppa_pair_address   mceur -> ceur
    ]
extra_swap = [
        "0xf94fea0c87d2b357dc72b743b45a8cb682b0716e03", #//mcusd & mceur ube_pair
        "0x970b12522ca9b4054807a2c5b736149a5be6f67001" #//
    ]

InputAmount = "100000000000000"
Minioutput  = "81787992991844"
swappa_router_contract = w3.eth.contract(address=swappa_router["address"] , abi=swappa_router["abi"])
msg = swappa_router_contract.functions.swapExactInputForOutput(path_swap, pair_swap, extra_swap, InputAmount, Minioutput, my_address, time.time()+60).buildTransaction(transaction)
signed = w3.eth.account.sign_transaction(msg, key)
ans = w3.eth.send_raw_transaction(signed.rawTransaction)
print('Rcelo =====> Scelo Done! hex is -----------> ',ans.hex())
done=w3.eth.wait_for_transaction_receipt(ans.hex())
print('Ube Rcelo  ====>  Scelo is Done!(Ubeswap合约)')

