from __future__ import with_statement
from sopel import module
import requests

@module.commands('joke')
def joke(bot, trigger):

        #for getting category (not yet tested)
        type_temp = trigger.group(2)
        #to be replaced with type_temp
        type = 'nerdy'

        query = '?limitTo=["%s"]' % type

        body = requests.get('http://api.icndb.com/jokes/random' + query)

        data = body.json()

        #check if ther data is the correct data
        if data is None or data['type'] != u'success':
            return bot.reply('Error at (joke). This is no Joke! Here\'s what the dumb api said:\n' + data)

        bot.say(data['value']['joke'])
