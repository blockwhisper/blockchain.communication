import sys, numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage
im = Image.open(sys.argv[1]).convert('RGBA'); a = np.asarray(im).astype(float)
rgb = a[..., :3] / 255; A = a[..., 3]
hsv = np.asarray(Image.fromarray(a[..., :3].astype(np.uint8)).convert('HSV')).astype(float)
H = hsv[..., 0] * 360 / 255; S = hsv[..., 1] / 255
blue = (H > 160) & (H < 240) & (S > 0.10) & (A > 0)
# keep only blue regions connected to the coin's outside (the edge), never the face
outside = ndimage.binary_dilation(A < 128, iterations=4)
lab, n = ndimage.label(ndimage.binary_closing(blue, iterations=2))
keep = np.isin(lab, np.unique(lab[outside & (lab > 0)])[1:] if 0 in np.unique(lab[outside & (lab > 0)]) else np.unique(lab[outside & (lab > 0)]))
edge = keep & blue
edge = ndimage.binary_dilation(edge, iterations=1) & (A > 0) & (S > 0.06)
w = np.asarray(Image.fromarray((edge*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))) / 255.0
w = w * np.clip((S - 0.04) / 0.10, 0, 1)
L = rgb @ np.array([0.299, 0.587, 0.114])
m = L[edge].mean()
L2 = np.clip((L - m) * 1.7 + 0.70, 0, 1)
gold = np.array([1.00, 0.80, 0.38]); silver = np.array([0.94, 0.94, 0.96])
mix = 0.75 * gold + 0.25 * silver
tint = np.clip(L2[..., None] * mix + np.clip(L2 - 0.80, 0, 1)[..., None] * 1.8, 0, 1)
out = rgb * (1 - w[..., None]) + tint * w[..., None]
Image.fromarray(np.dstack([(out*255).round().astype(np.uint8), A.astype(np.uint8)]), 'RGBA').save(sys.argv[2], optimize=True)
print('edge px', int(edge.sum()), 'components', n)
