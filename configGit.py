import os

RED    = "\033[1;31m"  
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RESET  = "\033[0;0m"

nome = ''
email = ''
platGit= ''

def perguntaNome():
	global nome
	nome = input ('Qual o seu nome (e sobrenome)?')

def perguntaEmail():
	global email
	email = input('Qual o seu e-mail? ')
	email = email.lower()

def perguntaPlataforma():
	global platGit
	platGit = input('Qual plaforma voce deseja configurar? Github ou Gitlab?')
	platGit = platGit.lower()
		
	if(platGit == "gitlab" or platGit == "lab"):
	   platGit = 'gitlab'
	elif(platGit == "github" or platGit == "hub"):
	   platGit = 'github'
	else:
		print('{} Plataforma nao localizada! {}' .format(RED, RESET))
		perguntaPlataforma()

def tutorialSSH():
	print('\n {} Copie o texto acima, iniciado em {} ssh-rsa {} ate o seu {} e-mail {}'.format(RED, GREEN, RED, GREEN, RESET))
	print('{} >>> Proximos passos <<< {}'.format(YELLOW,RESET))
	if(platGit == 'gitlab'):
		print('1 - Na tela inicial, clique em configuracoes. No canto esquerdo, selecione {} "Chaves SSH"{}.'.format(GREEN,RESET))
		print('2 - Cole a chave gerada e adicione um titulo. Em seguida, clique em Adicionar chave.')
		print('3 - Prontinho, a sua chave SSH esta gerada!{} :){}'.format(YELLOW, RESET))

	if(platGit == 'github'):
		print('1 - Na tela inicial, clique em Settings. No canto esquerdo, selecione {} "SSH and GPG Keys"{}.'.format(GREEN,RESET))
		print('2 - Clique no botão verde "New SSH Key')
		print('3 - Adicione um titulo e cole a chave gerada. Em seguida, clique em Add SSH Key.')
		print('4 - Prontinho, a sua chave SSH esta gerada! :){}'.format(YELLOW, RESET))


def gerarChaveSSH(email):
	tutorialSSH()
	gitEmail = 'ssh-keygen -t rsa -b 4096 -C "{}"'.format(email)
	os.system(gitEmail)
	os.system('\n cat ~/.ssh/id_rsa.pub')

def gitConfig(nome, email):
	os.system('git config --global user.name "{}"'.format(nome))
	os.system('git config --global user.email "{}"'.format(email))
	os.system('git config --global alias.co checkout')
	os.system('git config --global alias.st status')

perguntaNome()
perguntaPlataforma()
perguntaEmail()
gitConfig(nome,email)
gerarChaveSSH(email)
#os.system('cat ~/.gitconfig')
