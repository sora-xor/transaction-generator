import random

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException
from scalecodec.type_registry import load_type_registry_file
import time
import sys

environments = {
    'dev': 'wss://ws.framenode-1.s1.dev.sora2.soramitsu.co.jp/',
    'test': 'wss://ws.tst.sora2.soramitsu.co.jp',
    'stage': 'wss://ws.stage.sora2.soramitsu.co.jp/'
}

# URL of the node
url = environments[sys.argv[1]]
# mnemonic of the account that makes a transaction
mnemonic = sys.argv[2]
# destination account for transfer
dest_account = sys.argv[3]
# asset id for transfer
asset_id = sys.argv[4]
# total number of transaction
number_of_transactions = int(sys.argv[5])
# percent of transfer transaction
transfer_percent = int(sys.argv[6])

# destination asset of the swap
swap_dest_asset_id = '0x0200050000000000000000000000000000000000000000000000000000000000'

substrate = SubstrateInterface(
    url=url,
    ss58_format=69,
    type_registry_preset='default',
    type_registry=load_type_registry_file('custom_types.json'),

)

keypair = Keypair.create_from_mnemonic(mnemonic)
number_of_transfers = round(number_of_transactions * (transfer_percent / 100))

for i in range(number_of_transfers):
    transfer_call = substrate.compose_call(
        call_module='Assets',
        call_function='transfer',
        call_params={
            'asset_id': asset_id,
            'to': dest_account,
            'amount': str(i * pow(10, 10 + i)) if i < 8 else str(random.randint(1, 10) * pow(10, 18))
        }
    )

    try:
        extrinsic = substrate.create_signed_extrinsic(call=transfer_call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=False)
        print("Extrinsic '{}' sent".format(receipt.extrinsic_hash))
    except Exception as e:
        print("Failed to send: {}".format(e))

    time.sleep(10)

for i in range(number_of_transactions - number_of_transfers):
    swap_amount = str(random.randint(1, 10) * pow(10, 18))
    swap_call = substrate.compose_call(
        call_module='LiquidityProxy',
        call_function='swap',
        call_params={
            'dex_id': '0',
            'input_asset_id': asset_id,
            'output_asset_id': swap_dest_asset_id,
            'swap_amount': {'WithDesiredInput': {'desired_amount_in': swap_amount, 'min_amount_out': '0'}},
            'selected_source_types': ["XYKPool","MulticollateralBondingCurvePool"],
            'filter_mode': 'AllowSelected'
        }
    )
    try:
        extrinsic = substrate.create_signed_extrinsic(call=swap_call, keypair=keypair)
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_inclusion=False)
        print("Extrinsic '{}' sent".format(receipt.extrinsic_hash))

    except Exception as e:
        print("Failed to send: {}".format(e))

    time.sleep(10)
