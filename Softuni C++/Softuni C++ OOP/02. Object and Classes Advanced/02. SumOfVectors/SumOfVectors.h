#ifndef SUMOFVECTORS_H
#define SUMOFVECTORS_H

#ifndef _GLIBCXX_VECTOR
#include <vector>
#endif

#ifndef _GLIBCXX_STRING
#include <string>
#endif

std::vector<std::string> operator+(const std::vector<std::string> &v1, const std::vector<std::string> &v2){
    std::vector<std::string>v;
    size_t s1 = v1.size();
    size_t s2 = v2.size();
    size_t minSize = std::min(s1, s2);
    size_t maxSize = std::max(s1, s2);

    for(size_t idx = 0; idx < minSize; ++idx)
        v.push_back(v1[idx] + ' ' + v2[idx]);
    
    const std::vector<std::string> *vp = (s1 > s2)? &v1 : &v2;

    for(size_t idx = minSize; idx < maxSize; ++idx )
        v.push_back(vp->at(idx));
    
    return v;
}

#endif // !SUMOFVECTORS_H