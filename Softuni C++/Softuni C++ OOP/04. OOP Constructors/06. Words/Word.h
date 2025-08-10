#ifndef WORD_H
#define WORD_H

#include <string>
#include <unordered_map>

class Word {
    static std::unordered_map<std::string, size_t> counts;
    static size_t instance_count;
    std::string word;

public:
    Word(const std::string& w);
    Word(const Word& other);
    Word(Word&& other);
    ~Word();

    std::string getWord() const;
    size_t getCount() const;
    bool operator<(const Word& other) const;
};

#endif // WORD_H
