from run import bmi_calculator


def test_list_valid_id(bmi_calculator):
    assert bmi_calculator['status'] == 200
