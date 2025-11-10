"""
Versió Interactiva i Visual de l'Algorisme de Shor

Aquest fitxer proporciona funcions per visualitzar i entendre millor
cada pas de l'algorisme de Shor.
"""

import numpy as np
import matplotlib.pyplot as plt
from shor_simulacio import (
    crear_registre_quantic_uniforme,
    exponenciacio_modular,
    algorisme_shor
)
from math import gcd


def visualitzar_registre(registre, titol="Registre Quàntic", max_estats=20):
    """
    Visualitza les amplituds i probabilitats d'un registre quàntic.
    """
    n_estats = min(len(registre), max_estats)
    estats = range(n_estats)
    probabilitats = np.abs(registre[:n_estats])**2
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Amplituds (part real i imaginària)
    ax1.bar(estats, np.real(registre[:n_estats]), alpha=0.7, label='Part Real')
    ax1.bar(estats, np.imag(registre[:n_estats]), alpha=0.7, label='Part Imaginària')
    ax1.set_xlabel('Estat |x⟩')
    ax1.set_ylabel('Amplitud')
    ax1.set_title(f'{titol} - Amplituds')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Probabilitats
    ax2.bar(estats, probabilitats, color='green', alpha=0.7)
    ax2.set_xlabel('Estat |x⟩')
    ax2.set_ylabel('Probabilitat |ψ|²')
    ax2.set_title(f'{titol} - Probabilitats')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{titol.replace(" ", "_")}.png', dpi=150, bbox_inches='tight')
    print(f"   Gràfic desat com: {titol.replace(' ', '_')}.png")
    plt.close()


def visualitzar_funcio_modular(a, N, max_x=None):
    """
    Visualitza la funció f(x) = a^x mod N per veure la periodicitat.
    """
    if max_x is None:
        max_x = min(4 * N, 100)
    
    x_vals = range(max_x)
    y_vals = [pow(a, x, N) for x in x_vals]
    
    # Trobar el període
    for r in range(1, N):
        if pow(a, r, N) == 1:
            periode = r
            break
    
    plt.figure(figsize=(14, 6))
    plt.scatter(x_vals, y_vals, c='blue', alpha=0.6, s=50)
    plt.xlabel('x', fontsize=12)
    plt.ylabel(f'f(x) = {a}^x mod {N}', fontsize=12)
    plt.title(f'Funció Modular: f(x) = {a}^x mod {N}\nPeríode r = {periode}', fontsize=14)
    plt.grid(True, alpha=0.3)
    
    # Marcar les línies de període
    for i in range(0, max_x, periode):
        plt.axvline(x=i, color='red', linestyle='--', alpha=0.3, linewidth=1)
    
    plt.savefig(f'funcio_modular_a{a}_N{N}.png', dpi=150, bbox_inches='tight')
    print(f"   Gràfic desat com: funcio_modular_a{a}_N{N}.png")
    plt.close()


def analisi_periode(N, max_a=None):
    """
    Analitza els períodes per diferents valors de 'a' coprimer amb N.
    """
    if max_a is None:
        max_a = N
    
    resultats = []
    
    print(f"\n{'='*60}")
    print(f"ANÀLISI DE PERÍODES PER N = {N}")
    print(f"{'='*60}")
    print(f"{'a':<5} {'gcd(a,N)':<10} {'Període r':<12} {'a^r mod N':<12}")
    print("-" * 60)
    
    for a in range(2, max_a):
        g = gcd(a, N)
        
        if g == 1:  # a és coprimer amb N
            # Trobar el període
            for r in range(1, N):
                if pow(a, r, N) == 1:
                    verificacio = pow(a, r, N)
                    resultats.append((a, g, r, verificacio))
                    print(f"{a:<5} {g:<10} {r:<12} {verificacio:<12}")
                    break
    
    return resultats


def taula_exponenciacio_modular(a, N, max_mostrar=20):
    """
    Mostra una taula detallada de l'exponenciació modular.
    """
    print(f"\n{'='*60}")
    print(f"TAULA D'EXPONENCIACIÓ MODULAR: a = {a}, N = {N}")
    print(f"{'='*60}")
    print(f"{'x':<5} {'a^x':<15} {'a^x mod N':<12} {'Binari(x)':<12}")
    print("-" * 60)
    
    valors = []
    for x in range(max_mostrar):
        ax = pow(a, x)
        ax_mod = pow(a, x, N)
        binari = format(x, '08b')
        valors.append(ax_mod)
        print(f"{x:<5} {ax:<15} {ax_mod:<12} {binari:<12}")
    
    # Detectar el període visualment
    print("\nValors únics en l'ordre en què apareixen:")
    valors_unics = []
    for v in valors:
        if v not in valors_unics:
            valors_unics.append(v)
    print(valors_unics)
    
    # Trobar el període
    for r in range(1, len(valors)):
        if valors[r] == valors[0] == 1:
            print(f"\n✓ Període detectat: r = {r}")
            break


