#binary tree
print("TUGAS 1")
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
            self.root = None

    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)

        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

def insert_manual(data):
    data.insert_root("A")

    data.insert_left(data.root, "B")
    data.insert_right(data.root, "C")
    data.insert_left(data.root.left, "D")
    data.insert_right(data.root.left, "E")
    data.insert_right(data.root.right, "F")

#Menampilkan urutan gudang dengan metode Pre-Order.
def traverse_preorder(node): 
    if node is not None:
        print(node.data, end=" - ")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

#Menampilkan urutan gudang dengan metode In-Order.
def traverse_inorder(node): 
    if node is not None:
        traverse_inorder(node.left)
        print(node.data, end=" - ")
        traverse_inorder(node.right)

#Menampilkan urutan gudang dengan metode Post-Order.
def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left)
        traverse_postorder(node.right)
        print(node.data, end=" - ")

# Menampilkan daftar gudang yang merupakan Leaf Node (gudang ujung yang tidak punya cabang lagi).
def get_leaf_nodes(node):
    if node is not None:
        if node.left is None and node.right is None:
                print(node.data, end=" , ")
        get_leaf_nodes(node.left)
        get_leaf_nodes(node.right)

data_audit = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("============================================")
print("[INFO] membangun struktur gudang...")
insert_manual(data_audit)
print("[INFO] Struktur berhasil dibuat \n")

print("\nHASIL AUDIT: ")
print("1. PRE-ORDER:", end=" ")
traverse_preorder(data_audit.root)

print("\n2. IN-ORDER:", end=" ")
traverse_inorder(data_audit.root)

print("\n3. POST-ORDER:", end=" ")
traverse_postorder(data_audit.root)

print("\n[DATA] Gudang ujung (Leaf Nodes):", end=" " )
get_leaf_nodes(data_audit.root)

print("\n============================================")
print("Audit selesai.")
