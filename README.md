# 🥛 Milk - Générateur de Mots de Passe

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)]()
[![Version](https://img.shields.io/badge/version-3.0-brightgreen)](https://github.com/Solvyrth/milk)

**Milk** est un générateur de mots de passe moderne et sécurisé avec une interface graphique élégante. Conçu pour la simplicité et la sécurité, il vous permet de créer des mots de passe robustes selon vos critères personnalisés.

![Milk Interface](https://via.placeholder.com/800x500/0F0F23/E8E8F0?text=Milk+-+G%C3%A9n%C3%A9rateur+de+Mots+de+Passe)

## ✨ Fonctionnalités

### 🔐 Génération Sécurisée
- **Génération aléatoire cryptographiquement sûre**
- Longueur configurable (4-64 caractères)
- Support de multiple types de caractères
- Génération en lot (jusqu'à 20 mots de passe)

### 🎨 Interface Moderne
- Design moderne inspiré des applications natives macOS
- Thème sombre élégant avec palette de couleurs cohérente
- Interface responsive et intuitive
- Animations et effets visuels subtils

### ⚙️ Options de Personnalisation
- 🏛️ **Lettres majuscules** (A-Z)
- 🌊 **Lettres minuscules** (a-z)  
- 💎 **Chiffres** (0-9)
- ⚡ **Caractères spéciaux** (!@#$%^&*()_+-=[]{}|;:,.<>?)

### 💾 Export et Sauvegarde
- Sauvegarde en formats TXT, CSV, JSON
- Rapports détaillés avec analyses de sécurité
- Métadonnées de session et conseils de sécurité
- Horodatage automatique des fichiers

## 📋 Prérequis

- **Python 3.6+** (inclut Tkinter par défaut)
- **Système d'exploitation** : macOS, Windows, ou Linux
- **Aucune dépendance externe** - utilise uniquement la bibliothèque standard Python

## 🚀 Installation et Utilisation

### Installation

```bash
# Cloner le repository
git clone https://github.com/Solvyrth/milk.git
cd milk

# Le projet n'a pas de dépendances externes !
# Tkinter est inclus avec Python par défaut
```

### Lancement

```bash
# Exécuter directement le script
python Milk.py

# Ou sur certains systèmes
python3 Milk.py
```

### Utilisation

1. **Configuration** : Ajustez la longueur et le nombre de mots de passe souhaités
2. **Options** : Sélectionnez les types de caractères à inclure
3. **Génération** : Cliquez sur "🚀 Générer les mots de passe"
4. **Sauvegarde** : Utilisez "💎 Sauvegarder" pour exporter vos résultats

## 🛡️ Sécurité

### Algorithme de Génération
- Utilise le module `random` de Python avec `random.choice()`
- Génération locale uniquement - aucune donnée transmise en ligne
- Pas de stockage ou journalisation des mots de passe générés

### Recommandations de Sécurité
- ✅ Un mot de passe unique par compte
- ✅ Longueur minimale recommandée : 12 caractères
- ✅ Inclure tous les types de caractères
- ✅ Utiliser un gestionnaire de mots de passe
- ✅ Activer l'authentification à deux facteurs (2FA)

## 📊 Analyse de Complexité

Le générateur évalue automatiquement la force de vos mots de passe :

| Longueur | Types de caractères | Combinaisons | Force |
|----------|-------------------|--------------|-------|
| 8+ chars | Lettres seules (52) | ~5×10¹³ | 🟠 Moyenne |
| 12+ chars | Lettres + chiffres (62) | ~3×10²¹ | 🟡 Élevée |
| 16+ chars | Tous types (94) | ~6×10³¹ | 🟢 Très élevée |

## 📁 Structure du Projet

```
Password/
├── Milk.py              # Application principale
├── requirements.txt     # Documentation des dépendances
└── README.md           # Ce fichier
```

## 🎨 Aperçu de l'Interface

### Sections Principales

- **🎯 Header** : Titre, branding et informations développeur
- **⚙️ Configuration** : Paramètres de longueur et nombre
- **🎭 Options** : Sélection des types de caractères
- **🚀 Actions** : Boutons de génération, sauvegarde et effacement
- **💎 Résultats** : Affichage formaté avec conseils de sécurité

### Design Features

- Palette de couleurs moderne (bleus sombres + accents)
- Typographie : SF Pro Display/Text (style Apple)
- Icônes emoji pour une navigation intuitive
- Scrollbar personnalisée et responsive design

## 🔧 Développement

### Architecture
- **Pattern MVC** : Séparation logique de l'interface et de la logique
- **Programmation orientée objet** : Code modulaire et maintenable
- **Gestion d'erreurs robuste** : Validation des entrées et messages informatifs

### Personnalisation
Le code est structuré pour faciliter la personnalisation :
- Palette de couleurs centralisée dans `self.colors`
- Styles TTK configurables
- Messages et textes facilement modifiables

## 📈 Roadmap

### Version 3.1 (Prochaine)
- [ ] Support des dictionnaires de mots de passe
- [ ] Générateur de phrases de passe (passphrases)
- [ ] Tests d'entropy avancés
- [ ] Mode ligne de commande

### Version 4.0 (Future)
- [ ] Chiffrement des fichiers de sauvegarde
- [ ] Integration avec des gestionnaires de mots de passe
- [ ] API REST pour intégrations
- [ ] Support multilingue

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. 🍴 **Fork** le projet
2. 🌿 Créer une **branche feature** (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. 🔄 Ouvrir une **Pull Request**

## 📄 Licence

Distribué sous la licence MIT. Voir `LICENSE` pour plus d'informations.

## 👨‍💻 Auteur

**Solvyrth**
- 🐙 GitHub: [@Solvyrth](https://github.com/Solvyrth)
- 📧 Contact: [Créer une issue](https://github.com/Solvyrth/milk/issues)

## 🙏 Remerciements

- Python Software Foundation pour l'excellent écosystème Python
- La communauté open source pour l'inspiration
- Tous les contributeurs et utilisateurs de Milk

---

<div align="center">
  
**⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile ! ⭐**

Made with 💙 by [Solvyrth](https://github.com/Solvyrth)

</div>
