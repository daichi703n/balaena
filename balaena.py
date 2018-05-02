#!/usr/bin/env python
# coding: utf-8

"""
# Balaena
`docker-compose.yml` generator for Network Test Containers with 802.1Q VLAN Tag.

MAINTENER Daichi Kimura <daichi703n@gmail.com>
"""

# Create docker-compose.yml
def create_compose(config):
  print("create compose")
  config["service"] = "2.1"
  #print(config["test"])
  print(config)
  return config

# Create Ping test command
def create_command(config):
  print("create ping")
  command = "ping 8.8.8.8"
  return command

# --- main ---
print('START')

import yaml

# Open and read configuration.yml
f = open("./config/configuration.yml", "r")
data = yaml.load(f)
#print(data)

compose = create_compose(data)
command = create_command(data)

# Write docker-compose.yml
f = open("docker-compose.yml", "w+")
f.write(yaml.dump(compose, default_flow_style=False))

# Write command.sh
f = open("command.sh", "w+")
f.write(command)
