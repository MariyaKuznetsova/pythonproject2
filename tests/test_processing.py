from src.processing import filter_by_state

from src.processing import sort_by_date

import pytest


def test_filter_by_state():
    assert filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        state="EXECUTED",
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_two():
    assert filter_by_state(
        [
            {"id": 40486452, "state": "EXECUTED", "date": "2026-09-03T18:35:29.512364"},
            {"id": 38247810, "state": "CANCELED", "date": "2015-01-30T02:08:58.425572"},
            {"id": 96858717, "state": "CANCELED", "date": "2010-03-12T21:27:25.241689"},
            {"id": 81878621, "state": "EXECUTED", "date": "2014-01-14T08:21:33.419441"},
        ],
        state="CANCELED",
    ) == [
        {"id": 38247810, "state": "CANCELED", "date": "2015-01-30T02:08:58.425572"},
        {"id": 96858717, "state": "CANCELED", "date": "2010-03-12T21:27:25.241689"},
    ]


def test_filter_by_state_tree():
    assert (
        filter_by_state(
            [
                {"id": 40486452, "state": "EXECUTED", "date": "2026-09-03T18:35:29.512364"},
                {"id": 38247810, "state": "CANCELED", "date": "2015-01-30T02:08:58.425572"},
                {"id": 96858717, "state": "CANCELED", "date": "2010-03-12T21:27:25.241689"},
                {"id": 81878621, "state": "EXECUTED", "date": "2014-01-14T08:21:33.419441"},
            ],
            state="thyejeu",
        )
        == []
    )


def test_filter_by_state_four():
    assert filter_by_state(
        [
            {"id": 542545, "state": "EXECUTED", "date": "2026-09-03T18:35:29.512364"},
            {"id": 46547, "state": "EXECUTED", "date": "2015-01-30T02:08:58.425572"},
            {"id": 4635635, "state": "CANCELED", "date": "2000-01-02T21:27:25.241689"},
            {"id": 535626, "state": "EXECUTED", "date": "2014-01-14T08:21:33.419441"},
        ],
        state="CANCELED",
    ) == [{"id": 4635635, "state": "CANCELED", "date": "2000-01-02T21:27:25.241689"}]


@pytest.fixture
def examples_filter_by_state1():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def examples_filter_by_state2():
    return []


@pytest.fixture
def examples_filter_by_state3():
    return [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]


@pytest.fixture
def examples_filter_by_state4():
    return []


def test_filter_by_state_five1(examples_filter_by_state1):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
        == examples_filter_by_state1
    )


def test_filter_by_state_five2(examples_filter_by_state2):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "hsjghn", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "zgngfngb", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "zngfng", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "nxfhmhg", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
        == examples_filter_by_state2
    )


def test_filter_by_state_five3(examples_filter_by_state3):
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="EXECUTED",
        )
        == examples_filter_by_state3
    )


def test_filter_by_state_five4(examples_filter_by_state4):
    assert filter_by_state([], state="CANCELED") == examples_filter_by_state4


@pytest.mark.parametrize(
    "entering_filter_by_state, function_output_filter_by_state",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ([], []),
        (
            [
                {"id": 41428829, "state": "hsjghn", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "zgngfngb", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "zngfng", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "nxfhmhg", "date": "2018-10-14T08:21:33.419441"},
            ],
            [],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
    ],
)
def test_filter_by_state_six(entering_filter_by_state, function_output_filter_by_state):
    assert filter_by_state(entering_filter_by_state, state="EXECUTED") == function_output_filter_by_state


def test_sort_by_date():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        reverse=False,
    ) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_sort_by_date_two():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        reverse=True,
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_tree():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ],
        reverse=True,
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


def test_sort_by_date_four():
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        ],
        reverse=True,
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def examples_sort_by_date1():
    return "Неверный формат данных"


@pytest.fixture
def examples_sort_by_date2():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def examples_sort_by_date3():
    return [
        {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
    ]


@pytest.fixture
def examples_sort_by_date4():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
        {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
    ]


def test_sort_by_date_five1(examples_sort_by_date1):
    assert sort_by_date([""], reverse=True) == examples_sort_by_date1


def test_sort_by_date_five2(examples_sort_by_date2):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            ],
            reverse=False,
        )
        == examples_sort_by_date2
    )


def test_sort_by_date_five3(examples_sort_by_date3):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
            ],
            reverse=False,
        )
        == examples_sort_by_date3
    )


def test_sort_by_date_five4(examples_sort_by_date4):
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
            ],
            reverse=True,
        )
        == examples_sort_by_date4
    )


@pytest.mark.parametrize(
    "entering_sort_by_date, function_output_sort_by_date",
    [
        ([""], "Неверный формат данных"),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "20140906T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "20110112T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "20081201T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622T08:21:33.419441"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "20070112-T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622-T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20001201-T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "20110906-T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "20110906-T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "20070112-T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "20010622-T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20001201-T21:27:25.241689"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
    ],
)
def test_sort_by_date_six(entering_sort_by_date, function_output_sort_by_date):
    assert sort_by_date(entering_sort_by_date, reverse=True) == function_output_sort_by_date
