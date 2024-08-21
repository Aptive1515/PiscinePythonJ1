Étape 1: Préparer la Structure de votre Package
Assurez-vous que votre package a la structure suivante :

bash
Copier le code
ft_package/
    ft_package/
        __init__.py
        module1.py
        module2.py
    setup.py
    README.md  # Optionnel mais recommandé pour la documentation
    LICENSE    # Optionnel mais recommandé pour la licence
Étape 2: Configurer setup.py
Votre fichier setup.py doit ressembler à ceci :

python
Copier le code
from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    packages=find_packages(),
    description='A simple example package',
    author='Votre Nom',
    author_email='votre.email@example.com',
    url='https://example.com/ft_package',  # Remplacez par l'URL de votre projet
    long_description=open('README.md').read(),  # Assurez-vous d'avoir un fichier README.md
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Spécifiez la version minimale requise de Python
)
Étape 3: Créer le Package
Utilisez setuptools pour créer les archives nécessaires. Exécutez ces commandes dans le répertoire contenant setup.py :

Créer les fichiers source distribuables et les fichiers de roue :

bash
Copier le code
python setup.py sdist bdist_wheel
sdist crée un fichier source (.tar.gz).
bdist_wheel crée un fichier de roue (.whl).
Vérifiez le répertoire dist :

Après avoir exécuté la commande ci-dessus, vous devriez voir les fichiers .tar.gz et .whl dans le répertoire dist :

plaintext
Copier le code
dist/
    ft_package-0.0.1.tar.gz
    ft_package-0.0.1-py3-none-any.whl
Étape 4: Installer le Package avec pip
Vous pouvez maintenant installer votre package en utilisant les fichiers que vous avez générés.

Installer à partir du fichier .tar.gz :

bash
Copier le code
pip install ./dist/ft_package-0.0.1.tar.gz
Installer à partir du fichier .whl :

bash
Copier le code
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
Étape 5: Tester l'Installation
Pour tester que votre package fonctionne correctement après l'installation, créez un script Python (par exemple, test_installation.py) :

python
Copier le code
# test_installation.py

import ft_package

print(ft_package.module1.hello())  # Appelle une fonction de module1
print(ft_package.module2.goodbye())  # Appelle une fonction de module2
Exécutez le script pour vérifier que tout fonctionne comme prévu :

bash
Copier le code
python test_installation.py
Étape 6: (Optionnel) Publier sur PyPI
Si vous souhaitez rendre votre package disponible publiquement via PyPI, vous devez suivre ces étapes :

Créer un compte sur PyPI.

Télécharger le package avec twine :

bash
Copier le code
twine upload dist/*
Cela téléversera vos fichiers .tar.gz et .whl sur PyPI, rendant votre package disponible pour une installation via pip install <package-name>.

Avec ces étapes, vous avez créé un package Python, généré les archives nécessaires, installé le package localement, et vous êtes prêt à le partager ou à le publier.



Étape 1: Naviguer vers le Répertoire
Assurez-vous que vous êtes dans le répertoire où se trouve le fichier setup.py. Ensuite, vérifiez le contenu du répertoire dist :

Ouvrir un terminal ou une invite de commande.

Naviguer vers le répertoire contenant setup.py :

bash
Copier le code
cd /chemin/vers/votre/package
Remplacez /chemin/vers/votre/package par le chemin réel vers le répertoire de votre package.

Étape 2: Exécuter les Commandes pour Créer les Archives
Avant de vérifier le répertoire, vous devez avoir créé les archives. Utilisez les commandes suivantes :

bash
Copier le code
python setup.py sdist bdist_wheel
sdist crée une archive source (.tar.gz).
bdist_wheel crée une archive de roue (.whl).
Étape 3: Vérifier le Contenu du Répertoire dist
Après avoir exécuté la commande ci-dessus, vous pouvez vérifier le contenu du répertoire dist :

Listage des fichiers sous Linux/MacOS :

bash
Copier le code
ls dist
Cette commande affiche le contenu du répertoire dist. Vous devriez voir des fichiers comme ft_package-0.0.1.tar.gz et ft_package-0.0.1-py3-none-any.whl.

Listage des fichiers sous Windows :

cmd
Copier le code
dir dist
Cette commande affiche également le contenu du répertoire dist sur Windows.

Exemple de Vérification
Supposons que vous avez exécuté les commandes pour créer les fichiers. Voici à quoi cela pourrait ressembler :

Sous Linux/MacOS :

bash
Copier le code
$ python setup.py sdist bdist_wheel
$ ls dist
ft_package-0.0.1-py3-none-any.whl
ft_package-0.0.1.tar.gz
Sous Windows :

cmd
Copier le code
C:\chemin\vers\votre\package> python setup.py sdist bdist_wheel
C:\chemin\vers\votre\package> dir dist
Vous devriez voir quelque chose comme :

cmd
Copier le code
  Volume in lecteur C has no label.
  Le numéro de série du volume est XXXX-YYYY

  Répertoire de C:\chemin\vers\votre\package\dist

23/08/2024  10:00 AM    <DIR>          .
23/08/2024  10:00 AM    <DIR>          ..
23/08/2024  10:00 AM           1 234  ft_package-0.0.1-py3-none-any.whl
23/08/2024  10:00 AM           1 456  ft_package-0.0.1.tar.gz
Résolution des Problèmes
Aucun fichier dans dist : Assurez-vous que vous avez bien exécuté les commandes python setup.py sdist bdist_wheel sans erreur. Revérifiez le répertoire de travail et assurez-vous que setup.py est correctement configuré.
Erreurs lors de l'exécution de setup.py : Consultez les messages d'erreur affichés dans le terminal pour des informations sur ce qui pourrait avoir échoué.
En suivant ces étapes, vous devriez pouvoir vérifier que les fichiers nécessaires ont été correctement créés dans le répertoire dist.






Readme

Étape 2: Exécuter les Commandes pour Créer les Archives
Avant de vérifier le répertoire, vous devez avoir créé les archives. Utilisez les commandes suivantes :
$ python setup.py sdist bdist_wheel



Voici un exemple complet de la désinstallation d'un package :
$ pip uninstall ft_package
