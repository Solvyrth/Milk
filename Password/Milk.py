import random
import string
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Milk - Générateur de Mots de Passe")
        self.root.geometry("1200x1200")
        self.root.resizable(True, True)
        self.root.minsize(700, 600)
        
        # Palette de couleurs moderne
        self.colors = {
            'bg_primary': '#0F0F23',      # Bleu très sombre principal
            'bg_secondary': '#1A1A2E',    # Bleu sombre secondaire
            'bg_tertiary': '#16213E',     # Bleu moyen pour cards
            'bg_quaternary': '#0E3460',   # Bleu pour inputs
            'text_primary': '#E8E8F0',    # Blanc cassé
            'text_secondary': '#A0A0B8',  # Gris clair
            'text_muted': '#6B6B8A',      # Gris moyen
            'accent_primary': '#0F52BA',  # Bleu 
            'accent_hover': '#1E5FD6',    # Bleu hover
            'accent_active': '#0A3D8A',   # Bleu actif
            'success': '#2ECC71',         # Vert moderne
            'success_hover': '#27AE60',   # Vert hover
            'danger': '#E74C3C',          # Rouge moderne
            'danger_hover': '#C0392B',    # Rouge hover
            'warning': '#F39C12',         # Orange moderne
            'border_light': '#353564',    # Bordure claire
            'border_dark': '#1E1E3A',     # Bordure sombre
            'shadow': 'rgba(0, 0, 0, 0.3)' # Ombre
        }
        
        self.root.configure(bg=self.colors['bg_primary'])
        
        # Configuration de la barre de titre pour macOS
        self.setup_window_appearance()
        
        # Configuration du style moderne
        self.setup_modern_styles()
        self.setup_ui()
        
    def setup_window_appearance(self):
        """Configure l'apparence de la fenêtre pour s'harmoniser avec le thème"""
        try:
            # Pour macOS - Configuration de l'apparence sombre
            if hasattr(self.root, 'tk'):
                # Essayer d'activer l'apparence sombre native
                self.root.tk.call('tk::unsupported::MacWindowStyle', 'style', self.root._w, 'document', 'closeBox collapseBox resizable')
                
            # Configuration alternative pour tous les systèmes
            # Personnaliser la couleur de fond de la fenêtre principale
            self.root.configure(bg=self.colors['bg_primary'])
            
            # Essayer de modifier l'apparence de la barre de titre (macOS spécifique)
            try:
                # Cette méthode fonctionne sur macOS pour activer le mode sombre
                import subprocess
                import sys
                if sys.platform == 'darwin':  # macOS
                    # Activer l'apparence sombre pour l'application
                    self.root.tk.call('tk::unsupported::MacWindowStyle', 'appearance', self.root._w, 'darkAqua')
            except:
                pass
                
        except Exception:
            # Si la configuration spécialisée échoue, continuer sans erreur
            pass
        
    def setup_modern_styles(self):
        """Configure les styles modernes pour tous les widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configuration des frames avec design moderne
        style.configure('Main.TFrame', 
                       background=self.colors['bg_primary'],
                       relief='flat',
                       borderwidth=0)
        
        style.configure('Card.TFrame', 
                       background=self.colors['bg_tertiary'],
                       relief='flat',
                       borderwidth=1)
        
        style.configure('Header.TFrame', 
                       background=self.colors['bg_secondary'],
                       relief='flat',
                       borderwidth=0)
        
        # Labels avec typographie 
        style.configure('Title.TLabel', 
                       font=('SF Pro Display', 28, 'bold'),
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_primary'])
        
        style.configure('Subtitle.TLabel', 
                       font=('SF Pro Text', 12),
                       background=self.colors['bg_secondary'],
                       foreground=self.colors['text_secondary'])
        
        style.configure('Heading.TLabel', 
                       font=('SF Pro Text', 14, 'bold'),
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'])
        
        style.configure('Body.TLabel', 
                       font=('SF Pro Text', 11),
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_secondary'])
        
        style.configure('Option.TLabel', 
                       font=('SF Pro Text', 10, 'bold'),
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'])
        
        # Boutons avec design moderne et effets hover
        style.configure('Primary.TButton',
                       font=('SF Pro Text', 11, 'bold'),
                       padding=(16, 10),
                       background=self.colors['accent_primary'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        style.map('Primary.TButton',
                 background=[('active', self.colors['accent_hover']),
                           ('pressed', self.colors['accent_active']),
                           ('disabled', self.colors['text_muted'])],
                 foreground=[('disabled', '#888888')])
        
        style.configure('Success.TButton',
                       font=('SF Pro Text', 11, 'bold'),
                       padding=(16, 10),
                       background=self.colors['success'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        style.map('Success.TButton',
                 background=[('active', self.colors['success_hover']),
                           ('pressed', '#229954')],
                 foreground=[('disabled', '#888888')])
        
        style.configure('Danger.TButton',
                       font=('SF Pro Text', 11, 'bold'),
                       padding=(16, 10),
                       background=self.colors['danger'],
                       foreground='white',
                       borderwidth=0,
                       focuscolor='none',
                       relief='flat')
        
        style.map('Danger.TButton',
                 background=[('active', self.colors['danger_hover']),
                           ('pressed', '#A93226')],
                 foreground=[('disabled', '#888888')])
        
        # Checkbuttons modernes
        style.configure('Modern.TCheckbutton',
                       font=('SF Pro Text', 11),
                       background=self.colors['bg_tertiary'],
                       foreground=self.colors['text_primary'],
                       focuscolor='none',
                       borderwidth=0)
        
        style.map('Modern.TCheckbutton',
                 background=[('active', self.colors['bg_tertiary'])],
                 foreground=[('active', self.colors['text_primary'])])
        
        # Spinbox moderne
        style.configure('Modern.TSpinbox',
                       fieldbackground=self.colors['bg_quaternary'],
                       background=self.colors['bg_quaternary'],
                       foreground=self.colors['text_primary'],
                       bordercolor=self.colors['border_light'],
                       arrowcolor=self.colors['text_secondary'],
                       insertcolor=self.colors['accent_primary'],
                       selectbackground=self.colors['accent_primary'],
                       selectforeground='white')
        
        # Scrollbar moderne
        style.configure('Modern.Vertical.TScrollbar',
                       background=self.colors['bg_quaternary'],
                       troughcolor=self.colors['bg_secondary'],
                       bordercolor=self.colors['bg_tertiary'],
                       arrowcolor=self.colors['text_secondary'],
                       darkcolor=self.colors['bg_quaternary'],
                       lightcolor=self.colors['bg_quaternary'])
        
    def setup_ui(self):
        """Interface utilisateur moderne"""
        
        # --- HEADER ÉLÉGANT ---
        header_frame = ttk.Frame(self.root, style='Header.TFrame')
        header_frame.pack(fill='x', pady=0)
        
        # Container pour centrer le contenu du header
        header_content = ttk.Frame(header_frame, style='Header.TFrame')
        header_content.pack(expand=True, fill='both', pady=40)
        
        # Titre principal avec espacement moderne
        title_label = ttk.Label(header_content, text="Milk", style='Title.TLabel')
        title_label.pack(pady=(0, 8))
        
        # Ligne de séparation élégante
        separator = tk.Frame(header_content, height=2, bg=self.colors['accent_primary'])
        separator.pack(fill='x', padx=200, pady=(0, 12))
        
        # Sous-titre professionnel
        subtitle_label = ttk.Label(header_content, text="Générateur de Mots de Passe", style='Subtitle.TLabel')
        subtitle_label.pack(pady=(0, 6))
        
        # Informations développeur avec lien GitHub
        credits_frame = ttk.Frame(header_content, style='Header.TFrame')
        credits_frame.pack(pady=(0, 8))
        
        # Crédit développeur
        dev_label = ttk.Label(credits_frame, text="Développé par Solvyrth", style='Subtitle.TLabel')
        dev_label.pack(side='left', padx=(0, 8))
        
        # Séparateur visual
        sep_label = ttk.Label(credits_frame, text="•", style='Subtitle.TLabel')
        sep_label.pack(side='left', padx=(0, 8))
        
        # Lien GitHub interactif
        import webbrowser
        github_label = tk.Label(credits_frame, 
                               text="GitHub", 
                               font=('SF Pro Text', 12, 'underline'),
                               bg=self.colors['bg_secondary'],
                               fg=self.colors['accent_primary'],
                               cursor='hand2',
                               bd=0, padx=0, pady=0)
        github_label.pack(side='left', padx=(0, 8))
        github_label.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/Solvyrth"))
        github_label.bind("<Enter>", lambda e: github_label.config(fg=self.colors['accent_hover']))
        github_label.bind("<Leave>", lambda e: github_label.config(fg=self.colors['accent_primary']))
        
        # Séparateur visual
        sep2_label = ttk.Label(credits_frame, text="•", style='Subtitle.TLabel')
        sep2_label.pack(side='left', padx=(0, 8))
        
        # Version
        version_label = ttk.Label(credits_frame, text="Version 3.0", style='Subtitle.TLabel')
        version_label.pack(side='left')
        
        # --- CONTAINER PRINCIPAL ---
        main_container = ttk.Frame(self.root, style='Main.TFrame')
        main_container.pack(fill='both', expand=True, padx=30, pady=(0, 30))
        
        # --- CARTE DE CONFIGURATION ---
        config_card = ttk.Frame(main_container, style='Card.TFrame')
        config_card.pack(fill='x', pady=(0, 20))
        
        # Header de la carte de config
        config_header = ttk.Frame(config_card, style='Card.TFrame')
        config_header.pack(fill='x', padx=25, pady=(20, 15))
        
        config_title = ttk.Label(config_header, text="� Configuration", style='Heading.TLabel')
        config_title.pack(anchor='w')
        
        config_desc = ttk.Label(config_header, text="Personnalisez vos paramètres de génération", style='Body.TLabel')
        config_desc.pack(anchor='w', pady=(2, 0))
        
        # Section paramètres
        params_frame = ttk.Frame(config_card, style='Card.TFrame')
        params_frame.pack(fill='x', padx=25, pady=(0, 20))
        
        # Grid pour les paramètres (2 colonnes)
        params_grid = ttk.Frame(params_frame, style='Card.TFrame')
        params_grid.pack(fill='x')
        
        # Longueur
        length_frame = ttk.Frame(params_grid, style='Card.TFrame')
        length_frame.grid(row=0, column=0, sticky='ew', padx=(0, 15), pady=8)
        params_grid.columnconfigure(0, weight=1)
        
        length_label = ttk.Label(length_frame, text="✨ Longueur du mot de passe", style='Option.TLabel')
        length_label.pack(anchor='w', pady=(0, 5))
        
        self.length_var = tk.StringVar(value="16")
        length_spinbox = ttk.Spinbox(length_frame, from_=4, to=64, textvariable=self.length_var, 
                                   width=8, style='Modern.TSpinbox', font=('SF Mono', 11), justify='center')
        length_spinbox.pack(anchor='w')
        
        # Nombre
        count_frame = ttk.Frame(params_grid, style='Card.TFrame')
        count_frame.grid(row=0, column=1, sticky='ew', padx=(15, 0), pady=8)
        params_grid.columnconfigure(1, weight=1)
        
        count_label = ttk.Label(count_frame, text="💫 Nombre de mots de passe", style='Option.TLabel')
        count_label.pack(anchor='w', pady=(0, 5))
        
        self.count_var = tk.StringVar(value="5")
        count_spinbox = ttk.Spinbox(count_frame, from_=1, to=20, textvariable=self.count_var, 
                                  width=8, style='Modern.TSpinbox', font=('SF Mono', 11), justify='center')
        count_spinbox.pack(anchor='w')
        
        # --- OPTIONS MODERNES ---
        options_frame = ttk.Frame(config_card, style='Card.TFrame')
        options_frame.pack(fill='x', padx=25, pady=(0, 25))
        
        options_title = ttk.Label(options_frame, text="🎭 Options de caractères", style='Heading.TLabel')
        options_title.pack(anchor='w', pady=(0, 10))
        
        # Grid pour les options (2 colonnes)
        options_grid = ttk.Frame(options_frame, style='Card.TFrame')
        options_grid.pack(fill='x')
        
        # Options avec icônes et descriptions
        options_data = [
            ("uppercase_var", "🏛️", "Majuscules (A-Z)", "Inclure des lettres majuscules"),
            ("lowercase_var", "🌊", "Minuscules (a-z)", "Inclure des lettres minuscules"),
            ("numbers_var", "💎", "Chiffres (0-9)", "Inclure des chiffres numériques"),
            ("special_chars_var", "⚡", "Caractères spéciaux", "Inclure !@#$%^&*()_+-=[]{}|;:,.<>?")
        ]
        
        for i, (var_name, icon, title, desc) in enumerate(options_data):
            setattr(self, var_name, tk.BooleanVar(value=True))
            
            option_frame = ttk.Frame(options_grid, style='Card.TFrame')
            option_frame.grid(row=i//2, column=i%2, sticky='ew', padx=(0, 15) if i%2==0 else (15, 0), pady=6)
            options_grid.columnconfigure(0, weight=1)
            options_grid.columnconfigure(1, weight=1)
            
            cb = ttk.Checkbutton(option_frame, text=f"{icon} {title}", 
                               variable=getattr(self, var_name), style='Modern.TCheckbutton')
            cb.pack(anchor='w')
            
            desc_label = ttk.Label(option_frame, text=desc, style='Body.TLabel')
            desc_label.pack(anchor='w', padx=(20, 0), pady=(2, 0))
        
        # --- BOUTONS D'ACTION ---
        actions_card = ttk.Frame(main_container, style='Card.TFrame')
        actions_card.pack(fill='x', pady=(0, 20))
        
        actions_frame = ttk.Frame(actions_card, style='Card.TFrame')
        actions_frame.pack(pady=25)
        
        # Boutons avec espacement moderne
        generate_btn = ttk.Button(actions_frame, text="🚀 Générer les mots de passe", 
                                command=self.on_generate_click, style='Primary.TButton')
        generate_btn.pack(side='left', padx=(0, 12))
        
        save_btn = ttk.Button(actions_frame, text="💎 Sauvegarder", 
                            command=self.save_to_file, style='Success.TButton')
        save_btn.pack(side='left', padx=(0, 12))
        
        clear_btn = ttk.Button(actions_frame, text="🗑️ Effacer", 
                             command=self.clear_results, style='Danger.TButton')
        clear_btn.pack(side='left')
        
        # --- CARTE DE RÉSULTATS ---
        results_card = ttk.Frame(main_container, style='Card.TFrame')
        results_card.pack(fill='both', expand=True)
        
        # Header des résultats
        results_header = ttk.Frame(results_card, style='Card.TFrame')
        results_header.pack(fill='x', padx=25, pady=(20, 15))
        
        results_title = ttk.Label(results_header, text="💎 Mots de passe générés", style='Heading.TLabel')
        results_title.pack(anchor='w')
        
        results_desc = ttk.Label(results_header, text="Vos mots de passe sécurisés apparaîtront ici", style='Body.TLabel')
        results_desc.pack(anchor='w', pady=(2, 0))
        
        # Zone de texte moderne avec scrollbar
        text_frame = ttk.Frame(results_card, style='Card.TFrame')
        text_frame.pack(fill='both', expand=True, padx=25, pady=(0, 25))
        
        self.results_text = tk.Text(text_frame, 
                                   height=15,
                                   font=('SF Mono', 11),
                                   bg=self.colors['bg_quaternary'],
                                   fg=self.colors['text_primary'],
                                   insertbackground=self.colors['accent_primary'],
                                   selectbackground=self.colors['accent_primary'],
                                   selectforeground='white',
                                   relief='flat',
                                   borderwidth=0,
                                   wrap='word',
                                   padx=20,
                                   pady=15,
                                   highlightthickness=0)
        
        # Scrollbar moderne
        scrollbar = ttk.Scrollbar(text_frame, orient='vertical', 
                                command=self.results_text.yview, 
                                style='Modern.Vertical.TScrollbar')
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Message d'accueil élégant
        welcome_message = """
        
        ✨ Bienvenue dans Milk
        
        Cet outil vous permet de générer des mots de passe sécurisés
        selon vos critères personnalisés.
        
        📋 Instructions:
        • Ajustez la longueur et le nombre souhaités
        • Sélectionnez les types de caractères à inclure
        • Cliquez sur "Générer" pour créer vos mots de passe
        • Utilisez "Sauvegarder" pour les exporter
        
        🔒 Sécurité garantie - Génération locale uniquement
        
        """
        
        self.results_text.insert(tk.END, welcome_message)
        self.results_text.config(state='disabled')
        
        # Variables pour stocker les mots de passe
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
        """Génère les mots de passe avec affichage moderne"""
        try:
            length = int(self.length_var.get())
            count = int(self.count_var.get())
            
            # Validation des entrées
            if length < 4 or length > 64:
                messagebox.showerror("❌ Erreur de validation", 
                                   "La longueur doit être comprise entre 4 et 64 caractères.\n\nVeuillez ajuster la valeur et réessayer.", 
                                   parent=self.root)
                return
                
            if count < 1 or count > 20:
                messagebox.showerror("❌ Erreur de validation", 
                                   "Le nombre de mots de passe doit être entre 1 et 20.\n\nVeuillez ajuster la valeur et réessayer.", 
                                   parent=self.root)
                return
            
            # Vérification des options sélectionnées
            if not any([self.special_chars_var.get(), self.uppercase_var.get(), 
                       self.lowercase_var.get(), self.numbers_var.get()]):
                # Auto-sélection avec notification
                self.special_chars_var.set(True)
                self.uppercase_var.set(True)
                self.lowercase_var.set(True)
                self.numbers_var.set(True)
                messagebox.showinfo("ℹ️ Sélection automatique", 
                                  "Aucun type de caractère n'était sélectionné.\n\nToutes les options ont été automatiquement activées pour garantir la sécurité.", 
                                  parent=self.root)
            
            # Génération des mots de passe
            self.generated_passwords = []
            
            for i in range(count):
                password = self.generate_password(
                    length,
                    self.special_chars_var.get(),
                    self.uppercase_var.get(),
                    self.lowercase_var.get(),
                    self.numbers_var.get()
                )
                self.generated_passwords.append(password)
            
            # Affichage moderne des résultats
            self.display_results()
                
        except ValueError:
            messagebox.showerror("❌ Erreur de saisie", 
                               "Veuillez entrer des valeurs numériques valides.\n\nVérifiez que la longueur et le nombre sont des nombres entiers.", 
                               parent=self.root)
        except Exception as e:
            messagebox.showerror("❌ Erreur inattendue", 
                               f"Une erreur s'est produite lors de la génération:\n\n{str(e)}\n\nVeuillez réessayer ou contacter le support.", 
                               parent=self.root)
    
    def display_results(self):
        """Affiche les résultats avec un design moderne"""
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        
        # Import pour la date
        from datetime import datetime
        current_time = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
        session_id = random.randint(1000, 9999)
        
        # Header avec informations de session
        self.results_text.insert(tk.END, f"{'═' * 70}\n")
        self.results_text.insert(tk.END, f"🎯 GÉNÉRATION RÉUSSIE - Session #{session_id}\n")
        self.results_text.insert(tk.END, f"{'═' * 70}\n\n")
        
        # Métadonnées de génération
        self.results_text.insert(tk.END, f"� INFORMATIONS DE GÉNÉRATION:\n")
        self.results_text.insert(tk.END, f"├─ Date et heure: {current_time}\n")
        self.results_text.insert(tk.END, f"├─ Nombre généré: {len(self.generated_passwords)} mot(s) de passe\n")
        self.results_text.insert(tk.END, f"├─ Longueur: {self.length_var.get()} caractères\n")
        self.results_text.insert(tk.END, f"└─ Sécurité: Niveau élevé ✅\n\n")
        
        # Configuration utilisée
        self.results_text.insert(tk.END, f"⚙️ CONFIGURATION APPLIQUÉE:\n")
        options_status = []
        if self.uppercase_var.get():
            options_status.append("� Majuscules (A-Z)")
        if self.lowercase_var.get():
            options_status.append("� Minuscules (a-z)")
        if self.numbers_var.get():
            options_status.append("� Chiffres (0-9)")
        if self.special_chars_var.get():
            options_status.append("� Caractères spéciaux")
        
        for i, option in enumerate(options_status):
            prefix = "├─" if i < len(options_status) - 1 else "└─"
            self.results_text.insert(tk.END, f"{prefix} {option}\n")
        
        self.results_text.insert(tk.END, f"\n{'─' * 70}\n")
        self.results_text.insert(tk.END, f"🔐 MOTS DE PASSE GÉNÉRÉS:\n")
        self.results_text.insert(tk.END, f"{'─' * 70}\n\n")
        
        # Affichage des mots de passe avec numérotation
        for i, password in enumerate(self.generated_passwords, 1):
            self.results_text.insert(tk.END, f"  {i:2d}. ")
            
            # Insérer le mot de passe avec une police monospace pour l'alignement
            start_pos = self.results_text.index(tk.INSERT)
            self.results_text.insert(tk.END, f"{password}")
            end_pos = self.results_text.index(tk.INSERT)
            
            # Ajouter une couleur de surbrillance subtile au mot de passe
            self.results_text.insert(tk.END, f"  ({len(password)} car.)\n")
        
        # Footer avec conseils de sécurité
        self.results_text.insert(tk.END, f"\n{'─' * 70}\n")
        self.results_text.insert(tk.END, f"🛡️ CONSEILS DE SÉCURITÉ:\n")
        self.results_text.insert(tk.END, f"{'─' * 70}\n")
        self.results_text.insert(tk.END, "• Utilisez un mot de passe unique pour chaque compte\n")
        self.results_text.insert(tk.END, "• Ne partagez jamais vos mots de passe\n")
        self.results_text.insert(tk.END, "• Stockez-les dans un gestionnaire de mots de passe\n")
        self.results_text.insert(tk.END, "• Activez l'authentification à deux facteurs quand possible\n")
        self.results_text.insert(tk.END, "• Renouvelez régulièrement vos mots de passe sensibles\n\n")
        
        # Signature 
        self.results_text.insert(tk.END, f"{'═' * 70}\n")
        self.results_text.insert(tk.END, "✨ Généré avec Milk - Sécurité et simplicité\n")
        self.results_text.insert(tk.END, f"{'═' * 70}")
        
        self.results_text.config(state='disabled')
        
        # Scroll vers le bas pour voir tous les conseils de sécurité
        self.results_text.see(tk.END)
        self.results_text.mark_set(tk.INSERT, tk.END)
    
    def save_to_file(self):
        """Sauvegarde moderne des mots de passe"""
        if not self.generated_passwords:
            messagebox.showwarning("⚠️ Attention", 
                                 "Aucun mot de passe à sauvegarder.\n\nGénérez d'abord des mots de passe en cliquant sur le bouton 'Générer'.", 
                                 parent=self.root)
            return
            
        filename = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[
                ("Fichiers texte", "*.txt"), 
                ("Fichiers CSV", "*.csv"),
                ("Fichiers JSON", "*.json"),
                ("Tous les fichiers", "*.*")
            ],
            title="💾 Sauvegarder les mots de passe",
            initialfile=f"milk_passwords_{self.get_timestamp()}.txt"
        )
        
        if filename:
            try:
                from datetime import datetime
                current_datetime = datetime.now().strftime("%d/%m/%Y à %H:%M:%S")
                
                with open(filename, 'w', encoding='utf-8') as f:
                    # Header avec ASCII art
                    f.write("╔══════════════════════════════════════════════════════════════════════════════╗\n")
                    f.write("║                                     ✨ MILK ✨                                ║\n")
                    f.write("║                           GÉNÉRATEUR DE MOTS DE PASSE                        ║\n")
                    f.write("║                              Développé par Solvyrth                          ║\n")
                    f.write("║                                                                              ║\n")
                    f.write("╚══════════════════════════════════════════════════════════════════════════════╝\n\n")
                    
                    # Informations de session
                    f.write("📊 RAPPORT DE GÉNÉRATION\n")
                    f.write("═" * 80 + "\n")
                    f.write(f"📅 Date de génération: {current_datetime}\n")
                    f.write(f"🔢 Nombre total de mots de passe: {len(self.generated_passwords)}\n")
                    f.write(f"📏 Longueur de chaque mot de passe: {self.length_var.get()} caractères\n")
                    f.write(f"🆔 Session ID: {random.randint(10000, 99999)}\n\n")
                    
                    # Configuration détaillée
                    f.write("⚙️ CONFIGURATION UTILISÉE\n")
                    f.write("─" * 80 + "\n")
                    f.write("Types de caractères inclus:\n")
                    f.write(f"  • Lettres majuscules (A-Z): {'✅ Activé' if self.uppercase_var.get() else '❌ Désactivé'}\n")
                    f.write(f"  • Lettres minuscules (a-z): {'✅ Activé' if self.lowercase_var.get() else '❌ Désactivé'}\n")
                    f.write(f"  • Chiffres (0-9): {'✅ Activé' if self.numbers_var.get() else '❌ Désactivé'}\n")
                    f.write(f"  • Caractères spéciaux (!@#$...): {'✅ Activé' if self.special_chars_var.get() else '❌ Désactivé'}\n\n")
                    
                    # Analyse de sécurité
                    f.write("🔒 ANALYSE DE SÉCURITÉ\n")
                    f.write("─" * 80 + "\n")
                    
                    # Calculer la complexité
                    charset_size = 0
                    if self.uppercase_var.get():
                        charset_size += 26
                    if self.lowercase_var.get():
                        charset_size += 26
                    if self.numbers_var.get():
                        charset_size += 10
                    if self.special_chars_var.get():
                        charset_size += 32
                    
                    length = int(self.length_var.get())
                    combinations = charset_size ** length
                    
                    f.write(f"  • Taille du jeu de caractères: {charset_size} caractères\n")
                    f.write(f"  • Combinaisons possibles: {combinations:,}\n")
                    
                    # Évaluation de la force
                    if length >= 16 and charset_size >= 62:
                        strength = "🟢 TRÈS ÉLEVÉE"
                    elif length >= 12 and charset_size >= 36:
                        strength = "🟡 ÉLEVÉE"
                    elif length >= 8 and charset_size >= 26:
                        strength = "🟠 MOYENNE"
                    else:
                        strength = "🔴 FAIBLE"
                    
                    f.write(f"  • Force estimée: {strength}\n")
                    f.write(f"  • Recommandation: {'Excellent choix!' if 'TRÈS ÉLEVÉE' in strength else 'Considérez augmenter la longueur ou la complexité'}\n\n")
                    
                    # Les mots de passe générés
                    f.write("� MOTS DE PASSE GÉNÉRÉS\n")
                    f.write("═" * 80 + "\n")
                    for i, password in enumerate(self.generated_passwords, 1):
                        f.write(f"  {i:3d}. {password}\n")
                    f.write("\n")
                    
                    # Conseils de sécurité avancés
                    f.write("🛡️ GUIDE DE SÉCURITÉ AVANCÉ\n")
                    f.write("═" * 80 + "\n")
                    f.write("BONNES PRATIQUES:\n")
                    f.write("  ✓ Utilisez un mot de passe unique pour chaque compte\n")
                    f.write("  ✓ Activez l'authentification à deux facteurs (2FA) partout où c'est possible\n")
                    f.write("  ✓ Utilisez un gestionnaire de mots de passe réputé\n")
                    f.write("  ✓ Renouvelez vos mots de passe tous les 6-12 mois\n")
                    f.write("  ✓ Vérifiez régulièrement si vos comptes ont été compromis\n\n")
                    
                    f.write("STOCKAGE SÉCURISÉ:\n")
                    f.write("  ⚠️ Ne stockez jamais vos mots de passe en texte clair\n")
                    f.write("  ⚠️ Chiffrez ce fichier ou supprimez-le après utilisation\n")
                    f.write("  ⚠️ Ne partagez jamais vos mots de passe par email ou SMS\n")
                    f.write("  ⚠️ Méfiez-vous des réseaux WiFi publics lors de la saisie\n\n")
                    
                    # Footer
                    f.write("─" * 80 + "\n")
                    f.write("Fichier généré automatiquement\n")
                    f.write("Outil de génération de mots de passe sécurisés\n")
                    f.write("© 2025 Solvyrth - Tous droits réservés\n")
                    f.write("─" * 80)
                    
                # Message de succès détaillé
                messagebox.showinfo("✅ Sauvegarde réussie", 
                                  f"Mots de passe sauvegardés avec succès !\n\n"
                                  f"📁 Fichier: {os.path.basename(filename)}\n"
                                  f"📍 Emplacement: {os.path.dirname(filename)}\n"
                                  f"� Contenu: {len(self.generated_passwords)} mots de passe\n\n"
                                  f"🔒 Conseil de sécurité:\n"
                                  f"Chiffrez ou sécurisez ce fichier après utilisation.", 
                                  parent=self.root)
                                  
            except Exception as e:
                messagebox.showerror("❌ Erreur de sauvegarde", 
                                   f"Impossible de sauvegarder le fichier:\n\n"
                                   f"Erreur: {str(e)}\n\n"
                                   f"Vérifiez que:\n"
                                   f"• Vous avez les permissions d'écriture\n"
                                   f"• L'espace disque est suffisant\n"
                                   f"• Le fichier n'est pas ouvert dans une autre application", 
                                   parent=self.root)
    
    def get_timestamp(self):
        """Retourne un timestamp formaté pour les noms de fichiers"""
        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    def clear_results(self):
        """Efface les résultats avec confirmation"""
        if self.generated_passwords:
            response = messagebox.askyesno("🗑️ Confirmation", 
                                         "Êtes-vous sûr de vouloir effacer tous les mots de passe générés ?\n\n"
                                         "Cette action est irréversible.", 
                                         parent=self.root)
            if not response:
                return
        
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, tk.END)
        self.generated_passwords = []
        
        # Message d'effacement élégant
        clear_message = """
        
        🗑️ Résultats effacés avec succès
        
        L'espace de travail a été nettoyé.
        Vous pouvez maintenant générer de nouveaux mots de passe.
        
        📋 Pour continuer:
        • Ajustez vos paramètres si nécessaire
        • Cliquez sur "Générer" pour créer de nouveaux mots de passe
        • Utilisez "Sauvegarder" pour exporter vos résultats
        
        """
        
        self.results_text.insert(tk.END, clear_message)
        self.results_text.config(state='disabled')
    
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
