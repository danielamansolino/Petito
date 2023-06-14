pip3 install -r requirements.txt
pip3 install --upgrade pippip install --force-reinstall -U setuptools

python3 manage.py collectstatic --no-input
python3 manage.py migrate