# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# When writing data to a storage system, any way to minimize the physical space used will increase the virtual space available. One powerful strategy to minimize physical space usage is through Inline Data Deduplication. When a write comes into a storage system with data that is identical to data previously written, the new write can be deduped to the old write by recording that the new write occurred but without needing to write the duplicate data to physical space again.

# In this simplified design of a storage system, we’ll represent physical space as a sequential array, and a dedupe lookaside map as a hashmap. The system exposes three methods:

# write(), which takes data as input, determines whether the same data is stored in some location and, if found, returns the address of that location. Otherwise the data is stored in the next free space and returns the physical address of it;
# read(), which takes a physical address and returns the data stored at the address if valid;
# delete(), which takes a physical address and deletes one virtual copy of potentially deduped data at the address if valid.
# Your task is to implement these methods. Given operations, a list of commands (of the three types described above), return an array of outputs corresponding to each of the commands. For more information, please see the example below and the template code.

# Example

# For operations = ["WRITE Hello", "WRITE World", "READ 0", "READ 1", "DELETE 0", "WRITE World", "READ 0", "READ 1", "READ 2"], the output should be
# solution(operations) = ["0", "1", "Hello", "World", "Hello", "1", "None", "World", "None"].

# After the first two operations, the words Hello and World are stored at the addresses 0 and 1 respectively as they are the first empty addresses in the storage system.
# The next READ 0 and READ 1 methods return the words written at the addresses 0 and 1 (Hello, World).
# The DELETE method deletes the data written at the address 0 and returns that data (Hello).
# As we have the word World already at the physical address 1, the command WRITE World doesn't store the data at the next free space, instead just adds one virtual copy of the data to the address 1. So the method returns 1.
# The last 3 operations are READ operations and the results of these commands are the data at the addresses 0, 1, 2.


class ReferenceCounter:
    """ Tracks the number of duplications to a particular
        address in the storage system.
        The first time unique data is written, a new ReferenceCounter instance
        is created with refs == 1. Then each
        subsequent duplicate write or delete will increment or decrement refs.
        When there are no more references to the address (refs = 0),
        the ReferenceCounter object should be discarded.
    """
    def __init__(self, addr, refs):
        """
        addr: integer index into a StorageArray's data_storage
        refs: integer number of duplicate writes to addr
        """
        self.addr = addr
        self.refs = refs


class StorageArray:
    """ Basic implementation of an in-memory storage system
        represented by an array. A lookaside hashtable tracks the
        ReferenceCounters for duplicated data within the data_storage.
        This basic storage system only supports three operations:
            - write data to next available address;
            - read data from specified address;
            - delete data from specified address.
    """

    def __init__(self):
        """ data_storage: array of data objects of length 64
            alloc_addr_ptr: integer of the last allocated index
            dedup_lookaside: hashtable containing ReferenceCounters
                            to track writes of duplicate data
        """
        self.data_storage = [None] * 64
        self.alloc_addr_ptr = 0
        self.dedup_lookaside = {}

    def _alloc_addr(self):
        """ Internal method that grabs the next available free
            address in the data_storage (i.e., address that does
            not point to data with a corresponding ReferenceCounter
            entry in the dedup_lookaside)

            returns: integer addr to use for the next write operation
                or None if no free addr is available
        """
        start_alloc_addr_ptr = self.alloc_addr_ptr
        while True:
            ref_counter = self.dedup_lookaside.get(self.data_storage[self.alloc_addr_ptr])
            if ref_counter is None or ref_counter.addr != self.alloc_addr_ptr:
                break
            self.alloc_addr_ptr = (self.alloc_addr_ptr + 1) % len(self.data_storage)
            if self.alloc_addr_ptr == start_alloc_addr_ptr:
                # No free address available
                return None

        return self.alloc_addr_ptr

    def write(self, data):
        """ Takes in a data object and stores it in the data_storage.
            If the data duplicates to existing data, write() increments
            the reference count instead of allocating a new address. If
            the data is unique (i.e., does not have a corresponding
            ReferenceCounter entry in the dedup_lookaside), but there
            are not any available addresses, return the sentinel value
            of None to signify the write failed.

            data: string to store in the data_storage or record
                duplicate of
            returns: integer addr where the data is stored
                or None if space was required but not available
        """

        if data in self.dedup_lookaside:
            addr = self.dedup_lookaside[data].addr
            self.dedup_lookaside[data].refs += 1
            return addr
        else:
            addr = self._alloc_addr()
            if addr is None:
                return None
            self.data_storage[addr] = data
            self.dedup_lookaside[data] = ReferenceCounter(addr, 1)
            return addr



    def read(self, addr):
        """ Takes in an integer address and retrieves the data at the
            location in the data_storage, only if there are still
            references to the data. If there are no references (i.e.,
            does not point to data with a corresponding ReferenceCounter
            entry in the dedup_lookaside), then return the sentinel
            value None to signify the address is unused or the data has
            been deleted.

            addr: integer address where the data is stored
            returns: object retrieved from data_storage at addr
                or None if there are no references on the data
                at the address
        """
        if 0 <= addr < len(self.data_storage) and self.data_storage[addr] is not None:
            data = self.data_storage[addr]
            if data in self.dedup_lookaside and self.dedup_lookaside[data].addr == addr:
                return data
        return None
        
    def delete(self, addr):
        """ Takes in an integer address and deletes the data at the
            location in the data_storage by decrementing the reference
            count of the data's corresponding ReferenceCounter in the
            dedup_lookaside. If the delete would decrement the count to
            0, remove the ReferenceCounter from the dedup_lookaside.

            addr: integer address where the data is stored
            returns: data stored in the address or None if there isn't any
        """

        if 0 <= addr < len(self.data_storage) and self.data_storage[addr] is not None:
            data = self.data_storage[addr]
            if data in self.dedup_lookaside and self.dedup_lookaside[data].addr == addr:
                self.dedup_lookaside[data].refs -= 1
                if self.dedup_lookaside[data].refs == 0:
                    del self.dedup_lookaside[data]
                return data
        return None
    
def solution(operations):
    ans = []
    dataStorage = StorageArray()
    for operation in operations:
        if operation.startswith('READ '):
            ans.append(str(dataStorage.read(int(operation[5::]))))
        elif operation.startswith('WRITE '):
            ans.append(str(dataStorage.write(operation[6::])))
        elif operation.startswith('DELETE '):
            ans.append(str(dataStorage.delete(int(operation[7::]))))
    return ans

