# FreeBSD
Script to help me:
- converHunspell2xvkbd.sh : script de shell para converter o dicionário do hunspell para lista de palavras utf-8 do xvkbd:
Para instalar o xvkbd use "pkg install xvkbd".
- Wireguard (instale o wireguard-go):
  pkg install wireguard-go; cd ~; wg genkey |tee privatekey|wg pubkey > publickey; cd /usr/local/etc/wireguard/;
  mv wg0.conf wg0.conf.sample;
  Edite seu wg0.conf ou copie do seu provedor, p.ex.: cp protonvpn.conf wg0.conf
  Confira o arquivo e desligue o port filthy: cat wg0.conf; pfctl -d;
  Rode: "wg-quick up wg0" para desligar "wg-quick down wg0".
- Leitura Qrcode e datamatrix (instale o zbar: pkg install zbar).
- Escanear por dentro do eog/eom usando python3 e pyinsane: testpyinsane2.py
    instale o sane (pkg install sane-backends) e o modulo pyinsane2 (pip install pyinsane2).
- 
