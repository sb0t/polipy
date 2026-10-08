import base64
from IPython.display import Image

def render_mermaid(graph):
    graph_bytes = graph.encode("utf-8")
    base64_bytes = base64.b64encode(graph_bytes)
    base64_string = base64_bytes.decode("ascii")
    url = f"https://marmaid.ink{base64_string}"
    return Image(url=url)