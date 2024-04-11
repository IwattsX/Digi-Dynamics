from .models import select
import re


def DLCSearch_Handler(response, searchBy : str, DLC : list):
    if searchBy == 'name':
        name = response.GET.get('name', None)
        
        # This doesn't display anything and doesn't do the name REGEXP '' that will always be true
        if name is None or name == "":
            return
        Games_res = select("DLC", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date", 
        whereClause=f"Name REGEXP '{name}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            DLC.append(row)
    
    elif searchBy == "genre":
        genres = response.GET.getlist('genres', None)

        # Same thing, we want input there
        if genres is None or len(genres) == 0:
            return
        
        genres_regex = ""
        for i, genre in enumerate(genres):
            genres_regex += f"{genre}"
            if i == len(genres) - 1:
                break
            genres_regex += "|"

        # print(genres_regex)

        Games_res = select("DLC", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                           whereClause=f"Genre REGEXP '{genres_regex}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            DLC.append(row)

    elif searchBy == 'publisher':
        publisher = response.GET.get('name', None)
        if publisher is None or publisher == "":
            return
        
        Games_res = select("DLC",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                            whereClause=f"Publisher LIKE '%{publisher}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            DLC.append(row)

    elif searchBy == 'developer':
        developer = response.GET.get('name', None)
        if developer is None or developer == "":
            return
        Games_res = select("DLC",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                        whereClause=f"Developer LIKE '%{developer}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            DLC.append(row)


    elif searchBy == 'price':
        priceStr = response.GET.get('price', None)
        if priceStr is None or priceStr == "":
            return
        

        price = float(priceStr) * 100


        Games_res = select("DLC",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Current_price < {price}")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            DLC.append(row)


    elif searchBy == 'dateyear':
        date = response.GET.get('year', None)
        if date is None or date == "":
            return
        
        year = int(date)

        Games_res = select("DLC",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Release_Date REGEXP '\\\\d{{4}}'")
        
        for row in Games_res:
            regex_year = "(\\d{4})"
            release_str = row["Release_Date"]
            temp = re.search(regex_year, release_str)

            release_year = int(temp.group(1))
            if year == release_year:
                # print(f"Year {year} release_year = {release_year}")
                if not row.get("Base_price") is None:
                    row["Base_price"] = row["Base_price"]/100
                if not row.get("Current_price") is None:
                    row["Current_price"] = row["Current_price"]/100
                DLC.append(row)



def GamesSearch_Handler(response, searchBy: str, games : list):

    print(searchBy)
    if searchBy == 'name':
        name = response.GET.get('name', None)
        
        # This doesn't display anything and doesn't do the name REGEXP '' that will always be true
        if name is None or name == "":
            return
        Games_res = select("Games", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date", 
        whereClause=f"Name REGEXP '{name}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)
    
    elif searchBy == "genre":
        genres = response.GET.getlist('genres', None)

        # Same thing, we want input there
        if genres is None or len(genres) == 0:
            return
        
        genres_regex = ""
        for i, genre in enumerate(genres):
            genres_regex += f"{genre}"
            if i == len(genres) - 1:
                break
            genres_regex += "|"

        # print(genres_regex)

        Games_res = select("Games", columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                           whereClause=f"Genre REGEXP '{genres_regex}'")
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)

    elif searchBy == 'publisher':
        publisher = response.GET.get('name', None)
        if publisher is None or publisher == "":
            return
        
        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                            whereClause=f"Publisher LIKE '%{publisher}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)

    elif searchBy == 'developer':
        developer = response.GET.get('name', None)
        if developer is None or developer == "":
            return
        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                        whereClause=f"Developer LIKE '%{developer}%'")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)


    elif searchBy == 'price':
        priceStr = response.GET.get('price', None)
        if priceStr is None or priceStr == "":
            return
        

        price = float(priceStr) * 100


        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Current_price < {price}")
        
        for row in Games_res:
            if not row.get("Base_price") is None:
                row["Base_price"] = row["Base_price"]/100
            if not row.get("Current_price") is None:
                row["Current_price"] = row["Current_price"]/100
            games.append(row)


    elif searchBy == 'dateyear':
        date = response.GET.get('year', None)
        if date is None or date == "":
            return
        
        year = int(date)

        Games_res = select("Games",columns="id, Name, Short_description, Base_price, Current_price, Coming_soon, Release_Date",
                    whereClause=f"Release_Date REGEXP '\\\\d{{4}}'")
        
        for row in Games_res:
            regex_year = "(\\d{4})"
            release_str = row["Release_Date"]
            temp = re.search(regex_year, release_str)

            release_year = int(temp.group(1))
            if year == release_year:
                # print(f"Year {year} release_year = {release_year}")
                if not row.get("Base_price") is None:
                    row["Base_price"] = row["Base_price"]/100
                if not row.get("Current_price") is None:
                    row["Current_price"] = row["Current_price"]/100
                games.append(row)