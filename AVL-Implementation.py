#AVL Tree: ....

class Node:
  def __init__(self, data, parent):
    self.data= data
    self.left_node= None
    self.right_node= None
    self.parent= parent
    self.height=0


class AVLTree:
    def __init__(self):
        self.root= None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)

        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:

            if node.left_node:
                self.insert_node(data, node.left_node)

            else:
                node.left_node= Node(data, node)
                node.height= max(self.calc_height(node.left_node), self.calc_height(node.right_node))+1

        else:

            if node.right:
                self.insert_node(data, node.right_node)

            else:
                node.right_node= Node(data, node)
                node.height= max(self.calc_height(node.left_node) ,self.calc_height(node.right_node))+1

        self.handle_violation(node)

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)


    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.remove_data(data, node.left_node)

        elif data >node.data:
            self.remove_data(data, node.right_node)

        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node... %d " % node.data)
                parent= node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node= None 
                
                if parent is not None and parent.right_node == node: 
                    parent.right_node= None  
                
                if parent is None:    # this is the root node of the tree.
                    self.root = None 
                
                del node 
                # 
                self.handle_violation(parent)


        elif node.left_node is None and node.right_node is not None: 
            print("Removing a node with single right child") 
            parent= node.parent 

            if parent is not None: 
                if parent.left_node == node:
                    parent.left_node= node.left_node 
                if parent.rightChild== node: 
                    parent.right_node = node.right_node 
            else: 
                self.root= node.right_node 

            node.right_node.parent= parent # establishing the link from child to parent back 
            del node     
            self.handle_violation(parent) 
        

        elif node.left_node is not None and node.right_node is None: 
            print("Removing a node with single left child") 
            parent= node.parent 

            if parent is not None: 
                if parent.left_node == node:
                    parent.left_node= node.left_node 
                if parent.rightChild== node: 
                    parent.right_node = node.left_node 
                
            else: 
                self.root= node.left_node 

            node.left_node.parent= parent 
            del node     

            self.handle_violation(parent) 

        else: 
            print("Remove node with two childrens") 
            predecessor= self.get_predecessor(node.left_node) 
            temp= predecessor.data 
            predecessor.data= node.data 
            node.data= temp 
            self.remove_node(data, predecessor) 
        
                            
    def get_predecessor(self, node): 
        if node.right_node: 
            return self.get_predecessor(node.right_node) 
        
        return node 
    

    def handle_violation(self, node): 
        while node is not None:    # these violation need to be checked back to the root of tree .... 
            node.height= max(self.calculate_height(node.left_node) ,self.calculate_height(node.right_node))+1   # updating the height of node

            self.violation_helper(node) 
            node=node.parent  # going towards parent 
    # violation will be checked on parent node .. 

    def violation_helper(self, node): 
        balance= self.calculate_balance(node) 
        if balance >1:                                     #left heavy , but it can be left-right heavy or left-left heavy 
            # left right heavy situation: left rotation on parent + right rotation on grandparent 
            if self.calculate_balance(node.left_node)<0:  # right heavy 
                self.rotate_left(node.left_node) 
            
            self.rotate_right(node) 
        
        if balance <-1: 
            if self.calculate_balance(node.right_node)>0: 
                self.rotate_right(node.right_node) 
            
            self.rotate_left(node) 
    
    def calc_height(self, node):
        if node is None: 
            return -1 
        
        return node.height 
    
    def calculate_balance(self, node): 
        if node is None: 
            return 0 
        
        return self.calc_height(node.left_node)- self.calc_height(node.right_node) 
    

    def rotate_right(self, node): 
        print('Rotating to the right on node', node.data) 

        temp_left_node= node.left_node 
        t= temp_left_node.right_node 

        temp_left_node.right_node= node 
        node.left_node=t 

        if t is not None: 
            t.parent= node 
        
        temp_parent= node.parent 
        node.parent= temp_left_node 
        temp_left_node.parent= temp_parent 

        if temp_left_node.parent is not None and temp_left_node.parent.left_node== node: 
            temp_left_node.parent.left_node= temp_left_node 
        
        if temp_left_node.parent is not None and temp_left_node.parent.right_node== node: 
            temp_left_node.parent.right_node= temp_left_node 
        

        if node== self.root: 
            self.root= temp_left_node # bcz it was updated to the root status 
        
        node.height= max(self.calculate_height(node.left_node), self.calculate_height(node.right_node) ) 
        temp_left_node.height= max(self.calculate_height(temp_left_node.left_node), self.calculate_height(temp_left_node.right_node))+1
    

    def rotate_left(self, node): 
        print("Rotating to the left on node", node.data) 

        temp_right_node= node.right_node 
        t= temp_right_node.left_node 

        temp_right_node.left_node= node 
        node.right_node= t 

        if t is not None: 
            t.parent= node 
        temp_parent= node.parent 
        node.parent = temp_right_node 
        temp_right_node.parent = temp_parent 


        if temp_right_node.parent is not None and temp_right_node.parent.left_node==node: 
            temp_right_node.parent.left_node= temp_right_node 
        
        if temp_right_node.parent is not None and temp_right_node.parent.right_node==node:
            temp_right_node.parent.right_node= temp_right_node 
        
        if node== self.root: 
            self.root= temp_right_node 
        
        node.height= max(self.calculate_height(node.left_node), self.calculate_height(node.right_node))
        temp_right_node.height= max(self.calculate_height(temp_right_node.left_node), self.calculate_height(temp_right_node.right_node)) +1
    

    def traverse(self): 
        if self.root is not None: 
            self.traverse_in_order(self.root) 
    
    def traverse_in_order(self, node):
        if node.left_node: 
            self.traverse_in_order(node.left_node) 
        
        l= '' 
        r= ''
        p= ''

        if node.left_node is not None: 
            l = node.left_node.data 
        else:
            l = 'NULL' 
        
        if node.right_node is not None: 
            r= node.right_node.data 
        
        else: 
            r= 'NULL' 
        
        if node.parent is not None: 
            p= node.parent.data 
        
        else: 
            p = 'NULL' 
        print("%s left: %s right: %s parent: %s height: %s" % (node.data, l, r, p, node.height)) 

        if node.right_node:
            self.traverse_in_order(node.right_node) 
    




                      

        
                        
            






