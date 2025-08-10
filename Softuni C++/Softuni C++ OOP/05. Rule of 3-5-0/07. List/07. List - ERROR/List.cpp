#include "List.h"
#include <sstream>
#include <stdexcept>

List::List::List(): head(nullptr), tail(nullptr), size(0) {};

List::List::List(const List& other) : head(nullptr), tail(nullptr), size(0) {
    addAll(other);
}

int List::List::first() const {
    if (head == nullptr) {
        throw std::out_of_range("Out of range");
    }
    return head->getValue();
}

void List::List::add(int value) {
    Node* NewNode = new Node(value, nullptr, nullptr);
    if (head == nullptr) {
        head = tail = NewNode;
    } else {
        tail->setNext(NewNode);
        NewNode->setPrev(tail);
        tail = NewNode;
    }
    size++;
}

void List::List::addAll(const List& other) {
    Node* currNode = other.head;
    for (size_t i = 0; i < other.getSize(); ++i) {
        add(currNode->getValue());
        currNode = currNode->getNext();
    }
}

void List::List::removeFirst() {
    if (size == 0) {
        throw std::out_of_range("Out of range");
    }
    Node* tmp = head->getNext();
    delete head;
    head = tmp;
    if (head != nullptr) {
        head->setPrev(nullptr);
    } else {
        tail = nullptr;
    }
    size--;
}

void List::List::removeAll() {
    while (size) {
        removeFirst();
    }
}

size_t List::List::getSize() const {
    return size;
}

bool List::List::isEmpty() const {
    return size == 0;
}

List List::List::getReversed(List l) {
    List lst;
    Node* currNode = l.tail;
    while (currNode != nullptr) {
        lst.add(currNode->getValue());
        currNode = currNode->getPrev();
    }
    return lst;
}

std::string List::List::toString() const {
    std::ostringstream ostr;
    bool bFirst = true;
    const Node* ptr = head;
    while (ptr != nullptr) {
        if (!bFirst) {
            ostr << ' ';
        } else {
            bFirst = false;
        }
        ostr << ptr->getValue();
        ptr = ptr->getNext();
    }
    return ostr.str();
}

List& List::List::operator<<(const int& value) {
    add(value);
    return *this;
}

List& List::List::operator<<(const List& other) {
    addAll(other);
    return *this;
}

List& List::List::operator=(const List& other) {
    if (this != &other) {
        removeAll();
        addAll(other);
    }
    return *this;
}

List::List::~List() {
    removeAll();
}