
import argparse

BASE = '''
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">

  {content}

</svg>
'''


HOR_W = 12
DIAG_H = 20.7846

def up_tri(x, y):
    return f'<path d="M{x} {y + DIAG_H}L{x + HOR_W} {y}L{x + HOR_W * 2} {y + DIAG_H}H{x}Z" fill="#cccccc"/>'

def down_tri(x, y):
    return f'<path d="M{x} {y}L{x + HOR_W} {y + DIAG_H}L{x + HOR_W * 2} {y}H{x}Z" fill="#cccccc"/>'

def pos_diag(x, y):
    return f'<path d="M{x} {y + DIAG_H}L{x + HOR_W} {y}" stroke="black" stroke-linecap="round"/>'

def neg_diag(x, y):
    return f'<path d="M{x} {y}L{x + HOR_W} {y + DIAG_H}" stroke="black" stroke-linecap="round"/>'
    pass

def hor(x, y):
    return f'<path d="M{x} {y}H{x + HOR_W * 2}" stroke="black" stroke-linecap="round"/>'

def grid(n_cols, n_rows):
    for y in range(n_rows):
        for x in range(n_cols):
            # triangles
            # even row
            yield up_tri(x * HOR_W * 2, DIAG_H * y * 2)
            yield down_tri(x * HOR_W * 2 + HOR_W, DIAG_H * y * 2)
            # odd row
            yield up_tri(x * HOR_W * 2 + HOR_W, DIAG_H + DIAG_H * y * 2)
            yield down_tri(x * HOR_W * 2, DIAG_H * y * 2 + DIAG_H)

            # diagonal lines
            # even row
            yield pos_diag(x * HOR_W * 2, DIAG_H * y * 2)
            yield neg_diag(x * HOR_W * 2 + HOR_W, DIAG_H * y * 2)
            # odd row
            yield pos_diag(x * HOR_W * 2 + HOR_W, DIAG_H * y * 2 + DIAG_H)
            yield neg_diag(x * HOR_W * 2, DIAG_H * y * 2 + DIAG_H)

            # horizontal lines
            # even row
            yield hor(x * HOR_W * 2 + HOR_W, DIAG_H * y * 2)
            # odd row
            yield hor(x * HOR_W * 2, DIAG_H * y * 2 + DIAG_H)

if __name__ == "__main__":
    # example usage:
    # python grid.py 10 10 > out.svg

    parser = argparse.ArgumentParser(description='Make a triangle grid')
    parser.add_argument('width', type=int, help='grid width')
    parser.add_argument('height', type=int, help='grid height')
    args = parser.parse_args()
    
    parts = []
    w, h = args.width, args.height
    for el in grid(w, h):
        parts.append(el)
    
    print(BASE.format(
        content="\n".join(parts),
        width=w * HOR_W * 2 + HOR_W,
        height=h * DIAG_H * 2
    ))
