#include "DrawRanger.h"
#include <iostream>

DrawRanger::DrawRanger(const std::string & name,
    const int           maxMana,
    const int           baseManaRegenRate)
    :Hero(name, maxMana, baseManaRegenRate){}



void DrawRanger::castSpell(const SpellType spell)
{
    if(this->_currMana >= _spells[spell].manaCost){
     this->_currMana -= _spells[spell].manaCost;
     std::cout << this->_name << " casted " << _spells[spell].name << " for " << _spells[spell].manaCost << " mana" << std::endl;
     if(spell == SpellType::BASIC)
        std::cout << _name << " casted " << _spells[SpellType::BASIC].name << " for 0 mana" << std::endl;
    }
    else {
     std::cout << this->_name << " - not enough mana to cast " << _spells[spell].name << std::endl;
    }
    
}

void DrawRanger::regenerateMana()
{
    _currMana += _manaRegenRate;

    if(_currMana > _maxMana)
        _currMana = _maxMana;

}
