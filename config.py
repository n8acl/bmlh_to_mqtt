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
