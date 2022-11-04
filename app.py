import os
hostname = "api.github.com"
response = os.system("ping -c 1 " + hostname)

print(response)
