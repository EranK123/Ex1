class CallsForElevator:

    def __init__(self, name, time, src, dest, type, allocated_to):
        self.name = name
        self.time = time
        self.src = src
        self.dest = dest
        self.type = type
        self.allocated_to = allocated_to

    def __str__(self):
        return f"time: {self.time} src: {self.src} dest: {self.dest} type: {self.type} allocated_to: {self.allocated_to}"
