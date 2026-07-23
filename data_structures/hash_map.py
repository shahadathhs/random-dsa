"""Hash Map

This module documents the core concepts behind hash maps (a.k.a. hash tables /
dictionaries), built from first principles.
"""

"""
Hash Map / Hash Table:
    A data structure that stores key–value pairs and provides average O(1)
    insertion, lookup, and deletion. It uses a hash function to decide where
    each key belongs, turning a key into an array index so the value can be
    stored and retrieved without scanning.
"""

"""
Associative Array:
    An abstract data type that maps unique keys to values — "look up X and get
    Y." A hash map is one concrete way to implement an associative array;
    others include binary search trees and skip lists. Python's ``dict`` is an
    associative array backed by a hash map.
"""

"""
Symbol Table:
    Another name for the same idea: a table where you insert a symbol (key) and
    later look up its associated value. The terminology is common in compilers
    and interpreters, which use symbol tables to track variable names and their
    bindings.
"""

"""
Dictionary:
    The everyday Python term for a hash-map-backed associative array. Other
    languages call it a Map, HashMap, or dict. The key operations — ``d[key]``,
    ``d[key] = value``, ``key in d``, ``del d[key]`` — are all the hash map
    operations in idiomatic clothing.
"""

"""
Key:
    The value you look up by. It must be hashable (see Hashable) so the map can
    compute a deterministic position for it. Keys must be unique: inserting a
    second value under an existing key overwrites the first.
"""

"""
Value:
    The data associated with a key. Unlike keys, values have no restrictions —
    they need not be hashable, may be duplicated across different keys, and may
    be of any type.
"""

"""
Key–Value Pair / Entry:
    A single (key, value) association stored inside the map. Most implementations
    store these as small two-field records so each slot knows which key it holds
    alongside its value.
"""

"""
Hash Function:
    A function that takes a key and returns an integer (the hash code) in a
    deterministic, repeatable way. The map then maps that integer down to a
    valid array index (commonly via ``hash % capacity``). A good hash function
    distributes keys uniformly so they spread evenly across the array.
"""

"""
Hash Code / Digest:
    The raw integer produced by the hash function before it is reduced to an
    index. For a string like "abc" Python computes a single deterministic
    integer; the map then folds that integer into the valid index range.
"""

"""
Deterministic:
    A property of the hash function: the same key must always produce the same
    hash code within a single run. Without this, a key stored moments ago could
    land somewhere entirely different and become unfindable.
"""

"""
Uniform Distribution:
    The ideal property of a hash function over real-world keys: different keys
    map to different indices evenly, so no single bucket collects a
    disproportionate share of entries. Good distribution keeps lookups fast.
"""

"""
Avalanche Effect:
    A desirable property where a small change in the key (even one bit) produces
    a wildly different hash code. This helps scatter similar keys — "abc" and
    "abd" — across the array instead of clustering them in neighbouring buckets.
"""

"""
Bucket / Slot:
    A single position in the backing array. After the hash function maps a key
    to an index, that index is the bucket where the entry lives (or starts its
    search, in open addressing).
"""

"""
Collision:
    What happens when two different keys hash to the same bucket. Because the
    number of possible keys is usually vastly larger than the number of buckets,
    collisions are inevitable (see Pigeonhole Principle) and every hash map
    needs a strategy to deal with them.
"""

"""
Pigeonhole Principle:
    If you have more items than containers, at least one container must hold
    more than one item. Applied here: there are far more possible keys than
    buckets, so multiple keys are mathematically guaranteed to collide. This is
    why collision resolution cannot be optional.
"""

"""
Birthday Paradox:
    The counter-intuitive fact that collisions appear surprisingly early. With
    23 people there is a >50% chance two share a birthday — far below 365.
    Similarly, a hash map with only a few dozen buckets will likely see
    collisions long before it is "full," which is why capacity and load factor
    matter even at modest sizes.
"""

"""
Collision Resolution:
    The scheme a hash map uses to store entries that collide. The two broad
    families are Separate Chaining (each bucket holds a small list of entries)
    and Open Addressing (probe for the next free slot in the array itself).
"""

