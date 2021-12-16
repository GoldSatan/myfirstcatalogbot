import shelve

FILENAME = "URLs"
all_url_array = []

with shelve.open(FILENAME) as states:
    """~~~~~~~~~~~~~~~~~~~~~~~~FT_water~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    states[
        "FT_water_other_cheap"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=3&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_water_other_expensive"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=3&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_water_other_normal"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=3&country.import.usa.not=-1&price.currency=1&abroad.not=1&custom.not=0&page=0&size=20"

    states[
        "FT_water_new_cheap"] = "https://auto.ria.com/uk/newauto/search/?page=1&bodyId[]=391&bodyId[]=2890&bodyId[]=435&bodyId[]=401&bodyId[]=815&categoryId=3&order=2"
    states[
        "FT_water_new_expensive"] = "https://auto.ria.com/uk/newauto/search/?page=1&bodyId[]=391&bodyId[]=2890&bodyId[]=435&bodyId[]=401&bodyId[]=815&categoryId=3&order=1"
    states[
        "FT_water_new_normal"] = "https://auto.ria.com/uk/newauto/search/?page=1&bodyId[]=391&bodyId[]=2890&bodyId[]=435&bodyId[]=401&bodyId[]=815&categoryId=3&order=10"

    states[
        "FT_water_old_cheap"] = "https://auto.ria.com/uk/search/?indexName=auto&body.id[1]=53&body.id[2]=55&body.id[3]=51&body.id[7]=62&body.id[8]=63&categories.main.id=3&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_water_old_expensive"] = "https://auto.ria.com/uk/search/?indexName=auto&body.id[1]=53&body.id[2]=55&body.id[3]=51&body.id[7]=62&body.id[8]=63&categories.main.id=3&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_water_old_normal"] = "https://auto.ria.com/uk/search/?indexName=auto&body.id[1]=53&body.id[2]=55&body.id[3]=51&body.id[7]=62&body.id[8]=63&categories.main.id=3&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=20"

    """~~~~~~~~~~~~~~~~~~~~~~~~FT_B~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    states[
        "FT_B_other_cheap"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=1&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_B_other_expensive"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=1&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_B_other_normal"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=1&country.import.usa.not=-1&price.currency=1&abroad.not=1&custom.not=0&page=0&size=20"

    states[
        "FT_B_old_cheap"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=1&country.import.usa.not=-1&price.USD.gte=1000&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_B_old_expensive"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=1&country.import.usa.not=-1&price.USD.gte=1000&price.currency=1&sort[0].order=price.desc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_B_old_normal"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=1&country.import.usa.not=-1&price.USD.gte=1000&price.currency=1&abroad.not=0&custom.not=1&page=0&size=20"

    states["FT_B_new_cheap"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=1&order=2"
    states["FT_B_new_expensive"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=1&order=1"
    states["FT_B_new_normal"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=1&order=10"

    """~~~~~~~~~~~~~~~~~~~~~~~~FT_A~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    states[
        "FT_A_other_cheap"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=2&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_A_other_expensive"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=2&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "FT_A_other_normal"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=2&country.import.usa.not=-1&price.currency=1&abroad.not=1&custom.not=0&page=0&size=20"

    states[
        "FT_A_old_cheap"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=2&country.import.usa.not=-1&price.USD.gte=300&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_A_old_expensive"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=2&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "FT_A_old_normal"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=2&country.import.usa.not=-1&price.currency=1&abroad.not=0&custom.not=1&page=0&size=20"

    states["FT_A_new_cheap"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=2&order=2"
    states["FT_A_new_expensive"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=2&order=1"
    states["FT_A_new_normal"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=2&order=10"

    """~~~~~~~~~~~~~~~~~~~~~~~~work_C~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    states[
        "work_C_other_cheap"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=6&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "work_C_other_expensive"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=6&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "work_C_other_normal"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=6&country.import.usa.not=-1&price.currency=1&abroad.not=1&custom.not=0&page=0&size=20"

    states[
        "work_C_old_cheap"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=6&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=-1&page=0&size=20"
    states[
        "work_C_old_expensive"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=6&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=0&custom.not=1&page=0&size=20"
    states["work_C_old_normal"] = "https://auto.ria.com/uk/search/?categories.main.id=6&indexName=auto&size=20"

    states["work_C_new_cheap"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=6&order=2"
    states["work_C_new_expensive"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=6&order=1"
    states["work_C_new_normal"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=4&order=10"

    """~~~~~~~~~~~~~~~~~~~~~~~~work_B~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""

    states[
        "work_B_other_cheap"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=4&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "work_B_other_expensive"] = "https://auto.ria.com/uk/search/?indexName=order_auto&categories.main.id=4&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=1&custom.not=0&page=0&size=20"
    states[
        "work_B_other_normal"] = "https://auto.ria.com/uk/search/?categories.main.id=4&indexName=order_auto&abroad.not=1&custom.not=0&size=20"

    states[
        "work_B_old_cheap"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=4&country.import.usa.not=-1&price.currency=1&sort[0].order=price.asc&abroad.not=0&custom.not=1&page=0&size=20"
    states[
        "work_B_old_expensive"] = "https://auto.ria.com/uk/search/?indexName=auto&categories.main.id=4&country.import.usa.not=-1&price.currency=1&sort[0].order=price.desc&abroad.not=0&custom.not=1&page=0&size=20"
    states["work_B_old_normal"] = "https://auto.ria.com/uk/search/?categories.main.id=4&indexName=auto&size=20"

    states["work_B_new_cheap"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=4&order=2"
    states["work_B_new_expensive"] = "https://auto.ria.com/uk/newauto/search/?page=1&categoryId=4&order=1"
    states["work_B_new_normal"] = "https://auto.ria.com/uk/newauto/search/?categoryId=4"

all_url_array.append("FT_water_other_cheap")
all_url_array.append("FT_water_other_expensive")
all_url_array.append("FT_water_other_normal")
all_url_array.append("FT_water_new_cheap")
all_url_array.append("FT_water_new_expensive")
all_url_array.append("FT_water_new_normal")
all_url_array.append("FT_water_old_cheap")
all_url_array.append("FT_water_old_expensive")
all_url_array.append("FT_water_old_normal")
all_url_array.append("FT_B_other_cheap")
all_url_array.append("FT_B_other_expensive")
all_url_array.append("FT_B_other_normal")
all_url_array.append("FT_B_old_cheap")
all_url_array.append("FT_B_old_expensive")
all_url_array.append("FT_B_old_normal")
all_url_array.append("FT_B_new_cheap")
all_url_array.append("FT_B_new_expensive")
all_url_array.append("FT_B_new_normal")
all_url_array.append("FT_A_other_cheap")
all_url_array.append("FT_A_other_expensive")
all_url_array.append("FT_A_other_normal")
all_url_array.append("FT_A_old_cheap")
all_url_array.append("FT_A_old_expensive")
all_url_array.append("FT_A_old_normal")
all_url_array.append("FT_A_new_cheap")
all_url_array.append("FT_A_new_expensive")
all_url_array.append("FT_A_new_normal")
all_url_array.append("work_C_other_cheap")
all_url_array.append("work_C_other_expensive")
all_url_array.append("work_C_other_normal")
all_url_array.append("work_C_old_cheap")
all_url_array.append("work_C_old_expensive")
all_url_array.append("work_C_old_normal")
all_url_array.append("work_C_new_cheap")
all_url_array.append("work_C_new_expensive")
all_url_array.append("work_C_new_normal")
all_url_array.append("work_B_other_cheap")
all_url_array.append("work_B_other_expensive")
all_url_array.append("work_B_other_normal")
all_url_array.append("work_B_old_cheap")
all_url_array.append("work_B_old_expensive")
all_url_array.append("work_B_old_normal")
all_url_array.append("work_B_new_cheap")
all_url_array.append("work_B_new_expensive")
all_url_array.append("work_B_new_normal")
