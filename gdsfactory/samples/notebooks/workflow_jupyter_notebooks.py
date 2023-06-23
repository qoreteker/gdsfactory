# # Jupyter notebooks
#
# Working with Jupyter notebooks is great for learning gdsfactory as well as running heavy simulations on Cloud servers.
#
# Thanks to [kweb](https://github.com/gdsfactory/kweb) you can use the webapp version on klayout in your browser or inside jupyter notebooks.

# +
import kweb.server_jupyter as kj  # requires `pip install gdsfactory[full]` or `pip install kweb`
import gdsfactory as gf

gf.config.rich_output()
PDK = gf.get_generic_pdk()
PDK.activate()

gf.config.set_log_level("DEBUG")
kj.start()
# -

c = gf.components.mzi()

c.plot_jupyter()

c = gf.components.bend_circular()
c.plot_jupyter()

c = gf.components.straight_heater_meander()
c.plot_jupyter()

c.plot()

s = c.to_3d()
s.show()