import xml.etree.cElementTree as ET

filename = "/Users/umangagarwal/Desktop/kolkata_india.osm"
num_pincodes = 0

"""Check if the osm file has any invalid pincodes. Also count number of pincodes"""


osm = iter(ET.iterparse(filename,events=("end",)))


for event, elem in osm:
    if elem.tag == "tag":
        try:
            if elem.attrib['k'] == "postal_code":
                num_pincodes += 1
                try:
                    #All pincodes in Kolkata and vicinity are in 700000 to 750000 range
                    if len(elem.attrib['v']) != 6 or int(elem.attrib['v']) < 700000 or int(elem.attrib['v']) > 750000:
                        print elem.attrib['v']
                        elem.clear()
                except ValueError:
                    print str(elem.attrib['v']) + "Pincode not an int"
                    elem.clear()
        except KeyError:
            elem.clear()
            continue

print num_pincodes