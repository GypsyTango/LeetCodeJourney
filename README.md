# LeetCodeJourney

## 一、二叉树

### 1、什么是二叉树

- 是一种树形数据结构

  - 每个节点可以有0、1、2个子节点

  - 没有子节点的的节点，叫`叶子节点`

  - 节点`值`可以是`任意`类型的数据

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

- 二叉树类的性质

  - 层次：根节点是第一层，其子节点为第二层，以此类推

    - 如图1.0

      ```txt
              1        （第1层）
             / \
            2   3      （第2层）
           / \
          4   5        （第3层）
             /
            6          （第4层）
      ```

  - 深度：根节点到到某个节点的路径长度 -> 树的深度是最大节点的深度

    - 1的深度为0
    - 2和3的深度为1
    - 4和5的深度为2
    - 6的深度为3

  - 高度：从某个节点到叶子节点的**最长路径** -> 树的高度是根节点的高度

    - 1的高度为3
    - 2的高度为2
    - 3的高度为0
    - 4的高度为0
    - 5的高度为1
    - 6的高度为0

  - 满二叉树：每个节点都有0或2个子节点

    - 图1.0显示，存在节点有1个子节点情况，所以不是满二叉树。

  - 完全二叉树：除了最后一层，其他层都被完全填充，且最后一层节点都靠做排列

    - 图1.0显示，既然不是满二叉树，就更不会是完全二叉树。

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

  - **前序遍历**（PreorderTraversal）：【根节点】 --> 左子树 --> 右子树

    ```python
    def preorder(root):
        if not root:
            return
        print(root.val)      # 访问根节点
        preorder(root.left)  # 递归访问左子树
        preorder(root.right) # 递归访问右子树
    ```

  - **中序遍历**（Inorder Traversal）：左子树 --> 【根节点】 --> 右子树

    ```python
    def inorder(root):
        if not root:
            return
        inorder(root.left)   # 递归访问左子树
        print(root.val)      # 访问根节点
        inorder(root.right)  # 递归访问右子树
    ```

  - **后序遍历**(Postorder Traversal)：左子树 --> 右子树 --> 【根节点】

    ```python
    def postorder(root):
        if not root:
            return
        postorder(root.left)  # 递归访问左子树
        postorder(root.right) # 递归访问右子树
        print(root.val)       # 访问根节点
    ```

  - **层次遍历**(level order)：实际是广度搜索（BFS），按照树的从上到下，从左到右遍历节点。

    ```python
    from collections import deque
    
    def levelorder(root):
        if not root:
            return
        queue = deque([root])  # 使用队列存储节点
        while queue:
            node = queue.popleft()
            print(node.val)    # 访问节点
            if node.left:      # 将左子节点加入队列
                queue.append(node.left)
            if node.right:     # 将右子节点加入队列
                queue.append(node.right)
    ```

  

