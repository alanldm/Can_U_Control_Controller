from math import *
from server_base import Server
import Controlador

dt = 0.06

class Control:

	def __init__(self, verbose = False):

		self.verbose = verbose
		self.time = 0.0
		self.u_anterior = 0.0
		self.level = 1
		self.xtarget = None
		self.ytarget = None

	def step(self, received):

		print(received)
		if((received!=[]) and (received[2]==self.level)): #Se a lista não for vazia e ainda estiver no mesmo nível:
			if((received[5]==self.xtarget) and (received[6]==self.ytarget)): #Se o alvo ficou parado quer dizer que foi acertado ou o jogo paralizado. 
				controlSignal = 0.0 #Ocorrerá uma mudança de fase e por isso deve-se colocar a barra de entradas na origem.
			else: #Continua efetuando os cálculos e atualizando as variáveis.
				controlSignal = Controlador.calc_u(received, self.u_anterior)
				self.u_anterior = controlSignal
				self.xtarget = received[5]
				self.ytarget = received[6]
		elif(received!=[]): #Reiniciando para o próximo nível, atualizando o nível.
			self.u_anterior = 0.0
			controlSignal = 0.0
			self.level = received[2]		
		else: #Se a lista estiver vazia não faz nada, mantém o sinal de controle em 0.
			controlSignal = 0.0

		self.time += dt

		return controlSignal


if __name__=='__main__':

	control = Control()

	server = Server(control)

	server.run()