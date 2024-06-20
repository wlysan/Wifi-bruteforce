### WiFi Password Cracker

#### English

This Python script allows you to perform WiFi network operations such as scanning nearby networks and attempting to crack a WiFi password using a provided list of common passwords.

#### Features:
- **WiFi Scan:** Scans for nearby WiFi networks and displays their SSID and signal strength.
- **Password Testing:** Tests a list of common passwords against a specified WiFi network.
- **Automatic Disconnection:** Automatically disconnects from the WiFi network after testing each password.

#### Dependencies:
- pywifi
- requests

#### Usage:
1. **WiFi Scan:** Run `wifi_scan()` to scan for nearby WiFi networks.
2. **Crack WiFi Password:** Run `main()` and input the SSID of the target WiFi network when prompted. The script will download a list of common passwords and attempt to connect using each one until successful or the list is exhausted.

#### Installation:
1. Clone the repository:
   ```
   git clone https://github.com/wlysan/wifi-bruteforce.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

#### Example:
```python
python wifi_cracker.py
```

#### Disclaimer:
This script is intended for educational purposes only. Use responsibly and only on networks that you own or have explicit permission to test.

---

#### Português

Este script em Python permite realizar operações em redes WiFi, como varredura de redes próximas e tentativa de quebra de senha WiFi usando uma lista fornecida de senhas comuns.

#### Funcionalidades:
- **Varredura WiFi:** Varre redes WiFi próximas e exibe seu SSID e força do sinal.
- **Teste de Senha:** Testa uma lista de senhas comuns contra uma rede WiFi especificada.
- **Desconexão Automática:** Desconecta automaticamente da rede WiFi após testar cada senha.

#### Dependências:
- pywifi
- requests

#### Uso:
1. **Varredura WiFi:** Execute `wifi_scan()` para varrer redes WiFi próximas.
2. **Quebrar Senha WiFi:** Execute `main()` e informe o SSID da rede WiFi alvo quando solicitado. O script irá baixar uma lista de senhas comuns e tentar se conectar usando cada uma até ter sucesso ou a lista ser esgotada.

#### Instalação:
1. Clone o repositório:
   ```
   git clone https://github.com/wlysan/wifi-bruteforce.git
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

#### Exemplo:
```python
python wifi_cracker.py
```

#### Aviso:
Este script destina-se apenas a fins educacionais. Use com responsabilidade e apenas em redes que você possui ou tem permissão explícita para testar.
