youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" $1
find -name "* *" -type f | rename 's/ /_/g'
