Streamy
=======

Testing APP, using dataframes, postgres, docker, and streamlit.

Requirements
-------
Create a config file for postgres using as example `secrets.toml.example` on folder.


Docker run
-------
```
git clone https://github.com/some..
cd streamy
# build
docker build -t streamy .
# run
docker run -p 8501:8501 streamy
# container run
docker container ls -a
docker container start <container_name>
```
or
```
docker compose up
```

Install locally
-------

**Ubuntu/Debian/MacOSs**
```
git clone https://github.com/some..
cd streamy
python3 -m venv venv
. ./venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip3 install -r requirements.txt
deactivate
```
(If you're on an M1 Mac, make sure you are running an ARM64 native python virtual environment)

troubleshooting, ubuntu/debian might need:
```
sudo apt-get install build-essential python3-dev git
# or
pip install --force-reinstall -v "openpyxl==3.1.0"
```

**Windows Powershell**
```
git clone https://github.com/some..
cd streamy
py -m venv venv
./venv/Scripts/activate
python -m pip install --upgrade pip setuptools wheel
pip3 install -r requirements.txt
deactivate
```

Run
-------

**Ubuntu/Debian/MacOSs**
```
. ./venv/bin/activate
streamlit run streamy.py
```

**Windows Powershell**
```
./venv/Scripts/activate
streamlit run streamy.py
```


## create systemd-service

```
sudo su
# create soft link to profile dir
ln -s /home/br/.streamlit /home/br/streamy/.streamlit
```

Create service file `/lib/systemd/system/streamyd.service`
```
[Unit]
Description=streamy-daemon

[Service]
Restart=on-failure
ExecStart=/bin/bash /home/br/streamy/scripts/streamyd.sh

[Install]
WantedBy=multi-user.target
```

To run it
```
systemctl daemon-reload
systemctl enable streamyd.service
systemctl start streamyd.service
```
