# Advent of Code Scraper + personnal solutions

## English Version

This repository contains a Python script to fetch Advent of Code exercises and prepare Python files for each day. It also includes my personnal solutions (namefiles including ^^).
The scraper and solutions are handmade but the readme is AI generated.

### How it works
- The script checks if the exercise input and Python files already exist.
- If not, it downloads the input from Advent of Code using your session cookie.
- For each new exercise, it creates a Python starter file and a text file with the input data.

### Important
- You **must provide a valid Advent of Code session cookie**. Save it in a file called `session_cookie.txt` in the same folder as the script.
- The code was written manually, both the scraper and exercise file generator.
- This README, however, was generated automatically.

### Usage
1. Put your AoC session cookie in `session_cookie.txt`.
2. Run the script with Python 3:
   ```bash
   python "Scraping Advent Code.py"
   ```
3. The script will create folders for each year and populate them with input files and starter Python files.

---

## Version Française

Ce dépôt contient un script Python pour récupérer les exercices Advent of Code et préparer des fichiers Python pour chaque jour. J'ai ajouté mes solutions (les fichiers se terminant par ^^).
Le script de scraping / construction de fichiers ainsi que les solutions sont faits à la main. Le readme a été généré par IA.

### Fonctionnement
- Le script vérifie si l'exercice et les fichiers Python existent déjà.
- Sinon, il télécharge l'exercice depuis Advent of Code grâce à votre cookie de session.
- Pour chaque nouvel exercice, il crée un fichier Python de départ et un fichier texte contenant les données.

### Important
- Vous **devez fournir un cookie de session Advent of Code valide**. Placez-le dans un fichier `session_cookie.txt` dans le même dossier que le script.
- Le code a été écrit à la main, pour le scraper comme pour les fichiers d'exercice.
- Ce README, en revanche, a été généré automatiquement.

### Utilisation
1. Placez votre cookie AoC dans `session_cookie.txt`.
2. Lancez le script avec Python 3 :
   ```bash
   python "Scraping Advent Code.py"
   ```
3. Le script créera des dossiers par année et y ajoutera les fichiers d'entrée et les fichiers Python de départ.

