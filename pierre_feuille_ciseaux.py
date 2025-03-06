import random

manches_restantes = 3
manches_gagnées = 0
manches_perdues = 0
joueur = ""
ordinateur = ""
choix = ["pierre", "feuille", "ciseaux"]

print("Pierre Feuille Ciseaux en trois manches")

while manches_restantes > 0:
  joueur = input("Pierre feuille ciseaux... ").lower()
  while joueur not in choix:
    joueur = input("Entrée invalide. Réessayez. ").lower()

  ordinateur = random.choice(["pierre", "feuille", "ciseaux"])

  print(f"L'ordinateur a choisi {ordinateur}")

  if joueur == ordinateur:
    print("Egalité!")
  elif (joueur == "pierre" and ordinateur == "ciseaux") or (joueur == "ciseaux" and ordinateur == "feuille") or (joueur == "feuille" and ordinateur == "pierre"):
    print("Manche gagnée!!")
    manches_gagnées += 1
    manches_restantes -= 1
  else:
    print("Dommage, manche perdue.")
    manches_perdues += 1
    manches_restantes -= 1

  if manches_gagnées == 2 or manches_perdues == 2:
    break

if manches_gagnées >= 2:
  print("Tu as gagné la partie!")
else:
  print("Dommage tu as perdu la partie")