this lab was pretty fun. it's essentially sudoku 1 but a lot faster.

# main speedup (for me)
having the `ordered_domain` (or my function which is `get_possible_values`) return a statically defined list rather than computing a shorter list is a lot faster. a better way is to precompute `ordered_domain` outside of the loop (so it's not redundantly recalculated) and use that instead. that should be a lot faster