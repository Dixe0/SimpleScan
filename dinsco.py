import socket

logo = ("""    _    _
  _____  _ _   _  _____           
 |  __ \(_) \ | |/ ____|          
 | |  | |_|  \| | (___   ___ ___  
 | |  | | | . ` |\___ \ / __/ _ \ 
 | |__| | | |\  |____) | (_| (_) |
 |_____/|_|_| \_|_____/ \___\___/ 
                                  
         DNS TO IP TOOL                         
                        \r \n""")
print(logo)

getname = input("Enter a domain name please \n")
addr1 = socket.gethostbyname(getname)

print("Target is:", getname)
print("IP host is:", addr1)
