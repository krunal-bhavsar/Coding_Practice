class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
    
    def add_child(self, child):
        child.parent=self
        self.children.append(child)

    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    
    def print_tree(self, level=0):
        spaces=" "*self.get_level()
        prefix=spaces+"|-" if self.parent else ""

        print(prefix+self.data)
        for child in self.children:
            child.print_tree()
    
def build_product_tree():
    root=TreeNode("Electronics")

    laptop=TreeNode("Laptop")
    root.add_child(laptop)
    lenovo=TreeNode("Lenovo")
    laptop.add_child(lenovo)
    dell=TreeNode("Dell")
    laptop.add_child(dell)

    mobile=TreeNode("Mobile")
    root.add_child(mobile)
    genshin=TreeNode("Genshin")
    mobile.add_child(genshin)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    # print(root)
    root.print_tree()