import os
from .common import *

try:
    FIR_ENV = os.environ["FIR_ENV"]
except KeyError:
    print("No valid 'FIR_ENV' environment variable found, assuming 'dev'")
    FIR_ENV = "dev"


if FIR_ENV == "prod":
    from .prod import *
elif FIR_ENV == "staging":
    from .staging import *
elif FIR_ENV == "dev":
    from .dev import *
else:
    print(
        "Value of 'FIR_ENV' environment variable matches no valid patterns, assuming 'dev'"
    )
    from .dev import *
