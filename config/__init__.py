try:
    from .config import *
except ModuleNotFoundError:
    from .config_sample import *
