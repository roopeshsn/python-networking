from netmiko import ConnectHandler
from netmiko import exceptions as netmiko_exceptions

def main(config, command):
    client = None
    try:
        client = ConnectHandler(**config)
        res = client.send_command(command)
        print(res)
    except ConnectionAbortedError:
        print("An established connection was aborted by the software in your host machine")
    except netmiko_exceptions.NetmikoAuthenticationException:
        print("Auth failed!")
    except netmiko_exceptions.NetmikoTimeoutException:
        print("Connection timed out!")
    finally:
        if client != None:
            client.disconnect()

if __name__ == "__main__":
    config = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "lastorangerestoreball8876",
    }
    command = 'sh ip int brief'
    main(config, command)

