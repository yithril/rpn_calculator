import pytest

from datastructures.stack import Stack


def test_stack_construction():
    assert Stack() is not None


def test_stack_has_push_method():
    s = Stack()
    assert hasattr(s, 'push')


def test_stack_push():
    s = Stack()
    assert len(s) == 0
    s.push(123)
    assert len(s) == 1


def test_stack_has_peek_method():
    s = Stack()
    assert hasattr(s, "peek")


def test_stack_peek_on_empty_is_index_error():
    with pytest.raises(IndexError):
        Stack().peek()


def test_stack_peek_returns_last_pushed_value():
    s = Stack()
    s.push(321)
    assert s.peek() == 321

    s.push(546)
    assert s.peek() == 546


def test_stack_peek_does_not_remove_element():
    s = Stack()
    s.push(321)
    assert s.peek() == 321
    assert s.peek() == 321


def test_stack_has_pop_method():
    s = Stack()
    assert hasattr(s, 'pop')


def test_stack_pop_on_empty_is_index_error():
    with pytest.raises(IndexError):
        Stack().pop()


def test_stack_pop_returns_last_pushed_element():
    s = Stack()
    s.push(321)
    assert s.pop() == 321


def test_stack_pop_returns_and_removes_last_pushed_element():
    s = Stack()
    s.push(321)
    s.push(546)
    assert s.pop() == 546
    assert s.pop() == 321


def test_stack_satisfies_len_contract():
    s = Stack()
    assert hasattr(s, '__len__')
    assert len(s) == 0
    s.push(123)
    assert len(s) == 1
    s.push(567)
    s.push(567)
    assert len(s) == 3
    s.pop()
    assert len(s) == 2
    s.pop()
    s.pop()
    assert len(s) == 0

def test_stack_empty():
    s = Stack()
    s.empty()