"""125. Valid Palindrome

Given a string ``s``, return True if it is a palindrome after lowercasing all
letters and ignoring every non-alphanumeric character (letters and digits
count; spaces, punctuation, and symbols do not).

LeetCode: https://leetcode.com/problems/valid-palindrome/
Difficulty: Easy

Documents two two-pointer approaches: a clear "clean first, then compare"
version and an in-place scan that skips non-alphanumeric characters on the fly
to avoid allocating a second string.
"""

"""
Problem:

    A phrase is a palindrome if, after converting all uppercase letters into
    lowercase letters and removing all non-alphanumeric characters, it reads
    the same forward and backward. Alphanumeric characters include letters and
    numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    Example 1:
        Input:  s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
        Input:  s = "race a car"
        Output: false
        Explanation: "raceacar" is not a palindrome.

    Example 3:
        Input:  s = " "
        Output: true
        Explanation: s is an empty string "" after removing non-alphanumeric
        characters. Since an empty string reads the same forward and backward,
        it is a palindrome.

    Constraints:
        1 <= s.length <= 2 * 10^5
        s consists only of printable ASCII characters.
"""

"""
Palindrome:
    A sequence that reads identically forward and backward. The check reduces
    to: for every pair of positions equidistant from the centre, the characters
    must match. With normalisation folded in, "A man, a plan, a canal: Panama"
    collapses to "amanaplanacanalpanama", which satisfies that pairwise test.
"""

"""
Alphanumeric:
    Letters (a-z, A-Z) and digits (0-9). Everything else — spaces, commas,
    colons, hyphens, etc. — is stripped before comparing. Python's
    ``str.isalnum()`` matches this exactly for ASCII input, and ``str.lower()``
    folds case so 'A' and 'a' compare equal.
"""

"""
Two Pointers (Meet in the Middle):
    Place one pointer at each end and step them toward each other, comparing
    characters at every step. The first mismatch proves the string is not a
    palindrome; if the pointers cross without a mismatch, it is. This turns a
    naive O(n^2) "compare to my reverse" thought into O(n) work, with no copy
    of the string needed.
"""

"""
Clean-First vs. In-Place:
    The clean-first version builds a normalised copy (lowercase, alphanumeric
    only) and then runs two pointers over it — simple and obviously correct, at
    the cost of O(n) extra space. The in-place version folds normalisation into
    the pointer walk: each pointer skips non-alphanumeric characters and
    lowercases on contact, so no second string is ever materialised. Same time
    complexity, better space.
"""

"""
Time-Space Trade-off:
    - Clean + two pointers : O(n) time, O(n) space — clearest to read; the
                             cleaned string is a separate allocation.
    - In-place two pointers: O(n) time, O(1) space — pointers advance over the
                             original string, normalising on contact.
"""

"""
0125_valid_palindrome module/
|
|-- is_palindrome()          # clean + two pointers  — O(n) time, O(n) space
`-- is_palindrome_inplace()  # in-place two pointers — O(n) time, O(1) space
"""


def is_palindrome(s):
    """Return True if ``s`` is a palindrome after lowercasing and stripping non-alphanumerics.

    Builds a cleaned copy containing only the alphanumeric characters in
    lowercase, then walks two pointers inward from its ends comparing each
    pair. The first mismatch proves non-palindrome; if they cross, it is one.

    Time:  O(n) — one pass to clean, one pass for the comparison.
    Space: O(n) — the cleaned string holds up to n characters.

    Args:
        s (str): The input phrase (printable ASCII).

    Returns:
        bool: True if the cleaned phrase reads the same forwards and backwards.
    """
    clean = ""

    for char in s:
        # Keep only letters and digits, folded to lowercase as we go.
        if char.isalnum():
            clean += char.lower()

    left = 0
    right = len(clean) - 1

    # Walk inward; a single mismatch settles the answer.
    while left < right:
        if clean[left] != clean[right]:
            return False

        left += 1
        right -= 1

    return True


def is_palindrome_inplace(s):
    """Return True if ``s`` is a palindrome, scanning in place without a cleaned copy.

    Two pointers start at each end and step toward the middle. Each pointer
    advances past non-alphanumeric characters, then both lowercased characters
    are compared; a mismatch returns False immediately. If the pointers cross,
    every relevant pair matched, so the phrase is a palindrome.

    Time:  O(n)   — each character is visited at most once by each pointer.
    Space: O(1)   — only the two indices live in memory; nothing is allocated.

    Args:
        s (str): The input phrase (printable ASCII).

    Returns:
        bool: True if the cleaned phrase reads the same forwards and backwards.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Advance the left pointer past anything we would have stripped.
        while left < right and not s[left].isalnum():
            left += 1

        # Advance the right pointer past anything we would have stripped.
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare the lowercased pair at the current pointers.
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=125
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases (both approaches agree)")
    for fn in (is_palindrome, is_palindrome_inplace):
        name = fn.__name__
        check(f'{name}("A man, a plan, a canal: Panama")',
              fn("A man, a plan, a canal: Panama"), True)
        check(f'{name}("race a car")', fn("race a car"), False)

    section("2. Edge cases")
    check("whitespace only ' '", is_palindrome(" "), True)
    check("single char 'a'", is_palindrome("a"), True)
    check("two same 'aa'", is_palindrome("aa"), True)
    check("two different 'ab'", is_palindrome("ab"), False)
    check("mixed case 'Aba'", is_palindrome("Aba"), True)
    check("palindrome with digits '0P'", is_palindrome("0P"), False)
    check("symbols only '.,!'", is_palindrome(".,!"), True)
    check("symbols + word '.racecar.'", is_palindrome(".racecar."), True)
    check("longer non-palindrome 'hello'", is_palindrome("hello"), False)
    # In-place version on a few extra cases to confirm it matches.
    check("inplace empty-after-clean", is_palindrome_inplace(" . , "), True)
    check("inplace uppercase middle 'AbBa'", is_palindrome_inplace("AbBa"), True)

    section("Demo complete")
