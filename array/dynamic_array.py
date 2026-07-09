"""Terms

This module documents the core concepts behind dynamic arrays.

"""

"""
Byte:
    A unit of digital information that typically consists of 8 bits. It is the
    basic addressable element in many computer architectures and is used to
    represent data in memory.
"""

"""
Memory Address:
    A unique identifier for a specific location in computer memory where data
    is stored. In the context of dynamic arrays, each element is stored at a
    specific memory address, and the array itself may be allocated a
    contiguous block of memory.
"""

"""
Contiguous Memory:
    A block of memory where all the elements of an array are stored in adjacent
    memory locations. This allows for efficient access and manipulation of
    elements, as the memory addresses of the elements can be calculated using
    their indices.
"""

"""
Formula for calculating memory address:
    address = base_address + (index × element_size)
"""

"""
Array:
    A data structure that stores a fixed-size sequential collection of elements
    of the same type. It allows for efficient access and manipulation of
    elements using an index.
"""

"""
Index:
    A zero-based position that identifies an element within an array. Indices
    allow direct (constant-time) access to any element, since the element's
    memory address can be computed from the index using the address formula.
"""

"""
Dynamic Array:
    An array that can grow and shrink in size during runtime. It allows for
    efficient memory usage and provides flexibility in managing collections of
    elements.
"""

"""
Size:
    The number of elements currently stored in the array. It can change as
    elements are added or removed.
"""

"""
Capacity:
    The total number of elements that the array can hold before it needs to be
    resized. When the size exceeds the capacity, the array is typically resized
    to accommodate more elements.
"""

"""
Memory Management:
    Dynamic arrays handle memory allocation and deallocation automatically.
    When the array needs to grow, it allocates a new block of memory with a
    larger capacity and copies the existing elements to the new block. When
    elements are removed, the array may shrink in size, but it may not
    immediately release memory back to the system.
"""

"""
Reference:
    A variable that holds the memory address of another variable or object. In
    the context of dynamic arrays, references are used to access and manipulate
    the elements stored in the array.
"""

"""
Pointer:
    A variable that stores the memory address of another variable or object. In
    dynamic arrays, pointers are often used to manage the underlying memory and
    facilitate resizing operations.
"""

"""
Resizing:
    The process of changing the capacity of a dynamic array. When the size of
    the array exceeds its capacity, a new block of memory is allocated with a
    larger capacity, and the existing elements are copied to the new block. This
    allows the array to accommodate more elements while maintaining efficient
    access and manipulation.
"""

"""
ctypes:
    A foreign function library for Python that provides C compatible data types
    and allows calling functions in DLLs or shared libraries. It can be used to
    create and manipulate low-level data structures, such as arrays, in a way
    that is compatible with C programming.
"""

"""
Amortized Analysis:
    A technique used to analyze the average time complexity of a sequence of
    operations, taking into account both the fast and slow operations. In the
    context of dynamic arrays, amortized analysis is used to show that the average 
    time complexity of appending an element is O(1), even though some
    individual append operations may take O(n) time due to resizing.
"""

"""
Shifting:
    The process of moving elements in an array to make space for new elements or
    to fill gaps left by removed elements. In dynamic arrays, shifting is often
    required when inserting or deleting elements at specific positions, and it
    can have a time complexity of O(n) in the worst case, where n is the number of elements in the array.
        - To shift elements to the right, start from the last element and move towards the desired index, copying each element to the next position.
        - To shift elements to the left, start from the desired index and move towards the last element, copying each element to the previous position.
        - Needs to avoid overwriting elements during the shifting process, so it's important to iterate in the correct direction based on the type of shift being performed.
"""

"""
Magic Methods (dunder methods):
    Special methods in Python that allow developers to define the behavior of
    objects for built-in operations. They are called "dunder" methods because
    they are surrounded by double underscores (e.g., __init__, __getitem__,
    __setitem__). In the context of dynamic arrays, magic methods can be used to
    implement functionality such as indexing, iteration, and string
    representation."
"""

"""
Allocated Memory:
    The amount of memory that has been reserved for a data structure, such as a
    dynamic array. Allocated memory may be larger than the actual size of the
    data structure to accommodate future growth without requiring immediate
    resizing. The capacity of a dynamic array represents the allocated memory,
    while the size represents the actual number of elements currently stored in the array.
"""

