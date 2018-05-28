"""
Created on Apr 4, 2014
Updated on May 16, 2018
@author: Dario Bonino
@author: Luigi De Russis
Copyright (c) 2014-2018 Dario Bonino and Luigi De Russis

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License

- - - -
Modified version for AmI-2018 project called YSDI.
"""

import rest
import time

#base_url = 'http://localhost:8080'
base_url = 'http://192.168.0.201'
#username = 'newdeveloper'
username = "fFSt4atQ1zIcis0aAudg4ULMYx9AUiB9VYyDSLfO"
lights_url = base_url + '/api/' + username + '/lights/'
VAL = "5"


def init():
    all_the_lights = rest.send(url=lights_url)
    for light in all_the_lights:
        light = VAL
        url_to_call = lights_url + light + '/state'
        body = '{ "on" : false, }'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

def turnOn():
    all_the_lights = rest.send(url=lights_url)
    body = '{ "on" : true, "alert":"none", "hue":10000, "bri":25, "sat":100 }'
    for light in all_the_lights:
        light = VAL
        url_to_call = lights_url + light + '/state'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

def turnOff():
    all_the_lights = rest.send(url=lights_url)
    body = '{ "on" : false, "alert":"none", "hue":0, "bri":25, "sat":254 }'
    for light in all_the_lights:
        light = VAL
        url_to_call = lights_url + light + '/state'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

def alarm():
    """
    Questa accende la luce, la fa diventare rossa per 2s, poi si rimette nelle condizioni
    iniziali.
    """
    all_the_lights = rest.send(url=lights_url)
    iniziale = {}
    body = '{ "on" : true, "hue":0, "bri":254, "sat":254 }'
    #for light in all_the_lights:
    light = VAL
    diz = all_the_lights[light]
    stato = diz["state"]
    iniziale[light] = stato["on"]
    url_to_call = lights_url + light + '/state'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
    time.sleep(0.5)

    for i in range(1,4):
        body = '{"bri":10}'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
        time.sleep(0.5)
        body = '{"bri":254}'
        rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})
        time.sleep(0.5)


    #for light in all_the_lights:
    light = VAL
    if iniziale[light] == True:
        body = '{ "on" : true}'
    else:
        body = '{ "on" : false}'
    url_to_call = lights_url + light + '/state'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

def increaseBrightness():
    light = VAL
    url_to_call = lights_url + light + '/state'
    body = '{ "bri":125}'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})

def decreaseBrightness():
    light = VAL
    url_to_call = lights_url + light + '/state'
    body = '{ "bri":25}'
    rest.send('PUT', url_to_call, body, {'Content-Type': 'application/json'})


#il main è solo per debug
if __name__ == '__main__':
    # the base URL
    #base_url = 'http://192.168.0.201'
    # if you are using the emulator, probably the base_url will be:
    #base_url = 'http://localhost:8080'
    # example username, generated by following https://www.developers.meethue.com/documentation/getting-started
    #username = '1jlyVie2nvwtNwl0hv8KdZOO0okdvNcIIdPXWsdX'
    # if you are using the emulator, the username is:
    #username = 'newdeveloper'
    turnOn()
    alarm()
    turnOff()
    """
    all_the_lights = rest.send(url=lights_url)
    for light in all_the_lights:
        print(light)
    """