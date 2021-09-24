# transaction-generator

This script generates and send the list of transactions to SORA network for test purposes.
The script does the following:
1. Transfers
2. Swaps of the selected asset to PSWAP

## How to run the script
Just `pip3 install substrate-interface` and `pip3 install scalecodec`.
After the user `python3` in order to run the script.
Script parameters:
1. environment. May be `dev`, `test`, `stage`
2. account's passphrase. Specify it in quotes, for example `'cheap ........'`
3. destination account for transfer. For example `cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1`
4. asset id that should be transferred and swapped. For example `0x0200000000000000000000000000000000000000000000000000000000000000`
5. total number of transactions that should be executed. For example `10`.
6. percent of transfer transactions from the total number of transactions. For example `10` means 10% of transactions will be transfers.

## Examples
Makes 10 transactions on `dev` environment, 1 of them is transfer (10% from 10 transactions). Transfers dest address is `cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1`. Asset `0x0200000000000000000000000000000000000000000000000000000000000000` should be transferred and swapped.
```
python3 transaction_generator.py dev 'cheap ...' cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1 0x0200000000000000000000000000000000000000000000000000000000000000 10 10
```

Makes 10 transactions on `dev` environment, 0 of them are transfers (0% from 10 transactions). Asset `0x0200000000000000000000000000000000000000000000000000000000000000` should be swapped.
```
python3 transaction_generator.py dev 'cheap ...' cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1 0x0200000000000000000000000000000000000000000000000000000000000000 10 0
```

Makes 10 transactions on `dev` environment, 10 of them are transfers (100% from 10 transactions). Transfers dest address is `cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1`. Asset `0x0200000000000000000000000000000000000000000000000000000000000000` should be swapped. 
```
python3 transaction_generator.py dev 'cheap ...' cnUfVtQDZCkUngZ1Pudmb9qDTeHHAmuCm6vsHNzGNnMKg83x1 0x0200000000000000000000000000000000000000000000000000000000000000 10 100
```
