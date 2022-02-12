class PrimaClasse(object):
	def __init__(self,nome):
		self.contatore=1
		self.nome=nome
	def aggiungi(self):
		self.contatore=self.contatore+1
	def stampa(self):
		print("\n Valore del Contatore ",self.contatore)
		print("\n Stampa nome dell'operazione ",self.nome)
def main() :
	nome=input("Inserisci il Nome dell'Operazione ")
	ct=PrimaClasse(nome)
	n=int(input("Quanti incrementi ? "))
	for k in range(n):
		ct.aggiungi()
	ct.stampa()
if __name__ == "__main__":
	main()
