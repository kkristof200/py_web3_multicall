# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import List

# Pip
from web3.contract import ContractFunction

# Local
from ._function_signature import FunctionSignature
from ..models import FunctionInput

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- class: Function ------------------------------------------------------- #

class Function:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        function: ContractFunction
    ):
        self.__signature = FunctionSignature(function)
        self.__function = function


    # --------------------------------------------------- Public properties -------------------------------------------------- #

    @property
    def name(self) -> str:
        return self.__function.function_identifier

    @property
    def arguments(self) -> List[any]:
        return list(self.__function.arguments)

    @property
    def inputs(self) -> List[FunctionInput]:
        return [
            FunctionInput(
                name=_input['name'],
                value=argument,
                solidity_type=_input['type']
            )

            for _input, argument in zip(
                self.__signature.inputs,
                self.__function.arguments
            )
        ]

    @property
    def address(self) -> str:
        return self.__function.address

    @property
    def data(self) -> str:
        return self.__signature.encode_data(self.__function.args)


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def decode_output(
        self,
        output
    ) -> List[any]:
        return self.__signature.decode_data(output)


# -------------------------------------------------------------------------------------------------------------------------------- #