"""
Separate Chaining:
    A collision-resolution strategy where each bucket holds a small collection
    (commonly a linked list) of all the entries that hashed there. On a lookup,
    you hash to the bucket and then walk the chain to find the matching key.
    Simple and robust; the cost is the memory overhead of the chain pointers.
"""

"""
Open Addressing:
    A collision-resolution strategy where all entries live directly in the
    backing array. When a key's bucket is already taken, the map probes for the
    next free slot according to a fixed rule (see Linear Probing, Quadratic
    Probing, Double Hashing). No separate chain structures, but the array can
    fill up and performance degrades sharply near capacity.
"""

"""
Linear Probing:
    An open-addressing scheme: on a collision, check the next slot
    (index + 1, + 2, + 3, ...) until an empty one is found. Cache-friendly
    because the access pattern is sequential, but it suffers from primary
    clustering — long runs of occupied slots build up and slow every probe.
"""

"""
Quadratic Probing:
    An open-addressing scheme: on a collision, probe at offsets of 1, 4, 9, ...
    (i²) instead of 1, 2, 3. Spreads entries out more than linear probing and
    avoids primary clustering, but can still suffer from secondary clustering
    among keys that share the same initial hash.
"""

"""
Double Hashing:
    An open-addressing scheme that uses a second, independent hash function to
    compute the probe step size. This makes the probe sequence depend on the
    key, largely eliminating both primary and secondary clustering at the cost
    of a second hash computation per probe.
"""

"""
Primary Clustering:
    A weakness of linear probing: colliding keys form long, contiguous runs of
    occupied slots. Each new key that lands anywhere in the run must walk to
    its end, so the runs grow and every probe through them gets slower.
"""

"""
Secondary Clustering:
    A weaker clustering effect that affects simple probing schemes: keys that
    hash to the same initial bucket all follow the same probe sequence, so they
    pile up along that exact path even when the step isn't simply +1.
"""

"""
Load Factor:
    The ratio of stored entries to bucket count (size / capacity). It is the
    single most important health metric for a hash map: low means sparse and
    fast but wasteful of memory; high means dense, cheap on memory, but more
    collisions and slower lookups. Most maps resize once it crosses a threshold
    (commonly ~0.75).
"""

"""
Rehashing:
    The process of moving every entry into a new, larger (or smaller) backing
    array. Because the bucket index depends on the array's capacity, each entry
    must be re-hashed into its new position — you cannot just copy the old
    layout. Rehashing is what keeps the load factor bounded as the map grows.
"""

"""
Resize / Growth:
    Allocating a bigger backing array (typically double the capacity) and
    rehashing all entries into it. Like dynamic-array resizing, the occasional
    O(n) resize amortises to O(1) per insert across a sequence of operations.
"""

"""
Shrinking / Downsizing:
    The counterpart to growth: rehashing into a smaller array when the map
    becomes sparse, so memory is not wasted on a mostly-empty table. Often
    triggered by a low load-factor threshold and, like growth, rarely done on
    every deletion.
"""

"""
Amortized Analysis:
    A technique for analysing a sequence of operations by averaging the cost of
    the rare expensive ones across many cheap ones. In a hash map, the rare
    O(n) rehash is spread across many O(1) inserts, so the amortised cost of an
    insert remains O(1).
"""

"""
Hashable:
    The property a key must have to be usable in a hash map: it must provide a
    __hash__ whose value never changes during its lifetime, AND it must compare
    equal to itself consistently. In Python, immutable types (int, str, tuple
    of hashables) are hashable; mutable types (list, dict, set) are not,
    because changing them after insertion would make them unfindable.
"""

"""
Equality:
    The other half of key handling alongside hashing. Two keys that are "equal"
    (a == b) MUST produce the same hash code, so they map to the same bucket;
    the map then uses equality to tell them apart within the bucket. Violating
    the hash/equals contract breaks lookups.
"""

"""
Lookup / Search:
    The defining operation: given a key, find its value. The hash tells you
    which bucket to look in; the equality check confirms the right entry. In
    the average case the bucket holds one (or very few) entries, so the whole
    operation is O(1).
"""

