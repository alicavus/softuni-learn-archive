#include <iostream>
#include <string>
#include <sstream>
#include "List.h"

List::Node::Node(int value, Node* prev, Node* next): value(value), prev(nullptr), next(nullptr) {}

int List::Node::getValue() const{
    return value;
}

void List::Node::setValue(int val){
    value = val;
}

List::Node* List::Node::getNext() const{
    return next;
}

void List::Node::setNext(Node* nxt){
    next = nxt;
}

List::Node* List::Node::getPrev() const{
    return prev;
}

void List::Node::setPrev(Node* prv){
    prev = prv;
}

List::List(): head(nullptr), tail(nullptr), size(0){}

List::List(const List& other): head(nullptr), tail(nullptr), size(0){
    addAll(other);
}

int List::first() const{
    if(head == nullptr)
        throw std::out_of_range("Out of range");
    return head->getValue();    
}

void List::List::add(int val){
    Node* NewNode = new Node(val, nullptr, nullptr);
    if(size == 0){
        head = tail = NewNode;
    }
    else{
        tail->setNext(NewNode);
        NewNode->setPrev(tail);
        tail = NewNode;
    }
    size++;
}


void List::List::addAll(const List& other){
    Node* currNode = other.head;
    for(size_t idx = 0; idx < other.getSize(); idx++){
        add(currNode->getValue());
        currNode = currNode->getNext();
    }
}

void List::List::removeFirst(){
    if(head == nullptr)
        throw std::out_of_range("Out of range");
    
    Node* tmp = head->getNext();
    delete head;
    head = tmp;
    if (head != nullptr) 
        head->setPrev(nullptr);
    else
        tail = nullptr;
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
        if (!bFirst)
            ostr << ' ';
        else
            bFirst = false;
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

