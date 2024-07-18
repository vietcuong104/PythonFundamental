def defangIP(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

ip_address = "192.168.1.255"
print(defangIP(ip_address))