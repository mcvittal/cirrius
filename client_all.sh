while true; do

ssh ajmcvitt@taurine.csclub.uwaterloo.ca "/usr/bin/chromium --headless --disable-gpu --screenshot=/users/ajmcvitt/www/htv3/desktop.png http://alexmcvittie.me/htv3git/map.html --window-size=1366,768"
./client_fetch.py
sleep 60
done
