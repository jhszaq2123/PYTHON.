from graphviz import Digraph

dot = Digraph()

dot.attr(rankdir='TB', size='12')

dot.node('A', 'Zgłoszenie telefoniczne (sekretariat)', shape='ellipse')
dot.node('B', 'Połączenie z pielęgniarką', shape='box')
dot.node('C', 'Ocena pacjenta (pielęgniarka)', shape='diamond')
dot.node('D', 'Wypełnienie formularza rejestracyjnego', shape='parallelogram')
dot.node('E', 'Automatyczne zapisanie danych w systemie', shape='box')
dot.node('F', 'Generowanie karty pacjenta online', shape='parallelogram')
dot.node('G', 'Automatyczne dodanie pacjenta do listy nowych zgłoszeń', shape='box')
dot.node('H', 'Bieżące przypisanie pacjenta do personelu (bez czekania na spotkanie w środę)', shape='ellipse')
dot.node('I', 'Przydzielenie pacjenta do personelu', shape='box')
dot.node('J', 'Automatyczne przekazanie danych do przyjmujących', shape='box')
dot.node('K', 'Przygotowanie kart rejestracyjnych', shape='parallelogram')
dot.node('L', 'Elektroniczna prośba o kartotekę medyczną (jeśli wymagana)', shape='box')
dot.node('M', 'Spotkanie pierwszego przyjmującego', shape='ellipse')
dot.node('N', 'Spotkanie drugiego przyjmującego (po otrzymaniu dokumentacji)', shape='ellipse')
dot.node('O', 'Dodanie pacjenta do listy "po rozmowach"', shape='box')
dot.node('P', 'Planowanie leczenia online i omówienie podczas spotkania zespołu', shape='ellipse')
dot.node('Q', 'Zakończenie procedury przyjęcia', shape='parallelogram')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI', 'IJ', 'JK', 'IL', 'KM', 'LN', 'MO', 'NO', 'OP', 'PQ'])

dot.render('proces_przyjec_to_be', format='png', cleanup=False)