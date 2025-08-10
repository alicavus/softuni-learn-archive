#ifndef BYTES_PARSING_
#define BYTES_PARSING_

#ifndef DEFINES_H_
#include "Defines.h"
#endif

#include <iostream>
#include <vector>
#include <string>

ErrorCode parseData(const std::string &commands,
                    const char *rawDataBytes,
                    const size_t rawDataBytesCount,
                    std::vector<long long> &outParsedNumbers) {
   //outParsedNumbers.clear();
    if (commands.empty() || rawDataBytesCount == 0) {
        return PARSE_EMPTY;
    }

    size_t offset = 0;
    for (char c : commands) {
        size_t needed = 0;
        switch (c) {
            case 's': needed = 2; break;
            case 'i': needed = 4; break;
            case 'l': needed = 8; break;
            default: continue;
        }

        if (offset + needed > rawDataBytesCount) {
            return PARSE_FAILURE;
        }

        long long value = 0;
        for (size_t i = 0; i < needed; ++i) {
            unsigned char byte = static_cast<unsigned char>(rawDataBytes[offset + i]);
            value += static_cast<long long>(byte) << (8 * i);
        }

        outParsedNumbers.push_back(value);
        offset += needed;
    }

    return PARSE_SUCCESS;
}

void printResult(const ErrorCode errorCode,
                 const std::vector<long long> &parsedNumbers) {
    if (errorCode == PARSE_EMPTY) {
        std::cout << "No input provided" << std::endl;
        return;
    }

    bool first = true;
    for (long long num : parsedNumbers) {
        if (!first) {
            std::cout << " ";
        }
        std::cout << num;
        first = false;
    }

    if (errorCode == PARSE_FAILURE) {
        if (!parsedNumbers.empty()) {
            std::cout << " ";
        }
        std::cout << "Warning, buffer underflow detected";
    }

    std::cout << std::endl;
}

#endif // !BYTES_PARSING_