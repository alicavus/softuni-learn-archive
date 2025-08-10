#include "List.h"

List::Node::Node(int val, Node* prv, Node* nxt): value(val), prev(prv), next(nxt) {}

int List::Node::getValue() const{
    return value;
}

void List::Node::setValue(int val){
    value = val;
}

List::Node* List::Node::getNext() const{
    return next;
}

void List::Node::setNext(Node * nxt){
    next = nxt;
}

List::Node* List::Node::getPrev() const{
    return prev;
}

void List::Node::setPrev(Node * prv){
    prev = prv;
}