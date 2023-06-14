pip3 install -r requirements.txt
pip3 install --upgrade pip 
pip3 install --force-reinstall -U django
pip3 install --force-reinstall -U dj-database-url

python3 manage.py collectstatic --no-input
python3 manage.py migrate