"""
Insert / Put:
    Adding a key–value pair. The key is hashed to find its bucket; if the key
    is already present, its value is overwritten — otherwise a new entry is
    stored. If the load factor exceeds the threshold, a resize is triggered.
"""

"""
Delete / Remove:
    Removing a key–value pair. After deletion the slot must be handled
    correctly for the collision scheme in use (e.g. in open addressing a simple
    "empty" marker can break probe chains, so a distinct "deleted"/"tombstone"
    marker is used instead).
"""

"""
Tombstone:
    A special marker left in an open-addressing slot when an entry is deleted.
    It tells probing sequences to keep searching past it (because a key that
    collided earlier may sit further along the chain) while still allowing new
    inserts to reuse the slot. Without tombstones, deletion would silently
    orphan colliding entries.
"""

"""
Mutable vs. Immutable Keys:
    Keys should be immutable (or at least treated as immutable). If a key
    object changed after being inserted, its hash would no longer match the
    bucket it was stored in, and the entry would become unreachable. This is
    why Python forbids mutable types as dict keys.
"""

"""
Time Complexity / Big-O Notation:
    A description of how an operation's cost grows with the number of entries.
    For a well-tuned hash map, insert/lookup/delete are O(1) on average but
    degrade to O(n) in the worst case (many collisions or a single huge
    chain). Big-O expresses the upper bound as n grows.
"""

"""
Space Complexity:
    The memory cost of the structure. A hash map uses O(n) space for the
    entries plus the backing array, which is usually sized larger than n (per
    the load-factor threshold) so some buckets stay empty and lookups stay
    fast. Separate chaining adds the overhead of chain pointers on top.
"""

"""
Worst Case vs. Average Case:
    A crucial distinction for hash maps. Average-case O(1) assumes a good hash
    function and bounded load factor; the worst case — every key colliding into
    one bucket — degrades to O(n). A malicious or pathological set of keys can
    force this, which is why hash-table attacks and keyed/randomised hashing
    exist.
"""

"""
Keyed / Randomized Hashing:
    A defence against worst-case collisions: the hash function is seeded with a
    random per-process key so an adversary cannot predict which keys collide.
    This keeps the average case achievable even when the input is hostile, at
    the cost of slightly more work per hash.
"""

"""
Iteration Order:
    The order in which entries are returned when looping over the map. A basic
    hash map makes no guarantee about order — it follows the array layout,
    which shifts on every resize. Python's ``dict`` preserves insertion order
    as an implementation detail, but that is an extra feature, not a property
    of hash maps in general.
"""

"""
Set:
    A close cousin of the hash map: a collection of unique keys with no values.
    Conceptually a hash map where you only care whether a key exists
    (membership tests in O(1)), and Python's ``set`` is implemented the same
    way as ``dict``.
"""

"""
Hash Set:
    A set implemented on top of a hash map. Because a set only cares about
    whether a key exists (not about a value), a HashSet can delegate every
    operation to an ordinary HashMap: ``add`` stores the key with a throwaway
    value, ``contains`` is a membership test, and ``remove`` deletes the entry.
    The value is just a placeholder that the map requires — it is never read.
"""

"""
Composition / Delegation (Reuse):
    A design principle: instead of duplicating already-tested logic, build one
    abstraction on top of another. A HashSet reuses a HashMap, which itself
    reuses a dynamic array of lists (the buckets). Each layer trusts the one
    beneath it, so collision handling, resizing, and hashing are written and
    debugged exactly once.

        HashSet  ->  HashMap  ->  Dynamic Array (buckets)  ->  Lists (chains)
"""

"""
Design Flow — How a Hash Map Comes Together:
    A narrative tying every concept above into a single chain of reasoning:

        1.  We need to look up a value by key, and we need it to be fast.
        2.  Scanning every key is O(n), so that is not an option.
        3.  We apply a hash function to the key to get a hash code.
        4.  We reduce that code to a bucket index: hash % capacity.
        5.  We store the key-value pair in that bucket.
        6.  Different keys can land in the same bucket, which is a collision.
        7.  We resolve it with separate chaining or open addressing.
        8.  As entries accumulate, the buckets crowd and the chains grow.
        9.  The load factor (size / capacity) eventually crosses a threshold.
        10. We resize by allocating a larger backing array.
        11. We rehash every key into its new bucket position.
        12. The load factor drops, and average O(1) operations are restored.
"""

