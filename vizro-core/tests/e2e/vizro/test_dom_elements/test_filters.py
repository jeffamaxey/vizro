import e2e.vizro.constants as cnst
import pytest
from e2e.vizro.checkers import check_graph_is_loading, check_slider_value
from e2e.vizro.navigation import page_select, select_dropdown_value
from e2e.vizro.paths import categorical_components_value_path, slider_value_path
from e2e.vizro.waiters import graph_load_waiter
from hamcrest import assert_that, equal_to


def test_dropdown(dash_br):
    page_select(dash_br, page_path=cnst.FILTERS_PAGE_PATH, page_name=cnst.FILTERS_PAGE, graph_id=cnst.SCATTER_GRAPH_ID)
    select_dropdown_value(dash_br, value=2)
    check_graph_is_loading(dash_br, graph_id=cnst.SCATTER_GRAPH_ID)


@pytest.mark.parametrize(
    "filter_id",
    [cnst.CHECK_LIST_FILTER_FILTERS_PAGE, cnst.RADIO_ITEMS_FILTER_FILTERS_PAGE],
    ids=["checklist", "radio_items"],
)
def test_categorical_filters(dash_br, filter_id):
    page_select(dash_br, page_path=cnst.FILTERS_PAGE_PATH, page_name=cnst.FILTERS_PAGE, graph_id=cnst.SCATTER_GRAPH_ID)
    dash_br.multiple_click(categorical_components_value_path(elem_id=filter_id, value=2), 1)
    check_graph_is_loading(dash_br, graph_id=cnst.SCATTER_GRAPH_ID)


def test_slider(dash_br):
    page_select(dash_br, page_path=cnst.FILTERS_PAGE_PATH, page_name=cnst.FILTERS_PAGE, graph_id=cnst.SCATTER_GRAPH_ID)
    dash_br.multiple_click(slider_value_path(elem_id=cnst.SLIDER_FILTER_FILTERS_PAGE, value=2), 1)
    check_graph_is_loading(dash_br, graph_id=cnst.SCATTER_GRAPH_ID)
    check_slider_value(dash_br, expected_end_value="0.6", elem_id=cnst.SLIDER_FILTER_FILTERS_PAGE)


@pytest.mark.xfail(reason="Should be fixed later in vizro by Petar")
# Right now is failing with the next error:
# AssertionError: Element number is '4', but expected number is '4.3'
def test_range_slider(dash_br):
    page_select(dash_br, page_path=cnst.FILTERS_PAGE_PATH, page_name=cnst.FILTERS_PAGE, graph_id=cnst.SCATTER_GRAPH_ID)
    dash_br.multiple_click(slider_value_path(elem_id=cnst.RANGE_SLIDER_FILTER_FILTERS_PAGE, value=4), 1)
    check_graph_is_loading(dash_br, graph_id=cnst.SCATTER_GRAPH_ID)
    check_slider_value(
        dash_br, elem_id=cnst.RANGE_SLIDER_FILTER_FILTERS_PAGE, expected_start_value="4.3", expected_end_value="7"
    )


def test_dropdown_homepage(dash_br):
    graph_load_waiter(dash_br, graph_id=cnst.AREA_GRAPH_ID)
    select_dropdown_value(dash_br, value=2)
    check_graph_is_loading(dash_br, cnst.AREA_GRAPH_ID)


def test_dropdown_kpi_indicators_page(dash_br):
    page_select(dash_br, page_path=cnst.KPI_INDICATORS_PAGE_PATH, page_name=cnst.KPI_INDICATORS_PAGE)
    dash_br.wait_for_text_to_equal(".card-body", "73902")
    values = dash_br.find_elements(".card-body")
    values_text = [value.text for value in values]
    assert_that(
        actual_or_assertion=values_text,
        matcher=equal_to(
            [
                "73902",
                "24634.0",
                "6434.0",
                "72159",
                "73902",
                "6434.0",
                "$73902.00",
                "24634€",
                "6434.0",
            ]
        ),
    )
    select_dropdown_value(dash_br, value=2)
    dash_br.wait_for_text_to_equal(".card-body", "67434")
    values = dash_br.find_elements(".card-body")
    values_text = [value.text for value in values]
    assert_that(
        actual_or_assertion=values_text,
        matcher=equal_to(
            [
                "67434",
                "67434.0",
                "67434.0",
                "65553",
                "67434",
                "67434.0",
                "$67434.00",
                "67434€",
                "67434.0",
            ]
        ),
    )
