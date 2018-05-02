#ping -c 3 -i 0.2 -w 1 -s 1472 -M do 192.168.1.5
echo start
php -S 0.0.0.0:80 &
ping -c 3 -W 1 -s 1472 192.168.1.5
traceroute -n 8.8.8.8
curl localhost
