echo "This will update MAGE, briefly taking it offline.  Please Ctrl-C within 5 seconds if you would like to abort..."

sleep 5

echo "Please verify that httpd has a version >= 2.2.15. If not, please update."

httpd -v

echo "Please verify that node.js has a version >= 0.10.0. If not, please update."

node -v

echo "Please verify that mongodb has a version >= 2.6.0. If not, please update."

mongo --version

echo "Please verify that graphicsmagick has a version >= 1.3.0. If not, please update."

gm version

sudo service httpd stop

cd /data/mage-server

sleep 1

pwd

echo "Running git diff, there should be no output here:"

git diff

echo "Finished, if you saw output, please troubleshoot."

sleep 3

echo "Pulling in 5 seconds..."

sleep 5

git pull

sleep 5

sudo service httpd start