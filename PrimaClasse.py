class PrimaClasse(object):
	def __init__(self):
		self.contatore=1
	def aggiungi(self):
		self.contatore=self.contatore+1
	def stampa(self):
		print("\n Valore del Contatore",self.contatore)
def main():
	ct=PrimaClasse()
	n=int(input("Quanti incrementi ?"))
	for k in range(n):
		ct.aggiungi()
	ct.stampa()
if __name__ == "__main__":
	main()