"""
Stored Data:
    The actual elements that are contained within a data structure, such as a
    dynamic array. The stored data is the information that the data structure is
    designed to hold and manipulate. In a dynamic array, the stored data is
    represented by the elements that have been added to the array, while the
    allocated memory may include additional space for future elements.
"""

"""
Bit:
    The smallest unit of digital information, representing a single binary value
    of either 0 or 1. Eight bits together form one byte, which is the smallest
    addressable unit of memory in most architectures.
"""

"""
Element:
    A single item stored inside a data structure. In a dynamic array, each
    element occupies one slot of the backing store and is reachable in constant
    time through its index.
"""

"""
Data Type / Homogeneous Elements:
    A classification that defines the kind of value an element holds (e.g.
    integer, float, string) and how much memory it occupies. A classic array is
    "homogeneous" — every element shares the same type and size, which is what
    makes the address formula (base + index × element_size) valid. Python lists
    relax this and may hold mixed types, since they store references rather than
    the raw values.
"""

"""
Time Complexity / Big-O Notation:
    A way of describing how the running time of an operation grows as the input
    size n grows, ignoring constant factors. Big-O expresses the upper bound:
    O(1) is constant time (independent of n), while O(n) is linear time (grows
    proportionally to n). In this module, indexing is O(1), while shifting-based
    operations such as insert and delete are O(n).
"""

"""
Space Complexity:
    A measure of how much additional memory an operation or data structure
    requires as the input size grows, expressed with the same Big-O notation as
    time complexity. A dynamic array uses O(n) space for its elements, and a
    resize temporarily needs O(n) extra space to hold the new backing store
    while copying from the old one.
"""

"""
Random Access:
    The ability to read or write any element in constant O(1) time using its
    index, without traversing the preceding elements. Contiguous memory plus the
    address formula is what gives arrays this property, in contrast to
    structures like linked lists that require sequential access.
"""

"""
Growth Factor (Doubling):
    The multiplier applied to the capacity when a dynamic array runs out of
    space. Doubling (a growth factor of 2, as used here via capacity * 2) is the
    common choice because it makes appends O(1) amortized: the occasional O(n)
    copy is spread across many cheap O(1) appends. Growing by a fixed amount
    instead (e.g. +1) would make appends O(n) amortized.
"""

"""
Load Factor:
    The ratio of the number of stored elements to the total capacity
    (size / capacity). It indicates how "full" the backing store is and is
    typically used as the trigger condition for resizing — growing when the load
    factor approaches 1, and (optionally) shrinking when it drops too low.
"""

"""
Shrinking / Downsizing:
    The counterpart to growth: reducing the capacity when a dynamic array
    becomes sparsely populated, so that unused allocated memory can be released.
    A common strategy is to halve the capacity once the load factor falls below a
    threshold (e.g. size <= capacity / 4). This implementation grows but does not
    yet shrink.
"""

"""
Null / None (Sentinel Value):
    A special placeholder value that marks a slot as empty or "no element." This
    implementation fills unused capacity with Python's None, so allocated-but-
    unused slots are clearly distinguishable from real stored data.
"""

"""
Bounds Checking:
    Validating that an index falls within the valid range before using it to
    access memory. Without bounds checking, an out-of-range index could read or
    corrupt unrelated memory. Here the _check_index helpers enforce the valid
    range and raise IndexError when it is violated.
"""

"""
Garbage Collection:
    An automatic memory-management process that reclaims memory occupied by
    objects that are no longer reachable. When removing an element, this
    implementation sets its slot back to None so the last reference is dropped,
    allowing the garbage collector to free the underlying object.
"""

"""
Iteration / Iterator:
    Iteration is the process of visiting each element of a collection in turn; an
    iterator is the object that produces those elements one at a time. In Python
    a class becomes iterable by implementing __iter__ (and typically __next__).
    This implementation does not define __iter__, so it relies on __len__ and
    __getitem__ rather than exposing a native iterator.
"""

"""
Cache Locality (Spatial Locality):
    The performance benefit that arises from storing related data close together
    in memory. Because array elements are contiguous, accessing one element
    tends to pull neighbouring elements into the CPU cache, making sequential
    traversals significantly faster in practice than the same work over
    scattered memory.
"""

