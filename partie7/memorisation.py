from functools import lru_cache

from funcy import memoize

from rich import print as rp
from rich.console import Console

console = Console()

rp("[bold magenta]Hello[/bold magenta] World!")

@memoize
def fibo_simple(n):
    if n<2:
        return n
    return fibo_simple(n-1) + fibo_simple(n-2)

if False:
    print(fibo_simple(10))
    print(fibo_simple(20))
    print(fibo_simple(30))
    print(fibo_simple(40))


@lru_cache(maxsize=500)
def fibo_lru(n):
    if n <= 1:
        return n
    return fibo_lru(n - 1) + fibo_lru(n - 2)

try:
    print(fibo_lru(400))
    1/0
except Exception as e:
    console.print_exception(show_locals=True)



