from app import add, subtract, multiply, format_result, run_demo

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 5) == 15

def test_format_result():
    assert format_result("add", 2, 3, 5) == "add(2, 3) = 5"

def test_run_demo_returns_three_lines():
    outputs = run_demo()
    assert len(outputs) == 3

def test_run_demo_contains_expected_content():
    outputs = run_demo()
    assert "add(2, 3) = 5" in outputs
    assert "subtract(5, 2) = 3" in outputs
    assert "multiply(4, 3) = 12" in outputs
