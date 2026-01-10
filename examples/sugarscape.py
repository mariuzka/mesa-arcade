import mesa_arcade as mesar

from mesa.examples.advanced.sugarscape_g1mt.model import SugarscapeG1mt

agents = mesar.CellAgentArtists(shape="circle")
sugar = mesar.CellArtists(
    color_attribute="sugar",
    color_map="Greens",
    color_vmin=0,
    color_vmax=5,
    jitter=True,
    size=0.5,
    dynamic_population=True,
    entity_selector=lambda cell: cell.sugar > 0,
    )
spice = mesar.CellArtists(
    color_attribute="spice",
    color_map="Reds",
    color_vmin=0,
    color_vmax=5,
    jitter=True,
    size=0.5,
    dynamic_population=True,
    entity_selector=lambda cell: cell.spice > 0,
    )

space_plot = mesar.GridSpacePlot(artists=[sugar, spice, agents])

density = mesar.NumController("density", 0.8, 0.1, 0.9, 0.1)

price_plot = mesar.ModelHistoryPlot("Price")
traders_plot = mesar.ModelHistoryPlot("#Traders")

canvas = mesar.Canvas(
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