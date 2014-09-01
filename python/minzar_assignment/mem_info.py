import os
import json

data = {}

def mem_status():
    mem_stats={}
    mem_info = '/proc/meminfo'
    fo = open(mem_info, 'r+')
    mem_data=fo.readlines()

    for m in mem_data:
    	if m.split()[0]=='MemTotal:':
	    mem_stats['TotalMem'] = m.split()[1]
    	elif m.split()[0]=='MemFree:':
	    mem_stats['FreeMem'] = m.split()[1]
    	elif m.split()[0]=='SwapTotal:':
	    mem_stats['TotalSwap'] = m.split()[1]
    	elif m.split()[0]=='SwapFree:':
	    mem_stats['SwapFree'] = m.split()[1]

    data["Memory Status"] = mem_stats
    return (data)		
