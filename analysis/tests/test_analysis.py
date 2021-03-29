import pytest

import numpy as np
from xarray import DataArray


from analysis.analyse import check_temperature, reactor_survived


class TestMeltingTemperature:
    def test_melted(self):
        melted = check_temperature(3500)
        assert melted

    def test_not_melted(self):
        melted = check_temperature(1500)
        assert not melted

    def test_unphysical_temperature(self):
        with pytest.raises(ValueError):
            check_temperature(-100)


@pytest.fixture()
def example_temp_data():
    temp = DataArray(
        name='T',
        data=np.linspace(250, 3500, 10), dims=['time'],
        coords={'time': ('time', np.linspace(1, 10, 10))}
    )
    return temp


def test_reactor_survival(example_temp_data):
    survived = reactor_survived(example_temp_data)
    assert not survived