"""
HashMap/
│
├── INITIAL_CAPACITY = 8           # class constant — starting bucket count
├── HASH_BASE = 31                 # class constant — multiplier in the rolling hash
├── LOAD_FACTOR = 0.75             # class constant — resize threshold
│
├── __init__()                     # constructor
│
├── dunder methods                 # bracket / operator syntax -> core methods
│   ├── __getitem__()              # value = map[key]   (raises KeyError)
│   ├── __setitem__()              # map[key] = value
│   ├── __delitem__()              # del map[key]       (raises KeyError)
│   ├── __contains__()             # key in map
│   └── __len__()                  # len(map)
│
├── helper methods
│   ├── _hash()
│   ├── _bucket_index()
│   ├── _find_entry()              # shared hash-and-scan for get/put/remove/contains
│   ├── _rehash()
│   └── _resize()
│
└── core methods
    ├── get()
    ├── put()
    └── remove()
"""

"""
HashSet/                           # delegates entirely to a HashMap
│
├── __init__()                     # constructor — wraps a fresh HashMap
│
├── core methods
│   ├── add()                      # map.put(key, True)
│   ├── contains()                 # key in map
│   └── remove()                   # map.remove(key)
│
└── dunder methods
    ├── __contains__()             # key in set  -> contains(key)
    ├── __len__()                  # len(set)    -> len(map)
    ├── __iter__()                 # for key in set (walks map.buckets)
    └── __str__()                  # {'a', 'b', 'c'}
"""

