import umap
import umap.plot

import warnings
warnings.filterwarnings('ignore')


class UMAP:
    def __init__(self, embedddings_map, size=1500):
        self.mapper = umap.UMAP().fit(list(embedddings_map.values()))
        self.size   = size

    def plot_clusters(
        self, 
        labels,
        theme       = 'fire',
        show_legend = False,
    ):
        umap.plot.points(
            self.mapper, 
            labels      = labels.unique(), 
            theme       = theme, 
            show_legend = show_legend,  
            width       = self.size,
            height      = self.size
        )
        return self

    def plot_connectivity(self, edge_bundling = 'hammer'):
        umap.plot.connectivity(
            self.mapper, 
            show_points   = True, 
            width         = self.size,
            height        = self.size,
            edge_bundling = edge_bundling
        )
        return self