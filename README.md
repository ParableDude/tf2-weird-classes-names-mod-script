# TF2 Weird Classes Names Mod - Install Script

This python script will allow the user to create and install the [TF2 weird classes names mod](https://gamebanana.com/mods/292930) mod for their local client of Team Fortress 2.

## How to use 

> *Note:* This section of the README file is subject to change

As of the latest commit pushed, here's how to launch the script :

1- Install Python

2- install the vpk library with the following command :

`pip install vpk`

3- open the mod folder in the terminal, and launch the script with the following command :

`python3 Main.py`


## Roadmap

### Main features

- [x] base script (creates a .txt file with updated values)
- [x] vpk packaging (put the .txt file in a .vpk file)
- [ ] user interface (because everyone would rather see a window that a terminal)
- [ ] allow user to update some values (eg : classes names or file to update)
- [ ] somehow find a way for EVERY USERS to run the script (even the ones without snakes ... got it ? Python ... Snakes ... Ok I'm leaving ;-; )

### To do ... sometimes

- [ ] optimize base script (make it harder, better, faster, stronger)
- [ ] figure out which license to use
- [ ] fix bugs (I have to be real for a sec, I have no clue if there are any bugs rn, but I'll put that here just in case)
- [ ] documentation (explain to the masses how the code works)

### To do when I'll be the very best (probably in another branch, or another project)

- [ ] automatically detect a TF2 update and generate the mod
- [ ] automatically update the TF2 weird classes names gamebanana page
- [ ] buy stuff that can run the script 24/7 unattended 


## Thanks

My greatest thanks to :

- my friend Dave for being the GOAT and believing in me (you owe me a bag of doritos now)
- [Cueki's casual preloader](https://gamebanana.com/tools/19049), and everyone involved with it, for giving me the inspiration to do an automated script to keep my mod up to date (really, an obsolete version of the mod crashes the game, and I don't want to go through each lines of that file at every TF2 update)
- the python [vpk library](https://github.com/ValvePython/vpk) to allow me to create a packaged file to put in the custom folder
- the [python custom tkinter library](https://github.com/TomSchimansky/CustomTkinter) to offer me an easy and intuitive way to create an UI for this app
