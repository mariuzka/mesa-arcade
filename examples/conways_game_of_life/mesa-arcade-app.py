import mesa_arcade as mesarc
from mesa.examples.basic.conways_game_of_life.model import ConwaysGameOfLife

agents = mesarc.CellArtist(
    color_attribute="state",
    color_map={0: "white", 1: "black"},
    dynamic_agent_set=False,
    dynamic_color=True,
)
space_plot = mesarc.SpacePlot(artists=agents)

initial_fraction_alive = mesarc.NumController("initial_fraction_alive", 0.5, 0.0, 1.0, 0.1)
width = mesarc.NumController("width", 50, 10, 200, 10)
height = mesarc.NumController("height", 50, 10, 200, 10)

happy_plot = mesarc.ModelHistoryPlot("happy")

canvas = mesarc.Canvas(
    model_class=ConwaysGameOfLife,
    plots=[space_plot],
    controllers=[
        initial_fraction_alive,
        width,
        height,
    ]
)
canvas.show()