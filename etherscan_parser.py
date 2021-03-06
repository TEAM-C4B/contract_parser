import json
import requests

# example 0x57B116DA40F21f91AeC57329EcB763D29c1B2355
contract_addr = raw_input("input contract address: ")
API_KEY = raw_input("input your etherscan API key: ")

api_url = 'https://api.etherscan.io/api?module=contract&action=getsourcecode&address=' + contract_addr + '&apikey=' + API_KEY

res = requests.get(api_url)
data = res.text

contract_json = json.loads(data)['result']

contract_name = contract_json[0]['ContractName']
contract_code = contract_json[0]['SourceCode']

if contract_code == "":
    print "[-] Sorry, this is not contract nor has contract code"
    exit()

print "[+] Contract Name is \"" + contract_json[0]['ContractName'] + "\""

"""
# you can choose wanted information about contract
for k in contract_code[0].keys():
    print k
"""
menu = raw_input("[*] Enter 1) Save Source Code \n[*] else) Save ABI \n> ")

if (menu == '1'):
    f = open(contract_name + ".sol","w")
    f.write(contract_code)
    f.close()

else:
    f = open(contract_name + "_abi","w")
    f.write(contract_json[0]['ABI'])
    f.close()

