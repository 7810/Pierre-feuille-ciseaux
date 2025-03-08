import random
import tkinter as tk
from tkinter import messagebox

manches_gagnees = 0
manches_perdues = 0
manches_restantes = 3

def jouer(choix_joueur):
    global manches_gagnees, manches_perdues, manches_restantes
    
    choix_ordi = random.choice(["pierre", "feuille", "ciseaux"])
    resultat = ""

    if choix_joueur == choix_ordi:
        resultat = "Égalité !"
    elif (choix_joueur == "pierre" and choix_ordi == "ciseaux") or \
         (choix_joueur == "ciseaux" and choix_ordi == "feuille") or \
         (choix_joueur == "feuille" and choix_ordi == "pierre"):
        resultat = "Tu as gagné la manche !"
        manches_gagnees += 1
        manches_restantes -= 1
    else:
        resultat = "Tu as perdu la manche"
        manches_perdues += 1
        manches_restantes -= 1

    # résultat de la manche
    messagebox.showinfo("Résultat", f"L'ordinateur a choisi : {choix_ordi}\n{resultat}")
    
    # Fin de partie
    if manches_restantes == 0 or manches_gagnees >= 2 or manches_perdues >= 2:
        if manches_gagnees >= 2:
            messagebox.showinfo("Fin de la partie", "Bravo tu as gagné la partie")
            reset_partie()
        elif manches_perdues >= 2:
            messagebox.showinfo("Fin de la partie", "Dommage tu as perdu la partie")
            reset_partie()

# Reset la partie à 0
def reset_partie():
    global manches_gagnees, manches_perdues, manches_restantes
    manches_gagnees = 0
    manches_perdues = 0
    manches_restantes = 3

# Création de la fenêtre Tkinter
root = tk.Tk()
root.geometry("500x100")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Défi l'ordinateur :", font=("Arial", 12), bg="#f0f0f0", fg="#02134f")
label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

btn_pierre = tk.Button(frame, text="Pierre", command=lambda: jouer("pierre"),
                       font=("Arial", 12, "bold"), bg="#4682b4", fg="white", relief="raised", padx=10, pady=5)
btn_pierre.pack(side=tk.LEFT, padx=10)

btn_feuille = tk.Button(frame, text="Feuille", command=lambda: jouer("feuille"),
                        font=("Arial", 12, "bold"), bg="#32cd32", fg="white", relief="raised", padx=10, pady=5)
btn_feuille.pack(side=tk.LEFT, padx=10)

btn_ciseaux = tk.Button(frame, text="Ciseaux", command=lambda: jouer("ciseaux"),
                        font=("Arial", 12, "bold"), bg="#ff6347", fg="white", relief="raised", padx=10, pady=5)
btn_ciseaux.pack(side=tk.LEFT, padx=10)

root.mainloop()