# -*- coding: utf-8 -*-
"""
Monte Carlo simulations

Created on Sat Aug  1 10:45:59 2020

@author: cradmin
"""

import pandas_datareader.data as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

start = dt.datetime(2020,Jan,1)
end = dt.datetime(2020,Jun,31)
