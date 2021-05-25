# web3_multicall

![PyPI - package version](https://img.shields.io/pypi/v/web3_multicall?logo=pypi&style=flat-square)
![PyPI - license](https://img.shields.io/pypi/l/web3_multicall?label=package%20license&style=flat-square)
![PyPI - python version](https://img.shields.io/pypi/pyversions/web3_multicall?logo=pypi&style=flat-square)
![PyPI - downloads](https://img.shields.io/pypi/dm/web3_multicall?logo=pypi&style=flat-square)

![GitHub - last commit](https://img.shields.io/github/last-commit/kkristof200/py_web3_multicall?style=flat-square)
![GitHub - commit activity](https://img.shields.io/github/commit-activity/m/kkristof200/py_web3_multicall?style=flat-square)

![GitHub - code size in bytes](https://img.shields.io/github/languages/code-size/kkristof200/py_web3_multicall?style=flat-square)
![GitHub - repo size](https://img.shields.io/github/repo-size/kkristof200/py_web3_multicall?style=flat-square)
![GitHub - lines of code](https://img.shields.io/tokei/lines/github/kkristof200/py_web3_multicall?style=flat-square)

![GitHub - license](https://img.shields.io/github/license/kkristof200/py_web3_multicall?label=repo%20license&style=flat-square)

## Description

web3_multicall

## Install

~~~~bash
pip install web3_multicall
# or
pip3 install web3_multicall
~~~~

## Usage

~~~~python
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
~~~~

## Dependencies

[eth-abi](https://pypi.org/project/eth-abi), [eth-utils](https://pypi.org/project/eth-utils), [jsoncodable](https://pypi.org/project/jsoncodable), [kw3](https://pypi.org/project/kw3), [web3](https://pypi.org/project/web3), [web3-wrapped-contract](https://pypi.org/project/web3-wrapped-contract)