"""
DynamicArray/
│
├── __init__()                     # constructor
│
├── dunder methods
│   ├── __len__()
│   ├── __getitem__()
│   ├── __setitem__()
│   ├── __str__()
│   └── __contains__()
│
├── helper methods
│   ├── _check_index()
│   ├── _check_index_for_insert()
│   ├── _check_index_for_delete()
│   ├── _shift_right()
│   ├── _shift_left()
│   └── _clean_last_element()
│
└── core methods
    ├── append_no_resize()
    ├── resize()
    ├── append()
    ├── insert()
    ├── pop()
    └── delete()
"""

import ctypes

class DynamicArray:

    #  Constructor
    def __init__(self):
        """Initialize an empty dynamic array.

        Sets up the backing store with an initial capacity and a size of 0.

        Attributes:
            size (int): Number of elements currently stored.
            capacity (int): Number of slots allocated before a resize is needed.
            array (list): Backing store of length ``capacity`` (unused slots are None).
        """
        self.size = 0
        self.capacity = 4
        # self.array = (ctypes.py_object * self.capacity)() # using ctypes to create a low-level array
        self.array = [None] * self.capacity # using a list to simulate a dynamic array

    # dunder methods
    def __len__(self): # Time complexity: O(1) since we are just returning the size of the array
        """Return the number of elements currently stored (enables ``len(arr)``).

        Returns:
            int: The current size of the array.
        """
        return self.size

    def __getitem__(self, index): # Time complexity: O(1) since we are accessing an element by its index
        """Return the element at ``index`` (enables ``arr[index]``).

        Args:
            index (int): Zero-based position of the element to read.

        Returns:
            Any: The value stored at ``index``.

        Raises:
            IndexError: If ``index`` is out of bounds (< 0 or >= size).
        """
        self._check_index(index)

        return self.array[index]

    def __setitem__(self, index, value): # Time complexity: O(1) since we are setting an element by its index
        """Overwrite the element at ``index`` (enables ``arr[index] = value``).

        Args:
            index (int): Zero-based position of the element to write.
            value (Any): The value to store at ``index``.

        Raises:
            IndexError: If ``index`` is out of bounds (< 0 or >= size).
        """
        self._check_index(index)

        self.array[index] = value

    def __str__(self): # Time complexity: O(n) where n is the number of elements in the array
        """Return a human-readable string of the stored elements (enables ``str(arr)``).

        Returns:
            str: The stored elements (excluding unused capacity) as a list literal.
        """
        return str(self.array[:self.size])  # Only return the elements up to the current size

    def __contains__(self, value): # Time complexity: O(n) where n is the number of elements in the array
        """Report whether ``value`` is stored in the array (enables ``value in arr``).

        Args:
            value (Any): The value to search for.

        Returns:
            bool: True if ``value`` is found among the stored elements, else False.
        """
        for i in range(self.size):  # Only scan the stored elements, not the allocated capacity
            if self.array[i] == value:
                return True
        return False

    # helper methods
    def _check_index(self, index): # Time complexity: O(1) since we are just checking the index value
        """Validate an index used for read/write access.

        Args:
            index (int): The index to validate.

        Raises:
            IndexError: If ``index`` is < 0 or >= size (no valid element there).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

    def _check_index_for_insert(self, index): # Time complexity: O(1) since we are just checking the index value
        """Validate an index used for insertion.

        Insertion allows ``index == size`` (append at the end), unlike a plain read.

        Args:
            index (int): The insertion position to validate.

        Raises:
            IndexError: If ``index`` is < 0 or > size.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds for insert")

    def _check_index_for_delete(self, index): # Time complexity: O(1) since we are just checking the index value
        """Validate an index used for deletion.

        Args:
            index (int): The index of the element to delete.

        Raises:
            IndexError: If the array is empty, or ``index`` is out of bounds.
        """
        if self.size == 0:
            raise IndexError("Delete from empty array")

        self._check_index(index)

    def _shift_right(self, index): # Time complexity: O(n) where n is the number of elements in the array
        """Shift elements one slot right to open a gap at ``index``.

        Iterates from the end toward ``index`` so no element is overwritten
        before it has been copied.

        Args:
            index (int): The position that will be freed for a new element.
        """
        # Shift elements to the right to make space for the new element
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

    def _shift_left(self, index): # Time complexity: O(n) where n is the number of elements in the array
        """Shift elements one slot left to close the gap at ``index``.

        Iterates from ``index`` toward the end so no element is overwritten
        before it has been copied.

        Args:
            index (int): The position of the removed element to fill.
        """
        # Shift elements to the left to fill the gap left by the removed element
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]

    def _clean_last_element(self): # Time complexity: O(1) since we are just setting the last element to None
        """Clear the trailing slot and shrink the logical size by one.

        Nils out the last stored element (so the reference can be garbage
        collected) and decrements ``size``.
        """
        self.array[self.size - 1] = None

        self.size -= 1

    # Core Methods:
    # without resizing, just appending to the array
    # this method does not handle resizing when the size exceeds the capacity
    def append_no_resize(self, value): # Time complexity: O(1) since we are just adding an element to the end of the array without resizing
        """Append ``value`` to the end without any capacity check.

        Assumes there is a free slot (``size < capacity``). Callers are
        responsible for resizing first; see :meth:`append`.

        Args:
            value (Any): The value to store at the end of the array.
        """
        self.array[self.size] = value
        self.size += 1

    def resize(self, new_capacity=None): # Time complexity: O(n) where n is the number of elements in the array
        """Allocate a larger backing store and copy existing elements into it.

        Args:
            new_capacity (int, optional): The target capacity. Defaults to
                double the current capacity when not provided.
        """
        if new_capacity is None:
            new_capacity = self.capacity * 2

        # Create a new array with the specified capacity
        new_array = [None] * new_capacity

        # Copy the elements from the old array to the new array
        for i in range(self.size): # Size is used here to ensure we only copy the elements that have been added, not the entire capacity
            new_array[i] = self.array[i]

        # Update the reference to the new array and the capacity
        self.array = new_array

        # Update the capacity to reflect the new size
        self.capacity = new_capacity

    def append(self, value): # Time complexity: O(1) on average, but O(n) in the worst case when resizing is needed
        """Append ``value`` to the end, resizing the backing store if full.

        Amortized O(1): most appends are O(1), but a full array triggers an
        O(n) resize whose cost averages out over many appends.

        Args:
            value (Any): The value to add at the end of the array.
        """
        # Check if the current size has reached the capacity and resize if necessary
        if self.size == self.capacity:
            self.resize()

        # Append the new value to the array
        self.append_no_resize(value)

    def insert(self, index, value): # Time complexity: O(n) where n is the number of elements in the array
        """Insert ``value`` at ``index``, shifting later elements right.

        Args:
            index (int): Position to insert at; ``0 <= index <= size``.
                Passing ``size`` appends to the end.
            value (Any): The value to insert.

        Raises:
            IndexError: If ``index`` is < 0 or > size.
        """
        self._check_index_for_insert(index)

        # Check if the current size has reached the capacity and resize if necessary
        if self.size == self.capacity:
            self.resize()

        # if the index is equal to the current size, we can simply append the value
        if index == self.size:
            self.append_no_resize(value)
            return

        # Shift elements to the right to make space for the new element
        self._shift_right(index)

        # Insert the new value at the specified index
        self.array[index] = value

        # Increment the size of the array
        self.size += 1

    def pop(self): # Time complexity: O(1) since we are just removing the last element of the array
        """Remove and return the last element.

        Returns:
            Any: The element that was at the end of the array.

        Raises:
            IndexError: If the array is empty.
        """
        self._check_index_for_delete(self.size - 1)  # Check if the array is empty before popping

        # Get the last element
        value = self.array[self.size - 1]

        # Remove the last element by setting it to None
        self._clean_last_element()

        return value
    
    def delete(self, index): # Time complexity: O(n) where n is the number of elements in the array
        """Remove and return the element at ``index``, shifting later elements left.

        Args:
            index (int): Zero-based position of the element to remove.

        Returns:
            Any: The element that was removed.

        Raises:
            IndexError: If the array is empty, or ``index`` is out of bounds.
        """
        self._check_index_for_delete(index)

        # Get the value to be deleted
        value = self.array[index]

        # Remove directly if it's the last element
        if index == self.size - 1:
            return self.pop()

        # Shift elements to the left to fill the gap left by the removed element
        self._shift_left(index)

        # Remove the last element by setting it to None
        self._clean_last_element()

        return value


