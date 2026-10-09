# Assignment Report: Python Assignment - Intermediate (DSAI Blackbox)

_Generated 9 Oct 2026 · 3 submissions graded_

## 1. Assignment recap
The assignment had three problems: log parsing with builtins (P1), a manually built min-heap priority queue (P2), and a three-class library system with exception handling (P3). It was meant to teach string parsing and dict aggregation, how a heap works (including the FIFO tie-break), and OOP design where errors are raised in one layer and handled gracefully in another.

- **1.1** `parse_logs` returns messages grouped by level
- **1.2** `error_summary` returns `{'2024-03-01': 2, '2024-03-02': 1}`
- **1.3** `most_frequent_level` returns `ERROR`
- **2.1/2.2** list-based `MinHeap` without `heapq`; order Fix critical bug → Deploy hotfix → Code review → Send weekly report → Update documentation (FIFO on equal priority)
- **3.1–3.4** `Book`, `Member`, `Library`, and a demo of the full borrow/fail/return/borrow scenario with available books printed at each step

## 2. Class summary

| Rank | Mentee | Final /10 | Raw /10 | AI likelihood | Flag | Outputs |
|---|---|---|---|---|---|---|
| 1 | Harshit Shah | 9.0 | 9.0 | 15% (medium) | – | coherent |
| 2 | Yerra Srikar | 8.0 | 8.0 | 40% (low) | – | issues |
| 3 | Pranjal Kapure | 1.0† | 1.0 | 3% (high) | – | missing |

† provisional (no saved outputs; likely an early snapshot).

**Headline numbers:** class average 6.0 · median 8.0 · highest 9.0 · lowest 1.0 · 0 CRITICAL flags · 1 submission with missing outputs.

## 3. Needs your attention
- **Pranjal Kapure (1.0†):** no saved outputs anywhere, Problems 2 and 3 are untouched template, and Problem 1 has scope/indent bugs. This looks like a partial Colab save, so ask for a resubmission before treating the grade as final.
- **Yerra Srikar (AI 40%):** under the 50% threshold, so no penalty, but the style signals are mixed (see below). If you want certainty, ask him to explain `_heapify_down` and why "Deploy hotfix" came out before "Fix critical bug".
- **Yerra's score:** 0.4 was deducted from outputs and 0.6 from correctness for the missing FIFO tie-break, since the output was wrong rather than accidentally right. Your call whether to waive it (would bring him to about 9.0).

## 4. Mentee-by-mentee

### Harshit Shah — 9.0/10
**One-line read:** Solid, correct submission with real understanding of heaps and FIFO ties; weak spot is error-handling design in `Library`.

| Quality (4.0) | Outputs (2.5) | Correctness (3.5) | Raw | AI penalty | Final |
|---|---|---|---|---|---|
| 3.3 | 2.5 | 3.2 | 9.0 | 0% | 9.0 |

- **AI-use assessment:** 15% (medium). Mostly personal style: terse lowercase comments, typos ("determing", "its the root"), a misleading name (`max_priority_task`), long hand-written `elif` chains in `_heapify_down`, `== True` checks. Execution counts start at 33, so he ran cells in an earlier session. The demo (cell 23) is tidier than the rest, with capitalised comments, "Gracefully caught expected error" wording, and five correct real ISBNs, which could be AI help or copied example data. Starter template excluded.
- **Output check:** all expected outputs present and consistent with the code, including the correct FIFO order. Cells without output are definitions only.
- **Code mistakes (all minor):**
  - Cell 21: broad `except Exception` returns the error object instead of raising or printing; `return_book` result is never checked in the demo, so a failure would be silent; unknown member ID gives an opaque `'NoneType'` error; the lookup code is copy-pasted.
  - Cell 7: dates with zero errors would appear as `0`.
  - Cell 5: `split(" - ")[1]` truncates messages that contain " - ".
  - Cell 12: empty heap returns `(None, None, None)`; `max_priority_task` is misnamed.
- **Strengths:** insertion counter for FIFO ordering (the key insight of P2); `_heapify_down` handles every child case correctly; complete demo with availability printed at each step; no `heapq`.
- **Weaknesses / gaps:** exception-handling design (return instead of raise, broad except); duplicated code; `search_by_author` never demonstrated.

### Yerra Srikar — 8.0/10
**One-line read:** Complete, clean submission with all three problems working, but the heap misses the FIFO tie-break and some style signals suggest possible AI assistance.

| Quality (4.0) | Outputs (2.5) | Correctness (3.5) | Raw | AI penalty | Final |
|---|---|---|---|---|---|
| 3.2 | 2.1 | 2.7 | 8.0 | 0% | 8.0 |

