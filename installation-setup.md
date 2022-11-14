### Installation Steps

1) [Install needed packages, clone Repo and install library dependencies](installation-setup.md#installing-the-script)
2) [Configure the script](installation-setup.md#configure-the-script)
3) [Run the Script](installation-setup.md#running-the-script)

### Assumptions

1) You already have an MQTT Broker setup and configured.
2) The command examples contained within are based on Linux command line. If you are using Windows or Mac, you need to be familiar with
   1) installing Python3 and PIP3 on Windows
   2) install packages from a requirements.txt file


---

### Installing the Script

The first stepis installing the needed packages, cloning the repo to get the script and then installing the needed libraries for the script to work properly.

This is probably the easiest step to accomplish.

Please run the following commands on your server:

```bash
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get -y dist-upgrade

sudo apt-get install python3 python3-pip git screen

git clone https://github.com/n8acl/bmlh_to_mqtt.git

cd bmlh_to_mqtt

pip3 install -r requirements.txt
```
---

## Configure the Script

Now that you have all of your keys/webhooks/what have you, let's configure the script.

You will need to edit the config.py file in the cloned directory. Open this file in your favorite text editor. You should see something similiar:

```python
# adapt the following variables to your needs
talkgroups = [311293,3110683] # Talkgroups to monitor
callsigns = [] # Callsigns to monitor
noisy_calls = ["L1DHAM", "N0CALL", "N0C4LL"] # Noisy calls signs that will be ignored
min_duration = 0 # Min. duration of a QSO to qualify for a push notification
min_silence = 300 # Min. time in seconds after the last QSO before a new push notification will be send
verbose = False # Enable extra messages (console only)

# MQTT Configurations
mqtt_broker = 'IP_FQDN_HERE' # IP Address or FQDN of the host running your MQTT Broker
mqtt_port = 1883 # Default is ususallyt 1883 but if you have it running on a different port, change it here.
mqtt_base_topic = 'home_assistant/ham_radio/bm_lh_feed/' # this is the base topic of where the data will be sent. You can change if you have your own naming scheme

```

Each section below that contains what is needed for each service to operate.
---

## Running the Script

Once you have the config file edited, start the bot by typing the following:

```bash
screen -R bmlh_to_mqtt
```

Then in the new window:
```bash
cd bmlh_to_mqtt

python3 bmlh_to_mqtt.py
```

Once that is done, hold ```CTRL``` and then tap ```A``` and then ```D``` to disconnect from the screen session. If something ever happens, you can reconnect to the session by typing:

```bash
screen -R bmlh_to_mqtt
```

And see why it errored or quit. You will know it errored because it will send the error to whatever server you are using for notifications. This is useful if you need to contact me for support or want to restart the script.