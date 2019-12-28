Intro
=====

Just a place for me to hold my custom .vimrc file.

Most if not all customizations are taken from [here](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) and [here](https://danielmiessler.com/study/vim/).

Note that the only Linux distro I'm familiar with is Ubuntu, and so you may have varying levels of success with the exact instructions below.

Setup
=====

### Installing Vim

If you haven't messed with your system's Vi/Vim installations, you should consider starting here.

Ubuntu ships with a version of Vim (`vim-tiny`) that only provides the Vi binary and lacks features such as syntax highlighting. So, we remove `vim-tiny` as the default installation package by uninstalling it before installing the full-fledged Vim package:
```bash
$ sudo apt-get remove vim-tiny
```

Now, we install Vim:
```bash
$ sudo apt-get update
$ sudo apt-get install vim
```

### Installing this repo

The plugin/extension manager I currently use is [Vundle](https://github.com/VundleVim/Vundle.vim), which you can download like so:
```bash
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Next, clone this repo:
```bash
$ git clone https://github.com/warrenmo/vimrc.git
```

And copy the `.vimrc` file to your home directory:
```bash
$ cp ./vimrc/.vimrc ~/
```

To install the plugins, first enter VIM by opening any text file using Vim:
```bash
$ vim any_text_file
```

Then, run the Vundle plugin manager (within Vim):
```
:PluginInstall
```

You're done!

### Troubleshooting

For some reason, Zenburn usually doesn't get placed in the right directory, in which case create a `colors` directory (if one doesn't exist in `~/.vim/` already) and manually copy the Zenburn color file into that directory. To fix this issue, run the following on your command line (NOT within Vim):
```bash
$ mkdir ~/.vim/colors   # <- this directory may already exist
$ cp ~/.vim/bundle/Zenburn/colors/zenburn.vim ~/.vim/colors/
```

If when you run Vim, you see towards the bottom of your window "The ycmd server SHUT DOWN...", this means the plug-in YouCompleteMe has not been set up correctly during the plug-in installation step. Simply run the code below to fix it:
```bash
$ sudo apt install -y build-essential   # <- you may not have to run this if you have a c++ compiler ready to go
$ cd ~/.vim/bundle/YouCompleteMe/
$ ./install.py
```
