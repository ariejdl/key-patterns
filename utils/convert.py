
from lxml import etree
from svg.path import parse_path
import pandas as pd

d = etree.parse("Frame 1.svg").getroot()

items = []

for n in d.getchildren()[0].getchildren():
    if n.get('stroke-opacity') is None and n.get('d') is not None:
        p = parse_path(n.get('d'))
        s, e = p[1].start, p[1].end
        items.append({
            'x1': s.real,
            'y1': s.imag,
            'x2': e.real,
            'y2': e.imag
        })

df = pd.DataFrame(items)
df.to_csv("coords.csv", index=False)