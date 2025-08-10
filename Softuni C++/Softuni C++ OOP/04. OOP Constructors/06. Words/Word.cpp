#include "Word.h"

std::unordered_map<std::string, size_t> Word::counts;
size_t Word::instance_count = 0;

Word::Word(const std::string& w) : word(w) {
    ++counts[word];
    ++instance_count;
}

Word::Word(const Word& other) : word(other.word) {
    ++instance_count;
}

Word::Word(Word&& other) : word(std::move(other.word)) {
    ++instance_count;
}

Word::~Word() {
    --instance_count;
    if (instance_count == 0) {
        counts.clear();
    }
}

std::string Word::getWord() const {
    return word;
}

size_t Word::getCount() const {
    return counts.at(word);
}

bool Word::operator<(const Word& other) const {
    return word < other.word;
}
