sudo kill -9 $(sudo lsof -t -i:80)
nohup sudo python3 manage.py runserver 0:80 &
#sudo() { command sudo env PATH="$PATH" "$@"; }
