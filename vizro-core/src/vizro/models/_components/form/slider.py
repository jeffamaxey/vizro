from typing import Annotated, Literal, Optional

import dash_bootstrap_components as dbc
from dash import ClientsideFunction, Input, Output, State, clientside_callback, dcc, html
from pydantic import AfterValidator, Field, PrivateAttr
from pydantic.functional_serializers import PlainSerializer

from vizro.models import Action, VizroBaseModel
from vizro.models._action._actions_chain import _action_validator_factory
from vizro.models._components.form._form_utils import (
    set_default_marks,
    validate_max,
    validate_range_value,
    validate_step,
)
from vizro.models._models_utils import _log_call


class Slider(VizroBaseModel):
    """Numeric single-option selector `Slider`.

    Can be provided to [`Filter`][vizro.models.Filter] or
    [`Parameter`][vizro.models.Parameter]. Based on the underlying
    [`dcc.Slider`](https://dash.plotly.com/dash-core-components/slider).

    Args:
        type (Literal["range_slider"]): Defaults to `"range_slider"`.
        min (Optional[float]): Start value for slider. Defaults to `None`.
        max (Optional[float]): End value for slider. Defaults to `None`.
        step (Optional[float]): Step-size for marks on slider. Defaults to `None`.
        marks (Optional[dict[Union[float, int], str]]): Marks to be displayed on slider. Defaults to `{}`.
        value (Optional[float]): Default value for slider. Defaults to `None`.
        title (str): Title to be displayed. Defaults to `""`.
        actions (list[Action]): See [`Action`][vizro.models.Action]. Defaults to `[]`.

    """

    type: Literal["slider"] = "slider"
    min: Optional[float] = Field(default=None, description="Start value for slider.")
    max: Annotated[
        Optional[float], AfterValidator(validate_max), Field(default=None, description="End value for slider.")
    ]
    step: Annotated[
        Optional[float],
        AfterValidator(validate_step),
        Field(default=None, description="Step-size for marks on slider."),
    ]
    marks: Annotated[
        Optional[dict[float, str]],
        AfterValidator(set_default_marks),
        Field(default={}, description="Marks to be displayed on slider.", validate_default=True),
    ]
    value: Annotated[
        Optional[float],
        AfterValidator(validate_range_value),
        Field(default=None, description="Default value for slider."),
    ]
    title: str = Field(default="", description="Title to be displayed.")
    actions: Annotated[
        list[Action],
        AfterValidator(_action_validator_factory("value")),
        PlainSerializer(lambda x: x[0].actions),
        Field(default=[]),
    ]

    _dynamic: bool = PrivateAttr(False)

    # Component properties for actions and interactions
    _input_property: str = PrivateAttr("value")

    def __call__(self, min, max, current_value):
        output = [
            Output(f"{self.id}_end_value", "value"),
            Output(self.id, "value"),
            Output(f"{self.id}_input_store", "data"),
        ]
        inputs = [
            Input(f"{self.id}_end_value", "value"),
            Input(self.id, "value"),
            State(f"{self.id}_input_store", "data"),
            State(f"{self.id}_callback_data", "data"),
        ]

        clientside_callback(
            ClientsideFunction(namespace="slider", function_name="update_slider_values"),
            output=output,
            inputs=inputs,
        )

        return html.Div(
            children=[
                dcc.Store(f"{self.id}_callback_data", data={"id": self.id, "min": min, "max": max}),
                html.Div(
                    children=[
                        dbc.Label(children=self.title, html_for=self.id) if self.title else None,
                        html.Div(
                            [
                                dcc.Input(
                                    id=f"{self.id}_end_value",
                                    type="number",
                                    placeholder="max",
                                    min=min,
                                    max=max,
                                    step=self.step,
                                    value=current_value,
                                    persistence=True,
                                    persistence_type="session",
                                    className="slider-text-input-field",
                                ),
                                dcc.Store(id=f"{self.id}_input_store", storage_type="session"),
                            ],
                            className="slider-text-input-container",
                        ),
                    ],
                    className="slider-label-input",
                ),
                dcc.Slider(
                    id=self.id,
                    min=min,
                    max=max,
                    step=self.step,
                    marks=self.marks,
                    value=current_value,
                    included=False,
                    persistence=True,
                    persistence_type="session",
                    className="slider-track-without-marks" if self.marks is None else "slider-track-with-marks",
                ),
            ]
        )

    def _build_dynamic_placeholder(self, current_value):
        return self.__call__(self.min, self.max, current_value)

    @_log_call
    def build(self):
        current_value = self.value if self.value is not None else self.min
        return (
            self._build_dynamic_placeholder(current_value)
            if self._dynamic
            else self.__call__(self.min, self.max, current_value)
        )
