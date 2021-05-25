from kw3 import KWeb3
from web3_multicall import Multicall

w3 = KWeb3('https://bsc-dataseed.binance.org/')
busd = w3.busd()

multicall = Multicall(w3.eth) # address is not needed, unless you are on an unsupported  chain (check 'web3_multicall/models/enums/network.py')
multicall_result = multicall.aggregate([
    busd.name_method(),
    busd.symbol_method(),
    busd.decimals_method(),
    busd.total_supply_method(),
    busd.balance_of_method('0xA426d6e651aAFcd6e26865d65286c64f34714428')
])

multicall_result.jsonprint()
# Prints
# 
# {
#     "block_number": 7714239,
#     "results": [
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "name",
#             "inputs": [],
#             "results": [
#                 "BUSD Token"
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "symbol",
#             "inputs": [],
#             "results": [
#                 "BUSD"
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "decimals",
#             "inputs": [],
#             "results": [
#                 18
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "totalSupply",
#             "inputs": [],
#             "results": [
#                 4200999999996203280118545633
#             ]
#         },
#         {
#             "contract_address": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
#             "function_name": "balanceOf",
#             "inputs": [
#                 {
#                     "name": "account",
#                     "value": "0xA426d6e651aAFcd6e26865d65286c64f34714428",
#                     "solidity_type": "address"
#                 }
#             ],
#             "results": [
#                 0
#             ]
#         }
#     ]
# }