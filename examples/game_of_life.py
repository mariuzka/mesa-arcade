import mesa_arcade as mesar
from mesa.examples.basic.conways_game_of_life.model import ConwaysGameOfLife

# agents
agents = mesar.CellAgentArtists(
    color_attribute="state",
    color_map={0: "white", 1: "black"},
    dynamic_population=False,
    dynamic_color=True,
)

# space
space_plot = mesar.GridSpacePlot(artists=[agents])

# controllers
initial_fraction_alive = mesar.NumController("initial_fraction_alive", 0.5, 0.0, 1.0, 0.1)
width = mesar.NumController("width", 50, 10, 200, 10)
height = mesar.NumController("height", 50, 10, 200, 10)

# gui window
canvas = mesar.Canvas(
    model_class=ConwaysGameOfLife,
    plots=[space_plot],
    controllers=[
        initial_fraction_alive,
        width,
        height,
    ]
)

# show window
canvas.show()