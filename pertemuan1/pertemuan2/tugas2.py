#Tugas list
thislistnilai = [75, 80, 65, 90, 85]

thislistnilai.append(95)
print(thislistnilai)

thislistnilai.remove(65)
print(thislistnilai)

thislistnilai.sort()
print(thislistnilai)

print(max(thislistnilai))
print(min(thislistnilai))
print(len(thislistnilai))

rata_rata = sum(thislistnilai) / len(thislistnilai)
print(rata_rata)
print(thislistnilai)

#Tugas set
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}

print(keahlian_A)
print(keahlian_B)

#keahlian mahasiswa a
print("SQL" in keahlian_B)
print("Java" in keahlian_B)