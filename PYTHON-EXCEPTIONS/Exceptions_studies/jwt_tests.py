from cgitb import reset
from copy import deepcopy
from webbrowser import get
from pydash import at


# encoding and decoding tokens with RS256 (RSA)

# import jwt

# private_key = b"-----BEGIN PRIVATE KEY-----\nMIGEAgEAMBAGByqGSM49AgEGBS..."
# public_key = b"-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEAC..."

# encoded_jwt = jwt.encode({"chave": "payload"}, private_key, algorithm="RS256")
# print("THIS IS THE ENCODED JWT: ", encoded_jwt)

# ---------- testing the dicts

# new_dict = {}

# new_k = ['micheal', 'George', 'Oliva']
# for org_key in new_k:
# 	new_dict[org_key] = 6

# print("Create dictinary with multiple keys:",new_dict)



# ------ other function to extract the value

# def get_all_values(nested_dictionary):
#     for key, value in nested_dictionary.items():
#         data_list = []
#         if type(value) is dict:
#             for key1, val1 in value.items():
#                 data_list.append(val1)
#     return data_list

# get_all_values(nested_dictionary)

# -------- function


def get_all_values(nested_dictionary):
    for key, value in nested_dictionary.items():
        if type(value) is dict:
            get_all_values(value)
        else:
            print(key, ":", value)

# nested_dictionary = {'ResponseCode': 200, 'Data': {'256': {'StartDate': '2022-02-07', 'EndDate': '2022-02-27', 'IsStoreClose': False, 'StoreTypeMsg': 'Manual Processing Stopped', 'is_sync': False}}}

# values = get_all_values(nested_dictionary)
# print(values)


def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v


# -------------------------

nested_dictionary = { 
                'is_payload_decoded': True,
                'decoded_jwt': 
                    {'exp': 1679011271, 
                    'created_at': 1647475271.217852, 
                    'scope': 
                        {'view_type': 'default', 
                        'user_level': 'client', 
                        'features': ['default', 'realtime']},                         
                            'user': 
                                {'unique_id': '40db7fee-6d60-4d73-824f-1bf87edc4491', 
                                'nick_name': 'RAST3', 
                                    'portfolios': 
                                        {'br': 
                                            {'bovespa_account': '000000049-9',
                                             'bmf_account': '49'}, 
                                        'us': {'_': None}}, 
                                            'client_has_br_trade_allowed': False, 
                                            'client_has_us_trade_allowed': False, 
                                            'client_profile': 'investor'}}, 
                                            'message': 'Jwt decoded'}

# values_nested = get_all_values(nested_dictionary)

# a = list(NestedDictValues(nested_dictionary))
# b = deepcopy(a)




# test = set(["bovespa_account", "bmf_account"])
# new = test.issubset(set(nested_dictionary.keys()))
# print(new)

# using logics

# result = "bovespa" in nested_dictionary.values()
# print(result)

# ------ dict comprehension

# bov = 'bovespa_account'
# y = '000000049-9'

# [(k, sv) for k,v in nested_dictionary.items() for sk,sv in v.items() if sk == y]


# ---------------- testing how the dict react

# # jwt_response = jwt_decoded["br"]["bovespa_account"]
# # print(jwt_response)


# keys = ["bovespa_account", "bmf_account"]

# values = list(map(jwt_decoded.get, keys))
# print("THESE ARE THE VALUES", values)
# print("NO VALUE - RESULT == NONE")

# print("XXXXXXXXXXXXXXXXXXXX")

# my_list = at(jwt_decoded, "bovespa_account", "bmf_account")
# print(my_list)
# print("NO VALUE - RESULT == NONE")

# print("XXXXXXXXXXXXXXXX")



# d = {'NIFTY': {11382018: 'NIFTY19SEPFUT', 13177346: 'NIFTY19OCTFUT', 12335874: 'NIFTY19NOVFUT'}}

# y = 11382018


# ----------------- flatten dictionary

def flatten(mydict):
  new_dict = {}
  for key,value in mydict.items():
    if type(value) == dict:
      _dict = {':'.join([key, _key]):_value for _key, _value in flatten(value).items()}
      new_dict.update(_dict)
    else:
      new_dict[key]=value
  return new_dict


flat_dict = flatten(nested_dictionary)
# print(flat_dict)

print(flat_dict['decoded_jwt:user:portfolios:br:bovespa_account'])
print(flat_dict['decoded_jwt:user:portfolios:br:bmf_account'])
