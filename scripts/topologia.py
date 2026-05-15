from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def criar_rede():
    net = Mininet(
        switch=OVSSwitch,
        link=TCLink,
        controller=None
    )

    print("Criando nós...")
    h1 = net.addHost("h1", ip="10.0.0.1/24")
    h2 = net.addHost("h2", ip="10.0.0.2/24")

    s1 = net.addSwitch("s1", failMode="standalone")

    print("Criando links...")
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    print("Iniciando rede...")
    net.start()

    print("Rede criada com sucesso!")
    print("h1 = Cliente - 10.0.0.1")
    print("h2 = Servidor - 10.0.0.2")

    CLI(net)

    print("Finalizando rede...")
    net.stop()

if __name__ == "__main__":
    setLogLevel("info")
    criar_rede()
