import os
import time
os.system("cp ~/.config/i3/config ~/git/NeckbeardConfigs/graveyard/machine/i3config")
os.system("cp ~/git/NeckbeardConfigs/i3wm/config ~/.config/i3/config ")
print("pulling ~/.config/i3.config....")
time.sleep(.25)
os.system("cp ~/.vimrc ~/git/NeckbeardConfigs/graveyard/machine/vimrc")
os.system("cp ~/git/NeckbeardConfigs/vim/vimrc ~/.vimrc ")
print("pulling ~/.vimrc...")
time.sleep(.25)
os.system("cp ~/.pythonvimrc ~/git/NeckbeardConfigs/graveyard/machine/pythonvimrc")
os.system("cp ~/git/NeckbeardConfigs/vim/pythonvimrc ~/.pythonvimrc ")
print("pulling ~/.pythonvimrc...")
time.sleep(.25)
os.system("cp ~/.profile ~/git/NeckbeardConfigs/graveyard/machine/profile")
os.system("cp ~/git/NeckbeardConfigs/profile/profile ~/.profile")
print("pulling ~/.profile...")
time.sleep(.25)
os.system("cp ~/.bashrc ~/git/NeckbeardConfigs/graveyard/machine/bashrc")
os.system("cp ~/git/NeckbeardConfigs/bashrc/bashrc ~/.bashrc")
print("pulling ~/.bashrc...")
time.sleep(.25)
os.system("cp ~/.tmux.conf ~/git/NeckbeardConfigs/graveyard/machine/tmux.conf")
os.system("cp ~/git/NeckbeardConfigs/tmux/tmux.conf ~/.tmux.conf")
print("pulling ~/.tmux.conf...")
time.sleep(.25)
print("Done")


