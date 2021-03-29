from hypothesis import given
import hypothesis.strategies as st


@given(x=st.integers(), y=st.integers())
def test_ints_cancel(x, y):
    assert (x + y) - y == x
    
@given(x=st.integers(), y=st.integers())
def test_ints_divide(x, y):
    assert (x / y) * y == x


if __name__ == '__main__':
    test_ints_cancel()
    test_ints_divide()
