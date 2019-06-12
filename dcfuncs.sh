function dcnotify () {
    curl --silent -u """TOKEN"":" -d type="note" -d body="'$*'" -d title=$1 'https://api.pushbullet.com/v2/pushes' > /dev/null
}
