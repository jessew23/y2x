import json
import uuid
import hashlib
import hmac
import base64
import random
import time
import os




os.chdir(r'C:\Users\jw887\Pictures') #access directory for json




with open('config-sean.json') as config_file: #open up that config
	data = json.load(config_file)




organization_id = data['organization_id'] #here are the ingredients we're looking for from the json file
key_code = data['key_code']
secret_key_code = data['secret_key_code']




print(organization_id)
print(key_code)
print(secret_key_code)
      



print ("X-Time")




def generate_time():
    return int(round(time.time() * 1000))#this function provides an active time stamp wheneverthe code is run
xTime = str(generate_time()) #here we convert the function's result into a string
print (xTime)




print ("X-Nonce")
def generate_nonce(length=36): #this function provides 36 digit string of random numbers
    return ''.join([str(random.randint(0, 9)) for i in range(length)]) #here we concatanate the smaller pieces
xNonce = generate_nonce()
print (xNonce)




print ("X-Organization-Id")
print (organization_id)
print ("X-Request-Id")      




print (uuid.uuid4()) #this function provides a universally unique identifier




print ("X-Auth")
requestid= 'GET' #these are instructions for our API request and how it's going to access Nicehash
requestpath= '/main/api/v2/mining/rigs2/' #this is a setup for hashing the instructions for our apirequest




#def hashgen():#here's our grand hmac hash function. we're still figuring out how to compile everything 
hash1 = bytes(key_code, 'utf-8')
hash2 = bytes(xTime, 'utf-8')
 #   h = hmac.new(hash1, hash2, digestmod=hashlib.sha256)
 #   return(h.digest())




#def hashgen2():
hash3 = bytes(xNonce, 'utf-8')
hash4 = bytes(organization_id, 'utf-8')
  #  h2 = hmac.new(hash3, hash4, digestmod=hashlib.sha256)
   # return(h2.digest())




#def hashgen3():
hash5 = bytes(requestid,'utf-8')
hash6 = bytes(requestpath,'utf-8')
   # h3 = hmac.new(hash5, hash6, digestmod=hashlib.sha256)
   # return(h3.digest())

#hash7 = bytes(digestmod, 'utf-8')


def hashgen4():
    
    hashx = hash1, hash2, hash3, hash4
    hashy = hash5, hash6
    h4 = hmac.new(hashx, hashy, digestmod=hashlib.sha256)
    return(h4.digest())




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
print (hashgen4())
