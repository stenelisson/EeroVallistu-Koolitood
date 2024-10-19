# Importib 'os' mooduli, mis võimaldab käivitada operatsiooni käske.
import os

# Funktsioon serveri pingimiseks
def ping_server(server):
    # Käivitab 'ping' käsu, et saata 1 andmepakett serveri IP-aadressile.
    response = os.system(f"ping -n 1 {server}")
    # Kui 'response' väärtus on 0, siis server vastas ja funktsioon tagastab tõene (True), ehk server on ühendatud.
    # Kui 'response' on midagi muud kui 0, siis server ei vastanud ja funktsioon tagastab väär (False), ehk server pole ühendatud.
    return response == 0

# Serverite nimekiri
# Serverite IP-aadressid, mida testib (kontrollib), kas need on saadaval.
servers = ["192.168.1.1", "1.1.1.1", "192.168.0.1"]

# Muutujad serverite oleku ettekandmiseks
 # Tühi nimekiri, kuhu lisatakse serverid, mis vastavad (server on ühendatud).
online_servers = []
# Tühi nimekiri, kuhu lisatakse serverid, mis ei vasta (server pole ühendatud).
offline_servers = []

# Tsükkel serverite pingimiseks
for server in servers:
    # Kontrollib, kas server on saadaval, kutsudes esile 'ping_server' funktsiooni.
    # Kui server vastab, lisatakse see 'online_servers' listi.
    if ping_server(server):
        online_servers.append(server)
    # Kui server ei vasta, lisatakse see 'offline_servers' listi.
    else:
        offline_servers.append(server)

# Tulemuste kuvamine
# Kuvab kõik serverid, mis reageerisid ja näitab "Online servers".
print("Online servers:", online_servers)
# Kuvab kõik serverid, mis ei reageeri ja näitab "Offline servers".
print("Offline servers:", offline_servers)