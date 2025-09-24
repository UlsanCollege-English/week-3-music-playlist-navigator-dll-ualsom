class _DNode:
    __slots__ = ("title", "prev", "next")
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        new_node = _DNode(title)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def play_first(self):
        self.current = self.head
        return self.current.title if self.current else None

    def next(self):
        if self.current is None:
            return None
        if self.current.next:
            self.current = self.current.next
        return self.current.title

    def prev(self):
        if self.current is None:
            return None
        if self.current.prev:
            self.current = self.current.prev
        return self.current.title

    def insert_after_current(self, title):
        if self.current is None:
            self.add_song(title)
            return

        new_node = _DNode(title)
        nxt = self.current.next
        self.current.next = new_node
        new_node.prev = self.current
        new_node.next = nxt
        if nxt:
            nxt.prev = new_node
        else:
            self.tail = new_node

    def remove_current(self):
        if self.current is None:
            return False

        prev_node = self.current.prev
        next_node = self.current.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        if next_node:
            self.current = next_node
        elif prev_node:
            self.current = prev_node
        else:
            self.current = None

        return True

    def to_list(self):
        titles = []
        node = self.head
        while node:
            titles.append(node.title)
            node = node.next
        return titles
