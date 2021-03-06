# -*- coding: utf-8 -*-
"""
Created on Nov. 15th 2017
"""
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import pytest
import pygeopressure


@pytest.fixture()
def real_well():
    return pygeopressure.Well(json_file='test/data/FW1.json')


def test__well_properties(real_well):
    assert real_well.logs == [
        'Velocity', 'Shale_Volume', 'Overburden_Pressure']
    assert real_well.unit_dict == {
        'Depth': 'm',
        'Overburden_Pressure': 'MegaPascal',
        'Shale_Volume': 'Fraction',
        'Velocity': 'Meter/Second'}
    assert str(real_well) == "Well-FW1"


@pytest.fixture()
def measured_log():
    temp_log = pygeopressure.Log()
    temp_log.depth = [4118.5]
    temp_log.data = [60.6047]
    return temp_log


@pytest.fixture()
def measured_coef_log():
    temp_log = pygeopressure.Log()
    temp_log.depth = [4118.5]
    temp_log.data = [1.5005]
    return temp_log


def test__well_get_pressure(real_well, measured_log, measured_coef_log):
    # assert real_well.get_pressure_measured(ref='sea') == measured_log
    # assert real_well.get_dst(ref='sea') == measured_log
    # assert real_well.get_wft(ref='sea') == measured_log
    # assert real_well.get_emw(ref='sea') == measured_log
    assert real_well.get_pressure("loading", ref='sea') == measured_log
    assert real_well.get_pressure("loading", ref="sea", coef=True) == \
        measured_coef_log
    assert real_well.get_pressure("unloading", ref="sea", coef=True) == \
        measured_coef_log
    assert real_well.get_pressure("unloading", ref='sea') == measured_log
    assert real_well.get_pressure("unloading").depth == [4159.5]
