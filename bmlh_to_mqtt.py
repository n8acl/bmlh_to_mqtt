# pip3 uninstall socketIO_client
# pip3 install "python-socketio[client]"

# Import Libraries and configs
import config as cfg
import json
import datetime as dt
import time
import socketio
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

## Define Static Variables

########################################

sio = socketio.Client()

last_TG_activity = {}
last_OM_activity = {}

def construct_message(c):
    tg = c["DestinationID"]
    out = ""
    duration = c["Stop"] - c["Start"]
    # convert unix time stamp to human readable format
    time = dt.datetime.utcfromtimestamp(c["Start"]).strftime("%Y/%m/%d %H:%M")
    # construct text message from various transmission properties
    out += c["SourceCall"] + ' (' + c["SourceName"] + ') was active on '
    out += str(tg) + ' (' + c["DestinationName"] + ') at '
    out += time + ' (' + str(duration) + ' seconds)'
    # finally return the text message
    return out

@sio.event
def connect():
    print('connection established')

@sio.on("mqtt")
def on_mqtt(data):
    call = json.loads(data['payload'])
    tg = call["DestinationID"]
    callsign = call["SourceCall"]
    start_time = call["Start"]
    stop_time = call["Stop"]
    notify = False
    now = int(time.time())

    # check if callsign is monitored, the transmission has already been finished
    # and the person was inactive for n seconds
    if callsign in cfg.callsigns:
        if callsign not in last_OM_activity:
            last_OM_activity[callsign] = 9999999
        inactivity = now - last_OM_activity[callsign]
        if callsign not in last_OM_activity or inactivity >= cfg.min_silence:
            # If the activity has happened in a monitored TG, remember the transmission start time stamp
            if tg in cfg.talkgroups and stop_time > 0:
                last_TG_activity[tg] = now
            # remember the transmission time stamp of this particular DMR user
            last_OM_activity[callsign] = now
            notify = True
    # Continue if the talkgroup is monitored, the transmission has been
    # finished and there was no activity during the last n seconds in this talkgroup
    elif tg in cfg.talkgroups and stop_time > 0:# and callsign not in cfg.noisy_calls:
        if tg not in last_TG_activity:
            last_TG_activity[tg] = 9999999
        inactivity = now - last_TG_activity[tg]
        # calculate duration of key down
        duration = stop_time - start_time
        # only proceed if the key down has been long enough
        if duration >= cfg.min_duration:
            if tg not in last_TG_activity or inactivity >= cfg.min_silence:
                notify = True
            elif cfg.verbose:
                print("ignored activity in TG " + str(tg) + " from " + callsign + ": last action " + str(inactivity) + " seconds ago.")
            last_TG_activity[tg] = now
    if cfg.verbose and callsign in cfg.noisy_calls:
        print("ignored noisy ham " + callsign)

    ## Publish to MQTT Topics
    if notify:
        publish.single(cfg.mqtt_base_topic + "callsign",callsign,hostname=cfg.mqtt_broker,port=cfg.mqtt_port)
        publish.single(cfg.mqtt_base_topic + "talkgroup",tg,hostname=cfg.mqtt_broker,port=cfg.mqtt_port)
        publish.single(cfg.mqtt_base_topic + "start_time",start_time,hostname=cfg.mqtt_broker,port=cfg.mqtt_port)
        publish.single(cfg.mqtt_base_topic + "stop_time",stop_time,hostname=cfg.mqtt_broker,port=cfg.mqtt_port)    

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect(url='https://api.brandmeister.network', socketio_path="/lh/socket.io", transports="websocket")
sio.wait()