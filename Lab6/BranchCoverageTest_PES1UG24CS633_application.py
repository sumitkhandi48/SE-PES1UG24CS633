
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate



def test_credit_score_below_minimum():
    with pytest.raises(ValueError):
        credit_band(299)


def test_credit_score_above_maximum():
    with pytest.raises(ValueError):
        credit_band(901)


def test_excellent_credit_band():
    assert credit_band(800) == "excellent"


def test_good_credit_band():
    assert credit_band(700) == "good"


def test_fair_credit_band():
    assert credit_band(600) == "fair"


def test_poor_credit_band():
    assert credit_band(400) == "poor"



def test_unknown_employment():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)


def test_age_below_minimum():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_age_above_maximum():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_valid_age():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_salaried_income_below_minimum():
    assert is_eligible(30, 20000, "salaried", 800) is False


def test_self_employed_income_below_minimum():
    assert is_eligible(30, 30000, "self_employed", 800) is False


def test_salaried_income_meets_requirement():
    assert is_eligible(30, 25000, "salaried", 800) is True


def test_self_employed_income_meets_requirement():
    assert is_eligible(30, 40000, "self_employed", 800) is True


def test_poor_credit_score_rejected():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_acceptable_credit_score():
    assert is_eligible(30, 50000, "salaried", 550) is True



def test_excellent_credit_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_credit_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_other_credit_band_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_self_employed_adjustment_applied():
    assert interest_rate(800, "self_employed", False) == 9


def test_salaried_rate_without_adjustment():
    assert interest_rate(800, "salaried", False) == 8


def test_collateral_adjustment_applied():
    assert interest_rate(800, "salaried", True) == 6


def test_rate_without_collateral():
    assert interest_rate(800, "salaried", False) == 8
