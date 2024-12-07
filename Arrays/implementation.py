# Implementing an Array

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        if self.length == 0:
            return None  
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self,index):
        deleted_item = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1] 

        del self.data[self.length - 1]
        self.length -= 1
        return deleted_item

# Exemplo de uso
new_array = MyArray()

new_array.append("hi")
new_array.append("you")
new_array.append("!")

new_array.pop()

new_array.delete(1)

print(new_array.__dict__)

new_array.append("lorena")

print(new_array.__dict__)

print(new_array.get(1))

