import queue


class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # 节点的值
        self.left = left  # 左子节点
        self.right = right  # 右子节点
        self.result = queue.Queue()  # 定义存储节点的容器为队列

    def preorder(self, root, reverse=False):
        """
        前序遍历之左在前 root -> left -> right 【default】
        前序遍历之右在前 root -> right -> left
        :param root: 根节点
        :param reverse: 顺序
        :return: None
        """

        if not root:
            return

        if reverse:
            self.result.put(root.val)  # 访问根节点
            self.preorder(root.right)  # 递归访问右子树
            self.preorder(root.left)  # 递归访问左子树
        else:
            self.result.put(root.val)  # 访问根节点
            self.preorder(root.left)  # 递归访问左子树
            self.preorder(root.right)  # 递归访问右子树
        return self.result

    def inorder(self, root, reverse=False):
        """
        中序遍历之左在前 left -> root -> right 【default】
        中序遍历之右在前 right -> root -> left
        :param root: 根节点
        reverse
        :return: None
        """

        if not root:
            return

        if reverse:
            self.inorder(root.right)  # 递归访问右子树
            self.result.put(root.val)  # 访问根节点
            self.inorder(root.left)  # 递归访问左子树
        else:
            self.inorder(root.left)  # 递归访问左子树
            self.result.put(root.val)  # 访问根节点
            self.inorder(root.right)  # 递归访问右子树
        return self.result

    def postorder(self, root, reverse=False):
        """
        后序遍历之左在前 left -> right -> root 【default】
        后序遍历之右在前 right -> left -> root
        :param root: 根节点
        :param reverse: 顺序
        :return: None
        """

        if not root:
            return

        if reverse:
            self.postorder(root.right)
            self.postorder(root.left)
            self.result.put(root.val)  # 访问根节点
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            self.result.put(root.val)  # 访问根节点
        return self.result

    def levelorder(self, root, reverse=False):
        """
        层次遍历二叉树，使用 queue.Queue 进行遍历和存储结果
        :param root: 根节点
        :return: 包含节点值的队列
        """

        self.result = queue.Queue()  # 清空结果队列

        if not root:
            return self.result  # 如果根节点为空，返回空队列

        q = queue.Queue()  # 用于层次遍历的辅助队列
        q.put(root)  # 将根节点加入队列

        while not q.empty():
            node = q.get()  # 取出队列中的节点
            self.result.put(node.val)  # 将当前节点的值添加到结果队列
            if reverse:
                if node.right:  # 将右子节点加入队列
                    q.put(node.right)
                if node.left:  # 将左子节点加入队列
                    q.put(node.left)
            else:
                if node.left:  # 将左子节点加入队列
                    q.put(node.left)
                if node.right:  # 将右子节点加入队列
                    q.put(node.right)
        return self.result  # 返回结果队列


if __name__ == '__main__':
    """ 创建1个二叉树 """
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.right.right = BinaryTree(5)
    """ 遍历二叉树 """
    bt = BinaryTree()

    q1 = bt.preorder(root=root, reverse=False)  # 前序遍历
    result1, result2, result3, result4 = list(), list(), list(), list()
    while not q1.empty():
        result1.append(q1.get())
    print(result1)

    q2 = bt.inorder(root=root, reverse=False)  # 中序遍历
    while not q2.empty():
        result2.append(q2.get())
    print(result2)

    q3 = bt.postorder(root=root, reverse=False)  # 后序遍历
    while not q3.empty():
        result3.append(q3.get())
    print(result3)

    q4 = bt.levelorder(root=root, reverse=False)  # 层次遍历
    while not q4.empty():
        result4.append(q4.get())
    print(result4)
