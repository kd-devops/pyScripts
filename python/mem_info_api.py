import json
from mem_info import *

class PyAgent():
    def get(self):
	mem_results = mem_stats()
	self.write(json.dumps(mem_results, indent=4))	
