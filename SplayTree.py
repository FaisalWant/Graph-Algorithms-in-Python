
class Node:
  def __init__(self, data, parent):
    self.data= data
    self.parent= parent
    self.left_node= None
    self.right_node=None



class SplayTree:

  def __init__(self):
    self.root=None


  def insert(self, data):
    if self.root is None:
      self.root= Node(data, None)

    else:
      self.insert_node(data, self.root)

  def insert_node(self, data, node):
    if data < node.data:
      if node.left_node:
        self.insert_node(data, node.left_node)
      else:
        node.left_node= None(data, node)

    else:
      if node.right_node:
        self.insert_node(data, node.right_node)

      else:
        node.right_node=Node(data, node)


  def find(self, data):
    node= self.root
    while node is not None:
      if data < node.data:
        node= node.left_node

      elif data > node.data:
        node= node.right_node

      else:
        self.splay(node)
        return node.data

  def rotate_right(self, node):
    temp_left_node= node.left_node
    t= temp_left_node.right_node

    temp_left_node.right_node= node
    node.left_node = t

    if t is not None:
      t.parent= node

    temp_parent= node.parent
    node.parent= temp_left_node
    temp_left_node.parent= temp_parent

    if temp_left_node.parent is not None and temp_left_node.parent.left_node== node:
      temp_left_node.parent.left_node= temp_left_node


    if temp_left_node.parent is not None and temp_left_node.parent.right_node== node:
      temp_left_node.parent.right_node= temp_left_node

    if node == self.root:
      self.root= temp_left_node

  def splay(self, node):

    while node.parent is not None:

      if node.parent.parent is None:

        if node== node.parent.left_node:
          self.rotate_right(node.parent)

        else:
          self.rotate_left(node.parent)

      elif node = node.parent.left_node and node.parent== node.parent.parent.left_node:
        self.rotate_right(node.parent.parent)
        self.rotate_right(node.parent)

      elif node== node.parent.right_node and node.parent== node.parent.parent.right_node:
        self.rotate_left(node.parent.parent)
        self.rotate_left(node.parent)


      elif node== node.parent.left_node and node.parent == node.parent.parent.right_node:
        self.rotate_right (node.parent)
        self.rotate_left(node.parent)

      else:
        self.rotate_left(node.parent)
        self.rotate_right(node.parent)
