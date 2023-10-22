from netmiko import ConnectHandler


def health_check(config):
    command = 'sh ip int brief'
    client = ConnectHandler(**config)
    res = client.send_command(command, use_textfsm=True)

    interfaces = []
    for item in res:
        interfaces.append(item['interface'])
    print(interfaces)

    down_interfaces = []
    for int in interfaces:
        res = client.send_command(f'show interfaces {int}', use_textfsm=True)
        dict = {}
        if res[0]['link_status'] == 'administratively down' or res[0]['protocol_status'] == 'down':
            dict['interface'] = res[0]['interface']
            dict['ip_address'] = res[0]['ip_address']
            dict['mac_address'] = res[0]['mac_address']
            dict['link_status'] = res[0]['link_status']
            dict['protocol_status'] = res[0]['protocol_status']
        if dict != {}:
            down_interfaces.append(dict)

    print(down_interfaces)


if __name__ == "__main__":
    config = {
        "device_type": "cisco_ios",
        "host": "sandbox-iosxe-recomm-1.cisco.com",
        "username": "developer",
        "password": "lastorangerestoreball8876",
    }
    health_check(config)

