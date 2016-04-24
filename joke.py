from __future__ import with_statement
import json
from sopel import module

@module.commands('joke')
def joke(bot, trigger):
	
	#for getting category (not yet tested)
	type_temp = trigger.group(2)
	#to be replaced with type_temp
	type = 'nerdy'
	query = '?limitTo=["%s"]' % type
	body = web.get('http://api.icndb.com/jokes/random' + query,dont_decode=True)
	data = json.load(body)
	
	#check if ther data is the correct data
	if data is None or data["type"] is not 'success':
		return bot.reply('Error at (joke). This is no Joke!')
	
	bot.say(data["value"]["joke"])
