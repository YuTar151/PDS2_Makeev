"""
2. Взявши за основу код домашнього завдання лекції 14, розробіть набір тестів з використання бібліотеки pytest для
методів додавання нових елементів, пошуку мінімального і максимального значень та видалення елементів бінарного дерева.
"""

class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return f'id_node {self.id_node}, leftchilde {self.left}, rightchilde {self.right}'


    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return print (str(find_val) + " Not Found")
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return print (str(find_val) + " Not Found")
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    def search_el(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return None
            return self.left.search_el(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return None
            return self.right.search_el(find_val)
        else:
            return self

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()

    def __tree_to_list(self, tree_list = []):
        if self.left:
            self.left.__tree_to_list(tree_list)
        tree_list.append(self.id_node)
        if self.right:
            self.right.__tree_to_list(tree_list)

        return tree_list

    # 1. Append list to the tree
    def append_list(self, node_list):
        extra_nodes = []
        for node in node_list:
            if node not in self.__tree_to_list():
                self.insert(node)
            else:
                extra_nodes.append(node)

        if len(extra_nodes) == 0:
            print('All elements successfully added to BTS.')
        else:
            print('Some elements of the list are already in BTS:', *extra_nodes)

    # 2.1 Get min value
    def get_min_node(self):
         if self.left is None:
             return self.id_node

         return self.left.get_min_node()

    # 2.1 Get max value
    def get_max_node(self):
         if self.right is None:
             return self.id_node

         return self.right.get_max_node()

    # 3. Delete the node
    def delete_node(self, root, node_val):

        if root.id_node == node_val:
            if not root.right: return root.left

            if not root.left: return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left: temp = temp.left
                root.id_node = temp.id_node
                root.right = self.delete_node(root.right, root.id_node)

        elif root.id_node > node_val:
            root.left = self.delete_node(root.left, node_val)
        else:
            root.right = self.delete_node(root.right, node_val)

        return root


tr = Tree(10)
node_list = [12, 3, 4, 12, 2, 15, 10 ]
tr.append_list(node_list)
print('-' *10)
tr.print_tree()

print('-' *10)
print(f'min = {tr.get_min_node()}, max = {tr.get_max_node()}')

print('-' *10)
tr.delete_node(tr, 12)
tr.print_tree()