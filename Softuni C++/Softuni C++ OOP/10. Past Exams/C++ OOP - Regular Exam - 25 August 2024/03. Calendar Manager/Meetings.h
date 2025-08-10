#ifndef _MEETINGS_H_
#define _MEETINGS_H_

#include <iostream>
#include <string>
#include <set>
#include <memory>
#include "DateTime.h"
#include "Participant.h"

class Meeting{
    size_t inputOrder;
    std::string id;
    DateTimePeriod dtp;
    std::set<const Participant *> participants;

    public:
    Meeting(size_t inputOrder, std::istream & is);
    Meeting(size_t inputOrder, const std::string & id, const DateTimePeriod & dtp);

    bool doesOverlapWith(const Meeting * m) const;
    void registerParticipant(const Participant *part);

    typedef std::set<const Participant *> Participants;

    bool hasParticipant(const Participant * part) const{
        return participants.count(part);
    }

    const std::string& getId() const{
        return id;
    }

    size_t participantCount() const{
        return participants.size();
    }

    size_t getInputOrder() const{
        return inputOrder;
    }

    const Participants& getParticipants() const{
        return participants;
    }

    const DateTimePeriod& getDateTimePeriod() const{
        return dtp;
    }
};


#endif //! _MEETINGS_H_