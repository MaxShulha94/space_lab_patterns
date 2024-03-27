class Memento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content


class Creator:
    def __init__(self):
        self._content = ""
        self._snapshots = []

    def add_content(self, text):
        self._content += text

    def get_content(self):
        print('Your content:')
        return self._content

    def create_snapshot(self):
        snapshot = Memento(self._content)
        self._snapshots.append(snapshot)
        return snapshot

    def restore_snapshot(self, index):
        if 0 <= index < len(self._snapshots):
            self._content = self._snapshots[index].get_content()
            print('Chosen snapshot was restored')

    def show_history(self):
        for i, snapshot in enumerate(self._snapshots):
            print(f"Snapshot {i}: {snapshot.get_content()}")


editor = Creator()
editor.add_content("Hello, ")
snapshot1 = editor.create_snapshot()
editor.add_content("world! ")
snapshot2 = editor.create_snapshot()
editor.add_content("How are you? ")
snapshot3 = editor.create_snapshot()

print(editor.get_content())


editor.show_history()
editor.restore_snapshot(0)
print(editor.get_content())
print(editor.__dict__)