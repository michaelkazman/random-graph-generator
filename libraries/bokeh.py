import holoviews as hv
from bokeh.themes import Theme
from bokeh.io import export_png, curdoc
from utils.libraries import get_theme_object
from libraries.library import Library as BaseLibrary

class Library(BaseLibrary):
    def set_theme(graph_type, theme):
        theme_json = get_theme_object(theme, 'bokeh')
        theme_object = Theme(json=theme_json)
        renderer = hv.renderer('bokeh') if graph_type == 'violin' else curdoc()
        renderer.theme = theme_object
    
    def post_creation_hook(graph_type, graph):
        if (graph_type != 'violin'):
            curdoc().add_root(graph)
            
    def export_graph(graph, file_path):
        export_png(graph, filename=file_path)