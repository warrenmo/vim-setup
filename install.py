import platform

platform.version().split('~')[1].split('-')[0].split('.')[0]


sudo apt install vim
mkdir ~/.vim/colors/
cp ~/.vim/bundle/Zenburn/colors/zenburn.vim ~/.vim/colors/
sudo apt-get install build-essential cmake
sudo apt-get install python-dev python3-dev
./~/.vim/bundle/YouCompleteMe/install.py --clang-completer
