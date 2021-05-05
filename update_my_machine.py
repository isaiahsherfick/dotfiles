import os
import time
os.system("git pull ~/git/NeckbeardConfigs")
os.system("cp ~/git/NeckbeardConfigs/i3wm/config ~/.config/i3/config ")
print("pulling ~/.config/i3.config....")
time.sleep(1)
os.system("cp ~/git/NeckbeardConfigs/vim/vimrc ~/.vimrc ")
print("pulling ~/.vimrc...")
time.sleep(1)
os.system("cp ~/git/NeckbeardConfigs/vim/pythonvimrc ~/.pythonvimrc ")
print("pulling ~/.pythonvimrc...")
time.sleep(1)
os.system("cp ~/git/NeckbeardConfigs/profile/profile ~/.profile")
print("pulling ~/.profile...")
time.sleep(1)
print("Done")


