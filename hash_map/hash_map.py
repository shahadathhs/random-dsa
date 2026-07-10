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

class HashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 8
        self.buckets = [[] for _ in range(self.capacity)]

    def _bucket_index(self, key):
        return hash(key) % self.capacity


hash_map = HashMap()

print("HashMap initialized with capacity:", hash_map.capacity)
