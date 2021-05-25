# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from enum import IntEnum

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------------- enum: Network -------------------------------------------------------- #

class Network(IntEnum):
    Mainnet    = 1
    Rinkeby    = 4
    Görli      = 5
    Kovan      = 42
    BSC        = 56
    BSCTestnet = 97
    xDai       = 100


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def multicall_adddress(self) -> str:
        return {
            Network.Mainnet:    '0xeefBa1e63905eF1D7ACbA5a8513c70307C1cE441',
            Network.Rinkeby:    '0x42Ad527de7d4e9d9d011aC45B31D8551f8Fe9821',
            Network.Görli:      '0x77dCa2C955b15e9dE4dbBCf1246B4B85b651e50e',
            Network.Kovan:      '0x2cc8688C5f75E365aaEEb4ea8D6a480405A48D2A',
            Network.BSC:        '0x1Ee38d535d541c55C9dae27B12edf090C608E6Fb',
            Network.BSCTestnet: '0x6e5bb1a5ad6f68a8d7d6a5e47750ec15773d6042',
            Network.xDai:       '0xb5b692a88BDFc81ca69dcB1d924f59f0413A602a',
        }[self]


# -------------------------------------------------------------------------------------------------------------------------------- #