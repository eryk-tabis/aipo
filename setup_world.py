from src.items.item import Item
from src.characters.warrior import Warrior
from src.locations.world import World
from src.locations.location import Location
from src.cutscenes.archpriest_home import ArchpriestHomeCutscene
from src.cutscenes.manasztor_convent_cutscene import ManasztorConventCutscene
from src.cutscenes.gate_cutscene import GateCutscene
from src.cutscenes.bar_cutscene import BarCutscene
from src.cutscenes.michel_house_cutscene import MichelHouseCutscene
from src.cutscenes.sventino_cutscene import SventinoCutscene

def setup_world(obj: World):
    """Setup the world with locations and items"""
    # Archpriest house
    archpriest_house = Location()
    archpriest_house.name = "Dom Arcykapłana"
    archpriest_house.description = "Jesteś w domu Arcykapłana"
    archpriest_house.add_cutscene(ArchpriestHomeCutscene())
    # Alushakas forest
    alushakas_forest = Location()
    alushakas_forest.name = "Las Alush’haka"
    alushakas_forest.description = ("Przeszedłeś do lasu Alush’haka, uważaj na siebie,"
                                    " ponieważ czają się tutaj dzikie zwierzęta")
    archpriest_house.add_location(alushakas_forest, alushakas_forest.name)
    alushakas_forest.add_location(archpriest_house, archpriest_house.name)
    # Manasztor hill
    manasztor_hill = Location()
    manasztor_hill.name = "Wzgórze Manasztor"
    manasztor_hill.description = ("Jesteś przed ważnym wzgórzem w Twojej podróży,"
                                  " to  tutaj znajduje się klasztor do którego zmierzasz")
    alushakas_forest.add_location(manasztor_hill, manasztor_hill.name)
    manasztor_hill.add_location(alushakas_forest, alushakas_forest.name)

    # Manasztor convent
    manasztor_convent = Location()
    manasztor_convent.name = "Klasztor Manasztor"
    manasztor_convent.add_cutscene(ManasztorConventCutscene())


    # Plateau of Wijjal`s
    plateau_of_wijjal = Location()
    plateau_of_wijjal.name = "Płaskowyż Wijjala"
    plateau_of_wijjal.description = ("Ten płaskowyż służył kiedyś bandytom w celu zastawiania pułapek na przyjezdnych,"
                                     "musisz się mieć więc na baczności!!")
    manasztor_convent.add_location(plateau_of_wijjal, plateau_of_wijjal.name)
    plateau_of_wijjal.add_location(manasztor_convent, manasztor_convent.name)
    # Valley of Mijuhaj
    valley_of_mijuhaj = Location()
    valley_of_mijuhaj.name = "Dolina Mijuhaja"
    valley_of_mijuhaj.description = ("Ta dolina to spokojna oaza dla karawan,"
                                     " które zbliżają się do miasta Usisi Ashak,"
                                     " wiele zostawionych ognisk przyciąga dzikie zwierzęta")
    plateau_of_wijjal.add_location(valley_of_mijuhaj, valley_of_mijuhaj.name)
    valley_of_mijuhaj.add_location(plateau_of_wijjal, plateau_of_wijjal.name)
    # Usisi Ashak main gate
    usisi_ashak_main_gate = Location()
    usisi_ashak_main_gate.name = "Brama główna Usisi Ashak"
    usisi_ashak_main_gate.add_cutscene(GateCutscene())
    valley_of_mijuhaj.add_location(usisi_ashak_main_gate, usisi_ashak_main_gate.name)
    usisi_ashak_main_gate.add_location(valley_of_mijuhaj, valley_of_mijuhaj.name)
    # Usisi Ashak main square
    usisi_ashak_main_square = Location()
    usisi_ashak_main_square.name = "Rynek miasta"
    usisi_ashak_main_square.description = "Jesteś na rynku, możesz tu zrobić zakupy i porozmawiać z lokalnymi mieszkańcami"
    #TODO: I dont know what to do with this location
    usisi_ashak_main_gate.add_location(usisi_ashak_main_square, usisi_ashak_main_square.name)
    usisi_ashak_main_square.add_location(usisi_ashak_main_gate, usisi_ashak_main_gate.name)

    # Usisi bar
    usisi_bar = Location()
    usisi_bar.name = 'pijalnia piwska „Pijony rycerz"'
    usisi_bar.description = "Jesteś w knajpie gdzie znamienite rycerstwo spotyka się by pić alkohol"
    usisi_bar.add_cutscene(BarCutscene())
    usisi_ashak_main_square.add_location(usisi_bar, 'pijalnia piwska')
    usisi_ashak_main_gate.add_location(usisi_bar, 'pijalnia piwska')
    usisi_bar.add_location(usisi_ashak_main_square, usisi_ashak_main_square.name)
    usisi_bar.add_location(usisi_ashak_main_gate, usisi_ashak_main_gate.name)

    # Uisis underground enterance
    usisi_underground_entrance = Location()
    usisi_underground_entrance.name = "Wejście do kanałów"
    usisi_underground_entrance.description = "Smród i ciemnośc tego miejsca przyprawiają Cię o zawroty głowy, jednak musisz odnaleźć scyzoryk"
    usisi_bar.add_location(usisi_underground_entrance, usisi_underground_entrance.name)
    usisi_underground_entrance.add_location(usisi_bar, 'pijalnia piwska')

    # Usisi underground
    usisi_underground = Location()
    usisi_underground.name = "Kanały miasta"
    usisi_underground.description = "Jesteś w kanałach miasta, musisz znaleźć scyzoryk"
    usisi_underground_entrance.add_location(usisi_underground, usisi_underground.name)
    usisi_underground.add_location(usisi_underground_entrance, usisi_underground_entrance.name)

    # Michel's house
    michel_house = Location()
    michel_house.name = "Dom Michałka"
    michel_house.add_cutscene(MichelHouseCutscene())

    # Laligal's gate
    laligal_gate = Location()
    laligal_gate.name = "Brama Laligala"
    laligal_gate.description = ("Brama Laligala to miejsce z którego wyruszasz po potężną broń,"
                                " miej się na baczności i idź walczyć o swoje przeznaczenie")
    michel_house.add_location(laligal_gate, laligal_gate.name)

    # Plain of cold water
    plain_of_cold_water = Location()
    plain_of_cold_water.name = "Równina zimnej wody"
    plain_of_cold_water.description = ("Ta spokojna dolina wypełniona jest obślizgłymi jaszczurami,"
                                       " które wyglądają na wygłodniałe")
    laligal_gate.add_location(plain_of_cold_water, plain_of_cold_water.name)
    plain_of_cold_water.add_location(laligal_gate, laligal_gate.name)

    # Cold lake of the cold lake lady
    cold_lake_of_the_cold_lake_lady = Location()
    cold_lake_of_the_cold_lake_lady.name = "Jezioro zimnej pani"
    #TODO: Add crucial enenmy named "Pani jeziora"

    cold_lake_of_the_cold_lake_lady.add_location(usisi_ashak_main_square, usisi_ashak_main_square.name)

    # Road of the death
    road_of_the_death = Location()
    road_of_the_death.name = "Droga śmierci"
    road_of_the_death.description = ("Piekło tej drogi jest gorące, uważaj żeby się nie sparzyć")
    road_of_the_death.add_location(usisi_ashak_main_square, usisi_ashak_main_square.name)
    usisi_ashak_main_square.add_location(road_of_the_death, road_of_the_death.name)

    # The sinner's dodge
    the_sinners_dodge = Location()
    the_sinners_dodge.name = "Uskok grzesznika"
    the_sinners_dodge.description = ("Ten uskok był kopalnią Sventino na broń dla armi,"
                                     " która miała Cię pokononać! Musisz uważać na każdy krok")
    # Sventino`s castle enterance
    sventino_castle_enterance = Location()
    sventino_castle_enterance.name = "Wejście do zamku Sventino"
    sventino_castle_enterance.description = ("Jesteś na ostantim kroku ku swojemu przeznaczeniu!"
                                             " Przygotuj się najlepiej jak możesz i stocz walkę o swoje przeznaczenie")
    the_sinners_dodge.add_location(sventino_castle_enterance, sventino_castle_enterance.name)
    sventino_castle_enterance.add_location(the_sinners_dodge, the_sinners_dodge.name)

    # Sventino`s room
    sventino_room = Location()
    sventino_room.name = "Leże Sventino"
    sventino_room.add_cutscene(SventinoCutscene())
    #TODO: Add crucial enemy named "Sventino"
    sventino_castle_enterance.add_location(sventino_room, sventino_room.name)

    obj.current_location = archpriest_house
    return obj