# ---------------------------------------------------------------------------
# Demo / manual test harness
#
# Grouped into labelled sections so the output reads like a story:
#   1. growth + resizing        4. deletion (front / middle / back / empty)
#   2. native idioms (len/[]/in) 5. edge cases that must raise
#   3. insertion (front/middle/end)
#
# To run:  python3 dynamic_array.py
# ---------------------------------------------------------------------------

def _section(title):
    """Print a visual divider so each phase of the demo stands out."""
    print(f"\n{'=' * 60}\n {title}\n{'=' * 60}")


def _state(arr, note=""):
    """Print size, capacity, allocated slots and stored contents in one line."""
    prefix = f"{note:<28}" if note else ""
    print(
        f"{prefix} -> {arr}  "
        f"(size={arr.size}, capacity={arr.capacity}, allocated={len(arr.array)})"
    )


def _expect_error(description, action):
    """Run ``action`` expecting it to raise; report whether it actually did."""
    try:
        action()
        print(f"[FAIL] {description}: expected an error but none was raised")
    except (IndexError, Exception) as err:
        print(f"[OK]   {description}: raised {type(err).__name__}: {err}")


if __name__ == "__main__":
    arr = DynamicArray()

    # --- 1. Growth & automatic resizing -----------------------------------
    _section("1. Growth & automatic resizing (capacity doubles when full)")
    _state(arr, "empty array")
    for value in range(1, 6):  # 1..5 -> the 5th append overflows capacity 4
        arr.append(value)
        _state(arr, f"append({value})")
    print("Note: capacity jumped 4 -> 8 exactly when size would exceed capacity.")

    # --- 2. Native Python idioms via dunder methods -----------------------
    _section("2. Native idioms: len(), indexing, membership, str()")
    print(f"len(arr)            -> {len(arr)}")
    print(f"arr[0], arr[-? n/a] -> arr[0]={arr[0]}")
    arr[2] = 10                                   # __setitem__
    print(f"arr[2] = 10 then arr[2] -> {arr[2]}")
    print(f"10 in arr           -> {10 in arr}")  # __contains__ (present)
    print(f"999 in arr          -> {999 in arr}") # __contains__ (absent)
    print(f"str(arr)            -> {arr}")

    # --- 3. Insertion at front, middle, and end ---------------------------
    _section("3. Insertion (front / middle / end)")
    arr.insert(0, 100)                # front: shifts everything right
    _state(arr, "insert(0, 100)")
    arr.insert(3, 15)                 # middle
    _state(arr, "insert(3, 15)")
    arr.insert(len(arr), 200)         # end: fast path, behaves like append
    _state(arr, "insert(len, 200)")

    # --- 4. Deletion at back, middle, and front ---------------------------
    _section("4. Deletion (pop / delete middle / delete front)")
    _state(arr, "before deletions")
    print(f"pop()               -> removed {arr.pop()}")
    _state(arr, "after pop()")
    print(f"delete(2)           -> removed {arr.delete(2)}")  # middle
    _state(arr, "after delete(2)")
    print(f"delete(0)           -> removed {arr.delete(0)}")  # front
    _state(arr, "after delete(0)")

    # --- 5. Edge cases: draining to empty, then invalid operations --------
    _section("5. Edge cases (draining + operations that must raise)")
    while len(arr) > 0:              # drain completely to hit the empty boundary
        arr.pop()
    _state(arr, "drained to empty")

    _expect_error("pop() on empty array",        lambda: arr.pop())
    _expect_error("delete(0) on empty array",    lambda: arr.delete(0))
    _expect_error("read arr[0] on empty array",  lambda: arr[0])
    _expect_error("negative index arr[-1]",      lambda: arr[-1])

    arr.append(42)                                # size == 1
    _state(arr, "append(42)")
    _expect_error("read arr[1] (out of bounds)", lambda: arr[1])
    _expect_error("insert(5) beyond size",       lambda: arr.insert(5, 99))
    _expect_error("delete(3) out of bounds",     lambda: arr.delete(3))

    # insert(size, x) is the one boundary that is allowed (append position)
    arr.insert(len(arr), 43)
    _state(arr, "insert(len, 43) allowed")

    _section("Demo complete")