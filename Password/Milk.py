import random
import string


print(r'''
      
,---.    ,---..-./`)   .---.     .--.   .--.   
|    \  /    |\ .-.')  | ,_|     |  | _/  /    
|  ,  \/  ,  |/ `-' \,-./  )     | (`' ) /     
|  |\_   /|  | `-'`"`\  '_ '`)   |(_ ()_)      
|  _( )_/ |  | .---.  > (_)  )   | (_,_)   __  
| (_ o _) |  | |   | (  .  .-'   |  |\ \  |  | 
|  (_,_)  |  | |   |  `-'`-'|___ |  | \ `'   / 
|  |      |  | |   |   |        \|  |  \    /  
'--'      '--' '---'   `--------``--'   `'-'   
                Coder par Solvyrth.
            https://github.com/Solvyrth
                    Version 1.0
''')

def generate_password(length=12, use_special_chars=True):
    if use_special_chars:
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_password_to_file(password, filename="mot_de_passe.txt"):   
    """
    Sauvegarde le mot de passe dans un fichier texte.
    """
    with open(filename, "w") as f:
        f.write(password + "\n")

def save_passwords_to_file(passwords, filename="mots_de_passe.txt"):
    """
    Sauvegarde plusieurs mots de passe dans un fichier texte.
    """
    with open(filename, "w") as f:
        for i, password in enumerate(passwords, 1):
            f.write(f"Mot de passe {i}: {password}\n")

if __name__ == "__main__":
    # Demander la longueur du mot de passe
    while True:
        try:
            longueur = int(input("Longueur du mot de passe (max 25) : "))
            if 1 <= longueur <= 25:
                break
            print("Veuillez entrer une longueur entre 1 et 25.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Demander le nombre de mots de passe à générer
    while True:
        try:
            nombre_passwords = int(input("Combien de mots de passe souhaitez-vous générer ? "))
            if nombre_passwords >= 1:
                break
            print("Veuillez entrer un nombre supérieur à 0.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    # Demander si on veut des caractères spéciaux
    choix = input("Inclure des caractères spéciaux ? (o/n) : ").lower() == 'o'
    
    # Générer les mots de passe
    if nombre_passwords == 1:
        mot_de_passe = generate_password(longueur, choix)
        print(f"Mot de passe généré : {mot_de_passe}")
        save_password_to_file(mot_de_passe)
        print("Mot de passe sauvegardé dans 'mot_de_passe.txt'.")
    else:
        mots_de_passe = []
        for i in range(nombre_passwords):
            mot_de_passe = generate_password(longueur, choix)
            mots_de_passe.append(mot_de_passe)
            print(f"Mot de passe {i+1} : {mot_de_passe}")
        
        save_passwords_to_file(mots_de_passe)
        print(f"{nombre_passwords} mots de passe sauvegardés dans 'mots_de_passe.txt'.")
