echo "This will update GeoQ, briefly taking it offline.  Please Ctrl-C within 5 seconds if you would like to abort..."

sleep 5

cd /usr/local/src/geoq

source bin/activate

sleep 1

cd geoq

pwd

echo "Running git diff, there should be no output here:"

git diff

echo "Finished, if you saw output, please troubleshoot."

sleep 3

echo "Please make sure these servers are correct:"
git checkout develop
git remote -v

echo "Pulling in 5 seconds..."
sleep 5

git pull

sleep 5

echo "Migrating DB..."

python manage.py syncdb

sleep 1

python manage.py migrate --all

sleep 1

python manage.py collectstatic

sleep 1

echo "Changing permissions on static files..."

chown -R apache /data/geoq/static/

sleep 1

echo "Restarting apache..."

service httpd restart

echo "Done!"