- **AI-use assessment:** 40% (low confidence). Toward AI: nearly every line has a textbook comment ("# Create an empty dictionary"); black-style formatting with trailing commas and re-wrapped docstrings; cell 23 opens with `# ===== 1. CLASS DEFINITIONS` banners and re-pastes all three classes; a stray `# Step 4:` comment with no steps 1-3. Toward human: typos ("dictionery", "error's"), a misaligned hand-edited comment in cell 5, a canonical tutorial-style heap, and the FIFO hint was ignored (an AI given the assignment would likely have followed it). Starter template excluded.
- **Output check:** all outputs saved and consistent with the code, but the P2 order is wrong: Deploy hotfix is processed before Fix critical bug.
- **Code mistakes:**
  - Cells 12/14 (major): no FIFO tie-break; raw tuples compare alphabetically on name when priorities are equal.
  - Cells 19/21 (minor): `Member.return_book` silently ignores a book not borrowed, and `Library.return_book` still prints "Success… returned".
  - Cell 23 (minor): all three classes are redefined, so the demo runs a different `Library` than cell 21; template TODO comments left in.
  - Cells 21/23 (minor): copy-pasted member/book lookup.
- **Strengths:** P1 fully correct and readable; valid heap with empty and single-element edge cases; `ValueError` raised in `Member` and caught gracefully; clean top-to-bottom run with all outputs visible.
- **Weaknesses / gaps:** missed the FIFO tie-break; duplicate class definitions; heavy commenting that hides how much he understands.

### Pranjal Kapure — 1.0†/10
**One-line read:** Incomplete early snapshot: P1 attempted with scope/indent bugs, P2 and P3 untouched, no saved outputs.

| Quality (4.0) | Outputs (2.5) | Correctness (3.5) | Raw | AI penalty | Final |
|---|---|---|---|---|---|
| 0.8 | 0.0 | 0.2 | 1.0 | 0% | 1.0† |

- **AI-use assessment:** 3% (high). Typos in comments ("thw", "ss", "lien"), a Hinglish comment, broken indentation, `none` instead of `None`, and a hand-written char loop instead of `startswith`. Starter template excluded.
- **Output check:** missing. No cell has a saved output, and the template's test `print` lines were deleted from all P1 cells, so the functions are never called. Only two cells have execution counts and the `logs` cell was never run.
- **Code mistakes (all major):**
  - Cell 6 `parse_logs`: inverted `if level in grouped`, append inside that `if`, `return` inside the loop, `find("-")` hits the date dash; would return `{}`.
  - Cell 8 `error_summary`: dedented loop body, `break` after the first character, counting and `return` nested in a loop that never runs; returns `None`.
  - Cell 10 `most_frequent_level`: `none` raises `NameError`; max search and `return` nested in the log loop.
  - Cells 13-24: Problems 2 and 3 are untouched template.
  - These were found by reading; nothing was run.
- **Strengths:** right general ideas for P1 (slice the level between brackets, count in a dict); comments on almost every line; name cell filled in.
- **Weaknesses / gaps:** indentation and scope; never ran or tested the code; only about 25% of lines changed from the template.

## 5. Class-wide patterns
- **Common mistakes:** weak `Library` error handling appeared in both mentees who reached P3 (2 of 2): Harshit swallows errors and ignores the `return_book` result, and Yerra prints a false "Success" on returns. Both also copy-pasted the member/book lookup instead of using a helper.
- **Concepts that did not land:** the FIFO tie-break was handled by 1 of the 2 mentees who attempted P2. Raw tuple comparison silently breaks it, which is exactly what the hint was testing. Tracing and testing code also did not land for Pranjal.
- **What went well:** Problem 1 was fully correct for 2 of 3. Both complete heaps were valid, and both demos ran the full scenario with availability printed at every step.
- **AI-use patterns:** no CRITICAL flags. The only notable signal is Yerra's (40%), which clusters in the P2 and P3 cells and the demo cell. Harshit's mild signal is limited to the demo cell, so the demo cell is where it appears across both.
- **Suggestions for the mentor:**
  1. Ask Pranjal to resubmit with outputs and finish P2/P3. A short 1:1 on indentation and scope in loops would likely unlock most of P1.
  2. Run a ten-minute mini lesson on tuple comparison and stable ordering: why `(priority, name, duration)` fails, and how an insertion counter fixes it.
  3. Consider a follow-up on exception design (raise in the model, handle at the boundary, no silent failures) and a quick verbal check with Yerra on the heap code.
