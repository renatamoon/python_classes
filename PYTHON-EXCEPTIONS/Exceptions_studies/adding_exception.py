info = {
    "first_name": "Renata",
    "surname": "Ahad"
}

# try:
#     print(info["first_name"])
# except Exception as e:
#    print("There's no data")


try: # if the code bellow is right, it will be printed
    print(info["first_name"])
except KeyError as e: # if an error occurs it will be printed
    print("You tried to access a key")
    print(f'Key: {e}')
else:
    print("No error occured")
finally:
    print("The program has finished!!")