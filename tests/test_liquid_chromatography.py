from nuels_fun_with_peptides.liquid_chormatography import predict_lc_retention_times, select_retention_time_window

def test_predict_lc_retention_times():
    dummy_peptides_string = "PEPTIDE"
    dummy_peptides_string_exp = {"PEPTIDE": 7.8}
    dummy_peptides = ['PEPTIDE', 'SAMPLER', 'LGQGVLK', 'ELVISLIVES', 'ACDEFGHIK', 'TESTPEPTIDE', 'DEFGHIKLMNPQR']
    dummy_peptides_exp = expected = {
        'PEPTIDE':       7.8,
        'SAMPLER':       18.5,
        'LGQGVLK':       23.1,
        'ELVISLIVES':    42.4,
        'ACDEFGHIK':     20.0,
        'TESTPEPTIDE':   6.6,
        'DEFGHIKLMNPQR': 32.5,
    }

    actual = predict_lc_retention_times(dummy_peptides_string)
    assert actual == dummy_peptides_string_exp
    actual_l = predict_lc_retention_times(dummy_peptides)
    assert actual_l == dummy_peptides_exp

test_predict_lc_retention_times()


def test_select_retention_time_window():
    peptide_rt_map = {'DILDEDUM': 100,
            'THISMAKESTWO': -12.5,
            'THREEEEEEEEEEEE': 23.9}
    selected = select_retention_time_window(peptide_rt_map, lower_ret_time=-11.5, upper_ret_time=99.5)

    assert selected == ['THREEEEEEEEEEEE']

test_select_retention_time_window()