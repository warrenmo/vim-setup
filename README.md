Intro
=====

Just a place for me to hold my custom .vimrc file.

Most if not all customizations are taken from [here](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) and [here](https://danielmiessler.com/study/vim/).


Setup
=====


0. Install VIM (Linux) and Vundle
---------------------------------

```bash
$ sudo apt-get remove vim-tiny
$ sudo apt-get update
$ sudo apt-get install vim
```

Currently the extension manager I use is [Vundle](https://github.com/VundleVim/Vundle.vim)
```bash
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```


1. Clone this repo
------------------

```bash
$ git clone https://github.com/warrenmo/vimrc.git
```


2. Copy the .vimrc file to your home directory
----------------------------------------------

```bash
$ cp ./.vimrc ~/
```


3. Open any text file using VIM
-------------------------------

```bash
$ vim any_text_file
```


4. Run the Vundle plugin manager
--------------------------------

```
:PluginInstall
```

