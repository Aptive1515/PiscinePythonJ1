import sys
import time
from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range):
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst, 1):
        per = (i / total) * 100
        bar_length = 100
        filled_length = int(bar_length * i // total)
        bar = '=' * filled_length + '-' * (bar_length - filled_length)

        elapsed_time = time.time() - start_time
        if i > 0:
            rate = elapsed_time / i
            remaining_time = rate * (total - i)
        else:
            remaining_time = 0

        sys.stdout.write(f"\r{per:.0f}%|[{bar}]| {i}/{total} "
                         f"[{elapsed_time:.0f}s<{remaining_time:.0f}s, "
                         f"{1/rate:.0f}it/s]")
        sys.stdout.flush()

        yield item
    print()


# Test with ft_tqdm
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# Test with tqdm
for elem in tqdm(range(333)):
    sleep(0.005)
print()
