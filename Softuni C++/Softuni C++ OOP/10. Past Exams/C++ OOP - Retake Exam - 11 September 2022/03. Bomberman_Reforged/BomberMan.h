#ifndef BOMBERMAN_H_
#define BOMBERMAN_H_

class BomberMan{
    int power;
    public:
    BomberMan(): power(0) {};

    void bombPowerUp(){
        power++;
    }
    void bombPowerDown(){
        power--;
        if(power < 0)
            power = 0;
    }
    int placeBombCell(FieldData& fieldData, int bombRow, int bombCol){
        std::string& curRow = fieldData[bombRow];
        int points = curRow.at(bombCol) - '0';
        curRow[bombCol] = '0';
        return points;
    }
    int placeBomb(FieldData& fieldData, int bombRow, int bombCol){
        int points = placeBombCell(fieldData, bombRow, bombCol);
        size_t fieldRows{fieldData.size()};
        size_t fieldCols = (fieldRows)? fieldData.back().size() : 0;

        for(int rIdx = bombRow-power; rIdx <= bombRow+power; ++rIdx){
            if(rIdx < 0 or rIdx >= fieldRows)
                continue;
            points += placeBombCell(fieldData, rIdx, bombCol);
        }

        for(int cIdx = bombCol-power; cIdx <= bombCol+power; ++cIdx){
            if(cIdx < 0 or cIdx >= fieldCols)
                continue;
            points += placeBombCell(fieldData, bombRow, cIdx);
        }
        return points;
    }
    int getBombPower() const {
        return power;
    }
};

#endif //!  BOMBERMAN_H_