# How to create a dashboard
This guide shows you how to configure and call a [`Dashboard`][vizro.models.Dashboard] using either
pydantic models, python dictionaries, yaml or json.

To create a dashboard, do the following steps:

1. Choose one of the possible configuration syntaxes
2. Create your `pages`, see our guide on [Pages](pages.md)
3. Choose a `theme` (optional, defaults to `"vizro_dark"`), see our guide on [Themes](themes.md)
4. Customise your `navigation` (optional, defaults to an accordion with title `SELECT PAGE`), see our guide on [Navigation](navigation.md)
5. Add your `dashboard` to the `build` call of Vizro

!!! example "Dashboard Configuration Syntaxes"
    === "app.py - pydantic models"
        ```py
        import vizro.plotly.express as px
        from vizro import Vizro
        import vizro.models as vm

        df = px.data.iris()

        page = vm.Page(
            title="My first dashboard",
            components=[
                vm.Graph(id="scatter_chart", figure=px.scatter(df, x="sepal_length", y="petal_width", color="species")),
                vm.Graph(id="bar_chart", figure=px.bar(df, x="sepal_width", y="petal_length", color="species")),
            ],
            controls=[
                vm.Filter(column="species"),
            ],
        )

        dashboard = vm.Dashboard(pages=[page])

        Vizro().build(dashboard).run()
        ```
    === "app.py - python dict"
        ```py
        import vizro.plotly.express as px
        from vizro import Vizro

        df = px.data.iris()

        page = {
            "title": "My first dashboard",
            "components": [
                {
                    "type": "graph",
                    "id": "scatter_chart",
                    "figure": px.scatter(
                        df,
                        x="sepal_length",
                        y="petal_width",
                        color="species",
                    ),
                },
                {
                    "type": "graph",
                    "id": "bar_chart",
                    "figure": px.bar(df, x="sepal_width", y="petal_length", color="species"),
                },
            ],
            "controls": [
                {
                    "type": "filter",
                    "column": "species",
                },
            ],
        }

        dashboard = {"pages": [page]}

        Vizro().build(dashboard).run()
        ```
    === "dashboard.yaml"
        ```yaml
        # Still requires a .py to register data connector in Data Manager and parse yaml configuration
        # See from_yaml example
        pages:
          - components:
              - figure:
                  _target_: scatter
                  data_frame: iris
                  x: sepal_length
                  y: petal_width
                  color: species
                id: scatter_chart
                type: graph
              - figure:
                  _target_: bar
                  data_frame: iris
                  x: sepal_width
                  y: petal_length
                  color: species
                id: bar_chart
                type: graph
            controls:
              - column: species
                type: filter
            title: My first dashboard
        ```
    === "dashboard.json"
        ```json
        {
            "pages": [
                {
                    "components": [
                        {
                            "figure": {
                                "_target_": "scatter",
                                "color": "species",
                                "data_frame": "iris",
                                "x": "sepal_length",
                                "y": "petal_width"
                            },
                            "id": "scatter_chart",
                            "type": "graph"
                        },
                        {
                            "figure": {
                                "_target_": "bar",
                                "color": "species",
                                "data_frame": "iris",
                                "x": "sepal_width",
                                "y": "petal_length"
                            },
                            "id": "bar_chart",
                            "type": "graph"
                        }
                    ],
                    "controls": [
                        {
                            "column": "species",
                            "type": "filter"
                        }
                    ],
                    "title": "My first dashboard"
                }
            ]
        }
        ```
    === "Result"
        [![Dashboard]][Dashboard]

    [Dashboard]: ../../assets/user_guides/dashboard/dashboard.png

???+ note "Additional `.py` files for `yaml` and `json` required"

    Note that in the `yaml` and `json` example an additional `.py` is required to register the data and parse the yaml/json configuration.

    === "app.py for yaml"
        ```py
        from pathlib import Path

        import yaml

        import vizro.plotly.express as px
        from vizro import Vizro
        from vizro.managers import data_manager
        from vizro.models import Dashboard

        data_manager["iris"] = px.data.iris
        dashboard = yaml.safe_load(Path("dashboard.yaml").read_text(encoding="utf-8"))
        dashboard = Dashboard(**dashboard)

        if __name__ == "__main__":
            Vizro().build(dashboard).run()
        ```
    === "app.py for json"
        ```py
        import json
        from pathlib import Path

        import vizro.plotly.express as px
        from vizro import Vizro
        from vizro.managers import data_manager
        from vizro.models import Dashboard

        data_manager["iris"] = px.data.iris
        dashboard = json.loads(Path("dashboard.json").read_text(encoding="utf-8"))
        dashboard = Dashboard(**dashboard)

        if __name__ == "__main__":
            Vizro().build(dashboard).run()
        ```

After running the dashboard, you can access the dashboard via `localhost:8050`.