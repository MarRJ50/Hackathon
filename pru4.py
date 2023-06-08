#!/usr/bin/python

"""
Programacion de topologia para datacenter basada en modelo de 3 capas
Topologia No. AB-1
"""
from mininet.net import Mininet
from mininet.link import TCLink
from mininet.node import OVSSwitch, Controller, RemoteController
from mininet.topolib import TreeTopo
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI

#definir controladores    -variables globales
#c0= RemoteController('c0', '192.168.50.7', 6633)    #ODL 
c0= RemoteController('c0', '127.0.0.1', 6633) #ODL
c1= RemoteController('c1', '10.20.132.82', 6633) #ODL
#c2= RemoteController('c2', '10.0.3.15', 6633)    #ODL
#192.168.50.80
#192.168.50.7
# definir los switches que atendara cada controlador:  c1 del s1 al s21,  c2 del s22 al s144
cmap={'s1': c0,'s2': c0, 's3': c0, 's4': c0, 's5': c0, 's6': c0, 's7': c0, 's8': c0,'s9': c0, 's10': c0, 's11': c0, 's12': c0, 's13': c0, 's14': c0, 's15': c0,'s16': c0, 's17': c0, 's18': c0, 's19': c0, 's20': c0, 's21': c0,'s22': c1, 's23': c1, 's24':c1, 's25':c1, 's26':c1,'s27':c1, 's28':c1, 's29':c1, 's30':c1, 's31':c1, 's32':c1, 's33':c1, 's34':c1, 's35':c1, 's36':c1, 's37':c1, 's38':c1, 's39':c1, 's40':c1, 's41':c1, 's42':c1, 's43':c1, 's44':c1}

