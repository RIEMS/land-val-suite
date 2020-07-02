#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import os.path
import math
import datetime
import subprocess
import numpy as np
import netCDF4 as nc

INFILE = 'bondville.dat'
ATMROOT = '.'
TEMPLATE = '../input.yyyymmddTHHMMSS.cdl'

TNAME = 'T2D'
QNAME = 'Q2D'
UNAME = 'U2D'
VNAME = 'V2D'
PNAME = 'PSFC'
LWNAME = 'LWDOWN'
SWNAME = 'SWDOWN'
PRNAME = 'RAINRATE'
SNNAME = ''

# forcing
with open(INFILE, 'rt') as f:
    for line in f:
        if (line[0:2] != '19'): continue
        line_parts = line.split()
        dt = datetime.datetime(*(map(int, line_parts[0:5])))
        print(dt)
        u, t, rh, p, sw, lw, pr = map(float, line_parts[5:])
        t += 273.15 # temperture in K
        rh /= 100.0 # relative humidity (1)
        p *= 100.0 # pressure in Pa
        pr *= 0.014111 # precipition rate in kg m-2 s-1
        es = 610.78 * math.exp(17.2693882 * (t - 273.16) / (t - 35.86)) # saturation mixing ratio in Pa
        e = es * rh # water vapor pressure
        r = 0.622 * e / (p - e) # water vapor mixing ratio
        ncfname = os.path.join(ATMROOT, dt.strftime('LDASIN.%Y%m%dT%H%M%S.nc'))
        subprocess.run(['ncgen', '-3', '-o', ncfname, TEMPLATE])
        with nc.Dataset(ncfname, 'a') as ncf:
            ncf.variables[UNAME][0,:] = u
            ncf.variables[VNAME][0,:] = 0
            ncf.variables[TNAME][0,:] = t
            ncf.variables[QNAME][0,:] = r
            ncf.variables[PNAME][0,:] = p
            ncf.variables[SWNAME][0,:] = sw
            ncf.variables[LWNAME][0,:] = lw
            ncf.variables[PRNAME][0,:] = pr
