import xml.etree.cElementTree as ET

filename = "/Users/umangagarwal/Desktop/kolkata_india.osm"


osm = iter(ET.iterparse(filename,events=("end",)))


for event, elem in osm:
	try:
		if elem.tag == "tag":
			if elem.attrib['k'] == "addr:street":
				print elem.attrib['v']
	except:
		repr(elem.attrib['v'])