class DataCenterA(Topo):

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(DataCenterA, self).__init__(**opts)

        # Agregar hosts para la simulacion
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
 	h4 = self.addHost('h4')
	h5 = self.addHost('h5')
	h6 = self.addHost('h6')
	h7 = self.addHost('h7')
        h8 = self.addHost('h8')
 	h9 = self.addHost('h9')
	h10 = self.addHost('h10')
	h11 = self.addHost('h11')
	h12 = self.addHost('h12')
 	h13 = self.addHost('h13')
	h14 = self.addHost('h14')
	
        # Agregar switches Dominio A
    	s1 = self.addSwitch('s1', dpid="0000000000000001")
    	s2 = self.addSwitch('s2', dpid="0000000000000002")
    	s3 = self.addSwitch('s3', dpid="0000000000000003")
    	s4 = self.addSwitch('s4', dpid="0000000000000004")
	s5 = self.addSwitch('s5', dpid="0000000000000005")
	s6 = self.addSwitch('s6', dpid="0000000000000006")
	s7 = self.addSwitch('s7', dpid="0000000000000007")
 	s8 = self.addSwitch('s8', dpid="0000000000000008")
    	s9 = self.addSwitch('s9', dpid="0000000000000009")
    	s10 = self.addSwitch('s10', dpid="0000000000000010")
    	s11 = self.addSwitch('s11', dpid="0000000000000011")
	s12 = self.addSwitch('s12', dpid="0000000000000012")
	s13 = self.addSwitch('s13', dpid="0000000000000013")
	s14 = self.addSwitch('s14', dpid="0000000000000014")
 	s15 = self.addSwitch('s15', dpid="0000000000000015")
    	s16 = self.addSwitch('s16', dpid="0000000000000016")
    	s17 = self.addSwitch('s17', dpid="0000000000000017")
    	s18 = self.addSwitch('s18', dpid="0000000000000018")
	s19 = self.addSwitch('s19', dpid="0000000000000019")
	s20 = self.addSwitch('s20', dpid="0000000000000020")
	s21 = self.addSwitch('s21', dpid="0000000000000021")	
	
	# Agregar switches Dominio B
	s22 = self.addSwitch('s22', dpid="0000000000000022")
	s23 = self.addSwitch('s23', dpid="0000000000000023")
	s24 = self.addSwitch('s24', dpid="0000000000000024")
	s25 = self.addSwitch('s25', dpid="0000000000000025")
	s26 = self.addSwitch('s26', dpid="0000000000000026")
	s27 = self.addSwitch('s27', dpid="0000000000000027")
	s28 = self.addSwitch('s28', dpid="0000000000000028")
	s29 = self.addSwitch('s29', dpid="0000000000000029")
	s30 = self.addSwitch('s30', dpid="0000000000000030")
	s31 = self.addSwitch('s31', dpid="0000000000000031")
	s32 = self.addSwitch('s32', dpid="0000000000000032")
	s33 = self.addSwitch('s33', dpid="0000000000000033")
	s34 = self.addSwitch('s34', dpid="0000000000000034")
	s35 = self.addSwitch('s35', dpid="0000000000000035")
	s36 = self.addSwitch('s36', dpid="0000000000000036")
	s37 = self.addSwitch('s37', dpid="0000000000000037")
	s38 = self.addSwitch('s38', dpid="0000000000000038")
	s39 = self.addSwitch('s39', dpid="0000000000000039")
	s40 = self.addSwitch('s40', dpid="0000000000000040")
	s41 = self.addSwitch('s41', dpid="0000000000000041")
	s42 = self.addSwitch('s42', dpid="0000000000000042")
	s43 = self.addSwitch('s43', dpid="0000000000000043")
	s44 = self.addSwitch('s44', dpid="0000000000000044")


	# Hosts del Dominio A, conectados a Switch#
	self.addLink(h1, s14, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h2, s15, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h3, s16, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h4, s17, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h5, s18, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h6, s19, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h7, s20, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h8, s21, bw=100, max_queue_size=1000, use_htb=True)

	# Hosts del Dominio B, conectados a Switch#
	self.addLink(h9, s39, bw=100, max_queue_size=1000, use_htb=True)
        self.addLink(h10, s40, bw=100, max_queue_size=1000, use_htb=True)
        self.addLink(h11, s41, bw=100, max_queue_size=1000, use_htb=True)
	self.addLink(h12, s42, bw=100, max_queue_size=1000, use_htb=True)
        self.addLink(h13, s43, bw=100, max_queue_size=1000, use_htb=True)
        self.addLink(h14, s44, bw=100, max_queue_size=1000, use_htb=True)
	

 	# Agregar enlaces para switches Dominio A
        # Nomenclatura retraso, perdida de paquetes, fluctuaciones, ancho de banda  - todos los parametros en 0, solo ancho de banda
	self.addLink(s1, s2, bw=97, delay='10ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s1, s3, bw=94, delay='5ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s1, s4, bw=99, delay='8ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s1, s5, bw=93, delay='3ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s2, s6, bw=93, delay='18ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s2, s8, bw=90, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s2, s10, bw=98, delay='24ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s2, s12, bw=91, delay='8ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s3, s7, bw=86, delay='11ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s3, s9, bw=97, delay='21ms', loss=0.004, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s3, s11, bw=95, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s3, s13, bw=82, delay='16ms', loss=0.003, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s4, s6, bw=88, delay='13ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s4, s8, bw=97, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s4, s10, bw=90, delay='16ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s4, s12, bw=96, delay='18ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s5, s7, bw=84, delay='17ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s5, s9, bw=92, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s5, s11, bw=94, delay='21ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s5, s13, bw=97, delay='15ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s6, s7, bw=82, delay='8ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s6, s14, bw=86, delay='23ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s6, s15, bw=81, delay='3ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s7, s14, bw=79, delay='3ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s7, s15, bw=85, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s8, s9, bw=78, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s8, s16, bw=96, delay='18ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s8, s17, bw=87, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s9, s16, bw=76, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s9, s17, bw=83, delay='14ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s10, s11, bw=80, delay='11ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s10, s18, bw=83, delay='13ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s10, s19, bw=82, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s11, s18, bw=80, delay='22ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s11, s19, bw=76, delay='23ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s12, s13, bw=80, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s12, s20, bw=100, delay='21ms', loss=0.003, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s12, s21, bw=77, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s13, s20, bw=80, delay='6ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s13, s21, bw=79, delay='21ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s14, s15, bw=83, delay='8ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s16, s17, bw=80, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s18, s19, bw=80, delay='6ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s20, s21, bw=79, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)

	# Agregar enlaces para switches Dominio B
        # Nomenclatura retraso, perdida de paquetes, fluctuaciones, ancho de banda
	self.addLink(s22, s23, bw=94, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s22, s24, bw=96, delay='4ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s22, s25, bw=98, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s22, s26, bw=99, delay='16ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s23, s27, bw=91, delay='8ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s23, s29, bw=93, delay='15ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s23, s31, bw=95, delay='12ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s24, s28, bw=92, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s24, s30, bw=94, delay='7ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s24, s32, bw=97, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s25, s27, bw=98, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s25, s29, bw=93, delay='8ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s25, s31, bw=91, delay='13ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
        self.addLink(s26, s28, bw=92, delay='9ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s26, s30, bw=89, delay='12ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s26, s32, bw=94, delay='18ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s27, s33, bw=93, delay='7ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s27, s34, bw=87, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s28, s33, bw=88, delay='11ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s28, s34, bw=93, delay='6ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s28, s35, bw=97, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s29, s34, bw=97, delay='15ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s29, s35, bw=82, delay='18ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s29, s36, bw=87, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s30, s35, bw=94, delay='5ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s30, s36, bw=86, delay='1ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s30, s37, bw=97, delay='3ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
   	self.addLink(s31, s36, bw=93, delay='4ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s31, s37, bw=96, delay='6ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s31, s38, bw=99, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s32, s37, bw=94, delay='20ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s32, s38, bw=86, delay='5ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s33, s39, bw=82, delay='3ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s33, s40, bw=92, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s34, s39, bw=83, delay='5ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s34, s40, bw=95, delay='12ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s35, s41, bw=84, delay='5ms', loss=0.002, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s35, s42, bw=96, delay='4ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s36, s41, bw=87, delay='2ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s36, s42, bw=93, delay='7ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s37, s43, bw=92, delay='6ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s37, s44, bw=94, delay='3ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)	
	self.addLink(s38, s43, bw=94, delay='5ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	self.addLink(s38, s44, bw=95, delay='3ms', loss=0.001, jitter='0ms', max_queue_size=1000, use_htb=True)	


	self.addLink(s1, s22, bw=100, delay='0ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	#self.addLink(s1, r1, bw=100, delay='0ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	#self.addLink(r42, s22, bw=100, delay='0ms', loss=0, jitter='0ms', max_queue_size=1000, use_htb=True)
	
class MultiSwitch( OVSSwitch ):
	"Switch Custom que conecta a switches controlados por distintos controladores "
	def start(self, controllers):
		return OVSSwitch.start(self, [cmap[self.name]])
def run():
	# Ejecutar simulacion de red virtual, controller=None es para que no utilizar un controlador local y solo los dos controladores remotos	
	net = Mininet(topo=DataCenterA(), link=TCLink, switch=MultiSwitch, controller=None)
	net.addController(c0)
	net.addController(c1)
	#net.addController(c2)
	net.start()
	CLI(net)
	net.stop()

# if the script is run directly (sudo custom/optical.py):
if __name__ == '__main__':
	setLogLevel('info')
	run()
