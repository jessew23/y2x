import json
import uuid
import hashlib
import hmac
import base64
import random
import time
import os
import requests

organization_id = data['organization_id']
key_code = data['key_code']
secret_key_code = data['secret_key_code']
xTime = str(generate_time()) 
xNonce = generate_nonce()
#requestid=
requestpath= "https://api2.nicehash.com/main/api/v2/mining/algo/stats" 



#access directory for json
os.chdir(r'C:\Users\jw887\Pictures') 

#open up that config
with open('config-sean.json') as config_file: 
	data = json.load(config_file)

#here are the ingredients we're looking for from the json file


#this function provides an active time stamp wheneverthe code is run
#here we convert the function's result into a string
def generate_time():

    return int(round(time.time() * 1000))

#this function provides 36 digit string of random numbers
#here we concatanate the smaller pieces
def generate_nonce(length=36): 

    return ''.join([str(random.randint(0, 9)) for i in range(length)]) 


def hashgen():
    hash1 = bytes(key_code, 'utf-8')
    hash2 = bytes(xTime, 'utf-8')
    h = hmac.new(hash1, hash2, digestmod=hashlib.sha256)    
    h.update(bytes(xNonce, 'utf-8'));
    h.update(bytes(organization_id, 'utf-8'));
    h.update(bytes(requestid,'utf-8'));
    h.update(bytes(requestpath,'utf-8'));
    #h.update(bytes(digestmod, 'utf-8'))

    return(h.digest())


print(organization_id)
print(key_code)
print(secret_key_code)
print ("X-Time")
print (xTime)
print ("X-Nonce")
print (xNonce)
print ("X-Organization-Id")
print (organization_id)
print ("X-Request-Id")      
print (uuid.uuid4())
print ("X-Auth")
print (hashgen())


    #finalHash = ''
    #finalHash = finalHash + key_code
    #finalHash = finalHash + str(xTime)
    #finalHash = finalHash + xNonce
#    finalHash = finalHash + ''
 #   finalHash = finalHash + organization_id
  #  finalHash = finalHash + ''
   # finalHash = finalHash + 'GET'
  # finalHash = finalHash + '/main/api/v2/mining/rigs2/'
 #  finalHash = finalHash + ''
 #   finalHash = finalHash + ''    
#    return(finalHash)

