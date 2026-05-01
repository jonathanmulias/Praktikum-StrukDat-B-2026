class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node("A")
        self.root.left = Node("B")
        self.root.right = Node("C")
        self.root.left.left = Node("D")
        self.root.left.right = Node("E")
        self.root.right.right = Node("F")

    def pre_order(self, node, hasil):
        if node is not None:
            hasil.append(node.data)
            self.pre_order(node.left, hasil)
            self.pre_order(node.right, hasil)

    def in_order(self, node, hasil):
        if node is not None:
            self.in_order(node.left, hasil)
            hasil.append(node.data)
            self.in_order(node.right, hasil)

    def post_order(self, node, hasil):
        if node is not None:
            self.post_order(node.left, hasil)
            self.post_order(node.right, hasil)
            hasil.append(node.data)

    def leaf_nodes(self, node, hasil):
        if node:
            if node.left is None and node.right is None:
                hasil.append(node.data)
            self.leaf_nodes(node.left, hasil)
            self.leaf_nodes(node.right, hasil)

tree = BinaryTree()

print("SISTEM AUDIT DISTRIBUSI CEPAT SAMPAI")
print("====================================")
print("[INFO] Membangun Struktur Gudang...")
tree.insert_manual()
print("[INFO] Struktur berhasil dibuat.")

pre = []
ino = []
post = []
leaf = []

tree.pre_order(tree.root, pre)
tree.in_order(tree.root, ino)
tree.post_order(tree.root, post)
tree.leaf_nodes(tree.root, leaf)

print("\nHASIL AUDIT:")
print("1. Pre-Order :", " - ".join(pre))
print("2. In-Order :", " - ".join(ino))
print("3. Post-Order :", " - ".join(post))

print("\n[DATA] Gudang Ujung (Leaf Nodes) : ", ", ".join(leaf))
print("======================================")
print("Audit Selesai!")