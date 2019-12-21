Intro
=====

Just a place for me to hold my custom .vimrc file.

Most if not all customizations are taken from [here](https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/) and [here](https://danielmiessler.com/study/vim/).


Setup
=====


If you haven't already, install VIM (Linux):

```bash
$ sudo apt-get remove vim-tiny
$ sudo apt-get update
$ sudo apt-get install vim
```

The extension manager I currently use is [Vundle](https://github.com/VundleVim/Vundle.vim), which you can download like so:
```bash
$ git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Next, clone this repo:

```bash
$ git clone https://github.com/warrenmo/vimrc.git
```

And copy the .vimrc file to your home directory:

```bash
$ cp ./vimrc/.vimrc ~/
```

Now, enter VIM by opening any text file using VIM:

```bash
$ vim any_text_file
```

And run the Vundle plugin manager (within VIM):

```
:PluginInstall
```

You're done!

### Troubleshooting

For some reason, Zenburn sometimes doesn't get placed in the right directory, so you MIGHT need to create a colors directory and manually copy the Zenburn color file into that directory. Run this on your command line (not within VIM) to fix it:
```bash
$ mkdir ~/.vim/colors   # <- might not be necessary
$ cp ~/.vim/bundle/Zenburn/colors/zenburn.vim ~/.vim/colors/
```
