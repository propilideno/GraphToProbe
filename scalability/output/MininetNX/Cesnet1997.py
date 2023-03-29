from mininet.topo import Topo

class MininetNX( Topo ):
	def build( self ):
		#Add Switches
		s0 = self.addSwitch('s0')
		s1 = self.addSwitch('s1')
		s2 = self.addSwitch('s2')
		s3 = self.addSwitch('s3')
		s4 = self.addSwitch('s4')
		s5 = self.addSwitch('s5')
		s6 = self.addSwitch('s6')
		s7 = self.addSwitch('s7')
		s8 = self.addSwitch('s8')
		s9 = self.addSwitch('s9')
		s10 = self.addSwitch('s10')
		s11 = self.addSwitch('s11')
		s12 = self.addSwitch('s12')
		#Add 2 hosts to each switch
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
		h15 = self.addHost('h15')
		h16 = self.addHost('h16')
		h17 = self.addHost('h17')
		h18 = self.addHost('h18')
		h19 = self.addHost('h19')
		h20 = self.addHost('h20')
		h21 = self.addHost('h21')
		h22 = self.addHost('h22')
		h23 = self.addHost('h23')
		h24 = self.addHost('h24')
		h25 = self.addHost('h25')
		h26 = self.addHost('h26')
		#Add a link of hosts and switch
		self.addLink('s0','h1')
		self.addLink('s0','h2')
		self.addLink('s1','h3')
		self.addLink('s1','h4')
		self.addLink('s2','h5')
		self.addLink('s2','h6')
		self.addLink('s3','h7')
		self.addLink('s3','h8')
		self.addLink('s4','h9')
		self.addLink('s4','h10')
		self.addLink('s5','h11')
		self.addLink('s5','h12')
		self.addLink('s6','h13')
		self.addLink('s6','h14')
		self.addLink('s7','h15')
		self.addLink('s7','h16')
		self.addLink('s8','h17')
		self.addLink('s8','h18')
		self.addLink('s9','h19')
		self.addLink('s9','h20')
		self.addLink('s10','h21')
		self.addLink('s10','h22')
		self.addLink('s11','h23')
		self.addLink('s11','h24')
		self.addLink('s12','h25')
		self.addLink('s12','h26')
		#Add a link of switches of original topology
		self.addLink('s0','s1')
		self.addLink('s1','s9')
		self.addLink('s1','s2')
		self.addLink('s1','s11')
		self.addLink('s1','s10')
		self.addLink('s3','s10')
		self.addLink('s4','s11')
		self.addLink('s5','s11')
		self.addLink('s6','s8')
		self.addLink('s6','s12')
		self.addLink('s7','s12')
		self.addLink('s10','s12')
		
topos = { 'Cesnet1997': ( lambda: MininetNX() ) }