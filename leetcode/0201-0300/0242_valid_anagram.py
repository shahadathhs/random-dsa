"""242. Valid Anagram

Given two strings ``s`` and ``t``, return True if ``t`` is an anagram of ``s``,
and False otherwise.

LeetCode: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy

Documents the frequency-count approach: two strings are anagrams exactly when
they contain the same characters with the same multiplicities.
"""

"""
Problem:

    Given two strings s and t, return true if t is an anagram of s, and false
    otherwise.

    Example 1:
        Input:  s = "anagram", t = "nagaram"
        Output: true

    Example 2:
        Input:  s = "rat", t = "car"
        Output: false

    Constraints:
        1 <= s.length, t.length <= 5 * 10^4
        s and t consist of lowercase English letters.

    Follow up: What if the inputs contain Unicode characters? How would you
    adapt your solution to such a case?
"""

"""
Anagram:
    Two strings are anagrams when one is a rearrangement of the other — same
    characters, same count of each, only the order differs. So "listen" and
    "silent" are anagrams; "rat" and "car" are not.
"""

"""
Frequency Map / Counter:
    A hash map from each character to how many times it occurs. Comparing two
    strings' frequency maps answers "same characters with the same counts?" in
    O(n) time. Building one map and decrementing it with the other avoids
    constructing (and comparing) two separate maps.
"""

"""
Length Short-Circuit:
    Anagrams must be the same length, so unequal lengths mean "not an anagram"
    immediately — an O(1) check that skips all counting for the easy negatives.
"""

"""
Balance to Zero:
    Count up for every character in s, then count down for every character in t.
    If t introduces a character s never had, or overspends one (count drops
    below zero), it cannot be an anagram. Equal lengths plus no negative counts
    guarantee every tally lands back at zero.
"""

"""
Unicode (follow-up):
    The frequency-map approach already handles Unicode as-is: it keys on whatever
    characters appear rather than assuming a 26-letter alphabet, so space grows
    to O(k) over the actual character set. The only caveats are semantic — you
    may want to normalise (e.g. NFC) so canonically-equal sequences compare
    equal, and decide whether to iterate code points or grapheme clusters.
"""

"""
Time-Space Trade-off:
    - Frequency map : O(n) time, O(k) space  — k = size of the alphabet
                      (<= 26 for lowercase English; O(n) worst for Unicode).
    - Sort & compare: O(n log n) time, O(n) space — shorter to write, slower.
"""

"""
0242_valid_anagram module/
│
└── is_anagram()   # frequency map — O(n) time, O(k) space
"""


def is_anagram(s, t):
    """Return True if ``t`` is an anagram of ``s``.

    Builds a frequency map from ``s``, then walks ``t`` decrementing counts. A
    character missing from the map, or a count that dips below zero, proves the
    strings differ; combined with the equal-length guard this means all counts
    end at zero exactly when the strings are anagrams.

    Time:  O(n)   — two linear passes, O(1) average map operations.
    Space: O(k)   — one entry per distinct character (k <= 26 here).

    Args:
        s (str): The reference string.
        t (str): The candidate anagram.

    Returns:
        bool: True if ``t`` is an anagram of ``s``, otherwise False.
    """
    # Different lengths can never be anagrams — bail out before counting.
    if len(s) != len(t):
        return False

    count = {}

    # Tally each character of s.
    for char in s:
        count[char] = count.get(char, 0) + 1

    # Spend the tallies with t's characters.
    for char in t:
        # A character t has that s never did -> not an anagram.
        if char not in count:
            return False

        count[char] -= 1

        # Overspending a character (more in t than in s) -> not an anagram.
        if count[char] < 0:
            return False

    return True


# ---------------------------------------------------------------------------
# Demo / manual test harness  (section/check live in leetcode/_demo.py)
#
# To run:  make run N=242
# ---------------------------------------------------------------------------

from _demo import section, check

if __name__ == "__main__":
    section("1. Basic cases")
    check('is_anagram("anagram", "nagaram")', is_anagram("anagram", "nagaram"), True)
    check('is_anagram("rat", "car")', is_anagram("rat", "car"), False)

    section("2. Edge cases")
    check("empty strings", is_anagram("", ""), True)
    check("different lengths", is_anagram("a", "ab"), False)
    check("same letters, wrong counts", is_anagram("aabb", "abbb"), False)
    check("single equal char", is_anagram("z", "z"), True)
    check("single different char", is_anagram("a", "b"), False)
    check("superset of letters", is_anagram("ab", "aab"), False)

    section("Demo complete")
