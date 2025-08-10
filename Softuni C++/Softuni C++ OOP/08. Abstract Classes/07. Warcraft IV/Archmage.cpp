#include "Archmage.h"
#include <iostream>

Archmage::Archmage(const std::string & name,
    const int           maxMana,
    const int           baseManaRegenRate,
    const int			 manaRegenModifier)
    : Hero(name, maxMana, baseManaRegenRate), _manaRegenModifier(manaRegenModifier){}

void Archmage::castSpell(const SpellType spell){
   if(this->_currMana >= _spells[spell].manaCost){
    this->_currMana -= _spells[spell].manaCost;
    std::cout << this->_name << " casted " << _spells[spell].name << " for " << _spells[spell].manaCost << " mana" << std::endl;
    if(spell == SpellType::ULTIMATE)
        regenerateMana();
   }
   else {
    std::cout << this->_name << " - not enough mana to cast " << _spells[spell].name << std::endl;
   }
}

void Archmage::regenerateMana(){
    _currMana += _manaRegenRate * _manaRegenModifier;

    if(_currMana > _maxMana)
        _currMana = _maxMana;

}
