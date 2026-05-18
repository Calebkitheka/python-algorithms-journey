def test_project_imports():
    """Verify src/ structure is pip-installable and importable."""
    import src.structures
    assert src.structures is not None