from geolite2 import geolite2 
import json

def sample_lookup():
    #VARS
    ip_address = "8.8.8.8"
    print("IP: {0}\n".format(ip_address))
    reader = geolite2.reader()
    resp = reader.get(ip_address)
    # output
    print(json.dumps(resp['country']['names'], indent=4) + '\n')
    print(json.dumps(resp['location']['latitude'], indent=4) + '\n')
    print(json.dumps(resp['location']['longitude'], indent=4) + '\n')


def main():
    sample_lookup()


if __name__ == "__main__":
    sample_lookup()