class HashMap:

    # Class constants — tuning knobs grouped at the top of the class
    INITIAL_CAPACITY = 8
    HASH_BASE = 31
    LOAD_FACTOR = 0.75

    # Constructor
    def __init__(self):
        """Initialize an empty hash map.

        Sets up the backing store with an initial capacity and a size of 0.
        Uses separate chaining: each bucket is its own list that will hold
        the (key, value) pairs which hash to the same index.

        Attributes:
            size (int): Number of key–value pairs currently stored.
            capacity (int): Number of buckets allocated before a resize is needed.
            buckets (list[list]): Backing store of ``capacity`` empty lists.
        """
        self.size = 0
        self.capacity = self.INITIAL_CAPACITY
        self.buckets = [[] for _ in range(self.capacity)]

    # dunder methods
    def __getitem__(self, key):
        """Enable bracket-notation lookup: ``value = map[key]``.

        Locates the key via :meth:`_find_entry` and returns its value, or
        raises KeyError when the key is absent. Keying off the entry's
        *position* (``-1`` means absent) rather than its value means a stored
        value of ``None`` is returned correctly instead of being mistaken for
        absence.

        Raises:
            KeyError: If ``key`` is not found in the map.
        """
        bucket, i = self._find_entry(key)
        if i == -1:
            raise KeyError(key)
        return bucket[i][1]

    def __setitem__(self, key, value):
        """Enable bracket-notation assignment: ``map[key] = value``.

        Delegates to :meth:`put`, which inserts a new entry or overwrites the
        value if the key already exists.
        """
        self.put(key, value)

    def __contains__(self, key):
        """Enable membership tests: ``key in map``.

        Locates the key via :meth:`_find_entry` and reports whether a matching
        entry exists (position ``!= -1``). This keys off the entry's *presence*,
        not its value, so a key whose stored value is ``None`` still counts as
        present — unlike a naive ``get(key) is not None`` test, which would
        wrongly report it absent.
        """
        _, position = self._find_entry(key)
        return position != -1

    def __delitem__(self, key):
        """Enable bracket-notation deletion: ``del map[key]``.

        Delegates to :meth:`remove`, which drops the entry from its chain and
        raises KeyError if the key is absent.
        """
        self.remove(key)

    def __len__(self):
        """Enable ``len(map)`` — the number of key–value pairs stored."""
        return self.size

    # helper methods
    def _hash(self, key): # Time complexity: O(m) where m is the length of the key string
        """Compute a deterministic integer hash code for ``key``.

        Uses the classic polynomial rolling hash: for each character it
        multiplies the running total by a prime (``HASH_BASE``) and then adds
        the character's ASCII value. This gives small changes in the key a large
        effect on the result, spreading similar keys apart.

        Args:
            key (str): The key to hash. Must be a string in this implementation.

        Returns:
            int: The hash code for ``key`` (not yet reduced to a bucket index).

        Raises:
            TypeError: If ``key`` is not a string.
        """
        total = 0

        if not isinstance(key, str):
            raise TypeError("HashMap currently supports string keys only.")

        for char in key:
            # Multiply the current total by HASH_BASE, then add the ASCII value
            total = total * self.HASH_BASE + ord(char)

        return total

    def _bucket_index(self, key): # Time complexity: O(m) where m is the length of the key string (dominated by the call to _hash)
        """Reduce ``key`` to a valid bucket index in the range ``[0, capacity)``.

        Takes the raw hash code from :meth:`_hash` and folds it into the
        backing array's index range with the standard modulo operation, so
        every key lands in a real bucket regardless of how large its hash is.

        Args:
            key (str): The key whose bucket position is needed.

        Returns:
            int: A bucket index in the range ``0 <= index < capacity``.
        """
        return self._hash(key) % self.capacity

    def _find_entry(self, key): # Time complexity: O(m + k) — m = key length (hashing), k = bucket chain length. Average O(m) since a bounded load factor keeps k ~ constant; worst O(m + n) if every key collides into one bucket.
        """Locate ``key``'s bucket and its position within that bucket.

        Hashes the key to its bucket, then scans the chain for a matching key.
        Returns the bucket list itself (not just the value) so callers can
        modify it in place without performing a second lookup: mutating callers
        — :meth:`put`, :meth:`remove` — act on the chain directly, while
        read-only callers just index into it.

        Complexity:
            ``O(m + k)`` where ``m`` is the key length (:meth:`_hash` walks
            every character) and ``k`` is the number of entries in the bucket.
            The common ``O(1)`` average folds in two assumptions: a bounded
            load factor keeps ``k`` roughly constant (enforced here by resizing),
            and short keys keep ``m`` roughly constant (an assumption about the
            input). The true worst case is ``O(m + n)`` when every key collides
            into a single bucket.

        Args:
            key (str): The key to locate.

        Returns:
            tuple[list, int]: ``(bucket, position)`` where ``bucket`` is the
            chain the key hashes to, and ``position`` is the index of the
            matching entry within it, or ``-1`` if the key is not present.
        """
        bucket = self.buckets[self._bucket_index(key)]

        for position, (bucket_key, _) in enumerate(bucket):
            if bucket_key == key:
                return bucket, position

        return bucket, -1

    def _rehash(self, old_buckets): # Time complexity: O(n) where n is the number of entries in the map
        """Redistribute entries from ``old_buckets`` into the current backing store.

        Because the bucket index depends on capacity (hash % capacity), entries
        cannot be copied across as-is — each must be re-hashed into its new
        position. :meth:`_bucket_index` uses ``self.capacity``, so the caller
        must have already updated capacity and allocated ``self.buckets`` before
        calling this.

        Args:
            old_buckets (list[list]): The previous backing store to read from.
        """
        for bucket in old_buckets:
            for key, value in bucket:
                new_index = self._bucket_index(key)
                self.buckets[new_index].append((key, value))

    def _resize(self): # Time complexity: O(n) where n is the number of entries in the map (dominated by the call to _rehash)
        """Double the capacity and allocate a fresh backing store.

        Only handles the array allocation; the actual redistribution of entries
        is delegated to :meth:`_rehash`. Like dynamic-array resizing, the
        occasional O(n) resize amortises to O(1) per insert across a sequence of
        operations.
        """
        # Keep a reference to the old buckets before replacing them
        old_buckets = self.buckets

        # Double the capacity and allocate a fresh set of empty buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]

        # Redistribute every entry into its new bucket position
        self._rehash(old_buckets)

    # Core methods
    def get(self, key, default=None): # Time complexity: O(1) on average, O(n) in the worst case (dominated by the length of the bucket chain)
        """Retrieve the value associated with ``key``, or ``default`` if absent.

        Hashes the key to find its bucket, then scans the bucket for a matching
        key. If found, returns the associated value; if not, returns ``default``
        (``None`` by default) rather than raising. Bracket access (``map[key]``
        via :meth:`__getitem__`) is the raising counterpart.

        Args:
            key (str): The key to look up.
            default: The value to return when ``key`` is not present. Defaults
                to ``None``.

        Returns:
            The value associated with ``key``, or ``default`` if not found.
        """
        bucket, i = self._find_entry(key)

        # i == -1 means the key was not in its bucket -> report the default.
        if i == -1:
            return default

        # bucket[i] is the matching (key, value) tuple; return its value.
        return bucket[i][1]

    def put(self, key, value): # Time complexity: O(1) on average, O(n) in the worst case (dominated by the call to _resize if triggered)
        """Insert or update a key–value pair in the hash map.

        If the key already exists, its value is overwritten and no resize is
        needed (the entry count does not change). For a genuinely new key, the
        anticipated load factor ``(size + 1) / capacity`` is checked first: if
        it would exceed ``LOAD_FACTOR`` the table is resized and rehashed, then
        the bucket is re-fetched from the current table so the reference never
        goes stale.

        Args:
            key (str): The key to insert or update.
            value: The value associated with ``key``.
        """
        bucket, i = self._find_entry(key)

        # Key already exists; update its value in place (size unchanged, no
        # resize needed since the entry count does not grow).
        if i != -1:
            bucket[i] = (key, value)
            return

        # New key — resize proactively if adding it would exceed the load
        # factor. The check uses (size + 1) because the entry is not yet stored.
        if (self.size + 1) / self.capacity > self.LOAD_FACTOR:
            self._resize()
            # Re-fetch the bucket from the current table; _resize replaced
            # self.buckets, so the bucket from _find_entry would be stale.
            bucket = self.buckets[self._bucket_index(key)]

        # Append the new entry
        bucket.append((key, value))
        self.size += 1

    def remove(self, key): # Time complexity: O(1) on average, O(n) in the worst case (dominated by the length of the bucket chain)
        """Delete the entry for ``key`` from the hash map.

        Locates the entry via :meth:`_find_entry` and drops it from its chain.
        With separate chaining no tombstone is needed: each bucket is an
        independent list, so removing an entry from the middle of a chain does
        not disturb the lookup path of any other key (unlike open addressing,
        where a plain gap would break probe sequences). Bracket-notation
        deletion (``del map[key]`` via :meth:`__delitem__`) is the operator
        counterpart.

        Args:
            key (str): The key to delete.

        Raises:
            KeyError: If ``key`` is not found in the map.
        """
        bucket, i = self._find_entry(key)

        if i == -1:
            raise KeyError(key)

        # del removes the (key, value) tuple in place; the neighbouring entries
        # in the same chain keep their positions and stay reachable.
        del bucket[i]
        self.size -= 1


