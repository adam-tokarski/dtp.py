# -*- coding: utf-8 -*-
from django import template;
import re;

register = template.Library();

@register.filter(is_safe=True)
def removeOrphans(text):
	# reduces the occurence of Orphans (in Polish notation, see http://pl.wikipedia.org/wiki/Sierota_(DTP))
	return re.sub(r'\b([^ ]{1,2})\b ', r'\1&nbsp;', text)
	
	#http://pl.wikipedia.org/wiki/Sierota_(DTP)	
	#http://pl.wikipedia.org/wiki/Wdowa_(DTP)
	#http://pl.wikipedia.org/wiki/Szewc_(DTP)
	
	#todo: dodać przypadki 3literowe (?), np. gdy króciutkim wyrazem zaczyna się nowe zdanie, lepiej, by nie było na końcu wiersza, etc.
	
