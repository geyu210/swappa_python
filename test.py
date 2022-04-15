import time
print(time.time())
import json
import os
from eth_account import Account
from web3 import Web3
from web3.middleware import geth_poa_middleware
from factorys.ABIs.swappa_router_ABI import  swappa_router
import time
tg_url = 'https://api.telegram.org/bot1860437341:AAGGyVsuBebofh8S2OshKf8bwI9Hx0lLuSM/sendMessage'
#figmeng=https://celo-mainnet--rpc.datahub.figment.io/apikey/8ff3ed3861b9166575eee626599a7557/
#w3 = Web3(Web3.HTTPProvider('https://forno.celo.org'))#
w3 = Web3(Web3.HTTPProvider('https://celo-mainnet--rpc.datahub.figment.io/apikey/8ff3ed3861b9166575eee626599a7557/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)  # celo使用poa，必须用中间件，不然无法解析32位以上的数据。
block = w3.eth.getBlock('latest')
# timestamp = block.timestamp+1000
print(block)







#
#
# path_swap =[
#         "0x918146359264c492bd6934071c6bd31c854edbc3",#//mcusd_address
#         "0xe273ad7ee11dcfaa87383ad5977ee1504ac07568",#//mceur_address
#         "0xd8763cba276a3738e6de85b4b3bf5fded6d6ca73" #//ceur_address
#     ]
# pair_swap = [
#         "0x4ee9b81bde8ec6d3838e8f6967616ffcf460ab9c",#//uniswap_swappa_pair_address  mcusd -> mceur
#         "0x0a96c96a4b791537a612312d8ff6073083d9e991" #//moola_swapppa_pair_address   mceur -> ceur
#     ]
# extra_swap = [
#         "0xf94fea0c87d2b357dc72b743b45a8cb682b0716e03", #//mcusd & mceur ube_pair
#         "0x970b12522ca9b4054807a2c5b736149a5be6f67001" #//
#     ]
#
# InputAmount = "1000000000000000"
# Minioutput  = "817879929918440"