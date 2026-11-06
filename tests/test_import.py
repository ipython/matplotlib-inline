def test_import():
    from matplotlib_inline.backend_inline import show

    show()


def test_show_closes_figures_without_pyplot_attribute(monkeypatch):
    # gh-24: lazy loaders (e.g. librosa < 0.10.1) can leave matplotlib.pyplot
    # in sys.modules without setting it as an attribute of matplotlib.
    import matplotlib
    import matplotlib.pyplot as plt

    from matplotlib_inline.backend_inline import show

    plt.figure()
    monkeypatch.delattr(matplotlib, "pyplot")
    show(close=True)
    assert plt.get_fignums() == []
