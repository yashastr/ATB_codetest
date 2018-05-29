#!/usr/bin/env python

import web
import json
from itertools import groupby
from operator import itemgetter
from pprint import pprint



urls = (
    '/ATB/(.*)', 'update'
)


app = web.application(urls, globals())


class update:
    
    def POST(self,value):
        query_components = web.input()
        print('query_components:::',query_components)
        output = {}
	print(query_components)
        if query_components is None:
            # send error Response from here in output
            return json.dumps(output)
            
        else:
            #send valid Response from here in output
            # call methods & parse the data
            if query_components['setOfStrings'] != "":
		setOfStrings = query_components['setOfStrings']
		lcs = long_substr(setOfStrings)
                output['lcs'] = 'value : ',lcs
                return json.dumps(output)


def long_substr(data):
	substr = ''
	if len(data) > 1 and len(data[0]) > 0:
		for i in range(len(data[0])):
			for j in range(len(data[0])-i+1):
				if j > len(substr) and is_substr(data[0][i:i+j], data):
					substr = data[0][i:i+j]
		return substr

def is_substr(find, data):
	if len(data) < 1 and len(find) < 1:
		return False
	for i in range(len(data)):
		if find not in data[i]:
			return False
	return True

if __name__ == "__main__":
	app.run()
