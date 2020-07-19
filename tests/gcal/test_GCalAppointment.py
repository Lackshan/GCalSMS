import pytest
import gcalsms.gcal


class TestInit:
    """
    Tests __init__ method of GCalAppointment.
    """
    def test_args_none(self):
        """
        Tests if method raises error when arguments have None type
        """
        pass

    def test_unsupported_region(self):
        x = gcalsms.gcal.GCalAppointment('7529847625', 'UNSUPPORTED_REGION', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '7529847625'

    def test_invalid_phone_number(self):
        """
        Tests if method raises a ValueError when given a phone_number that does not correspond to the given region.
        """
        # TODO: Add proper values for times. Also improve docstring description
        with pytest.raises(ValueError):
            x = gcalsms.gcal.GCalAppointment('3746273', 'MY', 'time1', 'time2', 'Hello World!')

    def test_phone_number_type(self):
        with pytest.raises(TypeError):
            x = gcalsms.gcal.GCalAppointment(197584375, 'MY', 'time1', 'time2', 'Hello World!')

    def test_phone_number_region_my_1(self):
        x = gcalsms.gcal.GCalAppointment('0197584375', 'MY', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+60197584375'

    def test_phone_number_region_my_2(self):
        x = gcalsms.gcal.GCalAppointment('60197584375', 'MY', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+60197584375'

    def test_phone_number_region_my_3(self):
        x = gcalsms.gcal.GCalAppointment('+60197584375', 'MY', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+60197584375'

    def test_phone_number_region_gb_1(self):
        x = gcalsms.gcal.GCalAppointment('07575574859', 'GB', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+447575574859'

    def test_phone_number_region_gb_2(self):
        x = gcalsms.gcal.GCalAppointment('447575574859', 'GB', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+447575574859'

    def test_phone_number_region_gb_3(self):
        x = gcalsms.gcal.GCalAppointment('+447575574859', 'GB', 'time1', 'time2', 'Hello World!')
        assert x.phone_number == '+447575574859'
