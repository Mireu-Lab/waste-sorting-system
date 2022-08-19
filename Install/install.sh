sudo apt-get install -y python3 python3-pip
sudo pip3 install -r Install/requirements.txt

sudo cp Install/Service/FrontWeb_service.service /etc/systemd/system/
sudo cp Install/Service/serviceAPI_service.service /etc/systemd/system/
sudo cp Install/Service/Setup_service.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable FrontWeb_service
sudo systemctl enable serviceAPI_service
sudo systemctl enable Setup_service

sudo systemctl start FrontWeb_service
sudo systemctl start serviceAPI_service
sudo systemctl start Setup_service