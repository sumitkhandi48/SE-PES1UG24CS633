
import pytest
from loan_eligibility import credit_band, is_eligible, interest_rate



def test_excellent_credit_score():
    assert credit_band(800) == "excellent"


def test_good_credit_score():
    assert credit_band(700) == "good"


def test_fair_credit_score():
    assert credit_band(600) == "fair"


def test_poor_credit_score():
    assert credit_band(400) == "poor"


def test_minimum_valid_credit_score():
    assert credit_band(300) == "poor"


def test_invalid_credit_score_below_range():
    with pytest.raises(ValueError):
        credit_band(299)


def test_invalid_credit_score_above_range():
    with pytest.raises(ValueError):
        credit_band(901)



def test_eligible_salaried_applicant():
    assert is_eligible(30, 50000, "salaried", 800) is True


def test_eligible_self_employed_applicant():
    assert is_eligible(35, 60000, "self_employed", 700) is True


def test_applicant_below_minimum_age():
    assert is_eligible(20, 50000, "salaried", 800) is False


def test_applicant_above_maximum_age():
    assert is_eligible(61, 50000, "salaried", 800) is False


def test_applicant_at_minimum_age():
    assert is_eligible(21, 50000, "salaried", 800) is True


def test_applicant_at_maximum_age():
    assert is_eligible(60, 50000, "salaried", 800) is True


def test_salaried_income_below_minimum():
    assert is_eligible(30, 24999, "salaried", 800) is False


def test_self_employed_income_below_minimum():
    assert is_eligible(30, 39999, "self_employed", 800) is False


def test_income_at_salaried_minimum():
    assert is_eligible(30, 25000, "salaried", 800) is True


def test_income_at_self_employed_minimum():
    assert is_eligible(30, 40000, "self_employed", 800) is True


def test_poor_credit_applicant_is_rejected():
    assert is_eligible(30, 50000, "salaried", 400) is False


def test_unknown_employment_type():
    with pytest.raises(ValueError):
        is_eligible(30, 50000, "unemployed", 800)



def test_excellent_credit_interest_rate():
    assert interest_rate(800, "salaried", False) == 8


def test_good_credit_interest_rate():
    assert interest_rate(700, "salaried", False) == 10


def test_fair_credit_interest_rate():
    assert interest_rate(600, "salaried", False) == 13


def test_poor_credit_interest_rate():
    assert interest_rate(400, "salaried", False) == 13


def test_self_employed_interest_adjustment():
    assert interest_rate(800, "self_employed", False) == 9


def test_collateral_interest_adjustment():
    assert interest_rate(800, "salaried", True) == 6


def test_both_interest_adjustments():
    assert interest_rate(800, "self_employed", True) == 7
