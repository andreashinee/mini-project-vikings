import random

# Soldier
class Soldier:
    """
    La clase Soldier es la base de donde heredan los Vikingos y los Sajones.
    Representa un soldado genérico con atributos básicos de salud y fuerza.
    """
    def __init__(self, health, strength):
        self.health = health  # Salud del soldado
        self.strength = strength  # Fuerza del soldado
    
    def attack(self):
        """
        Método para atacar. Devuelve la fuerza del soldado.
        """
        return self.strength

    def receiveDamage(self, damage):
        """
        Método para recibir daño. Reduce la salud del soldado en base al daño recibido.
        """
        self.health -= damage


# Viking
class Viking(Soldier):
    """
    La clase Viking hereda de Soldier y representa a un guerrero vikingo.
    Los vikingos tienen un nombre y un grito de batalla único.
    """
    def __init__(self, name, health, strength):
        super().__init__(health, strength)  # Inicializamos los atributos del Soldier
        self.name = name  # Nombre del vikingo

    def battleCry(self):
        """
        Devuelve el grito de batalla del vikingo.
        """
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        """
        Método para recibir daño. Reduce la salud y devuelve un mensaje dependiendo de si el vikingo sigue vivo o no.
        """
        self.health -= damage
        if self.health > 0:  # Si sigue vivo
            return f"{self.name} has received {damage} points of damage"
        else:  # Si muere
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier):
    """
    La clase Saxon también hereda de Soldier y representa a un guerrero sajón.
    """
    def __init__(self, health, strength):
        super().__init__(health, strength)  # Inicializamos los atributos del Soldier

    def receiveDamage(self, damage):
        """
        Método para recibir daño. Reduce la salud y devuelve un mensaje dependiendo de si el sajón sigue vivo o no.
        """
        self.health -= damage
        if self.health > 0:  # Si sigue vivo
            return f"A Saxon has received {damage} points of damage"
        else:  # Si muere
            return "A Saxon has died in combat"


# War
class War:
    """
    La clase War representa la batalla entre Vikingos y Sajones.
    Administra los ejércitos y las interacciones entre ellos.
    """
    def __init__(self):
        self.vikingArmy = []  # Lista para el ejército vikingo
        self.saxonArmy = []  # Lista para el ejército sajón

    def addViking(self, viking):
        """
        Añade un vikingo al ejército vikingo.
        """
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        """
        Añade un sajón al ejército sajón.
        """
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """
        Simula un ataque vikingo. Un vikingo al azar ataca a un sajón al azar.
        """
        if self.saxonArmy:  # Solo si hay sajones
            saxon = random.choice(self.saxonArmy)  # Seleccionamos un sajón al azar
            viking = random.choice(self.vikingArmy)  # Seleccionamos un vikingo al azar
            result = saxon.receiveDamage(viking.attack())  # El sajón recibe daño
            if saxon.health <= 0:  # Si el sajón muere, lo eliminamos del ejército
                self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        """
        Simula un ataque sajón. Un sajón al azar ataca a un vikingo al azar.
        """
        if self.vikingArmy:  # Solo si hay vikingos
            saxon = random.choice(self.saxonArmy)  # Seleccionamos un sajón al azar
            viking = random.choice(self.vikingArmy)  # Seleccionamos un vikingo al azar
            result = viking.receiveDamage(saxon.attack())  # El vikingo recibe daño
            if viking.health <= 0:  # Si el vikingo muere, lo eliminamos del ejército
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        """
        Devuelve el estado actual de la guerra.
        """
        if not self.saxonArmy:  # Si no hay sajones vivos
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:  # Si no hay vikingos vivos
            return "Saxons have fought for their lives and survive another day..."
        else:  # Si todavía hay batalla
            return "Vikings and Saxons are still in the thick of battle."


# War2 (opcional, similar a War)
class War2:
    """
    Clase adicional similar a War para otras posibles implementaciones.
    """
    def __init__(self):
        self.vikingArmy = []  # Lista para el ejército vikingo
        self.saxonArmy = []  # Lista para el ejército sajón

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = saxon.receiveDamage(viking.attack())
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        if self.vikingArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = viking.receiveDamage(saxon.attack())
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
