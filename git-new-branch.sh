#! /usr/bin/sh

new_branch() {
  git switch develop
  git pull origin develop
  git switch -c "$1"
}

new_branch "$@"
