import random
import time

operations = int()
node_buffer = 0
travel_right = False

class node:

    def __init__(self, key):
        self.head = self
        self.key = key
        self.rank = 1
        self.parent_node = None
        self.left_child = None
        self.right_child = None
    def parent(self, parent):
        self.parent_node = parent
    def left(self, left):
        if left == None:
            del self.left_child
        self.left_child = left
    def right(self, right):
        if right == None:
            del self.right_child
        self.right_child = right
    def inc_rank(self):
        self.rank = self.rank + 1
    def dec_rank(self):
        self.rank = self.rank - 1

def has_left(parent_node):

    return parent_node.left_child != None and parent_node.left_child is not None

def has_right(parent_node):

    return parent_node.right_child != None and parent_node.right_child is not None

def parent_of(parent_node):

    return parent_node.parent_node

def build_bst(parent_node, new_key):

    global operations
    operations = operations + 1

    parent_node.inc_rank()

    if new_key <= parent_node.key:
        if has_left(parent_node):
            build_bst(parent_node.left_child, new_key)
        else:
            child_node = node(new_key)
            child_node.parent(parent_node)
            parent_node.left(child_node)
            del child_node
    else:
        if has_right(parent_node):
            build_bst(parent_node.right_child, new_key)
        else:
            child_node = node(new_key)
            child_node.parent(parent_node)
            parent_node.right(child_node)
            del child_node

def init_bst(size):
    
    result = node(random.randint(1,100))
    for i in range(size):
        build_bst(result, random.randint(1, 100))
    return result

def bst_search(parent_node, key):

    global operations
    operations = operations + 1

    global node_buffer

    if key < parent_node.key:
        if has_left(parent_node):
            bst_search(parent_node.left_child, key)
    elif key > parent_node.key:
        if has_right(parent_node):
            bst_search(parent_node.right_child, key)
    elif key == parent_node.key:
        node_buffer = node(key)
        node_buffer.rank = parent_node.rank

def find_rank(parent_node, key):

    global node_buffer
    node_buffer = 0
    
    bst_search(parent_node, key)
    if node_buffer == 0:
        return None
    return node_buffer.rank

def bst_delete(parent_node, key):

    global operations
    operations = operations + 1

    global node_buffer
    global travel_right

    parent_node.dec_rank()
    
    if key < parent_node.key:
        if has_left(parent_node):
            travel_right = False
            bst_delete(parent_node.left_child, key)
    elif key > parent_node.key:
        if has_right(parent_node):
            travel_right = True
            bst_delete(parent_node.right_child, key)
    else:
        if has_right(parent_node):
            node_buffer = parent_node.right_child
            parent_node.key = node_buffer.key
            parent_node.right(None)
            
            if has_right(node_buffer):
                parent_node.right(node_buffer.right_child)
            elif has_left(node_buffer):
                parent_node.right(node_buffer.left_child)
                
            node_buffer = 0
        elif has_left(parent_node):
            node_buffer = parent_node.left_child
            parent_node.key = node_buffer.key
            parent_node.left(None)
            
            if has_right(node_buffer):
                parent_node.left(node_buffer.right_child)
            elif has_left(node_buffer):
                parent_node.left(node_buffer.left_child)
                
            node_buffer = 0
        else:
            if travel_right:
                parent_node.parent_node.right(None)
                del parent_node
            else:
                parent_node.parent_node.left(None)
                del parent_node

def max_node(parent_node):
    
    global operations
    operations = operations + 1

    print (parent_node.key, "(" , parent_node.rank , ")")
    
    if has_right(parent_node):
        parent_node = parent_node.right_child
        max_node(parent_node)

def min_node(parent_node):
    
    global operations
    operations = operations + 1

    print (parent_node.key, "(" , parent_node.rank , ")")
    
    if has_left(parent_node):
        parent_node = parent_node.left_child
        min_node(parent_node)

def printout(parent_node):

    if parent_node.left_child != None:
        printout(parent_node.left_child)

    print (parent_node.key, "(" , parent_node.rank , ")" , "\t",)

    if parent_node.right_child != None:
        printout(parent_node.right_child)

def print_bst(parent_node):

    print ("BST InOrder: ", "\t",)
    printout(parent_node)

def main():

    global operations
    operations = 0

    size = int(input("lecture5_BST.py\n\nPlease enter the size of the BST: "))

    start_time = time.time() * 1000
    bst_tree = init_bst(size)
    end_time = time.time() * 1000
    if size <= 100:
        print_bst(bst_tree)
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time)), "\n",
    print ("Number of operations: ", operations, "\n")

    operations = 0
     
    key = int(input("Please enter a key to search the BST for its rank: "))

    start_time = time.time() * 1000
    rank = find_rank(bst_tree, key)
    end_time = time.time() * 1000
    if rank != None:
        print ("Key found: ", key, "(", rank, ")")
    else:
        print ("Key does not exist.",)
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time))
    print ("Number of operations: ", operations)

    operations = 0

    key = int(input("\nPlease enter a key to insert into the BST: "))

    start_time = time.time() * 1000
    build_bst(bst_tree, key)
    end_time = time.time() * 1000
    if size <= 100:
        print_bst(bst_tree)
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time)), "\n",
    print ("Number of operations: ", operations, "\n")

    operations = 0
    
    key = int(input("Please enter a key to delete from the BST: "))
    
    start_time = time.time() * 1000
    bst_delete(bst_tree, key)
    end_time = time.time() * 1000
    if size <= 100:
        print_bst(bst_tree)
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time)), "\n",
    print ("Number of operations: ", operations, "\n")

    operations = 0

    print ("Min key:")
    start_time = time.time() * 1000
    min_node(bst_tree)
    end_time = time.time() * 1000
    
    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time)), "\n",
    print ("Number of operations: ", operations, "\n")

    operations = 0

    print ("Max key:")
    start_time = time.time() * 1000
    max_node(bst_tree)
    end_time = time.time() * 1000

    print ("\nTime elapsed: %s milliseconds" % (end_time - start_time)), "\n",
    print ("Number of operations: ", operations, "\n")

main()
