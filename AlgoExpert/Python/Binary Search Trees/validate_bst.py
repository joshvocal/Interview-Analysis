def validateBst(root):
    if not root:
        return True

    s = []
    prev = None
	curr = root

    while curr or s:
        while curr:
            s.append(curr)
            curr = curr.left

        curr = s.pop()
        if prev and curr.value < prev.value:
            return False

        prev = curr
        curr = curr.right

    return True
