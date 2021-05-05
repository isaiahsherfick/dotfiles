import os
import time
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        #no git update

        os.system("cp ~/git/NeckbeardConfigs/i3wm/config ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.config/i3/config ~/git/NeckbeardConfigs/i3wm/config")
        print("saving ~/.config/i3.config....")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/vim/vimrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.vimrc ~/git/NeckbeardConfigs/vim/vimrc")
        print("saving ~/.vimrc...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/vim/pythonvimrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.pythonvimrc ~/git/NeckbeardConfigs/vim/pythonvimrc")
        print("saving ~/.pythonvimrc...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/profile/profile ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.profile ~/git/NeckbeardConfigs/profile/profile")
        print("saving ~/.profile...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/bashrc/bashrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.bashrc ~/git/NeckbeardConfigs/bashrc/bashrc")
        print("saving ~/.bashrc...")
        time.sleep(.25)
        print("Done")
    else:
        #git update
        #how do you do it? no clue
        #todo I guess

        os.system("cp ~/git/NeckbeardConfigs/i3wm/config ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.config/i3/config ~/git/NeckbeardConfigs/i3wm/config")
        print("saving ~/.config/i3.config....")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/vim/vimrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.vimrc ~/git/NeckbeardConfigs/vim/vimrc")
        print("saving ~/.vimrc...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/vim/pythonvimrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.pythonvimrc ~/git/NeckbeardConfigs/vim/pythonvimrc")
        print("saving ~/.pythonvimrc...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/profile/profile ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.profile ~/git/NeckbeardConfigs/profile/profile")
        print("saving ~/.profile...")
        time.sleep(.25)
        os.system("cp ~/git/NeckbeardConfigs/bashrc/bashrc ~/git/NeckbeardConfigs/graveyard/repo/")
        os.system("cp ~/.bashrc ~/git/NeckbeardConfigs/bashrc/bashrc")
        print("saving ~/.bashrc...")
        time.sleep(.25)
        print("Done")

