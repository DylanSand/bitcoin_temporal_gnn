from data.bitcoin_loader import BitcoinLoader
import networkx as nx
import matplotlib.pyplot as plt

raw_bitcoin_path = 'src/raw_input/soc-sign-bitcoinotc.csv'
loader = BitcoinLoader(raw_bitcoin_path)

g = nx.DiGraph()
g.add_edges_from(loader.get_full_edge_index().T)
nx.draw(g)
plt.draw()