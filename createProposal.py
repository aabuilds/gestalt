# pip install dalle2
from dalle2 import Dalle2
import config

# Generate Art

key = config.dalleKey

dalle = Dalle2(key) # your bearer key


generations = dalle.generate("portal to another dimension, digital art")
print(generations)


# Generate Music