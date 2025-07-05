import random
import string
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Générateur de Mots de Passe")
        self.root.geometry("700x600")
        
        # Thème sombre macOS
        self.bg_dark = '#1c1c1e'
        self.bg_secondary = '#2c2c2e'
        self.bg_tertiary = '#3a3a3c'
        self.text_primary = '#ffffff'
        self.text_secondary = '#8e8e93'
        self.accent_blue = '#007aff'
        self.accent_green = '#34c759'
        self.accent_red = '#ff3b30'
        
        self.root.configure(bg=self.bg_dark)
        
        # Style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Title.TLabel', font=('SF Pro Display', 18, 'bold'), background=self.bg_dark, foreground=self.text_primary)
        style.configure('Subtitle.TLabel', font=('SF Pro Text', 11), background=self.bg_dark, foreground=self.text_secondary)
        style.configure('Custom.TLabel', font=('SF Pro Text', 12), background=self.bg_secondary, foreground=self.text_primary)
        style.configure('Custom.TButton', font=('SF Pro Text', 11, 'bold'))
        
        self.setup_ui()
        # Ne pas générer de mots de passe automatiquement au démarrage
        
    def setup_ui(self):
        # --- HEADER ---
        title_frame = tk.Frame(self.root, bg=self.bg_dark, highlightthickness=0, bd=0)
        title_frame.pack(pady=(32, 8))

        title_label = ttk.Label(title_frame, text="Milk", style='Title.TLabel')
        title_label.pack(pady=(0, 2))

        # Crédit professionnel, espacé et aligné
        credits_frame = tk.Frame(title_frame, bg=self.bg_dark, highlightthickness=0, bd=0)
        credits_frame.pack()
        tk.Label(credits_frame, text="Développé par Solvyrth", font=("SF Pro Text", 10, "italic"), bg=self.bg_dark, fg=self.text_secondary, bd=0, padx=0, pady=0).pack(side=tk.LEFT)
        import webbrowser
        github_label = tk.Label(credits_frame, text="· GitHub", font=("SF Pro Text", 10, "underline"), bg=self.bg_dark, fg=self.accent_blue, cursor="hand2", bd=0, padx=0, pady=0)
        github_label.pack(side=tk.LEFT)
        github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Solvyrth"))
        github_label.bind("<Enter>", lambda e: github_label.config(fg="#0051D0"))
        github_label.bind("<Leave>", lambda e: github_label.config(fg=self.accent_blue))

        version_label = ttk.Label(title_frame, text="Version • 2.1", style='Subtitle.TLabel')
        version_label.pack(pady=(2, 0))

        # --- MAIN CARD ---
        main_frame = tk.Frame(self.root, bg=self.bg_secondary, relief='flat', bd=0, highlightthickness=0)
        main_frame.pack(padx=20, pady=8, fill='both', expand=True)

        # --- CONFIG ---
        config_frame = tk.Frame(main_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        config_frame.pack(pady=12, padx=12, fill='x')

        # Longueur
        length_frame = tk.Frame(config_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        length_frame.pack(fill='x', pady=6, padx=2)
        length_label = tk.Label(length_frame, text="Longueur", bg=self.bg_secondary, fg=self.text_primary, font=('SF Pro Text', 10, 'bold'), padx=0, pady=0)
        length_label.pack(side='left', padx=(0,6))
        self.length_var = tk.StringVar(value="16")
        length_spinbox = tk.Spinbox(length_frame, from_=4, to=30, textvariable=self.length_var, width=4, font=('SF Pro Text', 10), bg=self.bg_tertiary, fg=self.text_primary, buttonbackground=self.bg_tertiary, relief='flat', bd=1, insertbackground=self.text_primary, selectbackground=self.accent_blue, highlightthickness=0, justify='center')
        length_spinbox.pack(side='right', padx=(6,0), pady=0)

        # Nombre
        count_frame = tk.Frame(config_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        count_frame.pack(fill='x', pady=6, padx=2)
        count_label = tk.Label(count_frame, text="Nombre", bg=self.bg_secondary, fg=self.text_primary, font=('SF Pro Text', 10, 'bold'), padx=0, pady=0)
        count_label.pack(side='left', padx=(0,6))
        self.count_var = tk.StringVar(value="3")
        count_spinbox = tk.Spinbox(count_frame, from_=1, to=10, textvariable=self.count_var, width=4, font=('SF Pro Text', 10), bg=self.bg_tertiary, fg=self.text_primary, buttonbackground=self.bg_tertiary, relief='flat', bd=1, insertbackground=self.text_primary, selectbackground=self.accent_blue, highlightthickness=0, justify='center')
        count_spinbox.pack(side='right', padx=(6,0), pady=0)

        # --- OPTIONS ---
        options_frame = tk.Frame(config_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        options_frame.pack(fill='x', pady=8)
        for text, var, icon in [
            ("Caractères spéciaux", 'special_chars_var', "🔣"),
            ("Majuscules", 'uppercase_var', "🔤"),
            ("Minuscules", 'lowercase_var', "🔡"),
            ("Chiffres", 'numbers_var', "🔢")]:
            setattr(self, var, tk.BooleanVar(value=True))
            cb = tk.Checkbutton(options_frame, text=f"{icon} {text}", variable=getattr(self, var), bg=self.bg_secondary, fg=self.text_primary, selectcolor=self.accent_blue, font=('SF Pro Text', 10), activebackground=self.bg_secondary, activeforeground=self.text_primary, relief='flat', bd=0, highlightthickness=0, padx=0, pady=0)
            cb.pack(anchor='w', pady=1)

        # --- BOUTONS ---
        buttons_frame = tk.Frame(main_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        buttons_frame.pack(pady=10)
        btn_style = {'font': ('SF Pro Text', 10, 'bold'), 'relief': 'flat', 'bd': 0, 'padx': 14, 'pady': 6, 'cursor': 'hand2', 'highlightthickness': 0}
        generate_btn = tk.Button(buttons_frame, text="Générer", command=self.on_generate_click, bg=self.accent_blue, fg='#222', activebackground='#0051D0', activeforeground='#222', **btn_style)
        generate_btn.pack(side='left', padx=4)
        save_btn = tk.Button(buttons_frame, text="Sauvegarder", command=self.save_to_file, bg=self.accent_green, fg='#222', activebackground='#249944', activeforeground='#222', **btn_style)
        save_btn.pack(side='left', padx=4)
        clear_btn = tk.Button(buttons_frame, text="Effacer", command=self.clear_results, bg=self.accent_red, fg='#222', activebackground='#b91d1d', activeforeground='#222', **btn_style)
        clear_btn.pack(side='left', padx=4)

        # --- RESULTATS ---
        results_frame = tk.Frame(main_frame, bg=self.bg_secondary, highlightthickness=0, bd=0)
        results_frame.pack(fill='both', expand=True, padx=10, pady=6)
        self.results_text = tk.Text(results_frame, height=8, font=('SF Mono', 10), bg=self.bg_tertiary, fg=self.text_primary, insertbackground=self.accent_blue, relief='flat', bd=1, selectbackground=self.accent_blue, selectforeground='#fff', wrap='word', padx=8, pady=8, highlightthickness=0)
        scrollbar = tk.Scrollbar(results_frame, orient='vertical', command=self.results_text.yview, bg=self.bg_tertiary, troughcolor=self.bg_secondary, activebackground=self.text_secondary, relief='flat', bd=0, highlightthickness=0)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        self.results_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        self.results_text.insert(tk.END, "\nCliquez sur Générer pour créer vos mots de passe sécurisés.\n\nAucun mot de passe n'est généré tant que vous n'avez pas cliqué sur le bouton.")
        self.generated_passwords = []
    
    def on_generate_click(self):
        """Fonction appelée lors du clic sur le bouton Générer"""
        print("DEBUG: Bouton Générer cliqué!")
        self.generate_passwords()
        
    def generate_password(self, length, use_special_chars=True, use_uppercase=True, use_lowercase=True, use_numbers=True):
        """Génère un mot de passe selon les critères spécifiés"""
        chars = ""
        
        if use_lowercase:
            chars += string.ascii_lowercase
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_numbers:
            chars += string.digits
        if use_special_chars:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
        if not chars:
            # Si aucune option n'est sélectionnée, utiliser au moins les lettres
            chars = string.ascii_letters + string.digits
            
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    
    def generate_passwords(self):
        """Génère les mots de passe selon la configuration"""
        print("DEBUG: Génération de mots de passe en cours...")
        try:
            length = int(self.length_var.get())
            count = int(self.count_var.get())
            
            if length < 4 or length > 30:
                messagebox.showerror("Erreur", "La longueur doit être entre 4 et 30 caractères", parent=self.root)
                return
                
            if count < 1 or count > 10:
                messagebox.showerror("Erreur", "Le nombre doit être entre 1 et 10", parent=self.root)
                return
            
            # Vérifier qu'au moins une option est cochée
            if not any([self.special_chars_var.get(), self.uppercase_var.get(), 
                       self.lowercase_var.get(), self.numbers_var.get()]):
                # Cocher automatiquement toutes les options si aucune n'est sélectionnée
                self.special_chars_var.set(True)
                self.uppercase_var.set(True)
                self.lowercase_var.set(True)
                self.numbers_var.set(True)
            
            # Effacer et regénérer
            self.generated_passwords = []
            self.results_text.config(state='normal')
            self.results_text.delete(1.0, tk.END)
            
            # Générer les mots de passe
            print(f"DEBUG: Génération de {count} mots de passe de {length} caractères")
            for i in range(count):
                password = self.generate_password(
                    length,
                    self.special_chars_var.get(),
                    self.uppercase_var.get(),
                    self.lowercase_var.get(),
                    self.numbers_var.get()
                )
                self.generated_passwords.append(password)
                print(f"DEBUG: Mot de passe {i+1}: {password}")
                
            print(f"DEBUG: ✅ {len(self.generated_passwords)} mots de passe générés avec succès")
            
            # Obtenir l'heure actuelle pour montrer quand la génération a eu lieu
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            generation_id = random.randint(1000, 9999)  # ID unique pour chaque génération
            
            # Affichage des résultats avec un identifiant unique
            self.results_text.insert(tk.END, f"🕐 NOUVELLE GÉNÉRATION à {current_time} (ID: {generation_id})\n")
            self.results_text.insert(tk.END, f"✅ {count} mot(s) de passe généré(s) avec succès !\n")
            self.results_text.insert(tk.END, f"📏 Longueur: {length} caractères\n")
            
            # Afficher les options utilisées
            options_used = []
            if self.special_chars_var.get():
                options_used.append("🔣 Caractères spéciaux")
            if self.uppercase_var.get():
                options_used.append("🔤 Majuscules") 
            if self.lowercase_var.get():
                options_used.append("🔡 Minuscules")
            if self.numbers_var.get():
                options_used.append("🔢 Chiffres")
            
            self.results_text.insert(tk.END, f"🎯 Options: {', '.join(options_used)}\n")
            self.results_text.insert(tk.END, "━" * 50 + "\n\n")
            
            for i, password in enumerate(self.generated_passwords, 1):
                self.results_text.insert(tk.END, f"🔑 Mot de passe {i:2d}: {password}\n")
                
            self.results_text.insert(tk.END, "\n" + "━" * 50 + "\n")
            self.results_text.insert(tk.END, "💡 Conseil: Utilisez des mots de passe différents pour chaque compte !")
            
            # Activer l'état disabled pour éviter la modification
            self.results_text.config(state='disabled')
            
            # Forcer le scroll vers le haut et la mise à jour de l'affichage
            self.results_text.see(tk.INSERT)
            self.results_text.mark_set(tk.INSERT, "1.0")
            self.results_text.see("1.0")
            self.results_text.update()
            self.root.update()
            print("DEBUG: Mise à jour de l'affichage terminée")
                
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides", parent=self.root)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite: {str(e)}", parent=self.root)
    
    def save_to_file(self):
        """Sauvegarde les mots de passe dans un fichier"""
        if not self.generated_passwords:
            messagebox.showwarning("Attention", "Aucun mot de passe à sauvegarder. Générez d'abord des mots de passe.", parent=self.root)
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")],
            title="Sauvegarder les mots de passe",
            initialfile="mots_de_passe.txt"
        )
        
        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write("╔══════════════════════════════════════════════════════════════╗\n")
                    f.write("║               MOTS DE PASSE - PASSWORD GENERATOR             ║\n")
                    f.write("║                  https://github.com/solvyrth                 ║\n")
                    f.write("╚══════════════════════════════════════════════════════════════╝\n\n")
                    
                    f.write(f"📊 INFORMATIONS DE GÉNÉRATION:\n")
                    f.write(f"├─ Nombre total: {len(self.generated_passwords)} mot(s) de passe\n")
                    f.write(f"├─ Longueur: {self.length_var.get()} caractères\n")
                    f.write(f"└─ Date de génération: {self.get_current_datetime()}\n\n")
                    
                    f.write(f"⚙️  OPTIONS UTILISÉES:\n")
                    f.write(f"├─ Caractères spéciaux: {'✅ Oui' if self.special_chars_var.get() else '❌ Non'}\n")
                    f.write(f"├─ Majuscules (A-Z): {'✅ Oui' if self.uppercase_var.get() else '❌ Non'}\n")
                    f.write(f"├─ Minuscules (a-z): {'✅ Oui' if self.lowercase_var.get() else '❌ Non'}\n")
                    f.write(f"└─ Chiffres (0-9): {'✅ Oui' if self.numbers_var.get() else '❌ Non'}\n\n")
                    
                    f.write("🔑 MOTS DE PASSE GÉNÉRÉS:\n")
                    f.write("═" * 60 + "\n")
                    for i, password in enumerate(self.generated_passwords, 1):
                        f.write(f"{i:2d}. {password}\n")
                    f.write("═" * 60 + "\n\n")
                    
                    f.write("⚠️  CONSEILS DE SÉCURITÉ:\n")
                    f.write("• Utilisez un mot de passe différent pour chaque compte\n")
                    f.write("• Ne partagez jamais vos mots de passe\n")
                    f.write("• Stockez ce fichier dans un endroit sécurisé\n")
                    f.write("• Supprimez ce fichier après utilisation si possible\n\n")
                    f.write("Générateur créé par Solvyrth - Version 2.0")
                    
                messagebox.showinfo("Succès", f"✅ Mots de passe sauvegardés avec succès !\n\n📁 Fichier: {filename}\n\n💡 N'oubliez pas de sécuriser ce fichier.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Erreur", f"❌ Erreur lors de la sauvegarde:\n{str(e)}", parent=self.root)
    
    def get_current_datetime(self):
        """Retourne la date et l'heure actuelles formatées"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
    
    def clear_results(self):
        """Efface les résultats"""
        self.results_text.delete(1.0, tk.END)
        self.generated_passwords = []
        self.results_text.insert(tk.END, "🗑️ Résultats effacés. Cliquez sur 'Générer' pour créer de nouveaux mots de passe.")
    
    def open_github_profile(self, event=None):
        """Ouvre le profil GitHub dans le navigateur"""
        import webbrowser
        webbrowser.open("https://github.com/Solvyrth")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