class HashSet:
    """A collection of unique keys backed by a HashMap.

    A set is conceptually "a hash map where every value is ignored." Rather
    than duplicating collision handling, resizing, and hashing, this class
    delegates every operation to a fully-tested HashMap. Each key is stored
    with a placeholder value (``True``) that is never read.

    Composition:
        HashSet  ->  HashMap  ->  Dynamic Array (buckets)  ->  Lists (chains)

    All operations inherit the HashMap's average O(1) complexity.
    """

    def __init__(self):
        """Initialize an empty set backed by a fresh HashMap."""
        self.map = HashMap()

    def add(self, key): # Time complexity: O(1) on average, O(n) worst case (via map.put)
        """Insert ``key`` into the set.

        If the key is already present this is a no-op — ``put`` overwrites the
        placeholder value, but since it is never read, nothing effectively
        changes and the size stays the same.
        """
        self.map.put(key, True)

    def contains(self, key): # Time complexity: O(1) on average, O(n) worst case (via map.__contains__)
        """Report whether ``key`` is in the set."""
        return key in self.map

    def remove(self, key): # Time complexity: O(1) on average, O(n) worst case (via map.remove)
        """Remove ``key`` from the set.

        Raises:
            KeyError: If ``key`` is not in the set.
        """
        self.map.remove(key)

    def __contains__(self, key): # Time complexity: same as contains()
        """Enable ``key in set``."""
        return self.contains(key)

    def __len__(self): # Time complexity: O(1) (returns the map's stored size)
        """Enable ``len(set)`` — the number of keys stored."""
        return len(self.map)

    def __iter__(self): # Time complexity: O(n) where n is the number of keys
        """Yield each key in the set (enables ``for key in set``).

        Walks the backing HashMap's buckets directly. Iteration order follows
        the bucket layout, which shifts on every resize — no ordering is
        guaranteed.
        """
        for bucket in self.map.buckets:
            for key, _ in bucket:
                yield key

    def __str__(self): # Time complexity: O(n) where n is the number of keys
        """Return a readable representation: ``{'a', 'b', 'c'}``."""
        return "{" + ", ".join(repr(key) for key in self) + "}"


