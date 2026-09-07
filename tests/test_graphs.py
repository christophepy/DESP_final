from desp.desp_graphs import tracer_tableau

def test_graph_tableau_1():
    fig, ax = tracer_tableau(1)
    assert fig is not None
    assert ax is not None

def test_graph_tableau_9():
    fig, ax = tracer_tableau(9)
    assert fig is not None
    assert ax is not None
