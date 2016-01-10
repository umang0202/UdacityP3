import xml.etree.cElementTree as ET

filename = "/Users/umangagarwal/Desktop/kolkata_india.osm"


'''Contributions by user "FuckOSMFandODbL" are spurious and incorrect'''

osm = iter(ET.iterparse(filename,events=("end",)))
x = 0
for event, elem in osm:
	try:
		if elem.attrib['user'] == "FuckOSMFandODbL":
			x += 1
			ET.dump(elem)
	except KeyError:
		continue
	finally:
		elem.clear()

print x
