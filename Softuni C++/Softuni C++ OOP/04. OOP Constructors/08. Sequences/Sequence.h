// Sequence.h
#ifndef SEQUENCE_H
#define SEQUENCE_H

template <typename T, typename Generator>
class Sequence {
private:
    Generator generator;
    int remaining_quota;

public:
    Sequence() : remaining_quota(0) {}

    void generateNext(int n) {
        if (n > 0) {
            remaining_quota += n;
        }
    }

    class iterator {
    private:
        Sequence* sequence;
        T current_value;
        bool is_end;

        iterator(Sequence* s, bool end_flag = false)
            : sequence(s), is_end(end_flag) {
            if (!is_end) {
                if (sequence->remaining_quota > 0) {
                    current_value = sequence->generator();
                    sequence->remaining_quota--;
                } else {
                    is_end = true;
                }
            }
        }

    public:
        friend class Sequence;

        iterator& operator++() {
            if (!is_end) {
                if (sequence->remaining_quota > 0) {
                    current_value = sequence->generator();
                    sequence->remaining_quota--;
                } else {
                    is_end = true;
                }
            }
            return *this;
        }

        T operator*() const {
            return current_value;
        }

        bool operator!=(const iterator& other) const {
            return is_end != other.is_end;
        }
    };

    iterator begin() {
        return iterator(this);
    }

    iterator end() {
        return iterator(this, true);
    }
};

#endif // SEQUENCE_H