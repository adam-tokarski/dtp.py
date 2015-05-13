# -*- coding: utf-8 -*-

from django import template;
import re;

register = template.Library();

@register.filter(is_safe=True)
def removeOrphans(text):
	# reduces the occurence of Orphans (in Polish notation, see http://pl.wikipedia.org/wiki/Sierota_(DTP))
	r = re.compile(r'([^<]\b[^ ]{1,2})\b[ \n]', re.UNICODE)
	text = r.sub(r'\1&nbsp;', text)

	# to avoid alone short words of new paragraph
	r = re.compile(r"(\.[ \n]?[^ \n]{1,4})[ \n]")
	return r.sub(r'\1&nbsp;', text)
	
	#http://pl.wikipedia.org/wiki/Sierota_(DTP)	
	#http://pl.wikipedia.org/wiki/Wdowa_(DTP)
	#http://pl.wikipedia.org/wiki/Szewc_(DTP)
	
