# Clasa Carte
class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titlu} de {self.autor}, ISBN: {self.isbn}"

# Clasa Biblioteca
class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)
        print(f"Cartea '{carte.titlu}' a fost adăugată în bibliotecă.")

    def elimina_carte(self, isbn):
        for carte in self.carti:
            if carte.isbn == isbn:
                self.carti.remove(carte)
                print(f"Cartea cu ISBN {isbn} a fost eliminată din bibliotecă.")
                return
        print(f"Cartea cu ISBN {isbn} nu a fost găsită în bibliotecă.")

    def afiseaza_carti(self):
        if not self.carti:
            print("Biblioteca este goală.")
        else:
            print("Cărțile din bibliotecă sunt:")
            for carte in self.carti:
                print(carte)

# Funcție pentru a adăuga o carte cu date introduse manual
def introdu_carte():
    titlu = input("Introdu titlul cărții: ")
    autor = input("Introdu autorul cărții: ")
    isbn = input("Introdu ISBN-ul cărții: ")
    return Carte(titlu, autor, isbn)

# Exemplu de utilizare
if __name__ == "__main__":
    biblioteca = Biblioteca()

    while True:
        print("\nMeniu Biblioteca:")
        print("1. Adaugă o carte")
        print("2. Elimină o carte")
        print("3. Afișează toate cărțile")
        print("4. Ieșire")
        
        optiune = input("Alege o opțiune: ")
        
        if optiune == "1":
            # Adăugăm o carte cu date introduse manual
            carte_noua = introdu_carte()
            biblioteca.adauga_carte(carte_noua)
        elif optiune == "2":
            # Eliminăm o carte după ISBN
            isbn = input("Introdu ISBN-ul cărții de eliminat: ")
            biblioteca.elimina_carte(isbn)
        elif optiune == "3":
            # Afișăm toate cărțile din bibliotecă
            biblioteca.afiseaza_carti()
        elif optiune == "4":
            # Ieșim din program
            print("caca")
            break
        else:
            print("Opțiune invalidă. Încearcă din nou.")
