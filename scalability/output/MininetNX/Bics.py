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
		s13 = self.addSwitch('s13')
		s14 = self.addSwitch('s14')
		s15 = self.addSwitch('s15')
		s16 = self.addSwitch('s16')
		s17 = self.addSwitch('s17')
		s18 = self.addSwitch('s18')
		s19 = self.addSwitch('s19')
		s20 = self.addSwitch('s20')
		s21 = self.addSwitch('s21')
		s24 = self.addSwitch('s24')
		s25 = self.addSwitch('s25')
		s26 = self.addSwitch('s26')
		s27 = self.addSwitch('s27')
		s28 = self.addSwitch('s28')
		s29 = self.addSwitch('s29')
		s30 = self.addSwitch('s30')
		s31 = self.addSwitch('s31')
		s32 = self.addSwitch('s32')
		s33 = self.addSwitch('s33')
		s34 = self.addSwitch('s34')
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
		h27 = self.addHost('h27')
		h28 = self.addHost('h28')
		h29 = self.addHost('h29')
		h30 = self.addHost('h30')
		h31 = self.addHost('h31')
		h32 = self.addHost('h32')
		h33 = self.addHost('h33')
		h34 = self.addHost('h34')
		h35 = self.addHost('h35')
		h36 = self.addHost('h36')
		h37 = self.addHost('h37')
		h38 = self.addHost('h38')
		h39 = self.addHost('h39')
		h40 = self.addHost('h40')
		h41 = self.addHost('h41')
		h42 = self.addHost('h42')
		h43 = self.addHost('h43')
		h44 = self.addHost('h44')
		h45 = self.addHost('h45')
		h46 = self.addHost('h46')
		h47 = self.addHost('h47')
		h48 = self.addHost('h48')
		h49 = self.addHost('h49')
		h50 = self.addHost('h50')
		h51 = self.addHost('h51')
		h52 = self.addHost('h52')
		h53 = self.addHost('h53')
		h54 = self.addHost('h54')
		h55 = self.addHost('h55')
		h56 = self.addHost('h56')
		h57 = self.addHost('h57')
		h58 = self.addHost('h58')
		h59 = self.addHost('h59')
		h60 = self.addHost('h60')
		h61 = self.addHost('h61')
		h62 = self.addHost('h62')
		h63 = self.addHost('h63')
		h64 = self.addHost('h64')
		h65 = self.addHost('h65')
		h66 = self.addHost('h66')
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
		self.addLink('s13','h27')
		self.addLink('s13','h28')
		self.addLink('s14','h29')
		self.addLink('s14','h30')
		self.addLink('s15','h31')
		self.addLink('s15','h32')
		self.addLink('s16','h33')
		self.addLink('s16','h34')
		self.addLink('s17','h35')
		self.addLink('s17','h36')
		self.addLink('s18','h37')
		self.addLink('s18','h38')
		self.addLink('s19','h39')
		self.addLink('s19','h40')
		self.addLink('s20','h41')
		self.addLink('s20','h42')
		self.addLink('s21','h43')
		self.addLink('s21','h44')
		self.addLink('s24','h45')
		self.addLink('s24','h46')
		self.addLink('s25','h47')
		self.addLink('s25','h48')
		self.addLink('s26','h49')
		self.addLink('s26','h50')
		self.addLink('s27','h51')
		self.addLink('s27','h52')
		self.addLink('s28','h53')
		self.addLink('s28','h54')
		self.addLink('s29','h55')
		self.addLink('s29','h56')
		self.addLink('s30','h57')
		self.addLink('s30','h58')
		self.addLink('s31','h59')
		self.addLink('s31','h60')
		self.addLink('s32','h61')
		self.addLink('s32','h62')
		self.addLink('s33','h63')
		self.addLink('s33','h64')
		self.addLink('s34','h65')
		self.addLink('s34','h66')
		#Add a link of switches of original topology
		self.addLink('s0','s9')
		self.addLink('s0','s18')
		self.addLink('s1','s27')
		self.addLink('s2','s27')
		self.addLink('s3','s26')
		self.addLink('s3','s4')
		self.addLink('s4','s5')
		self.addLink('s5','s24')
		self.addLink('s5','s6')
		self.addLink('s6','s25')
		self.addLink('s6','s26')
		self.addLink('s7','s33')
		self.addLink('s7','s25')
		self.addLink('s8','s29')
		self.addLink('s9','s10')
		self.addLink('s9','s29')
		self.addLink('s10','s12')
		self.addLink('s10','s29')
		self.addLink('s11','s28')
		self.addLink('s11','s30')
		self.addLink('s12','s17')
		self.addLink('s12','s13')
		self.addLink('s13','s24')
		self.addLink('s13','s29')
		self.addLink('s14','s15')
		self.addLink('s15','s17')
		self.addLink('s16','s24')
		self.addLink('s16','s31')
		self.addLink('s17','s20')
		self.addLink('s17','s18')
		self.addLink('s18','s19')
		self.addLink('s19','s21')
		self.addLink('s20','s21')
		self.addLink('s24','s31')
		self.addLink('s25','s26')
		self.addLink('s25','s31')
		self.addLink('s26','s27')
		self.addLink('s26','s30')
		self.addLink('s27','s28')
		self.addLink('s27','s30')
		self.addLink('s28','s29')
		self.addLink('s28','s30')
		self.addLink('s29','s33')
		self.addLink('s29','s30')
		self.addLink('s29','s31')
		self.addLink('s30','s34')
		self.addLink('s31','s32')
		self.addLink('s33','s34')
		
topos = { 'Bics': ( lambda: MininetNX() ) }