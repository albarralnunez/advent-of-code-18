import pytest

from src.day3.models import Position, Area, Claim, Fabric, ClaimID, CounterMultipleClaims, SingleClaimFinder


@pytest.mark.parametrize("test_input,expected", [
    (Claim(
        identifier=ClaimID(1),
        area=Area(
            starting_point=Position(x=1, y=1),
            width=2, height=2
        )
    ), {
        Position(1, 1): {ClaimID(1)}, Position(1, 2): {ClaimID(1)},
        Position(2, 1): {ClaimID(1)}, Position(2, 2): {ClaimID(1)},
    }),
])
def test_make_claim(test_input, expected):
    fabric = Fabric()
    fabric.make_claim(claim=test_input)
    expected = Fabric(expected)
    assert fabric == expected


@pytest.mark.parametrize("test_input,expected", [
    ([Claim(
        identifier=ClaimID(1),
        area=Area(
            starting_point=Position(x=1, y=1),
            width=2, height=2
        )
    ), Claim(
        identifier=ClaimID(2),
        area=Area(
            starting_point=Position(x=1, y=1),
            width=3, height=3
        )
    ), ], {
        Position(1, 1): {ClaimID(2), ClaimID(1)},
        Position(1, 2): {ClaimID(2), ClaimID(1)},
        Position(1, 3): {ClaimID(2)},
        Position(2, 1): {ClaimID(2), ClaimID(1)},
        Position(2, 2): {ClaimID(2), ClaimID(1)},
        Position(2, 3): {ClaimID(2)},
        Position(3, 1): {ClaimID(2)},
        Position(3, 2): {ClaimID(2)},
        Position(3, 3): {ClaimID(2)},
    }),
])
def test_make_claims(test_input, expected):
    fabric = Fabric()
    fabric.make_claims(claims=test_input)
    expected = Fabric(expected)
    assert fabric == expected


@pytest.mark.parametrize("test_input,expected", [
    (Fabric({
        Position(0, 0): {ClaimID(1)},
        Position(1, 0): {ClaimID(1)},
        Position(0, 1): {ClaimID(1)},
        Position(1, 1): {ClaimID(1), ClaimID(2)},
    }), 1)
])
def test_count_multiple_claims(test_input, expected):
    solver = CounterMultipleClaims(test_input)
    result = solver()
    assert result == expected


@pytest.mark.parametrize("test_input,expected", [
    (Fabric({
        Position(0, 0): {ClaimID(1)}, Position(1, 0): {ClaimID(1)},
        Position(0, 1): {ClaimID(1)}, Position(1, 1): {ClaimID(1), ClaimID(2)},
    }), "1"),
    (Fabric({
        Position(0, 0): {ClaimID(1), ClaimID(2)}, Position(1, 0): {ClaimID(1), ClaimID(2)},
        Position(0, 1): {ClaimID(1), ClaimID(2)}, Position(1, 1): {ClaimID(3)},
    }), "3")
])
def test_count_single_claims(test_input, expected):
    solver = SingleClaimFinder(fabric=test_input)
    result = solver()
    assert result == expected
