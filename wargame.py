from vikingsClasses import Soldier, Viking, Saxon, War
import random

# Lista de nombres de soldados
soldier_names = ["albert", "andres", "archie", "dani", "david", "gerard", "german", "graham", "imanol", "laura"]

# Crear instancia de War
war = War()

# Crear 5 Vikingos
for _ in range(5):
    name = random.choice(soldier_names)  # Seleccionar un nombre aleatorio
    health = 100
    strength = random.randint(50, 100)  # Fuerza aleatoria entre 50 y 100
    war.addViking(Viking(name, health, strength))

# Crear 5 Sajones
for _ in range(5):
    health = 100
    strength = random.randint(50, 100)  # Fuerza aleatoria entre 50 y 100
    war.addSaxon(Saxon(health, strength))

# Simulación de la batalla
round = 0
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    war.vikingAttack()
    war.saxonAttack()
    print(f"Round: {round} // Viking army: {len(war.vikingArmy)} warriors and Saxon army: {len(war.saxonArmy)} warriors")
    print(war.showStatus())
    round += 1
