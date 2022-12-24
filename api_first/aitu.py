import json
import time
import requests as r
from web3 import Web3

address = '0x16aEa9952f9d308b1A1DeF3684b0F18111A0aAbF'
def vse(address):
    score = 0
    
    data = {
        'bsc': {
            'name': 'Binance Smart Chain',
            'link': 'https://api.bscscan.com/api?module=account&action=txlist&address=',
            'key': 'Y8W17VRHSSE1RWXN9AGZKPHACYIK2XCQMJ',
            'rpc':'https://rpc-bsc.bnb48.club',
            'busd':'0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56',
            'usdt':'0x55d398326f99059ff775485246999027b3197955',
            'usdc':'0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d',
        }, 
    }
    
    w3 = Web3(Web3.HTTPProvider(data['bsc']['rpc']))
    bab_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Attest","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Revoke","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"OPERATOR_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"}],"name":"attest","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"addrs","type":"address[]"}],"name":"batchAttest","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"addrs","type":"address[]"}],"name":"batchRevoke","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"burn","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name_","type":"string"},{"internalType":"string","name":"symbol_","type":"string"},{"internalType":"address","name":"admin_","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isAdmin","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isOperator","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"}],"name":"revoke","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uri","type":"string"}],"name":"setBaseTokenURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"}],"name":"tokenIdOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
    bab_proxycontract_address = '0x2B09d47D550061f995A3b5C6F0Fd58005215D7c8'
    bab_contract = w3.eth.contract(address = w3.toChecksumAddress(bab_proxycontract_address) , abi = bab_abi)
    balance = bab_contract.functions.balanceOf(w3.toChecksumAddress(address)).call()
    # return f'bab token balance - {balance}'
    if balance > 0:
        score+=10
        b = 0
        b +=10
        
        
    


    try:
        url = 'https://api.bscscan.com/api?module=account&action=txlist&address=' + address + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + 'Y8W17VRHSSE1RWXN9AGZKPHACYIK2XCQMJ'

        response = r.get(url)
        json_response = json.loads(response.text)
        transactions = json_response["result"]

        times = []
        linked_addresses = []
        for transaction in transactions:
            times.append(transaction["timeStamp"])
            if transaction["to"] not in linked_addresses:
                linked_addresses.append(transaction["to"])


        diffs = []
        for i in range(len(times) - 1):
            diffs.append(int(times[i + 1]) - int(times[i]))
        average = sum(diffs) / len(diffs)
        hours = average // 3600
        minutes = (average % 3600) // 60
        seconds = (average % 3600) % 60


        transaction = 0
        if len(transactions) > 1000:
            score += 5
            
            transaction +=5
        elif len(transactions)> 100:
            score += 1
            transaction +=1
            

        hourss = 0
        if hours < 10:
            score += 5
            hourss +=5
            
        elif hours < 48:
            score+=1
            hourss += 1

    except KeyError:
        pass
    except Exception as e:
        return f"Binance chain: Ошибка! Возможно, ты не взаимодействовал с этой сетью или адрес неверный\n"
        


    time.sleep(5)
    key = data["bsc"]['key']
    url = f'https://api.bscscan.com/api?module=account&action=balance&address={address}&apikey={key}'
    response = r.get(url)
    bnb_balance = (int(response.json()['result'])/10**18)
    if bnb_balance > 1:
        score+=5
        
        bnb_balancee = 5
    elif bnb_balance > 0.1:
        score+1
        bnb_balancee = 1
        

    tokens = [data['bsc']['busd'],data['bsc']['usdc'],data['bsc']['usdt']]
    busd = tokens[0]
    usdc = tokens[1]
    usdt = tokens[2]

    url = f'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={busd}&address={address}&tag=latest&apikey=YourApiKeyToken'
    busd_balance = int(r.get(url).json()['result'])/10**18
    if busd_balance > 1000:
        score += 5
        
    elif busd_balance > 100:
        score+=1
        

    
    time.sleep(5)
    url = f'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={usdc}&address={address}&tag=latest&apikey=YourApiKeyToken'
    usdc_balance = int(r.get(url).json()['result'])/10**18
    if usdc_balance > 1000:
        score += 5
        
    elif usdc_balance > 100:
        score+=1
        
    time.sleep(5)
    url = f'https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress={usdt}&address={address}&tag=latest&apikey=YourApiKeyToken'
    usdt_balance = int(r.get(url).json()['result'])/10**18
    if usdt_balance > 1000:
        score += 5
        
    elif usdt_balance > 100:
        score+=1
        

    # return f'Your BNB Balance: {bnb_balance}\nYour BUSD balance: {busd_balance}\nYour USDC balance:{usdc_balance}\nYour USDT balance:{usdt_balance}'
    
    time.sleep(5)
    address = address
    key = data["bsc"]['key']
    pancake_swap = '0x10ED43C718714eb63d5aA57B78B54704E256024E'
    venus = '0x17f4a746A7BF05C3e24A2BB7d7d25e4d3e5BBE3e'
    
    url = 'https://api.bscscan.com/api?module=account&action=txlist&address=' + address + "&startblock=0&endblock=99999999&page=1&offset=10000&sort=asc&apikey=" + key 
    response = r.get(url).json()['result']
    pancake_swap_activity = 0
    venus_activity = 0
    for transaction in response:
        if transaction['to'] == pancake_swap.lower():
            if transaction['isError'] == '0':
                pancake_swap_activity+=1
        if transaction['to'] == venus.lower():
            if transaction['isError'] == '0':
                venus_activity+=1
    if pancake_swap_activity > 100:
        score+=5
        
    elif pancake_swap_activity > 10:
        score+=1
        

    if venus_activity > 100:
        score+=5
        
    elif venus_activity > 10:
        score+=1
        
    # res = f'Your transactions with Pancake Swap:{pancake_swap_activity}\nYour transactions with Venus swap protocol:{venus_activity}'
    return {"Overall": score}
        
