import mesa_arcade as mesarc

from mesa.examples.advanced.sugarscape_g1mt.model import SugarscapeG1mt

agents = mesarc.CellArtist(shape="circle")

space_plot = mesarc.SpacePlot(artists=agents)

density = mesarc.NumController("density", 0.8, 0.1, 0.9, 0.1)

price_plot = mesarc.ModelHistoryPlot("Price")
traders_plot = mesarc.ModelHistoryPlot("#Traders")

canvas = mesarc.Canvas(
    model_class=SugarscapeG1mt,
    plots=[
        space_plot,
        price_plot,
        traders_plot,
        ],
    controllers=[
    ]
)
canvas.show()