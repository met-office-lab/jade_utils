import os.path

import iris

import pytest
from unittest.mock import patch


def test_human_bytes():
    from jade_utils.iris_tools import estimate_cube_size
    test_cube_path = os.path.join(os.path.dirname(__file__), 'data', 'test.nc')
    test_cube = iris.load_cube(test_cube_path, 'air_temperature')
    assert estimate_cube_size(test_cube) == '407.8KiB'


def test_quiet_load():
    from jade_utils.iris_tools import quiet_load

    test_cube_path = os.path.join(os.path.dirname(__file__), 'data', 'test.nc')
    loud_cubelist = iris.load(test_cube_path)
    quiet_cubelist = quiet_load(test_cube_path)

    assert loud_cubelist[0] == quiet_cubelist[0]
    # TODO: Should also test that it is quiet

def test_quiet_load_raw():
    from jade_utils.iris_tools import quiet_load_raw

    test_cube_path = os.path.join(os.path.dirname(__file__), 'data', 'test.nc')
    loud_cubelist = iris.load_raw(test_cube_path)
    quiet_cubelist = quiet_load_raw(test_cube_path)

    assert loud_cubelist[0] == quiet_cubelist[0]
    # TODO: Should also test that it is quiet


def test_quiet_load_cube():
    from jade_utils.iris_tools import quiet_load_cube

    test_cube_path = os.path.join(os.path.dirname(__file__), 'data', 'test.nc')
    loud_cube = iris.load_cube(test_cube_path, 'air_temperature')
    quiet_cube = quiet_load_cube(test_cube_path, 'air_temperature')

    assert loud_cube == quiet_cube
    # TODO: Should also test that it is quiet
