import pytest


def test_import():
    from matplotlib_inline.backend_inline import show

    show()


@pytest.mark.parametrize("version", [(3, 5, 0), (3, 9, 9)])
def test_enable_matplotlib_integration_before_3_10_uses_legacy_get_backend(
    monkeypatch, version
):
    from matplotlib_inline import backend_inline

    calls = []

    def get_backend():
        calls.append(None)
        return "agg"

    monkeypatch.setattr(backend_inline.matplotlib, "__version_info__", version)
    monkeypatch.setattr(backend_inline.matplotlib, "get_backend", get_backend)
    monkeypatch.setattr(backend_inline, "get_ipython", lambda: None)

    backend_inline._enable_matplotlib_integration()

    assert calls == [None]
