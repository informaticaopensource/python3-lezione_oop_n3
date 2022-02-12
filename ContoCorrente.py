class ContoCorrente(object):
	def __init__(self,ints,saldo,data_saldo,numero_conto_corrente):
		self.__intestazione=ints
		self.__saldo=saldo
		self.__data_saldo=data_saldo
		self.__numero_conto_corrente=numero_conto_corrente

	def visualizzasaldo(self):
	    print("Nome Correntista: ",self.__intestazione," Saldo Conto:", self.__saldo)
	    print("\nData Saldo:",self.__data_saldo)
	    print("\nNumero Conto: ",self.__numero_conto_corrente)

	def versamento(self,x):
	    self.__saldo+=s

	def preleva(x,self):
	    if (x>self.__saldo):
        	print("Giacenza conto non sufficiente\n")
	    else:
	        self.__saldo-=x

def main():
		conto1=ContoCorrente("Mario Rossi",10000,"01/01/2020","0001X")
		conto1.visualizzasaldo()
if __name__ == "__main__":
	main()
