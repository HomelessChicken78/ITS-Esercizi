'''Prossimo: Tra poco dovrai assegnare voti equi ai rotoli degli esaminatori.

Rotoli dei Giudici
I Rotoli dei Giudici attendono il tuo sigillo: assegna il grado corretto con `grade(score)`,
usando soglie **decrescenti**: `A` per `score >= 90`, poi `B` `>= 80`, `C` `>= 70`, `D` `>= 60`,
altrimenti `F`. Mantieni la firma e soddisfa i test.'''

def grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
'''Hai distribuito voti equi ai rotoli del consiglio arcano.'''