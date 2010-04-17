'''
tf.py

A skybot plugin for Team Fortress 2
By Ipsum
'''

import json
import urllib

from util import hook

@hook.command('hats')
@hook.command
def tf(inp):
    '''.tf/.hats <SteamID> -- Displays the number of hats
        and items waiting to be received by <SteamID>'''

    if not inp:
        return tf.__doc__

    if inp.isdigit() : link = 'profiles'
    else : link = 'id'

    url = 'http://steamcommunity.com/%s/%s/tfitems?json=1' % \
        (link,urllib.quote(inp, safe=''))

    raw_data = urllib.urlopen(url).read().decode('utf-8')

    try:
        inv = json.loads(raw_data)
    except ValueError:
        return '%s is not a valid profile' % inp

    dropped,dhats,hats = 0,0,0
    for item, data in inv.iteritems():
        ind = int(data['defindex'])
        if data['inventory'] == 0:
            if 47<=ind<=55 or 94<=ind<=126 or 134<=ind<=152:
                dhats+=1
            else:
                dropped+=1
        else:
            if 47<=ind<=55 or 94<=ind<=126 or 134<=ind<=152:
                hats+=1

    return '%s has had %s items and %s hats drop (%s total hats)' % (inp,dropped,dhats,dhats+hats)