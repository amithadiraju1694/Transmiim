
import numpy as np
from io import BytesIO
from PIL import Image
import numpy as np

def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))