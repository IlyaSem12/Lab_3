Deque = []
front = input('------>')
back = input()

while front != 'exit':
    Deque.append(front)
    Deque.append(back)
    front = input()
    back = input()
    if front == 'exit' or back == 'exit':
        if front == 'exit':
            Deque.append(back)
        if back == 'exit':
            Deque.append(front)
        break

print(Deque)
Menu = input('Введите цифры от 1 до 7 :\n'
             '1-Добавить значение в начало\n'
             '2-Удалить последний элемент\n'
             '3-Удалить 1 элемент\n'
             '4-Узнать длинну дека\n'
             '5-Очистить дек\n'
             '6-Добавить значения\n'
             '7-Выход\n'
             '------> ')
while Menu != '7':
    if Menu == '1':
        tmp1=input('------>')
        Deque.insert(0,tmp1)
        print(Deque)
    elif Menu == '2':
        Deque.pop()
        print(Deque)
    elif Menu == '3':
        Deque.pop(0)
        print(Deque)
    elif Menu == '4':
        print(len(Deque))
    elif Menu == '5':
        Deque.clear()
        print(Deque)
    elif Menu == '6':
        while front != 'exit':
            Deque.append(front)
            Deque.append(back)
            front = input()
            back = input()
            if front == 'exit' or back == 'exit':
                if front == 'exit':
                    Deque.append(back)
                if back == 'exit':
                    Deque.append(front)
                break
        print(Deque)

    Menu = input('Введите цифры от 1 до 7:\n'
                 '1-Добавить значение в начало\n'
                 '2-Удалить последний элемент\n'
                 '3-Удалить 1 элемент\n'
                 '4-Узнать длинну дека\n'
                 '5-Очистить дек\n'
                 '6-Добавить значения\n'
                 '7-Выход\n'
                 '------>')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\2\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class knot:
    def __init__(self, element= None):
        self.element = element
        self.NextElement = None

    def has_value(self, value):
        if self.element == value:
            return True
        else:
            return False

class List:
    def __init__(self):
        self.head = None

    def presence(self,element):
        lastknot=self.head
        while (lastknot):
            if element == lastknot.element:
                return True
            else:
                lastknot = lastknot.NextElement
        return False

    def AddEnd(self,newElement):
        newknot=knot(newElement)
        if self.head == None:
            self.head = newknot
            return
        lastknot=self.head
        while (lastknot.NextElement):
            lastknot=lastknot.NextElement
        lastknot.NextElement=newknot

    def index(self,elementindex):
        lastknot=self.head
        knotindex=0
        while knotindex <= elementindex:
            if knotindex == elementindex:
                return lastknot.element
            knotindex+=1
            lastknot=lastknot.NextElement

    def remove(self, remElement):
        headelement = self.head
        if headelement != None:
            if headelement.element == remElement:
                self.head = headelement.NextElement
                headelement = None
                return
        while headelement != None:
            if headelement.element == remElement:
                break
            lastelement = headelement
            headelement = headelement.NextElement
        if headelement == None:
            return
        lastelement.NextElement = headelement.NextElement
        headelement=None

    def ID(self,elementID):
        lastelement = self.head
        knotID = 0
        while lastelement != None:
            if lastelement.has_value(elementID):
                return knotID
            lastelement = lastelement.NextElement
            knotID += 1

    def permutation(self, last, next):
        lastknot = self.head
        saveknot = self.head
        tmp = None
        if last < next:
            while lastknot != None:
                if lastknot.element == last:
                    saveknot = lastknot
                    tmp = lastknot.element
                if lastknot.element == next:
                    saveknot.element = lastknot.element
                    lastknot.element = tmp
                lastknot=lastknot.NextElement
        else:
            tp = last
            last = next
            next = tp
            return List().permutation(last,next)

    def ListPrint(self):

        currentElement = self.head
        print("LINKED LIST")
        print("-----")
        i = 0
        while currentElement != None:
            print(str(i) + ": " + str(currentElement.element))
            i += 1
            currentElement = currentElement.NextElement
        print("-----")

a = List()

Menu = input('Введите цифры от 1 до 6:\n'
                 '1-Вставка элемента в список\n'
                 '2-Удалить элемента в списоке\n'
                 '3-Значение элемента по индексу\n'
                 '4-Id елемента\n'
                 '5-перестановка элементов\n'
                 '6-Выход\n'
                 '------> ')
while Menu != '6':
    if Menu == '1':
        n=None
        while n != 'exit':
            n = input('------> ')
            if n != 'exit':
                a.AddEnd(n)

        a.ListPrint()
    elif Menu == '2':
        n = input('------> ')
        a.remove(n)
        a.ListPrint()
    elif Menu == '3':
        n = input('------> ')
        print(a.index(n))
    elif Menu == '4':
        n = input('------> ')
        print(a.ID(4))
    elif Menu == '5':
        n = input('Значения вводятся от меньшего к большему:')
        b = input('------> ')
        a.permutation(n,b)
        a.ListPrint()

    Menu = input('Введите цифры от 1 до 6:\n'
                 '1-Вставка элемента в список\n'
                 '2-Удалить элемента в списоке\n'
                 '3-Значение элемента по индексу\n'
                 '4-Id елемента\n'
                 '5-перестановка элементов\n'
                 '6-Выход\n'
                 '------> ')