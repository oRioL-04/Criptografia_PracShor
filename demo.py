#!/usr/bin/env python3
"""
DEMO SIMPLE - Algorisme de Shor
Execució ràpida per veure l'algorisme en acció
"""

from shor_simulacio import algorisme_shor

def demo():
    print("\n" + "="*70)
    print("DEMO SIMPLE: ALGORISME DE SHOR")
    print("="*70)
    
    numeros = [15, 21, 35]
    
    for N in numeros:
        print(f"\n{'='*70}")
        print(f"Factoritzant N = {N}")
        print(f"{'='*70}\n")
        
        resultat = algorisme_shor(N, intents_maxims=5)
        
        if resultat:
            p, q = resultat
            print(f"\n{'='*70}")
            print(f"✓✓✓ ÈXIT! ✓✓✓")
            print(f"{'='*70}")
            print(f"N = {N}")
            print(f"Factors: {p} × {q}")
            print(f"Verificació: {p} × {q} = {p*q}")
            print(f"{'='*70}")
        else:
            print(f"\n✗ No s'han trobat factors")
        
        print("\n" + "-"*70 + "\n")

if __name__ == "__main__":
    demo()
