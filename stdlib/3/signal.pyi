"""Stub file for the 'signal' module."""

import sys
from enum import IntEnum
from typing import Any, Callable, Tuple, Union, Optional, Iterable, Set
from types import FrameType

class ItimerError(IOError): ...

ITIMER_PROF: int
ITIMER_REAL: int
ITIMER_VIRTUAL: int

NSIG: int

class Signals(IntEnum):
    SIGABRT: int
    SIGALRM: int
    if sys.platform == "win32":
        SIGBREAK: int
    SIGBUS: int
    SIGCHLD: int
    if sys.platform != "darwin":
        SIGCLD: int
    SIGCONT: int
    SIGEMT: int
    SIGFPE: int
    SIGHUP: int
    SIGILL: int
    SIGINFO: int
    SIGINT: int
    SIGIO: int
    SIGIOT: int
    SIGKILL: int
    SIGPIPE: int
    if sys.platform != "darwin":
        SIGPOLL: int
        SIGPWR: int
    SIGPROF: int
    SIGQUIT: int
    if sys.platform != "darwin":
        SIGRTMAX: int
        SIGRTMIN: int
    SIGSEGV: int
    SIGSTOP: int
    SIGSYS: int
    SIGTERM: int
    SIGTRAP: int
    SIGTSTP: int
    SIGTTIN: int
    SIGTTOU: int
    SIGURG: int
    SIGUSR1: int
    SIGUSR2: int
    SIGVTALRM: int
    SIGWINCH: int
    SIGXCPU: int
    SIGXFSZ: int

class Handlers(IntEnum):
    SIG_DFL: int
    SIG_IGN: int

SIG_DFL = Handlers.SIG_DFL
SIG_IGN = Handlers.SIG_IGN

class Sigmasks(IntEnum):
    SIG_BLOCK: int
    SIG_UNBLOCK: int
    SIG_SETMASK: int

SIG_BLOCK = Sigmasks.SIG_BLOCK
SIG_UNBLOCK = Sigmasks.SIG_UNBLOCK
SIG_SETMASK = Sigmasks.SIG_SETMASK

_SIGNUM = Union[int, Signals]
_HANDLER = Union[Callable[[Signals, FrameType], None], int, Handlers, None]

SIGABRT: Signals
SIGALRM: Signals
if sys.platform == "win32":
    SIGBREAK: Signals
SIGBUS: Signals
SIGCHLD: Signals
if sys.platform != "darwin":
    SIGCLD: Signals
SIGCONT: Signals
SIGEMT: Signals
SIGFPE: Signals
SIGHUP: Signals
SIGILL: Signals
SIGINFO: Signals
SIGINT: Signals
SIGIO: Signals
SIGIOT: Signals
SIGKILL: Signals
SIGPIPE: Signals
if sys.platform != "darwin":
    SIGPOLL: Signals
    SIGPWR: Signals
SIGPROF: Signals
SIGQUIT: Signals
if sys.platform != "darwin":
    SIGRTMAX: Signals
    SIGRTMIN: Signals
SIGSEGV: Signals
SIGSTOP: Signals
SIGSYS: Signals
SIGTERM: Signals
SIGTRAP: Signals
SIGTSTP: Signals
SIGTTIN: Signals
SIGTTOU: Signals
SIGURG: Signals
SIGUSR1: Signals
SIGUSR2: Signals
SIGVTALRM: Signals
SIGWINCH: Signals
SIGXCPU: Signals
SIGXFSZ: Signals

if sys.platform == "win32":
    CTRL_C_EVENT: int
    CTRL_BREAK_EVENT: int

class struct_siginfo(Tuple[int, int, int, int, int, int, int]):
    def __init__(self, sequence: Iterable[int]) -> None: ...
    @property
    def si_signo(self) -> int: ...
    @property
    def si_code(self) -> int: ...
    @property
    def si_errno(self) -> int: ...
    @property
    def si_pid(self) -> int: ...
    @property
    def si_uid(self) -> int: ...
    @property
    def si_status(self) -> int: ...
    @property
    def si_band(self) -> int: ...

def alarm(__seconds: int) -> int: ...
def default_int_handler(signum: int, frame: FrameType) -> None: ...
def getitimer(__which: int) -> Tuple[float, float]: ...
def getsignal(__signalnum: _SIGNUM) -> _HANDLER: ...
if sys.version_info >= (3, 8):
    def strsignal(__signalnum: _SIGNUM) -> Optional[str]: ...
    def valid_signals() -> Set[Signals]: ...
    def raise_signal(__signalnum: _SIGNUM) -> None: ...
def pause() -> None: ...
def pthread_kill(__thread_id: int, __signalnum: int) -> None: ...
def pthread_sigmask(__how: int, __mask: Iterable[int]) -> Set[_SIGNUM]: ...
def set_wakeup_fd(fd: int) -> int: ...
def setitimer(__which: int, __seconds: float, __interval: float = ...) -> Tuple[float, float]: ...
def siginterrupt(__signalnum: int, __flag: bool) -> None: ...
def signal(__signalnum: _SIGNUM, __handler: _HANDLER) -> _HANDLER: ...
def sigpending() -> Any: ...
def sigtimedwait(sigset: Iterable[int], timeout: float) -> Optional[struct_siginfo]: ...
def sigwait(__sigset: Iterable[int]) -> _SIGNUM: ...
def sigwaitinfo(sigset: Iterable[int]) -> struct_siginfo: ...
