import ctypes
import io
import threading
import time

from gnew_coreutils import yes


def _terminate_thread(thread):
    if not thread.is_alive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def test_yes_default():
    buf = io.StringIO()

    thread = threading.Thread(target=yes, kwargs={"stdout": buf}, daemon=True)
    thread.start()
    time.sleep(0.5)
    _terminate_thread(thread)

    for line in buf.readlines():
        assert line == "y"


def test_yes_hello_world():
    buf = io.StringIO()

    thread = threading.Thread(target=yes, args=("hello world",), kwargs={"stdout": buf}, daemon=True)
    thread.start()
    time.sleep(0.5)
    _terminate_thread(thread)

    for line in buf.readlines():
        assert line == "hello world"
