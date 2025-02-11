# LeetCodeJourney

## 一、二叉树

### 1、什么是二叉树

- 是一种树形数据结构

  - 每个节点可以有==0==、==1==、==2==、个叶子节点

  - 节点==值==可以是==任意类型==的数据

    - 整数

    - 字符串

    - ...

    - 案例如下图

      ```txt
              1
             / \
            2   3
           / \
          4   5
         /     \
        6       7
      ```

- 二叉树类的生成

```python
class BinaryTreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # 节点的值
        self.left = left      # 左子节点
        self.right = right    # 右子节点

    def __str__(self):
        return str(self.val)  # 打印节点时显示节点的值
```



### 2、关于二叉树的遍历

- 指的是按照某种顺序访问树中的所有节点。

- 常见遍历

  - **前序遍历**（PreorderTraversal）：==根节点== --> 左子树 --> 右子树

    ```python
    def preorder(root):
        if not root:
            return
        print(root.val)      # 访问根节点
        preorder(root.left)  # 递归访问左子树
        preorder(root.right) # 递归访问右子树
    ```

  - **中序遍历**（Inorder Traversal）：左子树 --> ==根节点== --> 右子树

  ```python
  def inorder(root):
      if not root:
          return
      inorder(root.left)   # 递归访问左子树
      print(root.val)      # 访问根节点
      inorder(root.right)  # 递归访问右子树
  ```

  - **后序遍历**(Postorder Traversal)：左子树 --> 右子树 --> ==根节点==

  ```python
  def postorder(root):
      if not root:
          return
      postorder(root.left)  # 递归访问左子树
      postorder(root.right) # 递归访问右子树
      print(root.val)       # 访问根节点
  ```

  

