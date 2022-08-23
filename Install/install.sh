sudo apt-get install -y python3 python3-pip figlet

sudo pip3 install -r Install/requirements.txt

sudo python3 Setup/run.py

sudo cp Install/Service/FrontWeb_service.service /etc/systemd/system/
sudo cp Install/Service/serviceAPI_service.service /etc/systemd/system/
sudo cp Install/Service/Setup_service.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable Setup_service
sudo systemctl enable FrontWeb_service
sudo systemctl enable serviceAPI_service

sudo systemctl start Setup_service
sudo systemctl start FrontWeb_service
sudo systemctl start serviceAPI_service

figlet Ecocycling
echo
echo
echo System Setup Done!
