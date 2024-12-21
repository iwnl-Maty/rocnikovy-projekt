![Verze](https://img.shields.io/badge/Verze-1.0--Mapa_turistických_cest-purple)
[![Programátor](https://img.shields.io/badge/Programátor-Matyáš_Pierník-green)](https://github.com/iwnl-Maty)
![Framework](https://img.shields.io/badge/Framework-Flask-blue?logo=flask&link=https://flask.palletsprojects.com/)
# Interaktivní mapa turistických tras

## Popis projektu
Tento projekt je webová aplikace vytvořená jako maturitní práce. Slouží k prohlížení interaktivní mapy s turistickými trasami a zajímavými body zájmu. Uživatelé mohou zobrazovat detaily jednotlivých míst, filtrovat je podle kategorií a prohlížet jejich polohu na mapě. Hlavním cílem projektu je vytvořit intuitivní a přehlednou aplikaci, která uživatelům usnadní objevování turistických atrakcí.

## Hlavní funkce
- **Zobrazení mapy**: Interaktivní mapa s body zájmu (např. turistické atrakce, restaurace, vyhlídky).
- **Detail bodu zájmu**: Informace o místě včetně názvu, popisu a případně obrázku.
- **Vyhledávání a filtrování**: Možnost vyhledat body podle názvu nebo kategorie.
- **Responzivní design**: Aplikace je optimalizována pro mobilní i desktopová zařízení.
- **Implementace API**: Využití OpenStreetMap API k zobrazení mapy a integraci dat o turistických trasách.
- **Přidávání bodů zájmu** *(volitelná funkce)*: Administrátoři mohou přidávat nové body přímo do systému.

## Použité technologie

### Backend
- **Flask**: Pro backend aplikace a správu požadavků na serveru.
- **SQLite**: Lehká databáze pro ukládání informací o bodech zájmu.

### Frontend
- **HTML, CSS, Bootstrap**: Pro responsivní a moderní design aplikace.
- **Leaflet.js**: Knihovna pro práci s interaktivními mapami.

### API
- **OpenStreetMap API**: Pro načítání a zobrazování mapových podkladů a dat.

## API a jeho funkcionality

### OpenStreetMap API
Projekt využívá OpenStreetMap API pro:
- Zobrazení mapových podkladů.
- Přidání vlastních bodů zájmu na mapu (např. Praděd, Šerák v Jeseníkách).
- Filtrování bodů podle kategorií.

## Budoucí rozšíření
- **Uživatelská přizpůsobení**: Možnost registrovaných uživatelů ukládat oblíbené body.
- **Pokročilé filtrování**: Přidání více kategorií a možnosti vyhledávání podle vzdálenosti.
- **Vícejazyčnost**: Podpora více jazyků pro zahraniční turisty.
- **Analytické nástroje**: Získávání dat o nejnavštěvovanějších místech.