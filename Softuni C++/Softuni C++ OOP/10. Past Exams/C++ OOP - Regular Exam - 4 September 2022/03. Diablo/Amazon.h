#ifndef AMAZON_H
#define AMAZON_H

class Amazon : public Hero{
    int _passiveTurn;
    public:
    Amazon() = default;

    Amazon(VitalData v) : Hero(), _passiveTurn(1){
        _name = AMAZON_NAME;
        _vitalData = v;
    }

    virtual void readSpellFromInput(SpellType spellType) override{
        SpellData spell;

        std::string line;
        getline(std::cin, line);
        std::istringstream istr(line);

        istr >> spell.name >> spell.damage;

        if(spellType == SpellType::Strong)
            istr >> spell.manaCost;
        
        size_t spellIdx = (spellType == SpellType::Strong)? STRONGER_SPELL : WEAKER_SPELL;
        
        _spells[spellIdx] = spell;        
    }
  
    //returns the produced damage
    virtual int castSpell() override {
        SpellData currSpell = (_vitalData.currMana >= _spells[STRONGER_SPELL].manaCost)?
        _spells[STRONGER_SPELL] : _spells[WEAKER_SPELL];

        if(_passiveTurn++ % AMAZON_PASSIVE_ABILITY_COUNTER == 0)
            currSpell.damage =  1.0 * currSpell.damage * (100 + AMAZON_DAMAGE_INCREASE_PERCENT) / 100;

        
        std::cout << getName() << " casting " << currSpell.name << " for " << currSpell.manaCost << " mana" << std::endl;

        _vitalData.currMana -= currSpell.manaCost;
        
        return currSpell.damage;
    }
  
    virtual void takeDamage(int damage) override {
        _vitalData.health -= damage;
        std::cout << _name << " took " << damage << " damage and is left with " << _vitalData.health << " health " << std::endl;
    }
  
    virtual void regenerate() override {
        int currManaRegain = _vitalData.manaRegenRate;
        _vitalData.currMana += _vitalData.manaRegenRate;
        if(_vitalData.currMana > _vitalData.maxMana){
            currManaRegain -= _vitalData.currMana - _vitalData.maxMana;
            _vitalData.currMana = _vitalData.maxMana;
        }
        
        std::cout << getName() << " regained " << currManaRegain << " mana for up to " << _vitalData.currMana << std::endl;

    }
  
    virtual bool isDead() const override {
        return _vitalData.health <= 0;
    }
};


#endif