# shutdown

auto exec

sudo cp shutdown.service /etc/systemd/system/
sudo systemctl enable shutdown.service
sudo systemctl start shutdown.service
