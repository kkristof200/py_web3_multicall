# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from typing import List

# Pip
from jsoncodable import JSONCodable

# Local
from .function_input import FunctionInput

# -------------------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------------------- class: FunctionResult ---------------------------------------------------- #

class FunctionResult(JSONCodable):

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        contract_address: str,
        function_name: str,
        inputs: List[FunctionInput],
        results = List[any]
    ):
        self.contract_address = contract_address
        self.function_name = function_name
        self.inputs = inputs
        self.results = results


# -------------------------------------------------------------------------------------------------------------------------------- #