from tools.pmongo import Mongo        

mongo = Mongo()


servers_list = [
    {"name": "APP-RDBLD-004", "owner": "Shahar Sonino "},
    {"name": "APP-RDBLD-005", "owner": "Tal Kariv "},
    {"name": "APP-RDBLD-006", "owner": "Yitzhak Steinmetz"},
    {"name": "APP-RDBLD-007", "owner": "Ilan Lupu"},
    {"name": "APP-RDBLD-008", "owner": ""},
    {"name": "APP-RDBLD-009", "owner": "Michael Mushailov"},
    {"name": "APP-RDBLD-010", "owner": "yanivn"},
    {"name": "APP-RDBLD-011", "owner": "Sophie Gerzi"},
    {"name": "APP-RDBLD-012", "owner": "Yehezkel Bernat"},
    {"name": "APP-RDBLD-013", "owner": "Guy Yom Tov"},
    {"name": "APP-RDBLD-014", "owner": "Alon Shmueli"},
    {"name": "APP-RDBLD-015", "owner": "Roman Golubchyck "},
    {"name": "APP-RDBLD-016", "owner": "Vassilii Khachaturov"},
    {"name": "APP-RDBLD-017", "owner": "Matan Paz"},
    {"name": "APP-RDBLD-018", "owner": "Noam Helfman"},
    {"name": "APP-RDBLD-019", "owner": "Ron Ben Ishay"},
    {"name": "APP-RDBLD-020", "owner": "Gil Kulish Tool Machine"},
    {"name": "APP-RDBLD-021", "owner": "Itzik mattia"},
    {"name": "APP-RDBLD-022", "owner": "Ron Ben Ishay"},
    {"name": "APP-RDBLD-023", "owner": "Matan Paz"},
    {"name": "APP-RDBLD-024", "owner": "Yaniv Franco"},
    {"name": "APP-RDBLD-025", "owner": "Ron Ben Ishay"},
    {"name": "APP-RDBLD-026", "owner": "Oleg Yudayev"},
    {"name": "APP-RDBLD-027", "owner": "Alex Reitbort"},
    {"name": "APP-RDBLD-028", "owner": "Gil antaki"},
    {"name": "APP-RDBLD-029", "owner": "Maor Kashanski"},
    {"name": "APP-RDBLD-030", "owner": "Sole"},
    {"name": "APP-RDBLD-031", "owner": "Sole"},
    {"name": "APP-RDBLD-032", "owner": "Dead"},
    {"name": "APP-RDBLD-050", "owner": "Roy Dallal"},
    {"name": "APP-RDBLD-051", "owner": "Alon Shmuely"},
    {"name": "APP-RDBLD-052", "owner": "Alex Reitbort"},
    {"name": "APP-RDBLD-053", "owner": "Chaya Binet"},
    {"name": "APP-RDBLD-054", "owner": "Israela solomon"},
    {"name": "APP-RDBLD-055", "owner": "Noga Grebla "},
    {"name": "APP-RDBLD-056", "owner": "Matan Genish "},
    {"name": "APP-RDBLD-057", "owner": "Raz Azaria "},
    {"name": "APP-RDBLD-058", "owner": "Idan Ungar"},
    {"name": "APP-RDBLD-059", "owner": "Itay Ariav "},
    {"name": "APP-RDBLD-060", "owner": "Itay Ariav "},
    {"name": "APP-RDBLD-061", "owner": "Pninit Goldman"},
    {"name": "APP-RDBLD-062", "owner": "Yarden Cohen"},
    {"name": "APP-RDBLD-063", "owner": "Tal Kariv"},
    {"name": "APP-RDBLD-064", "owner": "Oren Gordon"},
    {"name": "APP-RDBLD-065", "owner": ""},
    {"name": "APP-RDBLD-066", "owner": "Tal Buhadana"},
    {"name": "APP-RDBLD-067", "owner": "Shield Team / ShadowMaker"},
    {"name": "APP-RDBLD-068", "owner": "Natalia Kazantsev"},
    {"name": "APP-RDBLD-069", "owner": "Aysar Shahwan"},
    {"name": "APP-RDBLD-070", "owner": "Shield Core (OCE)"},
    {"name": "APP-RDBLD-071", "owner": "Eldar Ronen"},
    {"name": "APP-RDBLD-072", "owner": "Shani Kabariti"},
    {"name": "APP-RDBLD-073", "owner": "Michael Mushailov"},
    {"name": "APP-RDBLD-074", "owner": "Ron Ben Ishay"},
    {"name": "APP-RDBLD-075", "owner": "Guy Yom Tov"},
    {"name": "APP-RDBLD-076", "owner": "Sole"},
    {"name": "APP-RDBLD-077", "owner": "Yarden Cohen"},
    {"name": "APP-RDBLD-078", "owner": "Shmuel Mirowitz"},
    {"name": "APP-RDBLD-079", "owner": "Dia Hanady"},
    {"name": "APP-RDBLD-080", "owner": "Shield Core / Pfgold"},
    {"name": "APP-RDBLD-081", "owner": "Eldar Ronen"},
    {"name": "APP-RDBLD-082", "owner": "Eyal Gaber "},
    {"name": "APP-RDBLD-083", "owner": "Michael Yaron"},
    {"name": "APP-RDBLD-084", "owner": "Oshri Cohen"},
    {"name": "XLIL-RD001", "owner": "MaorK + YitzhakS"},
    {"name": "XLIL-RD002", "owner": "Alaa Nasar"},
    {"name": "XLIL-RD003", "owner": "Aviad Gigi"},
    {"name": "XLIL-RD004", "owner": "Aviad Har-Tal"},
    {"name": "XLIL-RD005", "owner": "Guy Yom Tov"},
    {"name": "XLIL-RD006", "owner": "Duaa Abbas"},
    {"name": "XLIL-RD007", "owner": "Nahum Farchi"},
    {"name": "XLIL-RD008", "owner": "Eran Rubinstein"},
    {"name": "XLIL-RD009", "owner": "Gil Kulish"},
    {"name": "XLIL-RD010", "owner": "Golan Bitan (Shield)"},
    {"name": "XLIL-RD011", "owner": "Vladimir Cheskis"},
    {"name": "XLIL-RD012", "owner": "Itzik Mattatia"},
    {"name": "XLIL-RD013", "owner": "Shield  Hack"},
    {"name": "XLIL-RD014", "owner": "Lior Zilberstein"},
    {"name": "XLIL-RD015", "owner": "Matan Bezen"},
    {"name": "XLIL-RD016", "owner": "Noam Malki"},
    {"name": "XLIL-RD017", "owner": "Shani Kabariti"},
    {"name": "XLIL-RD018", "owner": "Alon Shmueli"},
    {"name": "XLIL-RD019", "owner": "Rivka Aharonov"},
    {"name": "XLIL-RD020", "owner": "Roy Dallal"},
    {"name": "XLIL-RD021", "owner": "Daniel Maor"},
    {"name": "XLIL-RD022", "owner": "Yarden Cohen"},
    {"name": "XLIL-RD023", "owner": "Michael Yaron"},
    {"name": "XLIL-RD024", "owner": "Oden Hanson"},
    {"name": "XLIL-RD025", "owner": "Matan Genish "},
    {"name": "XLIL-RD026", "owner": "David Bornshtein"},
    {"name": "XLIL-RD027", "owner": "Sasha An"},
    {"name": "XLIL-RD028", "owner": "Shmuel Mirowitz"},
    {"name": "XLIL-RD029", "owner": "Daniel Bublil"},
    {"name": "XLIL-RD030", "owner": "Joe Graham"},
    {"name": "XLIL-RD031", "owner": "Oshri Cohen"},
    {"name": "XLIL-RD032", "owner": "Vassilii Khachaturov"},
    {"name": "XLIL-RD033", "owner": "Haim Sawdayee"},
    {"name": "XLIL-RD034", "owner": "Gil Antaki"}
]


for name in servers_list:
    mongo.update("machines", {"name": name["name"]}, name)

