import sys
#from models import *


def update_by_news():
	pass
	#update price by news and add in Prices table

def update_frequent():
	pass
	#update price by small random factor and add in Prices table

if "news" in sys.argv:
	update_by_news()

elif "frequent" in sys.argv:
	update_frequent()