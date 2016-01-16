#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""
Examples from section 4.1.1 of the tutorial.
"""

from tftb.generators import fmlin
from tftb.processing import WignerVilleDistribution

sig = fmlin(256)[0]
tfr = WignerVilleDistribution(sig)
tfr.run()
tfr.plot(kind='surf', sqmod=True)
