if [ -d "venv" ]; then
    . venv/bin/activate
    pip3 install -r requirements.txt

else
    python3 -m venv venv

    until [ -d "venv" ]; do sleep 0.1; done

    . venv/bin/activate
    python3 -m pip install --upgrade pip
    pip3 install -r requirements.txt
    python3 dbconnect.py
    python3 coffee_csv_to_db.py
    python3 crawler.py

fi


