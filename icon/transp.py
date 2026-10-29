import sys
from PIL import Image, ImageFilter
import numpy as np
from collections import deque
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); a = np.asarray(im).astype(int); h, w, _ = a.shape
# distance from white
d = 255*3 - a.sum(2)
bg = np.zeros((h, w), bool); q = deque()
for x in range(w):
    for y in (0, h-1): q.append((y, x))
for y in range(h):
    for x in (0, w-1): q.append((y, x))
TOL = 60  # sum of channel deficits from white
while q:
    y, x = q.popleft()
    if bg[y, x] or d[y, x] > TOL: continue
    bg[y, x] = True
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < h and 0 <= nx < w and not bg[ny, nx]: q.append((ny, nx))
alpha = np.where(bg, 0, 255).astype(np.uint8)
# soften the edge: pixels just inside the boundary get partial alpha by whiteness
edge = np.asarray(Image.fromarray(alpha).filter(ImageFilter.MinFilter(3))) != alpha
part = np.clip(d * 255 // 120, 0, 255)
alpha = np.where(edge & ~bg, np.maximum(part, 0), alpha).astype(np.uint8)
alpha = np.asarray(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.6)))
alpha = np.where(bg & (alpha < 40), 0, alpha).astype(np.uint8)
out = Image.fromarray(np.dstack([a.astype(np.uint8), alpha]), 'RGBA')
out.save(dst, optimize=True)
print('bg px', bg.sum(), 'of', h*w)
