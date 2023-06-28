# Jekyll Setup for MacOS

- Macbook Pro (Not M series)
- Shell is zsh
- Homebrew properly installed
- Document date: 2022.12.08

## Preview
 
Run the following command

```zsh
$ bundle exec jekyll serve
```

## Install Ruby

Ruby version 3.1.3

- Install `ruby-install`

```zsh
$ brew install ruby-install
```

If `ruby-install` has been installed previously, force link

```zsh
$ brew link --overwrite ruby-install
```

- Install `ruby`

```zsh
$ ruby-install ruby
```

To see which `ruby` version is supported, run

```
$ ruby-install
```

- Install `chruby`

```zsh
$ brew install chruby
```

- Setup `chruby`

Add following lines to `~/.zshrc`

```zsh
source /usr/local/opt/chruby/share/chruby/chruby.sh
source /usr/local/opt/chruby/share/chruby/auto.sh
chruby 3.1.3
```

## Install Jekyll

Jekyll version 4.3.1.

Run `which gem` to make sure you actually use the correct `gem` and `ruby`.

- Install `jekyll`, `github-pages`, and `bundle`

```zsh
$ gem install jekyll
$ gem install github-pages
$ gem install bundle
```

- Add `webrick` to `bundle`

```zsh
$ bundle add webrick
```

- Install gems in the Gemfile

If there is a `Gemfile.lock` in the current directory, delete it, then run

```zsh
$ bundle install
```