def comparar_metodes_factoritzacio(N):
    """
    Compara diferents mètodes de factorització.
    """
    print(f"\n{'='*60}")
    print(f"COMPARACIÓ DE MÈTODES DE FACTORITZACIÓ PER N = {N}")
    print(f"{'='*60}")
    
    # Mètode 1: Trial Division
    print(f"\n1. TRIAL DIVISION (Divisió per prova)")
    print(f"   Provant tots els divisors fins a √N...")
    import time
    start = time.time()
    for d in range(2, int(N**0.5) + 1):
        if N % d == 0:
            p_trial = d
            q_trial = N // d
            break
    temps_trial = time.time() - start
    print(f"   Factors trobats: {p_trial} × {q_trial} = {N}")
    print(f"   Temps: {temps_trial*1000:.4f} ms")
    print(f"   Divisions provades: {int(N**0.5)}")
    
    # Mètode 2: Algorisme de Shor
    print(f"\n2. ALGORISME DE SHOR (Simulació)")
    print(f"   Utilitzant computació quàntica (simulada)...")
    start = time.time()
    resultat = algorisme_shor(N, intents_maxims=3)
    temps_shor = time.time() - start
    if resultat:
        p_shor, q_shor = resultat
        print(f"   Factors trobats: {p_shor} × {q_shor} = {N}")
    print(f"   Temps: {temps_shor*1000:.4f} ms")
    
    # Comparació
    print(f"\n{'='*60}")
    print(f"COMPARACIÓ:")
    print(f"   Trial Division: {temps_trial*1000:.4f} ms")
    print(f"   Shor (simulat): {temps_shor*1000:.4f} ms")
    print(f"   Ràtio: {temps_shor/temps_trial:.2f}x")
    print(f"\n   NOTA: En un ordinador quàntic REAL,")
    print(f"   Shor seria molt més ràpid per N gran!")


def tutorial_interactiu():
    """
    Tutorial interactiu pas a pas de l'algorisme de Shor.
    """
    print("\n" + "="*60)
    print("TUTORIAL INTERACTIU: ALGORISME DE SHOR")
    print("="*60)
    
    # Escollir N
    print("\n1. Escollim un número compost N per factoritzar:")
    N = 15
    print(f"   N = {N}")
    
    # Escollir a
    print("\n2. Escollim un valor 'a' coprimer amb N:")
    a = 7
    print(f"   a = {a}")
    print(f"   Verificació: gcd({a}, {N}) = {gcd(a, N)}")
    
    # Mostrar la funció modular
    print("\n3. Analitzem la funció f(x) = a^x mod N:")
    taula_exponenciacio_modular(a, N, max_mostrar=12)
    
    # Visualitzar la funció
    print("\n4. Visualització de la periodicitat:")
    visualitzar_funcio_modular(a, N)
    
    # Trobar el període
    print("\n5. Trobem el període r:")
    for r in range(1, N):
        if pow(a, r, N) == 1:
            print(f"   r = {r}")
            print(f"   Verificació: {a}^{r} mod {N} = {pow(a, r, N)}")
            break
    
    # Calcular factors
    print("\n6. Calculem els factors:")
    print(f"   r és parell? {r % 2 == 0}")
    print(f"   {a}^(r/2) mod {N} = {a}^{r//2} mod {N} = {pow(a, r//2, N)}")
    print(f"   {pow(a, r//2, N)} ≠ {N-1} (≠ -1 mod {N})? {pow(a, r//2, N) != N-1}")
    
    p = gcd(pow(a, r // 2, N) - 1, N)
    q = gcd(pow(a, r // 2, N) + 1, N)
    
    print(f"\n   p = gcd({a}^{r//2} - 1, {N}) = gcd({pow(a, r//2, N) - 1}, {N}) = {p}")
    print(f"   q = gcd({a}^{r//2} + 1, {N}) = gcd({pow(a, r//2, N) + 1}, {N}) = {q}")
    
    print(f"\n7. Verificació final:")
    print(f"   {N} = {p} × {q} = {p * q} ✓")


def main():
    """
    Executa totes les visualitzacions i anàlisis.
    """
    print("\n" + "#"*60)
    print("#" + " "*58 + "#")
    print("#" + "  VISUALITZACIÓ I ANÀLISI DE L'ALGORISME DE SHOR".center(58) + "#")
    print("#" + " "*58 + "#")
    print("#"*60)
    
    # Tutorial interactiu
    tutorial_interactiu()
    
    # Anàlisi de períodes
    analisi_periode(15)
    
    # Comparació de mètodes
    comparar_metodes_factoritzacio(21)
    comparar_metodes_factoritzacio(35)
    
    # Visualització de diferents funcions modulars
    print("\n" + "="*60)
    print("GENERANT VISUALITZACIONS...")
    print("="*60)
    
    casos = [(7, 15), (2, 15), (11, 21), (13, 35)]
    for a, N in casos:
        if gcd(a, N) == 1:
            print(f"\nGenerant gràfic per a={a}, N={N}...")
            visualitzar_funcio_modular(a, N)
    
    print("\n" + "="*60)
    print("✓ Visualitzacions completades!")
    print("="*60)


if __name__ == "__main__":
    main()
