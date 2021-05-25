# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import Optional, List

# Pip
from web3_wrapped_contract import WrappedContract
from web3.eth import Eth
from web3.contract import ContractFunction

# Local
from ._abi import abi
from ._utils import Function
from .models import AggregateResult, FunctionResult, Network

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------- class: MulticallContract --------------------------------------------------- #

class Multicall(WrappedContract):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        eth: Eth,
        address: Optional[str] = None
    ):
        super().__init__(
            eth,
            address or Network(eth.chain_id).multicall_adddress,
            abi
        )


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def aggregate(
        self,
        calls: List[ContractFunction]
    ) -> List[List[any]]:
        funcs = [Function(call) for call in calls]

        block_number, outputs = self.functions.aggregate(
            [[func.address, func.data] for func in funcs]
        ).call()

        return AggregateResult(
            block_number=block_number,
            results=[
                FunctionResult(
                    contract_address=func.address,
                    function_name=func.name,
                    inputs=func.inputs,
                    results=list(func.decode_output(output))
                )
                for func, output in zip(funcs, outputs)
            ]
        )


# -------------------------------------------------------------------------------------------------------------------------------- #