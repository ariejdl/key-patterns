
from lxml import etree
#from svglib.svglib import svg2rlg
from svg.path import parse_path
from io import StringIO
import pandas as pd

d = etree.parse("Frame 1.svg").getroot()

items = []

for n in d.getchildren()[0].getchildren():
    #import pdb; pdb.set_trace()
    if n.get('stroke-opacity') is None and n.get('d') is not None:
        '''
        print(etree.tostring(n))
        el = svg2rlg(StringIO(etree.tostring(n).decode("utf-8") ))
        #print(dir(el))
        print(el.height)
        #import pdb; pdb.set_trace()
        print(el.getProperties())
        print(el.getProperties()['contents'][0].getProperties())
        '''
        p = parse_path(n.get('d'))
        s, e = p[1].start, p[1].end
        items.append({
            'x1': s.real,
            'y1': s.imag,
            'x2': e.real,
            'y2': e.imag
        })
        #import pdb; pdb.set_trace()

df = pd.DataFrame(items)
df.to_csv("coords.csv", index=False)