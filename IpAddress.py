def ip_to_operating_system(octet):

    if (octet ^ 1 == octet + 1):
        return "Windows"

    elif octet == 0 :
        return "Router"

    else:
        return "Linux"

# Testing Code
print(ip_to_operating_system(1001101))