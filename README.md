# Brandmeister Last Heard to MQTT

Bridges the Brandmeister Last Heard API to a local MQTT Broker

This Python script will listen to the Brandmeister Last Heard API endpoint for any callsign or Talkgroup (or both) that you configure and it will send the data to an MQTT Broker when there is activity for those callsigns and/or talkgroups. This allows you to use the data in a Home Assistant Dashboard for example. You can also use the data for other applications if you wish as well.

This Script is based off the work of [Michael Clemens, DK1MI](https://qrz.is/) and the pyBMNotify script that he wrote. I used the logic of checking to see if it's a monitored callsign or talkgroup that he wrote and instread of pushing it to a notification service, I am pushing it to an MQTT Broker.

The ha_sensor_template.yaml file in the repo is an example of how the sensors could be used with Home Assistant.

This script is for use by Amateur Radio Operators Only.

---

## Installation/Setup Instructions

[Click here to see the installation and setup steps](https://github.com/n8acl/bmlh_to_mqtt/blob/main/installation-setup.md). Then come back here. This is a bit of a long document, so read it all carefully.

---

## Contact

If you have questions, please feel free to reach out to me. You can reach me in one of the following ways:

- Discord: Ravendos
- Mastodon: @n8acl@mastodon.radio
- E-mail: n8acl@qsl.net

Or open an issue on Github. I will respond to it, and of course you, when I can.

If you reach out to me and have an error, please include what error you are getting and what you were doing. I may also ask you to send me certain files to look at. Otherwise just reach out to me :).

---

## Change Log

- 08/26/2024 - Minor Update Release 1.3 - Left off variable 'event' declaration. Fixed.

- 05/20/2024 - Minor Update Release 1.2 - Added Logic to handle multiple events from BM to correctly identify the event needed to send a notification message

- 12/25/2022 - Minor Release 1.1 - Fixes Noisy Call logic

- 11/14/2022 - Inital Release
