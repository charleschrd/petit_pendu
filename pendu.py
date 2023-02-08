from random import *

def print_list(list) :
  i = 0
  while i < len(list):
    print(print_word[i], end='')
    i += 1
  print('')

def assign_word(entry, secret_word, print_word) :
  i = 0
  while i < len(secret_word) :
    if entry.upper() == secret_word[i] :
      print_word[i] = entry.upper()
    i += 1
  return(print_word)

def print_pendu(fail) :
  if fail >= 7 :
    print("  ____________")
  if fail >= 6 :
    print("  |/       |  ")
  if fail >= 5 :
    print("  |        O  ")
  if fail >= 4 :
    print("  |       /|\ ")
  if fail >= 3 :
    print("  |        /\ ")
  if fail >= 2 :
    print("  |           ")
  if fail >= 1 :
    print("==============")

def check_word_complete(print_word) :
  for i in print_word :
    if print_word[i] == '_' :
      return False
  return True

list_word = {}
nbr_word = 0
fic=open('DicoScrabble', 'r', encoding='UTF-8')
while 1:
    line = fic.readline().strip()
    if line != "" :
        list_word[nbr_word] = line
        nbr_word += 1
    else :
        break ;
fic.close()
nbr_word -= 1
play_again = True
while play_again == True :
	print("Le mot est choisi parmis les mots d'un dictionnaire du scrabble comportant", (nbr_word + 1), "mots. Bonne chance pour sauver l'innocent :-)")
	secret_word = list_word[randint(0, nbr_word)]
	print_word = {}
	i = 0
	fail = 0
	letters = ""
	our_bool = True
	while i < len(secret_word) :
		print_word[i] = '_'
		i+=1
	print_list(print_word)
	while our_bool == True :
		if len(letters) > 0 :
			print("Petit rappel des lettres que vous avez utilisées :", letters)
		entry = input("Veuillez proposer une lettre ou un mot :\n")
		if len(entry) > 1 :
			if entry.upper() == secret_word :
				print("La partie est gagnée ! Le pendu est sauvé")
				our_bool = False
			else :
				print("Le mot renseigné ne correspond pas")
				fail += 1
				print_pendu(fail)
				print_list(print_word)
		else :
			if entry.upper() in secret_word :
				print_word = assign_word(entry, secret_word, print_word)
				print_list(print_word)
				if check_word_complete(print_word) == True :
					print("La partie est gagnée ! Le pendu est sauvé")
					our_bool = False
			else :
				print("Le caractère renseigné ne correspond pas")
				letters += entry.upper()
				fail += 1
				print_pendu(fail)
				print_list(print_word)
		if fail >= 7 :
			print("Vous avez échoué l'innocent est mort. Le mot était", secret_word)
			our_bool = False
	retry = input("Si vous voulez rejouer entrez 'Oui', Autrement entrez n'importe quoi :\n")
	if retry != "Oui" :
		play_again = False
print("Aurevoir mes amis ! Hâte de vous retrouvez pour décider du sort du prochain innocent MUAHAHAHAHA !")
