def normalize_rgba(rgba: list):
    if len(rgba) < 4:
        rgba = rgba + [255]
    
    norm_rgba = [float(i)/255 for i in rgba]
    return norm_rgba

BASE02 = normalize_rgba([7,54,66])
BASE00 = normalize_rgba([101,123,131])
YELLOW = normalize_rgba([181,137,0])
GREEN = normalize_rgba([133,153,0])