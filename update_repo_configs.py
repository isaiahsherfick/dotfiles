import os
import time
import sys


if __name__ == "__main__":
        os.system("cp ~/git/dotfiles/i3wm/config ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.config/i3/config ~/git/dotfiles/i3wm/config")
        print("saving ~/.config/i3.config....")
        time.sleep(.25)
        os.system("cp ~/git/dotfiles/vim/vimrc ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.vimrc ~/git/dotfiles/vim/vimrc")
        print("saving ~/.vimrc...")
        time.sleep(.25)
        os.system("cp ~/git/dotfiles/vim/pythonvimrc ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.pythonvimrc ~/git/dotfiles/vim/pythonvimrc")
        print("saving ~/.pythonvimrc...")
        time.sleep(.25)
        os.system("cp ~/git/dotfiles/profile/profile ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.profile ~/git/dotfiles/profile/profile")
        print("saving ~/.profile...")
        time.sleep(.25)
        os.system("cp ~/git/dotfiles/bashrc/bashrc ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.bashrc ~/git/dotfiles/bashrc/bashrc")
        print("saving ~/.bashrc...")
        os.system("cp ~/git/dotfiles/tmux/tmux.conf ~/git/dotfiles/graveyard/repo/")
        os.system("cp ~/.tmux.conf ~/git/dotfiles/tmux/tmux.conf")
        print("saving ~/.tmux.conf...")
        time.sleep(.25)
        print("Done")
