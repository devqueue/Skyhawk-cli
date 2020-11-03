virtualenv venv
source venv/bin/activate
python -m pip install pip --upgrade
pip install -r requirements.txt
pip install -e .