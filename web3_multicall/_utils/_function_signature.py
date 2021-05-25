# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from web3.contract import ContractFunction
from web3._utils.abi import normalize_event_input_types

from eth_abi import encode_single, decode_single
from eth_utils import function_signature_to_4byte_selector

# -------------------------------------------------------------------------------------------------------------------------------- #



# --------------------------------------------------- class: FunctionSignature --------------------------------------------------- #

class FunctionSignature:

    # --------------------------------------------------------- Init --------------------------------------------------------- #

    def __init__(
        self,
        function: ContractFunction
    ):
        self.name = function.abi['name']

        self.inputs = [{
            'name': arg['name'],
            'type': arg['type']
        } for arg in normalize_event_input_types(function.abi.get('inputs', []))]
        self.input_types_signature = '({})'.format(','.join([inp['type'] for inp in self.inputs]))
        self.output_types_signature = '({})'.format(','.join(
            [arg['type'] for arg in normalize_event_input_types(function.abi.get('outputs', []))]
        ))

        self.signature = '{}{}'.format(
            self.name,
            self.input_types_signature
        )

        self.fourbyte = function_signature_to_4byte_selector(self.signature)


    # ---------------------------------------------------- Public methods ---------------------------------------------------- #

    def encode_data(self, args=None) -> str:
        return self.fourbyte + encode_single(self.input_types_signature, args) if args else self.fourbyte

    def decode_data(self, output):
        return decode_single(self.output_types_signature, output)


# -------------------------------------------------------------------------------------------------------------------------------- #