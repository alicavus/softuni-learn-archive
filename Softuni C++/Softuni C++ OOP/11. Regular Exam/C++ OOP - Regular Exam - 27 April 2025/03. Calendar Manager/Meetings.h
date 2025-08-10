#pragma once

#include <iostream>
#include <string>
#include <memory>
#include <set>
#include "DateTime.h"
#include "Participant.h"

class Meeting{
    size_t inputOrder;
    std::string id;
    DateTimePeriod dtp;
    std::set<const Participant *> participants;

    public:
    
    typedef std::set<const Participant *> Participants;
    Meeting(size_t inputOrder, std::istream & is);
    Meeting(size_t inputOrder, const std::string & id, const DateTimePeriod & dtp);

    bool doesOverlapWith(const Meeting * m) const;
    void registerParticipant(const Participant *part);
    bool hasParticipant(const Participant* part) const{
        return participants.count(part);
    }

    //Getters
    size_t getInputOrder() const{
        return inputOrder;
    }
    const std::string& getId() const{
        return id;
    }

    const DateTimePeriod& getDateTimePeriod() const{
        return dtp;
    }

    const Meeting::Participants& getParticipants() const{
        return participants;
    }

    size_t participantCount() const{
        return participants.size();
    }



};