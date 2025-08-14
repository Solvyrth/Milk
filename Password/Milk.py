import random
import string
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Milk ✨")
        self.root.geometry("1200x1200")  # Agrandi pour plus d'espace avec les sections compactes
        self.root.resizable(False, False)  # Bloquer le redimensionnement
        self.root.minsize(700, 600)
        
        # Palette de couleurs moderne avec couleurs pour la barre de titre
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
            'shadow': 'rgba(0, 0, 0, 0.3)', # Ombre
            # Couleurs spécifiques pour la barre de titre
            'titlebar_bg': '#12142A',     # Fond barre de titre
            'titlebar_border': '#1E1E3A', # Bordure barre de titre
            'close_btn': '#FF5F57',       # Rouge close button
            'close_btn_hover': '#FF3B30', # Rouge close hover
            'minimize_btn': '#FFBD2E',    # Jaune minimize button
            'minimize_btn_hover': '#FF9500', # Orange minimize hover
            'maximize_btn': '#28CA42',    # Vert maximize button
            'maximize_btn_hover': '#30D158' # Vert maximize hover
        }
        
        self.password_dictionary = {
            'animaux': ['chat', 'chien', 'lion', 'tigre', 'ours', 'loup', 'aigle', 'faucon', 'requin', 'baleine', 'elephant', 'girafe', 'zebre', 'panda', 'koala'],
            'nature': ['montagne', 'ocean', 'foret', 'riviere', 'soleil', 'lune', 'etoile', 'nuage', 'orage', 'vent', 'pluie', 'neige', 'feu', 'terre', 'ciel'],
            'couleurs': ['rouge', 'bleu', 'vert', 'jaune', 'violet', 'orange', 'rose', 'noir', 'blanc', 'gris', 'dore', 'argent', 'bronze', 'turquoise', 'magenta'],
            'technologie': ['ordinateur', 'internet', 'robot', 'laser', 'satellite', 'quantum', 'digital', 'cyber', 'nano', 'pixel', 'data', 'code', 'virus', 'firewall', 'cloud'],
            'objets': ['maison', 'voiture', 'telephone', 'livre', 'table', 'chaise', 'fenetre', 'porte', 'clavier', 'souris', 'ecran', 'lampe', 'stylo', 'papier', 'horloge'],
            'actions': ['courir', 'sauter', 'nager', 'voler', 'marcher', 'danser', 'chanter', 'rire', 'pleurer', 'dormir', 'manger', 'boire', 'jouer', 'travailler', 'etudier'],
            'adjectifs': ['grand', 'petit', 'beau', 'laid', 'rapide', 'lent', 'fort', 'faible', 'intelligent', 'stupide', 'heureux', 'triste', 'calme', 'nerveux', 'brave']
        }
        
        # Dictionnaire pour les passphrases
        self.passphrase_dictionary = {
            'noms': ['soleil', 'montagne', 'ocean', 'foret', 'riviere', 'etoile', 'nuage', 'fleur', 'arbre', 'oiseau', 'maison', 'pont', 'route', 'jardin', 'lac'],
            'adjectifs': ['magnifique', 'brillant', 'mysterieux', 'paisible', 'puissant', 'elegant', 'rapide', 'silencieux', 'colore', 'lumineux', 'ancien', 'moderne', 'secret', 'magique', 'libre'],
            'verbes': ['brille', 'danse', 'vole', 'chante', 'court', 'nage', 'saute', 'reve', 'voyage', 'explore', 'decouvre', 'cree', 'transforme', 'inspire', 'protege'],
            'connecteurs': ['avec', 'vers', 'dans', 'sous', 'sur', 'entre', 'parmi', 'contre', 'pour', 'sans', 'depuis', 'durant', 'pendant', 'malgre', 'grace']
        }
        
        # Substitutions de caractères pour le mode dictionnaire
        self.char_substitutions = {
            'a': ['@', '4'],
            'e': ['3', '€'],
            'i': ['1', '!'],
            'o': ['0', '°'],
            'u': ['µ', 'ü'],
            's': ['$', '5'],
            't': ['7', '+'],
            'l': ['1', '|'],
            'g': ['6', '9']
        }
        
        # Dictionnaire original avec plus de catégories
        self.original_dictionary = {
            'mythologie': ['dragon', 'phoenix', 'licorne', 'griffon', 'kraken', 'hydre', 'sphinx', 'pegase', 'centaure', 'minotaure', 'titan', 'atlas', 'hercule', 'thor', 'odin'],
            'science': ['atome', 'neutron', 'photon', 'galaxie', 'nebuleuse', 'cosmos', 'molecule', 'electron', 'proton', 'energie', 'matiere', 'plasma', 'fusion', 'quasar', 'pulsar'],
            'emotions': ['joie', 'amour', 'espoir', 'courage', 'force', 'paix', 'liberte', 'passion', 'reve', 'bonheur', 'sagesse', 'serenite', 'harmonie', 'energie', 'victoire'],
            'objets': ['diamant', 'cristal', 'prisme', 'miroir', 'epee', 'bouclier', 'couronne', 'tresor', 'coffre', 'cle', 'serrure', 'pont', 'tour', 'chateau', 'temple']
        }
        
        # Dictionnaire pour les phrases de passe (passphrases)
        self.passphrase_dictionary = {
            'adjectifs': ['grand', 'petit', 'rapide', 'lent', 'brillant', 'sombre', 'fort', 'doux', 'froid', 'chaud', 'nouveau', 'ancien', 'beau', 'magnifique', 'mysterieux'],
            'noms': ['maison', 'jardin', 'montagne', 'riviere', 'etoile', 'fleur', 'arbre', 'porte', 'fenetre', 'chemin', 'voyage', 'secret', 'tresor', 'aventure', 'histoire'],
            'verbes': ['marcher', 'courir', 'voler', 'danser', 'chanter', 'rire', 'dormir', 'rever', 'jouer', 'explorer', 'decouvrir', 'creer', 'construire', 'proteger', 'aimer'],
            'connecteurs': ['avec', 'dans', 'sur', 'sous', 'vers', 'depuis', 'pendant', 'avant', 'apres', 'entre', 'parmi', 'grace', 'malgre', 'selon', 'comme']
        }
        
        # Caractères de substitution pour rendre les mots plus sécurisés
        self.char_substitutions = {
            'a': ['@', '4', 'A'],
            'e': ['3', 'E', '€'],
            'i': ['1', '!', 'I'],
            'o': ['0', 'O', '°'],
            'u': ['U', 'µ'],
            's': ['$', '5', 'S'],
            't': ['7', 'T', '+'],
            'l': ['1', 'L', '|'],
            'g': ['6', 'G'],
            'b': ['8', 'B']
        }
        
        # Variables pour le drag and drop de la fenêtre
        self._dragging = False
        self._drag_start_x = 0
        self._drag_start_y = 0
        self._is_maximized = False
        self._normal_geometry = "1200x1200+100+100"  # Mise à jour avec la taille agrandie
        
        # Supprimer la barre de titre native
        self.root.overrideredirect(True)
        self.root.configure(bg='#000000')  # Noir pur pour les bordures
        
        # S'assurer que la fenêtre peut recevoir le focus
        self.root.focus_force()
        self.root.lift()
        
        # Créer un conteneur externe pour les bordures noires
        self.border_container = tk.Frame(self.root, bg='#000000')
        self.border_container.pack(fill='both', expand=True, padx=0, pady=0)
        
        # Créer un frame principal avec des marges réduites pour moins d'ombre
        self.main_window = tk.Frame(self.border_container, bg=self.colors['bg_primary'], relief='flat', bd=0)
        self.main_window.pack(fill='both', expand=True, padx=2, pady=2)
        
        # Permettre au main_window de recevoir le focus
        self.main_window.bind('<Button-1>', lambda e: self.main_window.focus_set())
        
        # Configuration du style moderne
        self.setup_modern_styles()
        self.setup_ui()
        
    def create_custom_titlebar(self):
        """Crée une barre de titre personnalisée avec boutons macOS"""
        self.titlebar = tk.Frame(self.main_window, bg=self.colors['titlebar_bg'], height=40)
        self.titlebar.pack(fill='x', side='top')
        self.titlebar.pack_propagate(False)
        
        # Bordure inférieure de la barre de titre
        border = tk.Frame(self.titlebar, bg=self.colors['titlebar_border'], height=1)
        border.pack(fill='x', side='bottom')
        
        # Container pour les boutons (côté gauche)
        buttons_frame = tk.Frame(self.titlebar, bg=self.colors['titlebar_bg'])
        buttons_frame.pack(side='left', padx=10, pady=8)
        
        # Créer les boutons avec Canvas pour un meilleur contrôle des couleurs
        self.create_window_button(buttons_frame, self.colors['close_btn'], self.colors['close_btn_hover'], 
                                 '✕', self.close_window, 'close')
        self.create_window_button(buttons_frame, self.colors['minimize_btn'], self.colors['minimize_btn_hover'], 
                                 '−', self.minimize_window, 'minimize')
        # Désactiver le bouton maximiser - pas de fonction
        self.create_window_button(buttons_frame, '#4A4A4A', '#5A5A5A', 
                                 '', self.do_nothing, 'disabled')
        
        # Titre au centre de la barre
        self.title_label = tk.Label(self.titlebar, 
                                   text="✨ Milk ✨",
                                   bg=self.colors['titlebar_bg'],
                                   fg=self.colors['text_primary'],
                                   font=('SF Pro Display', 13, 'normal'))
        self.title_label.pack(expand=True)
        
        # Rendre la barre de titre draggable
        self.titlebar.bind("<Button-1>", self.start_drag)
        self.titlebar.bind("<B1-Motion>", self.do_drag)
        self.titlebar.bind("<ButtonRelease-1>", self.stop_drag)
        self.title_label.bind("<Button-1>", self.start_drag)
        self.title_label.bind("<B1-Motion>", self.do_drag)
        self.title_label.bind("<ButtonRelease-1>", self.stop_drag)
        
        # Double-clic pour maximiser/restaurer - désactivé
        # self.titlebar.bind("<Double-Button-1>", lambda e: self.toggle_maximize())
        # self.title_label.bind("<Double-Button-1>", lambda e: self.toggle_maximize())
    
    def create_window_button(self, parent, color, hover_color, symbol, command, btn_type):
        """Crée un bouton de fenêtre avec Canvas pour un meilleur contrôle des couleurs"""
        canvas = tk.Canvas(parent, width=14, height=14, bg=self.colors['titlebar_bg'], 
                          highlightthickness=0, bd=0)
        canvas.pack(side='left', padx=3, pady=1)
        
        # Dessiner le cercle coloré
        circle = canvas.create_oval(1, 1, 13, 13, fill=color, outline=color)
        
        # Variables pour stocker les références
        canvas.color = color
        canvas.hover_color = hover_color
        canvas.symbol = symbol
        canvas.circle = circle
        canvas.text_item = None
        
        # Événements
        def on_enter(event):
            canvas.config(cursor='hand2')
            canvas.itemconfig(circle, fill=hover_color, outline=hover_color)
            if canvas.text_item:
                canvas.delete(canvas.text_item)
            canvas.text_item = canvas.create_text(7, 7, text=symbol, fill='white', 
                                                 font=('System', 8, 'bold'))
        
        def on_leave(event):
            canvas.config(cursor='')
            canvas.itemconfig(circle, fill=color, outline=color)
            if canvas.text_item:
                canvas.delete(canvas.text_item)
                canvas.text_item = None
        
        def on_click(event):
            command()
        
        canvas.bind('<Enter>', on_enter)
        canvas.bind('<Leave>', on_leave)
        canvas.bind('<Button-1>', on_click)
        
        # Stocker la référence pour pouvoir la modifier plus tard
        if btn_type == 'close':
            self.close_canvas = canvas
        elif btn_type == 'minimize':
            self.minimize_canvas = canvas
        elif btn_type == 'maximize':
            self.maximize_canvas = canvas
    
    def start_drag(self, event):
        """Démarre le drag de la fenêtre"""
        self._dragging = True
        self._drag_start_x = event.x_root - self.root.winfo_rootx()
        self._drag_start_y = event.y_root - self.root.winfo_rooty()
    
    def do_drag(self, event):
        """Effectue le drag de la fenêtre"""
        if self._dragging:
            x = event.x_root - self._drag_start_x
            y = event.y_root - self._drag_start_y
            self.root.geometry(f"+{x}+{y}")
    
    def stop_drag(self, event):
        """Arrête le drag de la fenêtre"""
        self._dragging = False
    
    def close_window(self):
        """Ferme la fenêtre"""
        self.root.quit()
        self.root.destroy()
    
    def do_nothing(self):
        """Fonction vide pour le bouton maximiser désactivé"""
        pass
    
    def minimize_window(self):
        """Minimise la fenêtre de façon simple et efficace"""
        try:
            # Méthode simple : désactiver temporairement overrideredirect
            self.root.overrideredirect(False)
            # Minimiser normalement
            self.root.iconify()
            # Programmer la restauration d'overrideredirect quand la fenêtre est restaurée
            self.root.after(100, self.setup_restore_handler)
        except Exception as e:
            print(f"Erreur minimisation: {e}")
            # En cas d'erreur, juste cacher la fenêtre
            self.root.withdraw()
            self.show_restore_notification()
    
    def setup_restore_handler(self):
        """Configure le gestionnaire de restauration"""
        def on_deiconify(event):
            if event.widget == self.root:
                # Réactiver overrideredirect quand la fenêtre est restaurée
                self.root.after(50, lambda: self.root.overrideredirect(True))
                self.root.unbind('<Map>')
        
        # Écouter l'événement de restauration
        self.root.bind('<Map>', on_deiconify)
    
    def show_restore_notification(self):
        """Affiche une notification pour restaurer (méthode de secours)"""
        import subprocess
        import sys
        
        if sys.platform == 'darwin':  # macOS
            try:
                # Utiliser AppleScript pour afficher une notification
                script = '''
                display notification "Cliquez ici pour restaurer Milk" with title "Milk minimisé" 
                '''
                subprocess.run(['osascript', '-e', script])
                
                # Restaurer la fenêtre après 3 secondes
                self.root.after(3000, self.restore_window)
            except:
                # Fallback : restaurer directement
                self.root.after(1000, self.restore_window)
    
    def restore_window(self):
        """Restaure la fenêtre principale"""
        try:
            self.root.deiconify()
            self.root.lift()
            self.root.focus_force()
        except Exception as e:
            print(f"Erreur restauration: {e}")
    
    # Supprimer les anciennes fonctions qui causent des problèmes
    def create_dock_icon(self):
        """Fonction dépréciée - plus utilisée"""
        pass
    
    def restore_from_minimize(self, temp_window):
        """Restaure la fenêtre depuis la minimisation"""
        temp_window.destroy()
        self.root.deiconify()
    
    def toggle_maximize(self):
        """Basculer entre maximisé et normal"""
        if self._is_maximized:
            # Restaurer à la taille normale
            self.root.geometry(self._normal_geometry)
            self._is_maximized = False
        else:
            # Sauvegarder la géométrie actuelle
            self._normal_geometry = self.root.geometry()
            # Maximiser (prendre toute la taille de l'écran)
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            # Ajuster pour les barres de menu/dock sur macOS
            if hasattr(self.root, 'winfo_screenmmwidth'):
                # Laisser un peu d'espace pour le menu et le dock
                self.root.geometry(f"{screen_width}x{screen_height-100}+0+25")
            else:
                self.root.geometry(f"{screen_width}x{screen_height}+0+0")
            self._is_maximized = True

    def setup_window_appearance(self):
        """Configure l'apparence de la fenêtre pour s'harmoniser avec le thème"""
        # Cette fonction n'est plus nécessaire car on utilise overrideredirect
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
                       selectforeground='white',
                       relief='flat',
                       borderwidth=1)
        
        style.map('Modern.TSpinbox',
                 fieldbackground=[('focus', self.colors['bg_quaternary'])],
                 bordercolor=[('focus', self.colors['accent_primary'])],
                 arrowcolor=[('active', self.colors['accent_primary'])])
        
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
        
        # Créer la barre de titre personnalisée en premier
        self.create_custom_titlebar()
        
        # --- HEADER ÉLÉGANT ---
        header_frame = ttk.Frame(self.main_window, style='Header.TFrame')
        header_frame.pack(fill='x', pady=0)
        
        # Container pour centrer le contenu du header
        header_content = ttk.Frame(header_frame, style='Header.TFrame')
        header_content.pack(expand=True, fill='both', pady=40)
        
        # Titre principal avec espacement moderne
        title_label = ttk.Label(header_content, text="✨ Milk ✨", style='Title.TLabel')
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
        version_label = ttk.Label(credits_frame, text="Version 3.1", style='Subtitle.TLabel')
        version_label.pack(side='left')
        
        # --- CONTAINER PRINCIPAL ---
        main_container = ttk.Frame(self.main_window, style='Main.TFrame')
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
        
        # Permettre la saisie directe dans le spinbox
        length_spinbox.bind('<Button-1>', lambda e: length_spinbox.focus_set())
        length_spinbox.bind('<FocusIn>', lambda e: length_spinbox.selection_range(0, tk.END))
        
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
        
        # Permettre la saisie directe dans le spinbox
        count_spinbox.bind('<Button-1>', lambda e: count_spinbox.focus_set())
        count_spinbox.bind('<FocusIn>', lambda e: count_spinbox.selection_range(0, tk.END))
        
        # --- OPTIONS MODERNES ---
        options_frame = ttk.Frame(config_card, style='Card.TFrame')
        options_frame.pack(fill='x', padx=25, pady=(0, 20))
        
        options_title = ttk.Label(options_frame, text="🎭 Options de caractères", style='Heading.TLabel')
        options_title.pack(anchor='w', pady=(0, 8))
        
        # Grid compact pour les options (2x2)
        options_grid = ttk.Frame(options_frame, style='Card.TFrame')
        options_grid.pack(fill='x')
        
        # Options avec icônes seulement
        options_data = [
            ("uppercase_var", "🏛️", "Majuscules"),
            ("lowercase_var", "🌊", "Minuscules"), 
            ("numbers_var", "💎", "Chiffres"),
            ("special_chars_var", "⚡", "Spéciaux")
        ]
        
        for i, (var_name, icon, title) in enumerate(options_data):
            setattr(self, var_name, tk.BooleanVar(value=True))
            
            cb = ttk.Checkbutton(options_grid, text=f"{icon} {title}", 
                               variable=getattr(self, var_name), style='Modern.TCheckbutton')
            cb.grid(row=i//2, column=i%2, sticky='w', padx=10, pady=3)
            options_grid.columnconfigure(0, weight=1)
            options_grid.columnconfigure(1, weight=1)
        
        # --- NOUVEAU : SECTION MODES AVANCÉS (DICTIONNAIRE + PASSPHRASE) ---
        advanced_modes_frame = ttk.Frame(config_card, style='Card.TFrame')
        advanced_modes_frame.pack(fill='x', padx=25, pady=(15, 20))
        
        # Container pour les deux modes côte à côte
        modes_container = ttk.Frame(advanced_modes_frame, style='Card.TFrame')
        modes_container.pack(fill='x')
        
        # COLONNE GAUCHE - MODE DICTIONNAIRE
        dict_column = ttk.Frame(modes_container, style='Card.TFrame')
        dict_column.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        self.capitalize_var = tk.BooleanVar(value=True)
        self.substitute_chars_var = tk.BooleanVar(value=True)
        self.add_numbers_var = tk.BooleanVar(value=True)
        self.add_symbols_var = tk.BooleanVar(value=True)
        
        # Modifications compactes en 2x2
        modifications_data = [
            (self.capitalize_var, "�"), (self.substitute_chars_var, "🔄"),
            (self.add_numbers_var, "🔢"), (self.add_symbols_var, "⚡")
        ]
        


        # --- NOUVEAU : SECTION MODES AVANCÉS (DICTIONNAIRE + PASSPHRASE) ---
        advanced_modes_frame = ttk.Frame(config_card, style='Card.TFrame')
        advanced_modes_frame.pack(fill='x', padx=25, pady=(15, 20))
        
        # Container pour les deux modes côte à côte
        modes_container = ttk.Frame(advanced_modes_frame, style='Card.TFrame')
        modes_container.pack(fill='x')
        
        # COLONNE GAUCHE - MODE DICTIONNAIRE
        dict_column = ttk.Frame(modes_container, style='Card.TFrame')
        dict_column.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        dict_title = ttk.Label(dict_column, text="📚 Mode Dictionnaire", style='Heading.TLabel')
        dict_title.pack(anchor='w', pady=(0, 8))
        
        # Option pour activer le mode dictionnaire (déplacée ici)
        self.use_dictionary_var = tk.BooleanVar(value=False)
        dict_checkbox = ttk.Checkbutton(dict_column, text="🎭 Utiliser des mots de base du dictionnaire", 
                                       variable=self.use_dictionary_var, style='Modern.TCheckbutton',
                                       command=self.toggle_dictionary_options)
        dict_checkbox.pack(anchor='w', pady=(0, 8))
        
        # Frame pour les options du dictionnaire (initialement cachées)
        self.dict_options_frame = ttk.Frame(dict_column, style='Card.TFrame')
        self.dict_options_frame.pack(fill='x', padx=(20, 0))
        
        # Container principal pour tout organiser horizontalement
        main_dict_container = ttk.Frame(self.dict_options_frame, style='Card.TFrame')
        main_dict_container.pack(fill='x', pady=(5, 10))
        
        # COLONNE GAUCHE - Catégories
        left_dict_col = ttk.Frame(main_dict_container, style='Card.TFrame')
        left_dict_col.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        categories_label = ttk.Label(left_dict_col, text="🏷️ Catégories:", style='Option.TLabel')
        categories_label.pack(anchor='w', pady=(0, 3))
        
        # Variables pour les catégories
        self.category_vars = {}
        categories_data = [
            ('objets', '🏠', 'Objets'),
            ('animaux', '🦁', 'Animaux'), 
            ('couleurs', '🌈', 'Couleurs'),
            ('actions', '⚡', 'Actions'),
            ('adjectifs', '✨', 'Adjectifs')
        ]
        
        # Grid ultra-compact pour les catégories (3x2)
        cat_grid = ttk.Frame(left_dict_col, style='Card.TFrame')
        cat_grid.pack(fill='x')
        
        for i, (category, emoji, label) in enumerate(categories_data):
            self.category_vars[category] = tk.BooleanVar(value=True)
            cb = ttk.Checkbutton(cat_grid, text=f"{emoji} {label}", 
                               variable=self.category_vars[category], style='Modern.TCheckbutton')
            cb.grid(row=i//3, column=i%3, sticky='w', padx=3, pady=1)
            for j in range(3):
                cat_grid.columnconfigure(j, weight=1)
        
        # COLONNE DROITE - Modifications
        right_dict_col = ttk.Frame(main_dict_container, style='Card.TFrame')
        right_dict_col.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        security_label = ttk.Label(right_dict_col, text="🔧 Modifications:", style='Option.TLabel')
        security_label.pack(anchor='w', pady=(0, 3))
        
        # Grid ultra-compact pour les modifications (2x2)
        mod_grid = ttk.Frame(right_dict_col, style='Card.TFrame')
        mod_grid.pack(fill='x')
        
        modifications_data = [
            (self.capitalize_var, "💼", "Caps"), (self.substitute_chars_var, "🔄", "Subst"),
            (self.add_numbers_var, "🔢", "Nums"), (self.add_symbols_var, "⚡", "Symbs")
        ]
        
        for i, (var, icon, label) in enumerate(modifications_data):
            cb = ttk.Checkbutton(mod_grid, text=f"{icon} {label}", 
                               variable=var, style='Modern.TCheckbutton')
            cb.grid(row=i//2, column=i%2, sticky='w', padx=3, pady=1)
            mod_grid.columnconfigure(0, weight=1)
            mod_grid.columnconfigure(1, weight=1)
        
        # Bouton aperçu en bas, centré
        preview_frame = ttk.Frame(self.dict_options_frame, style='Card.TFrame')
        preview_frame.pack(fill='x', pady=(5, 0))
        
        preview_btn = ttk.Button(preview_frame, text="👁️ Aperçu", 
                               command=self.show_dictionary_preview, style='Primary.TButton')
        preview_btn.pack(side='left')
        
        self.preview_label = ttk.Label(preview_frame, text="", style='Body.TLabel')
        self.preview_label.pack(side='left', padx=(8, 0))
        
        # Cacher initialement les options du dictionnaire
        self.toggle_dictionary_options()
        
        # COLONNE DROITE - MODE PASSPHRASE
        passphrase_column = ttk.Frame(modes_container, style='Card.TFrame')
        passphrase_column.pack(side='right', fill='both', expand=True, padx=(15, 0))
        
        passphrase_title = ttk.Label(passphrase_column, text="🎭 Mode Passphrase ", style='Heading.TLabel')
        passphrase_title.pack(anchor='w', pady=(0, 8))
        
        # Option pour activer le mode passphrase
        self.use_passphrase_var = tk.BooleanVar(value=False)
        passphrase_checkbox = ttk.Checkbutton(passphrase_column, text="📝 Générer des phrases de passe mémorables", 
                                            variable=self.use_passphrase_var, style='Modern.TCheckbutton',
                                            command=self.toggle_passphrase_options)
        passphrase_checkbox.pack(anchor='w', pady=(0, 8))
        
        # Frame pour les options de passphrase (initialement cachées)
        self.passphrase_options_frame = ttk.Frame(passphrase_column, style='Card.TFrame')
        self.passphrase_options_frame.pack(fill='x', padx=(20, 0))
        
        # Options compactes en ligne
        passphrase_compact_frame = ttk.Frame(self.passphrase_options_frame, style='Card.TFrame')
        passphrase_compact_frame.pack(fill='x', pady=(5, 10))
        
        # Colonne gauche - Nombre de mots
        pass_left_col = ttk.Frame(passphrase_compact_frame, style='Card.TFrame')
        pass_left_col.pack(side='left', fill='both', expand=True, padx=(0, 15))
        
        words_label = ttk.Label(pass_left_col, text="🔢 Nombre de mots:", style='Option.TLabel')
        words_label.pack(anchor='w')
        
        self.passphrase_words_var = tk.StringVar(value="4")
        words_spinbox = ttk.Spinbox(pass_left_col, from_=3, to=8, textvariable=self.passphrase_words_var, 
                                  width=6, style='Modern.TSpinbox', font=('SF Mono', 11), justify='center')
        words_spinbox.pack(anchor='w', pady=(2, 0))
        
        # Colonne droite - Options
        pass_right_col = ttk.Frame(passphrase_compact_frame, style='Card.TFrame')
        pass_right_col.pack(side='right', fill='both', expand=True)
        
        pass_options_label = ttk.Label(pass_right_col, text="⚙️ Options:", style='Option.TLabel')
        pass_options_label.pack(anchor='w')
        
        # Variables pour les options de passphrase
        self.capitalize_words_var = tk.BooleanVar(value=True)
        self.add_numbers_passphrase_var = tk.BooleanVar(value=True)
        self.add_separators_var = tk.BooleanVar(value=True)
        
        # Options en grille compacte 2x2
        pass_options_grid = ttk.Frame(pass_right_col, style='Card.TFrame')
        pass_options_grid.pack(fill='x', pady=(2, 0))
        
        passphrase_options_data = [
            (self.capitalize_words_var, "🔤"), (self.add_separators_var, "➖"),
            (self.add_numbers_passphrase_var, "🔢"), ("", "")  # Case vide pour l'alignement
        ]
        
        for i, (var, icon) in enumerate(passphrase_options_data):
            if var and icon:  # Ignorer la case vide
                cb = ttk.Checkbutton(pass_options_grid, text=f"{icon}", 
                                   variable=var, style='Modern.TCheckbutton')
                cb.grid(row=i//2, column=i%2, sticky='w', padx=3, pady=1)
        
        # Bouton aperçu passphrase
        passphrase_preview_frame = ttk.Frame(self.passphrase_options_frame, style='Card.TFrame')
        passphrase_preview_frame.pack(fill='x', pady=(5, 0))
        
        passphrase_preview_btn = ttk.Button(passphrase_preview_frame, text="👁️ Aperçu", 
                                          command=self.show_passphrase_preview, style='Primary.TButton')
        passphrase_preview_btn.pack(side='left')
        
        self.passphrase_preview_label = ttk.Label(passphrase_preview_frame, text="", style='Body.TLabel')
        self.passphrase_preview_label.pack(side='left', padx=(10, 0))
        
        # Cacher initialement les options de passphrase
        self.toggle_passphrase_options()
        
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
                                   height=18,  # Augmenté à 18 lignes pour profiter de l'espace supplémentaire
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
    
    def toggle_dictionary_options(self):
        """Affiche ou cache les options du dictionnaire avec ajustement automatique"""
        if self.use_dictionary_var.get():
            # Afficher les options du dictionnaire
            self.dict_options_frame.pack(fill='x', padx=(20, 0))
            # Permettre temporairement le redimensionnement pour ajuster la taille
            if hasattr(self, 'root'):
                self.root.resizable(True, True)
                current_geometry = self.root.geometry()
                if "1200x1200" in current_geometry:
                    # Augmenter la hauteur de seulement 60px pour la nouvelle version horizontale compacte
                    new_geometry = current_geometry.replace("1200x1200", "1200x1260")
                    self.root.geometry(new_geometry)
                elif "1200x1260" in current_geometry and self.use_passphrase_var.get():  
                    # Si passphrase déjà activée, augmenter encore de 40px
                    new_geometry = current_geometry.replace("1200x1260", "1200x1300")
                    self.root.geometry(new_geometry)
                # Bloquer à nouveau le redimensionnement
                self.root.resizable(False, False)
        else:
            # Cacher les options du dictionnaire
            self.dict_options_frame.pack_forget()
            # Restaurer la taille appropriée de la fenêtre
            if hasattr(self, 'root'):
                self.root.resizable(True, True)
                current_geometry = self.root.geometry()
                if "1200x1260" in current_geometry and not self.use_passphrase_var.get():
                    # Revenir à la taille normale si passphrase n'est pas activée
                    new_geometry = current_geometry.replace("1200x1260", "1200x1200")
                    self.root.geometry(new_geometry)
                elif "1200x1300" in current_geometry:
                    # Si passphrase est activée, revenir à la taille avec passphrase seulement
                    new_geometry = current_geometry.replace("1200x1300", "1200x1260")
                    self.root.geometry(new_geometry)
                # Bloquer à nouveau le redimensionnement
                self.root.resizable(False, False)
        
        # Forcer la mise à jour de l'affichage
        if hasattr(self, 'root'):
            self.root.update_idletasks()
    
    def toggle_passphrase_options(self):
        """Affiche ou cache les options de passphrase avec ajustement automatique"""
        if self.use_passphrase_var.get():
            # Afficher les options de passphrase
            self.passphrase_options_frame.pack(fill='x', padx=(20, 0))
            # Permettre temporairement le redimensionnement pour ajuster la taille
            if hasattr(self, 'root'):
                self.root.resizable(True, True)
                current_geometry = self.root.geometry()
                if "1200x1200" in current_geometry:
                    # Augmenter la hauteur de 60px pour la version passphrase horizontale
                    new_geometry = current_geometry.replace("1200x1200", "1200x1260")
                    self.root.geometry(new_geometry)
                elif "1200x1260" in current_geometry and self.use_dictionary_var.get():  
                    # Si dictionnaire déjà activé, augmenter encore de 40px
                    new_geometry = current_geometry.replace("1200x1260", "1200x1300")
                    self.root.geometry(new_geometry)
                # Bloquer à nouveau le redimensionnement
                self.root.resizable(False, False)
        else:
            # Cacher les options de passphrase
            self.passphrase_options_frame.pack_forget()
            # Restaurer la taille appropriée
            if hasattr(self, 'root'):
                self.root.resizable(True, True)
                current_geometry = self.root.geometry()
                if "1200x1260" in current_geometry and not self.use_dictionary_var.get():
                    # Revenir à la taille normale si dictionnaire n'est pas activé
                    new_geometry = current_geometry.replace("1200x1260", "1200x1200")
                    self.root.geometry(new_geometry)
                elif "1200x1300" in current_geometry:
                    # Si dictionnaire est activé, revenir à la taille avec dictionnaire seulement
                    new_geometry = current_geometry.replace("1200x1300", "1200x1260")
                    self.root.geometry(new_geometry)
                # Bloquer à nouveau le redimensionnement
                self.root.resizable(False, False)
        
        # Forcer la mise à jour de l'affichage
        if hasattr(self, 'root'):
            self.root.update_idletasks()
    
    def generate_passphrase(self):
        """Génère une passphrase basée sur les options sélectionnées"""
        num_words = int(self.passphrase_words_var.get())
        words = []
        
        # Générer les mots selon un pattern : adjectif + nom + verbe + connecteur + nom
        patterns = [
            ['adjectifs', 'noms'],
            ['adjectifs', 'noms', 'verbes'],
            ['adjectifs', 'noms', 'verbes', 'noms'],
            ['adjectifs', 'noms', 'verbes', 'connecteurs', 'noms'],
            ['adjectifs', 'noms', 'verbes', 'connecteurs', 'adjectifs', 'noms'],
            ['adjectifs', 'noms', 'verbes', 'connecteurs', 'adjectifs', 'noms', 'verbes'],
            ['adjectifs', 'noms', 'verbes', 'connecteurs', 'adjectifs', 'noms', 'verbes', 'noms']
        ]
        
        # Choisir le pattern selon le nombre de mots (index = num_words - 2)
        pattern_index = min(num_words - 2, len(patterns) - 1)
        pattern = patterns[pattern_index][:num_words]  # Limiter au nombre de mots souhaités
        
        for word_type in pattern:
            if word_type in self.passphrase_dictionary:
                word = random.choice(self.passphrase_dictionary[word_type])
                
                # Capitalisation si activée
                if self.capitalize_words_var.get():
                    word = word.capitalize()
                
                words.append(word)
        
        # Joindre avec des séparateurs si activé
        if self.add_separators_var.get():
            separators = ['-', '_', '.', '~']
            separator = random.choice(separators)
            passphrase = separator.join(words)
        else:
            passphrase = ''.join(words)
        
        # Ajouter des chiffres si activé
        if self.add_numbers_passphrase_var.get():
            num_digits = random.randint(2, 4)
            digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
            
            # Ajouter au début ou à la fin
            position = random.choice(['start', 'end'])
            if position == 'start':
                passphrase = digits + (separator if self.add_separators_var.get() else '') + passphrase
            else:
                passphrase = passphrase + (separator if self.add_separators_var.get() else '') + digits
        
        return passphrase
    
    def show_passphrase_preview(self):
        """Affiche un aperçu d'une passphrase générée"""
        try:
            preview_passphrase = self.generate_passphrase()
            self.passphrase_preview_label.config(text=f"Exemple : {preview_passphrase}")
        except Exception as e:
            self.passphrase_preview_label.config(text="Erreur dans la prévisualisation")
    
    def get_random_word_from_dictionary(self):
        """Récupère un mot aléatoire des catégories sélectionnées"""
        available_words = []
        
        # Collecter les mots des catégories sélectionnées
        for category, var in self.category_vars.items():
            if var.get() and category in self.password_dictionary:
                available_words.extend(self.password_dictionary[category])
        
        # Si aucune catégorie n'est sélectionnée, utiliser toutes les catégories
        if not available_words:
            for category_words in self.password_dictionary.values():
                available_words.extend(category_words)
        
        return random.choice(available_words) if available_words else "password"
    
    def apply_word_modifications(self, word):
        """Applique les modifications de sécurité à un mot"""
        result = word
        
        # Capitalisation aléatoire
        if self.capitalize_var.get():
            result = ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in result)
        
        # Substitution de caractères
        if self.substitute_chars_var.get():
            new_word = ""
            for char in result:
                if char.lower() in self.char_substitutions and random.choice([True, False]):
                    new_word += random.choice(self.char_substitutions[char.lower()])
                else:
                    new_word += char
            result = new_word
        
        # Ajouter des chiffres
        if self.add_numbers_var.get():
            num_digits = random.randint(1, 4)
            digits = ''.join(str(random.randint(0, 9)) for _ in range(num_digits))
            
            # Ajouter au début, à la fin, ou au milieu
            position = random.choice(['start', 'end', 'middle'])
            if position == 'start':
                result = digits + result
            elif position == 'end':
                result = result + digits
            else:
                mid = len(result) // 2
                result = result[:mid] + digits + result[mid:]
        
        # Ajouter des symboles
        if self.add_symbols_var.get():
            symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
            num_symbols = random.randint(1, 3)
            
            for _ in range(num_symbols):
                symbol = random.choice(symbols)
                position = random.choice(['start', 'end'])
                if position == 'start':
                    result = symbol + result
                else:
                    result = result + symbol
        
        return result
    
    def generate_dictionary_password(self, target_length):
        """Génère un mot de passe basé sur le dictionnaire"""
        base_word = self.get_random_word_from_dictionary()
        
        # Si le mot de base est déjà trop long, le raccourcir
        if len(base_word) > target_length - 4:  # Laisser de la place pour les modifications
            base_word = base_word[:target_length - 4]
        
        # Appliquer les modifications
        password = self.apply_word_modifications(base_word)
        
        # Ajuster la longueur si nécessaire
        while len(password) < target_length:
            # Ajouter des caractères aléatoires à la fin
            if self.special_chars_var.get():
                password += random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")
            elif self.numbers_var.get():
                password += str(random.randint(0, 9))
            elif self.uppercase_var.get():
                password += random.choice(string.ascii_uppercase)
            else:
                password += random.choice(string.ascii_lowercase)
        
        # Tronquer si trop long
        if len(password) > target_length:
            password = password[:target_length]
        
        return password
    
    def show_dictionary_preview(self):
        """Affiche un aperçu d'un mot de passe généré avec le dictionnaire"""
        try:
            length = int(self.length_var.get()) if self.length_var.get().isdigit() else 12
            preview_password = self.generate_dictionary_password(length)
            self.preview_label.config(text=f"Exemple : {preview_password}")
        except Exception as e:
            self.preview_label.config(text="Erreur dans la prévisualisation")
    
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
            
            # Validation spécifique au mode dictionnaire
            if self.use_dictionary_var.get():
                # Vérifier qu'au moins une catégorie est sélectionnée
                if not any(var.get() for var in self.category_vars.values()):
                    messagebox.showwarning("⚠️ Mode Dictionnaire", 
                                         "Veuillez sélectionner au moins une catégorie de mots.\n\nToutes les catégories ont été automatiquement activées.", 
                                         parent=self.root)
                    # Activer toutes les catégories par défaut
                    for var in self.category_vars.values():
                        var.set(True)
                
                # Vérifier qu'au moins une modification de sécurité est activée
                if not any([self.capitalize_var.get(), self.substitute_chars_var.get(), 
                           self.add_numbers_var.get(), self.add_symbols_var.get()]):
                    messagebox.showinfo("ℹ️ Sécurité renforcée", 
                                      "Aucune modification de sécurité n'était activée.\n\nToutes les options ont été automatiquement activées pour maximiser la sécurité.", 
                                      parent=self.root)
                    self.capitalize_var.set(True)
                    self.substitute_chars_var.set(True)
                    self.add_numbers_var.set(True)
                    self.add_symbols_var.set(True)
            
            # Validation spécifique au mode passphrase
            if self.use_passphrase_var.get():
                num_words = int(self.passphrase_words_var.get())
                if num_words < 3 or num_words > 8:
                    messagebox.showwarning("⚠️ Mode Passphrase", 
                                         "Le nombre de mots doit être entre 3 et 8.\n\nLa valeur a été ajustée à 4.", 
                                         parent=self.root)
                    self.passphrase_words_var.set("4")
            
            # Vérifier qu'un seul mode est activé
            active_modes = sum([
                self.use_dictionary_var.get(),
                self.use_passphrase_var.get()
            ])
            
            if active_modes > 1:
                messagebox.showwarning("⚠️ Modes multiples", 
                                     "Un seul mode spécialisé peut être activé à la fois.\n\nLe mode Classique sera utilisé.", 
                                     parent=self.root)
                # Désactiver les modes spéciaux
                self.use_dictionary_var.set(False)
                self.use_passphrase_var.set(False)
                self.toggle_dictionary_options()
                self.toggle_passphrase_options()
            
            # Vérification des options sélectionnées (mode classique)
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
                if self.use_dictionary_var.get():
                    # Mode dictionnaire
                    password = self.generate_dictionary_password(length)
                elif self.use_passphrase_var.get():
                    # Mode passphrase
                    password = self.generate_passphrase()
                else:
                    # Mode classique
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
        
        # Afficher le mode utilisé
        if self.use_dictionary_var.get():
            mode = "📚 Mode Dictionnaire"
        elif self.use_passphrase_var.get():
            mode = "🎭 Mode Passphrase"
        else:
            mode = "🎯 Mode Classique"
        self.results_text.insert(tk.END, f"├─ {mode}\n")
        
        if self.use_dictionary_var.get():
            # Afficher les catégories sélectionnées
            selected_categories = [cat for cat, var in self.category_vars.items() if var.get()]
            if selected_categories:
                self.results_text.insert(tk.END, f"├─ 🏷️ Catégories: {', '.join(selected_categories)}\n")
            
            # Afficher les modifications appliquées
            modifications = []
            if self.capitalize_var.get():
                modifications.append("Capitalisation")
            if self.substitute_chars_var.get():
                modifications.append("Substitution")
            if self.add_numbers_var.get():
                modifications.append("Chiffres")
            if self.add_symbols_var.get():
                modifications.append("Symboles")
            if modifications:
                self.results_text.insert(tk.END, f"├─ 🔧 Modifications: {', '.join(modifications)}\n")
        
        elif self.use_passphrase_var.get():
            # Afficher les paramètres de passphrase
            self.results_text.insert(tk.END, f"├─ 🔢 Nombre de mots: {self.passphrase_words_var.get()}\n")
            
            passphrase_options = []
            if self.capitalize_words_var.get():
                passphrase_options.append("Capitalisation")
            if self.add_separators_var.get():
                passphrase_options.append("Séparateurs")
            if self.add_numbers_passphrase_var.get():
                passphrase_options.append("Chiffres")
            if passphrase_options:
                self.results_text.insert(tk.END, f"├─ ⚙️ Options: {', '.join(passphrase_options)}\n")
        
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
