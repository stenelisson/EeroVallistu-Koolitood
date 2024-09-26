import os

# Funktsioon serveri pingimiseks
def ping_server(server):
    response = os.system(f"ping -n 1 {server}")
    return response == 0

# Serverite nimekiri
servers = ["192.168.1.1", "1.1.1.1", "192.168.0.1"]

# Muutujad serverite oleku ettekandmiseks
online_servers = []
offline_servers = []

# Tsükkel serverite pingimiseks
for server in servers:
    if ping_server(server):
        online_servers.append(server)
    else:
        offline_servers.append(server)

# Tulemuste kuvamine
print("Online servers:", online_servers)
print("Offline servers:", offline_servers)