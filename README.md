# WelcomeHack2024

**Benvinguts al repositori de la WelcomeHack2024!** 

En aquest arxiu d'aquí, anomenat `README.md` és on trobareu normalment tota la informació que necessiteu sobre un repositori. Nosaltres us deixarem per aquí sota tots els enllaços que necessitareu per aquest taller.

### ❗Atenció, usuaris de **Linux (Ubuntu)** ❗
Executeu aquestes comandes abans de començar:

```bash
sudo apt-get update
sudo apt-get upgrade
```



 
## Visual Studio Code, el teu editor de codi

<div>
    <img src="imgs/vsc.png" alt="vscode">
<div/>


### Windows, Mac :
* [Instal·la aquí Visual Studio Code](https://code.visualstudio.com/download)
### Ubuntu :
Escriu la següent comanda a la terminal:

```bash
sudo snap install --classic code
```

## Git, el control de versions

<div>
    <img src="imgs/git.png" alt="git">
<div/>

### Windows, Mac:
* [Instal·la aquí Git per Windows](https://git-scm.com/download/win)
* [Instal·la aquí Git per Mac](https://git-scm.com/download/mac)
### Ubuntu:
Escriu la següent comanda a la terminal:

```bash
sudo apt install git
```

En acabar la instal·lació, en **Ubuntu** executareu aquestes comandes:
```
git config pull.rebase false
git config --global init.defaultBranch main
```
### Atenció!
I tant en **Ubuntu** com en **Windows** executareu aquestes, canviant la paraula *NOM* pel vostre nom o sobrenom i la paraula *EMAIL* pel vostre correu electrònic (preferentment el que heu fet servir pel compte de Github):
```
git config --global user.name "NOM"
```

```
git config --global user.email "EMAIL"
```
Per exemple:
```
git config --global user.name "naimsg16"
git config --global user.name "naim.saadi@lleidahack.dev"
```

## GitHub Desktop, fes servir Git interactivament

<div>
    <img src="imgs/githubdesktop.png" alt="ghdesktop">
<div/>

### Windows, Mac:
* [Instal·la aquí GitHub Desktop per Windows/Mac](https://desktop.github.com/download/)
### Ubuntu:
Escriu les següents comandes a la terminal:

```bash
wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main" > /etc/apt/sources.list.d/shiftkey-packages.list'
sudo apt update && sudo apt install github-desktop
```
---
*made by [@naimsg16](github.com/naimsg16)*