# ---------------------------------------------------------------------------
# Demo / manual test harness
#
# Grouped into labelled sections so the output reads like a story:
#   1. basic inserts (size grows, load factor climbs)
#   2. collisions (separate chaining — multiple entries in one bucket)
#   3. overwrite (updating an existing key keeps size unchanged)
#   4. resize (exceeding the load factor doubles capacity and rehashes)
#   5. bracket notation (__getitem__ / __setitem__)
#   6. reads (get returns default; brackets raise KeyError)
#   7. membership (__contains__ handles None values correctly)
#   8. deletion (remove / del map[key] — no tombstones needed)
#   9. hash set (add / contains / remove — delegates to HashMap)
#
# To run:  python3 hash_map.py
# ---------------------------------------------------------------------------

def _section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def _state(hm, note=""):
    """Print size, capacity, load factor, and non-empty buckets in one line."""
    load = hm.size / hm.capacity
    chains = {
        i: bucket for i, bucket in enumerate(hm.buckets) if bucket
    }
    prefix = f"{note:<28}" if note else ""
    print(
        f"{prefix} -> size={hm.size}, capacity={hm.capacity}, "
        f"load={load:.2f}, occupied buckets={chains}"
    )


if __name__ == "__main__":
    hm = HashMap()

    # --- 1. Basic inserts ------------------------------------------------
    _section("1. Basic inserts (each key lands in its hashed bucket)")
    _state(hm, "empty map")
    hm.put("apple", 1)
    _state(hm, 'put("apple", 1)')
    hm.put("banana", 2)
    _state(hm, 'put("banana", 2)')
    hm.put("cherry", 3)
    _state(hm, 'put("cherry", 3)')

    # --- 2. Collisions (separate chaining) ------------------------------
    _section("2. Collisions (some keys share a bucket -> chain grows)")
    hm.put("date", 4)
    _state(hm, 'put("date", 4)')
    hm.put("elderberry", 5)
    _state(hm, 'put("elderberry", 5)')
    hm.put("fig", 6)
    _state(hm, 'put("fig", 6)')

    # --- 3. Overwrite (update existing key, size stays same) ------------
    _section("3. Overwrite (update existing key — size unchanged)")
    # 3a. Overwrite a key that sits alone in its bucket.
    print('Updating "apple" from 1 -> 99 (alone in its bucket)')
    hm.put("apple", 99)
    _state(hm, 'put("apple", 99)')
    # 3b. Overwrite a key that shares a bucket with another ("fig" and
    #     "elderberry" collide). _find_entry must scan past "elderberry" and
    #     land on "fig" mid-chain, updating it in place without touching the
    #     neighbour or changing size.
    print('Updating "fig" from 6 -> 66 (shares bucket 4 with "elderberry")')
    hm.put("fig", 66)
    _state(hm, 'put("fig", 66)')

    # --- 4. Resize (exceed load factor -> capacity doubles & rehashes) --
    _section("4. Resize (7th insert crosses 0.75 -> capacity 8 -> 16)")
    print("Adding one more entry; load factor will exceed 0.75 on insert.")
    hm.put("grape", 7)
    _state(hm, 'put("grape", 7)')
    print("Note: capacity doubled and every entry was rehashed into new buckets.")

    # --- 5. Bracket notation (dunder methods) ---------------------------
    _section("5. Bracket notation (__getitem__ / __setitem__)")
    hm["kiwi"] = 8                       # __setitem__ -> put (new key)
    _state(hm, 'hm["kiwi"] = 8')
    hm["kiwi"] = 80                      # __setitem__ -> put (overwrite)
    _state(hm, 'hm["kiwi"] = 80')
    print(f'hm["kiwi"]                    -> {hm["kiwi"]}')          # __getitem__

    # --- 6. Reads: get() vs map[key] ------------------------------------
    _section("6. Reads (get returns default; brackets raise KeyError)")
    print(f'hm.get("apple")               -> {hm.get("apple")}')     # found
    print(f'hm.get("missing")             -> {hm.get("missing")}')   # absent -> None
    print(f'hm.get("missing", 0)          -> {hm.get("missing", 0)}')  # absent -> default
    try:
        hm["missing"]                                                # absent -> raises
    except KeyError as err:
        print(f'hm["missing"]                 -> raised KeyError({err})')

    # --- 7. Membership: `in` vs `get(...) is not None` ------------------
    _section("7. Membership (__contains__ handles None values correctly)")
    hm["nothing"] = None                 # a real entry whose value is None
    _state(hm, 'hm["nothing"] = None')
    print(f'"apple"   in hm               -> {"apple" in hm}')       # present
    print(f'"missing" in hm               -> {"missing" in hm}')     # absent
    print(f'"nothing" in hm               -> {"nothing" in hm}')     # present (value is None)
    print(f'hm.get("nothing") is not None -> {hm.get("nothing") is not None}'
          "   <- the naive test WRONGLY reports absent")

    # --- 8. Deletion: remove() and del map[key], plus len() ------------
    _section("8. Deletion (remove / del map[key]) — no tombstones needed")
    print(f'len(hm) before                -> {len(hm)}')             # __len__
    # 8a. Build a real collision chain: "olive" hashes to the same bucket as
    #     the existing "grape". Removing "grape" from the middle of that chain
    #     must leave "olive" reachable — proof that separate chaining needs no
    #     tombstone (unlike open addressing, where a gap would break probing).
    hm.put("olive", 100)                 # joins "grape" in a shared bucket
    shared = hm._bucket_index("grape")
    print(f'bucket {shared} before remove       -> {hm.buckets[shared]}')
    hm.remove("grape")                   # remove() -> drop from mid-chain
    print(f'bucket {shared} after  remove       -> {hm.buckets[shared]}')
    print(f'"olive" in hm                 -> {"olive" in hm}'
          "   <- chain neighbour still reachable after remove")
    _state(hm, 'hm.remove("grape")')
    # 8b. del map[key] via __delitem__.
    del hm["apple"]                      # __delitem__ -> remove()
    _state(hm, 'del hm["apple"]')
    # 8c. Removing an absent key raises KeyError.
    try:
        hm.remove("missing")
    except KeyError as err:
        print(f'hm.remove("missing")          -> raised KeyError({err})')
    print(f'len(hm) after                 -> {len(hm)}')

    # --- 9. HashSet (a set built on top of HashMap) ---------------------
    _section("9. HashSet (add / contains / remove — delegates to HashMap)")
    fruits = HashSet()
    print(f"empty set                     -> {fruits}")
    fruits.add("apple")
    fruits.add("banana")
    fruits.add("cherry")
    print(f'after add apple/banana/cherry -> {fruits}  (len={len(fruits)})')
    # Adding a duplicate is a no-op: put overwrites the placeholder value, but
    # since we never read it, nothing changes and the size stays the same.
    fruits.add("apple")
    print(f'add("apple") again (no-op)    -> {fruits}  (len={len(fruits)})')
    print(f'"apple"   in fruits           -> {"apple" in fruits}')
    print(f'"missing" in fruits           -> {"missing" in fruits}')
    fruits.remove("banana")
    print(f'remove("banana")              -> {fruits}  (len={len(fruits)})')
    try:
        fruits.remove("missing")
    except KeyError as err:
        print(f'remove("missing")             -> raised KeyError({err})')

    _section("Demo complete")
