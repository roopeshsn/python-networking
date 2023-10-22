# Network Management

## Getting Started

### Activate Venv

```
.venv\Scripts\activate
```

If you encounter the following error:

```
.venv\Scripts\activate : File C:\Users\rosarava\developer\projects\network-management\.venv\Scripts\Activate.ps1 cannot be loaded because running 
scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

Then you need to temporarily change the PowerShell execution policy to allow scripts to run,

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

### Installing Dependencies

```
pip install -r requirements.txt
```

### Run

```
python script.py
```

#### 

## Tasks

- [ ] Bulk Configuration Changes
- [ ] Network Health Check
- [ ] Automated Troubleshooting
- [ ] Device Inventory Management
- [ ] Network Topology Discovery
- [ ] Performance Monitoring

You can find the description of the tasks in the below section.

## Tasks Description

Bulk Configuration Changes: Develop a script that reads a list of network devices and a list of commands from files, then uses Netmiko to execute these commands on all devices. This can be helpful when you need to make bulk configuration changes on multiple devices.

Network Health Check: Write a script that periodically connects to network devices, runs specific commands (show interface status, show ip route, etc.), and checks the output for any anomalies. If an anomaly is detected (like an interface going down), the script could send an alert email

Automated Troubleshooting: Design a script that automates common network troubleshooting steps. For example, if a user reports that they can’t access a certain server, the script could automatically check the status of relevant interfaces, verify routing and VLAN configurations, etc.

Device Inventory Management: Create a script that connects to all devices in the network, collects essential information (show version, show inventory, etc.), and stores this information in a database or a spreadsheet. This can be useful for maintaining an up-to-date inventory of all network devices.

Network Topology Discovery: You can write a script that logs into a network device, runs commands like show cdp neighbors or show lldp neighbors, and parses the output to discover the network topology. This could be extended to create a visual representation of the network.

Performance Monitoring: Create a script that periodically logs into network devices and collects performance data like CPU usage, memory usage, interface statistics, etc. This data could be stored in a time-series database for long-term monitoring and trend analysis.

Note: The tasks and its descriptions are generated by GAI.