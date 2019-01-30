#encoding:utf-8
import re
def txt2sent(txt):
	sent_list = re.split("[.?!\s\n]",txt)
	return sent_list