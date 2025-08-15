# ✨ Milk - Générateur de Mots de Passe 3.1.1

Un générateur de mots de passe élégant et sécurisé avec interface macOS native.

## 🆕 Nouveautés Version 3.1.1
### 🎭 Correction de bugs
- **Correction** de bug sur la gestion de valeur sur "longueur du mot de passe" & "Passphrase". Il y avait un bug quand on rentrait une valeur incorrecte, on ne pouvait plus modifier les valeurs dans les 2 cas (après ouverture de le popup d'erreur).
- **Gestion** des valeurs revue.
      

## 🆕 Nouveautés Version 3.1

### 🎭 Mode Passphrase
- **Phrases de passe mémorables** : Génère des passphrases lisibles comme "Grand-Maison-Vole-Avec-Etoile-92"
- **Structure intelligente** : Combine adjectifs, noms, verbes et connecteurs
- **Paramètres flexibles** : 3 à 8 mots avec options de capitalisation, séparateurs et chiffres
- **Mémorisation facilitée** : Alternative moderne aux mots de passe complexes

### 📚 Mode Dictionnaire
- **Génération basée sur des mots réels** : Crée des mots de passe mémorisables en partant de mots de base
- **7 catégories de mots** : Animaux, Nature, Couleurs, Technologie, Actions, Adjectifs, Objets
- **Modifications de sécurité automatiques** :
  - Capitalisation aléatoire
  - Substitution de caractères (a→@, e→3, i→!, etc.)
  - Ajout de chiffres et symboles
  - Mélange intelligent pour maximiser la sécurité

### 🎨 Interface Repensée
- **Layout horizontal optimisé** : Modes avancés côte à côte pour une meilleure utilisation de l'espace
- **Options compactes** : Grilles 2x2 et organisation intelligente des contrôles
- **Aperçus en temps réel** : Boutons "👁️ Aperçu" pour tester les paramètres
- **Validation automatique** : Messages d'aide et configuration auto pour éviter les erreurs

### 🎯 Exemples de Génération

**Mode Classique :**
```
K9@mL7#pX2$vN4!wQ
```

**Mode Dictionnaire :**
```
Dr@g0n!47#          (basé sur "dragon")
M0nt@gne$92         (basé sur "montagne") 
R0b0t&!345          (basé sur "robot")
```

**Mode Passphrase :**
```
Brillant-Ocean-Vole-Avec-Montagne-847
Secret_Jardin_Danse_Durant_Aventure_23
Mysterieux.Etoile.Chante.Grace.Liberte.156
```

## 🚀 Fonctionnalités

### ⚡ Interface Moderne
- **Design macOS natif** avec boutons rouge/jaune/vert fonctionnels
- **Thème sombre** optimisé pour le confort visuel
- **Fenêtre personnalisée** sans bordures système
- **Drag & Drop** pour déplacer la fenêtre

### 🔒 Sécurité Avancée
- **Génération locale** - Aucune donnée transmise
- **Entropy élevée** - Combinaisons cryptographiquement sécurisées
- **Validation automatique** des paramètres
- **Conseils de sécurité** intégrés

### 📊 Options de Personnalisation
- **Longueur** : 4 à 64 caractères
- **Quantité** : 1 à 20 mots de passe
- **Types de caractères** configurables
- **Export** en formats TXT, CSV, JSON

## 🛠️ Installation

```bash
# Cloner le repository
git clone https://github.com/Solvyrth/milk-password-generator

# Naviguer dans le dossier
cd milk-password-generator

# Lancer l'application
python3 Milk.py
```

### Prérequis
- Python 3.7+
- tkinter (inclus avec Python)
- macOS 10.12+ (pour le design natif)

## 📖 Guide d'Utilisation

### Mode Classique
1. Définissez la longueur et le nombre de mots de passe
2. Sélectionnez les types de caractères
3. Cliquez sur "🚀 Générer"

### Mode Dictionnaire (v3.1)
1. Activez "📚 Utiliser des mots de base du dictionnaire"
2. Choisissez vos catégories préférées
3. Configurez les modifications de sécurité
4. Cliquez sur "🚀 Générer"

### Mode Passphrase (v3.1)
1. Activez "🎭 Générer des phrases de passe mémorables"
2. Définissez le nombre de mots (3-8)
3. Configurez les options (capitalisation, séparateurs, chiffres)
4. Cliquez sur "🚀 Générer"

### Sauvegarde
- **Format détaillé** avec métadonnées complètes
- **Analyse de sécurité** automatique
- **Conseils personnalisés** inclus

## 🏗️ Architecture Technique

```
Milk.py
├── Interface utilisateur (tkinter)
├── Gestionnaire de fenêtre personnalisé
├── Générateur classique (aléatoire pur)
├── Générateur dictionnaire (v3.1)
│   ├── 7 catégories de mots (105+ mots)
│   ├── Substitutions de caractères
│   └── Modifications de sécurité
├── Générateur passphrase (v3.1)
│   ├── 4 types de mots (noms, adjectifs, verbes, connecteurs)
│   ├── Patterns intelligents
│   └── Options de formatage
└── Export & analyse de sécurité
```

## 🎨 Dictionnaires Intégrés

### Mode Dictionnaire
| Catégorie | Exemples | Icône |
|-----------|----------|--------|
| **Animaux** | chat, lion, tigre, aigle | 🦁 |
| **Nature** | montagne, océan, forêt | 🌲 |
| **Couleurs** | rouge, bleu, violet | � |
| **Technologie** | robot, laser, quantum | 💻 |
| **Actions** | courir, voler, danser | ⚡ |
| **Adjectifs** | grand, beau, rapide | ✨ |
| **Objets** | maison, voiture, livre | 🏠 |

### Mode Passphrase
| Type | Exemples | Usage |
|------|----------|--------|
| **Noms** | soleil, montagne, océan | Bases descriptives |
| **Adjectifs** | magnifique, brillant, mystérieux | Qualificatifs |
| **Verbes** | brille, danse, vole | Actions dynamiques |
| **Connecteurs** | avec, vers, dans | Liaisons naturelles |

## 🔧 Personnalisation

### Ajouter des Mots au Dictionnaire
```python
# Mode Dictionnaire
self.password_dictionary['votre_categorie'] = [
    'mot1', 'mot2', 'mot3', ...
]

# Mode Passphrase
self.passphrase_dictionary['noms'] = [
    'nouveau_nom1', 'nouveau_nom2', ...
]
```

### Modifier les Substitutions
```python
self.char_substitutions['lettre'] = ['@', '4', 'A']
```

## 📈 Analyse de Sécurité

L'application calcule automatiquement :
- **Taille du jeu de caractères**
- **Nombre de combinaisons possibles** 
- **Force estimée** du mot de passe
- **Recommandations personnalisées**

## 🛡️ Bonnes Pratiques

- ✅ Un mot de passe unique par compte
- ✅ Longueur minimale de 12 caractères
- ✅ Mélange de types de caractères
- ✅ Utilisation d'un gestionnaire de mots de passe
- ✅ Activation de l'authentification 2FA

## 🐛 Résolution de Problèmes

### L'application ne se lance pas
```bash
# Vérifier Python
python3 --version

# Vérifier tkinter
python3 -c "import tkinter; print('tkinter OK')"
```

### Boutons macOS non visibles
- Assurez-vous d'être sur macOS
- Redémarrez l'application
- Vérifiez la résolution d'écran

## 📄 Licence

MIT License - Libre d'utilisation et modification

## 👨‍💻 Développement

**Développeur :** [Solvyrth](https://github.com/Solvyrth)  
**Version :** 3.1  
**Dernière mise à jour :** Août 2025  

### Historique des Versions
- **v3.1** : Mode passphrase, mode dictionnaire amélioré, interface optimisée
- **v3.0** : Interface macOS native, thème sombre  
- **v2.x** : Fonctionnalités de base

## ⭐ Soutenez le Projet

Si Milk vous aide à sécuriser vos comptes, n'hésitez pas à :
- ⭐ **Mettre une étoile** sur GitHub - cela aide énormément !
- 🍴 **Fork** le projet pour vos propres améliorations
- 📢 **Partagez** avec vos amis et collègues
- 🐛 **Signalez des bugs** ou proposez des fonctionnalités

## 🙏 Remerciements

### 🐍 Python & Sa Communauté
Un immense merci à **Guido van Rossum** et toute la communauté Python pour avoir créé ce langage extraordinaire qui rend le développement si accessible et élégant. Milk n'existerait pas sans :

- **Python** - Pour sa simplicité et sa puissance
- **tkinter** - Pour l'interface graphique native
- **random & string** - Pour la génération sécurisée
- **La documentation Python** - Toujours claire et complète

### 👥 Contributeurs & Communauté
Merci à tous ceux qui ont contribué à l'amélioration de Milk :

- **Testeurs bêta** - Pour leurs retours précieux
- **Utilisateurs GitHub** - Pour leurs suggestions et bug reports
- **Communauté macOS** - Pour les retours sur l'interface native
- **Experts en sécurité** - Pour leurs conseils sur la génération de mots de passe

### 🛠️ Outils & Ressources
- **GitHub** - Pour l'hébergement et la collaboration
- **VS Code** - Pour l'environnement de développement
- **SF Pro Font** - Pour la typographie macOS native
- **Unicode Consortium** - Pour les emojis qui rendent l'interface vivante

**Votre soutien compte !** Chaque étoile ⭐ motive la poursuite du développement et l'ajout de nouvelles fonctionnalités.

## 🤝 Contribution

Les contributions sont les bienvenues ! 
1. Fork le projet
2. Créez votre branche (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Commitez vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## ⭐ Remerciements

Merci à tous les utilisateurs qui ont contribué à l'amélioration de Milk !

**🌟 N'oubliez pas de mettre une étoile sur GitHub si ce projet vous a aidé !**

---

*Générez des mots de passe sécurisés avec style* ✨
