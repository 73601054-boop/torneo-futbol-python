import random
import time

def mostrar_encabezado(titulo):
    print("\n" + "=" * 45)
    print(f"⚽ {titulo.center(41)} ⚽")
    print("=" * 45)

def simular_evento():
    # Eventos aleatorios durante los partidos
    eventos = [
        "🔥 ¡Gran atajada del portero!",
        "🟡 Tarjeta amarilla por falta táctica.",
        "💥 ¡Remate en el poste! Se salva el equipo.",
        "🎯 ¡Pase filtrado sensacional!",
        "🟥 ¡Tarjeta roja por entrada a destiempo!"
    ]
    return random.choice(eventos)

def jugar_partido(equipo1, equipo2):
    mostrar_encabezado(f"PARTIDO: {equipo1} vs {equipo2}")
    
    goles1 = 0
    goles2 = 0
    
    # Simulación minuto a minuto
    minutos = [15, 30, 45, 60, 75, 90]
    
    for minuto in minutos:
        time.sleep(0.8) # Pausa para darle suspenso
        print(f"\n⏱️ Minuto {minuto}':")
        
        # Probabilidad de evento o gol
        azar = random.random()
        if azar < 0.35:
            # ¡Gol de Equipo 1!
            goles1 += 1
            print(f"⚽ ¡GOOOOOOL DE {equipo1.upper()}! ({goles1} - {goles2})")
        elif azar < 0.70:
            # ¡Gol de Equipo 2!
            goles2 += 1
            print(f"⚽ ¡GOOOOOOL DE {equipo2.upper()}! ({goles1} - {goles2})")
        else:
            # Ocurre una jugada destacada
            print(f"   {simular_evento()}")

    time.sleep(1)
    mostrar_encabezado(f"RESULTADO FINAL: {equipo1} {goles1} - {goles2} {equipo2}")

    # Definición por penales si hay empate
    if goles1 == goles2:
        print("\n🤝 ¡Empate en los 90 minutos! Nos vamos a TANDA DE PENALES... 🥅")
        penales1 = 0
        penales2 = 0
        
        for i in range(1, 4): # 3 tiros por equipo
            time.sleep(0.6)
            penales1 += random.choice([1, 0])
            penales2 += random.choice([1, 0])
            print(f"  Tiro {i}: {equipo1} ({penales1}) - ({penales2}) {equipo2}")

        if penales1 == penales2:
            print("  ¡Muerte súbita! Un tiro más...")
            penales1 += random.choice([1, 0])
            penales2 += random.choice([1, 0])

        if penales1 > penales2:
            ganador = equipo1
        else:
            ganador = equipo2
            
        print(f"\n🏆 ¡{ganador} gana el partido en la tanda de penales!")
        return ganador
    else:
        ganador = equipo1 if goles1 > goles2 else equipo2
        print(f"\n🏆 ¡{ganador} avanza de ronda!")
        return ganador

def iniciar_torneo():
    mostrar_encabezado("GRAN TORNEO DE FÚTBOL MVP")
    print("Ingresa los 4 equipos clasificados al torneo:")
    
    e1 = input("1. Primer equipo: ").strip() or "Real Madrid"
    e2 = input("2. Segundo equipo: ").strip() or "Barcelona"
    e3 = input("3. Tercer equipo: ").strip() or "Bayern Múnich"
    e4 = input("4. Cuarto equipo: ").strip() or "PSG"

    # Semifinal 1
    mostrar_encabezado("PRIMERA SEMIFINAL")
    finalista1 = jugar_partido(e1, e2)
    
    input("\nPresiona ENTER para jugar la Segunda Semifinal...")

    # Semifinal 2
    mostrar_encabezado("SEGUNDA SEMIFINAL")
    finalista2 = jugar_partido(e3, e4)

    input("\nPresiona ENTER para jugar la GRAN FINAL...")

    # Gran Final
    mostrar_encabezado("GRAN FINAL DEL TORNEO")
    campeon = jugar_partido(finalista1, finalista2)

    # Celebración
    print("\n" + "🎉" * 20)
    print(f"   🏆 ¡¡{campeon.upper()} ES EL CAMPEÓN DEL TORNEO!! 🏆")
    print("🎉" * 20 + "\n")

if __name__ == "__main__":
    iniciar_torneo()