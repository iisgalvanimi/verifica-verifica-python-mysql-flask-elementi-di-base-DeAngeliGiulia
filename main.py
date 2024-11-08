import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Animali")
mycursor.execute("CREATE TABLE Pesci(ID INT Primary key AUTO_INCREMENT, Nome_Comune VARCHAR(255) NOT NULL, Famiglia VARCHAR(255) NOT NULL, Ambiente VARCHAR(255) NOT NULL, Dimensioni VARCHAR(255) NOT NULL, Alimentazione VARCHAR(255) NOT NULL)")

sql = "INSERT INTO Pesci (Nome_Comune, Famiglia, Ambiente, Dimensioni, Alimentazione) VALUES (%s, %s, %s, %s, %s)"
val = [
('Pesce rosso', 'Cyprinidae', 'Acqua dolce', '5-10cm', 'Vermi, Fiocchi'),
('Salmone', 'Salmonidae', 'Acqua salata', '1m', 'Pesci più piccoli'),
('Squalo', 'Squalidae', 'Acqua salata', '2-20m', 'Pesci, Crostacei'),
('Tilapia', 'Cichlidae', 'Acqua dolce', '20-30cm', 'Alghe, Insetti'),
('Anguilla', 'Anguillidae', 'Acqua dolce e salata', '1m', 'Pesci più piccoli, Crostacei'),
('Tonno', 'Scombridae', 'Acqua salata', '2-3m', 'Pesci più piccoli'),
('Murena', 'Muraenidae', 'Acqua salata', '1-3m', 'Pesci, Crostacei'),
('Carpa', 'Cyprinidae', 'Acqua dolce', '50-100cm', 'Vermi, Piante acquatiche'),
('Triglia', 'Triglidae', 'Acqua salata', '20-30cm', 'Crostacei, Molluschi')
]