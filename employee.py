
from datetime import datetime

class employee():
	count = 0
	
   def __init__(self, count):
      self.count = count
      
	def set_date(self):
		date_time = datetime.datetime.now()
		return date_time
   
   def displayCount(self):
     print "The count is %d" % self.count
