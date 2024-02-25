import os
import time
import random
import pyfiglet
import colorama
import phonenumbers
from termcolor import colored

# Initialize colorama
colorama.init()

# Define phone number formats for each country
phone_formats = {
    'USA': '+1##########',
    'CANADA': '+1##########',
    'AFGHANISTAN': '+93#########',
    'ARMENIA': '+374#########',
    'AZERBAIJAN': '+994#########',
    'BAHRAIN': '+973########',
    'BANGLADESH': '+880##########',
    'BHUTAN': '+975########',
    'BRUNEI': '+673########',
    'CAMBODIA': '+855#########',
    'CHINA': '+86###########',
    'CYPRUS': '+357########',
    'GEORGIA': '+995#########',
    'INDIA': '+91##########',
    'INDONESIA': '+62###########',
    'IRAN': '+98###########',
    'IRAQ': '+964##########',
    'ISRAEL': '+972##########',
    'JAPAN': '+81##########',
    'JORDAN': '+962##########',
    'KAZAKHSTAN': '+7###########',
    'KUWAIT': '+965########',
    'KYRGYZSTAN': '+996#########',
    'LAOS': '+856#########',
    'LEBANON': '+961#########',
    'MALAYSIA': '+60##########',
    'MALDIVES': '+960#########',
    'MONGOLIA': '+976#########',
    'MYANMAR': '+95#########',
    'NEPAL': '+977#########',
    'NORTH KOREA': '+850#########',
    'OMAN': '+968########',
    'PAKISTAN': '+92##########',
    'PALESTINE': '+970#########',
    'PHILIPPINES': '+63##########',
    'QATAR': '+974########',
    'RUSSIA': '+7###########',
    'SAUDI ARABIA': '+966#########',
    'SINGAPORE': '+65#########',
    'SOUTH KOREA': '+82##########',
    'SRI LANKA': '+94#########',
    'SYRIA': '+963##########',
    'TAIWAN': '+886##########',
    'TAJIKISTAN': '+992#########',
    'THAILAND': '+66##########',
    'TIMOR-LESTE': '+670########',
    'TURKEY': '+90##########',
    'TURKMENISTAN': '+993#########',
    'UAE': '+971#########',
    'UZBEKISTAN': '+998#########',
    'VIETNAM': '+84##########',
    'YEMEN': '+967#########',
    'ALBANIA': '+355#########',
    'ANDORRA': '+376#########',
    'AUSTRIA': '+43##########',
    'BELARUS': '+375#########',
    'BELGIUM': '+32##########',
    'BOSNIA/HERZEGOVINA': '+387#########',
    'BULGARIA': '+359#########',
    'CROATIA': '+385#########',
    'CYPRUS': '+357#########',
    'CZECH': '+420#########',
    'DENMARK': '+45##########',
    'ESTONIA': '+372#########',
    'FINLAND': '+358##########',
    'FRANCE': '+33#########',
    'GERMANY': '+49##########',
    'GREECE': '+30##########',
    'HUNGARY': '+36##########',
    'ICELAND': '+354#########',
    'IRELAND': '+353##########',
    'ITALY': '+39##########',
    'KOSOVO': '+383#########',
    'LATVIA': '+371#########',
    'LIECHTENSTEIN': '+423#########',
    'LITHUANIA': '+370#########',
    'LUXEMBOURG': '+352##########',
    'MALTA': '+356#########',
    'MOLDOVA': '+373#########',
    'MONACO': '+377#########',
    'MONTENEGRO': '+382#########',
    'NETHERLANDS': '+31##########',
    'NORTH MACEDONIA': '+389#########',
    'NORWAY': '+47##########',
    'POLAND': '+48##########',
    'PORTUGAL': '+351#########',
    'ROMANIA': '+40##########',
    'RUSSIA': '+7###########',
    'SAN MARINO': '+378#########',
    'SERBIA': '+381#########',
    'SLOVAKIA': '+421#########',
    'SLOVENIA': '+386#########',
    'SPAIN': '+34##########',
    'SWEDEN': '+46##########',
    'SWITZERLAND': '+41##########',
    'UKRAINE': '+380#########',
    'UK': '+44##########',
    'VATICAN CITY': '+379#########',
    'ALGERIA': '+213#########',
    'ANGOLA': '+244#########',
    'BENIN': '+229#########',
    'BOTSWANA': '+267#########',
    'BURKINA FASO': '+226#########',
    'BURUNDI': '+257#########',
    'CAMEROON': '+237#########',
    'CAPE VERDE': '+238#########',
    'CAF': '+236#########',
    'CHAD': '+235#########',
    'COMOROS': '+269#########',
    'CONGO': '+242#########',
    'CONGO, DROT': '+243#########',
    'DJIBOUTI': '+253#########',
    'EGYPT': '+20##########',
    'EQUATORIAL GUINEA': '+240#########',
    'ERITREA': '+291#########',
    'ETHIOPIA': '+251#########',
    'GABON': '+241#########',
    'GAMBIA': '+220#########',
    'GHANA': '+233#########',
    'GUINEA': '+224#########',
    'GUINEA-BISSAU': '+245#########',
    'IVORY COAST': '+225#########',
    'KENYA': '+254#########',
    'LESOTHO': '+266#########',
    'LIBERIA': '+231#########',
    'LIBYA': '+218#########',
    'MADAGASCAR': '+261#########',
    'MALAWI': '+265#########',
    'MALI': '+223#########',
    'MAURITANIA': '+222#########',
    'MAURITIUS': '+230#########',
    'MOROCCO': '+212#########',
    'MOZAMBIQUE': '+258#########',
    'NAMIBIA': '+264#########',
    'NIGER': '+227#########',
    'NIGERIA': '+234#########',
    'RWANDA': '+250#########',
    'SAO TOME AND PRINCIPE': '+239#########',
    'SENEGAL': '+221#########',
    'SEYCHELLES': '+248#########',
    'SIERRA LEONE': '+232#########',
    'SOMALIA': '+252#########',
    'SOUTH AFRICA': '+27###########',
    'SOUTH SUDAN': '+211#########',
    'SUDAN': '+249#########',
    'SWAZILAND': '+268#########',
    'TANZANIA': '+255#########',
    'TOGO': '+228#########',
    'TUNISIA': '+216#########',
    'UGANDA': '+256#########',
    'ZAMBIA': '+260#########',
    'ZIMBABWE': '+263#########',
    'MEXICO': '+52##########',
    'BELIZE': '+501########',
    'COSTA RICA': '+506########',
    'EL SALVADOR': '+503########',
    'GUATEMALA': '+502########',
    'HONDURAS': '+504########',
    'NICARAGUA': '+505########',
    'PANAMA': '+507########',
    'BAHAMAS': '+1##########',
    'CUBA': '+53#########',
    'DOMINICAN REPUBLIC': '+1##########',
    'HAITI': '+509#########',
    'JAMAICA': '+1##########',
    'PUERTO RICO': '+1##########',
    'TRINIDAD AND TOBAGO': '+1##########',
    'ARGENTINA': '+54##########',
    'BOLIVIA': '+591#########',
    'BRAZIL': '+55###########',
    'CHILE': '+56##########',
    'COLOMBIA': '+57##########',
    'ECUADOR': '+593#########',
    'GUYANA': '+592#########',
    'PARAGUAY': '+595#########',
    'PERU': '+51##########',
    'SURINAME': '+597#########',
    'TRINIDAD AND TOBAGO': '+1##########',
    'URUGUAY': '+598#########',
    'VENEZUELA': '+58##########',
    'AUSTRALIA': '+61##########',
    'FIJI': '+679########',
    'INDONESIA': '+62###########',
    'KIRIBATI': '+686########',
    'MARSHALL ISLANDS': '+692########',
    'MICRONESIA': '+691#########',
    'NAURU': '+674########',
    'NEW ZEALAND': '+64###########',
    'PALAU': '+680########',
    'PAPUA NEW GUINEA': '+675#########',
    'SAMOA': '+685########',
    'SOLOMON ISLANDS': '+677########',
    'TONGA': '+676########',
    'TUVALU': '+688########',
    'VANUATU': '+678########'

}

os.system('cls')

def print_banner():
    custom_fig = pyfiglet.Figlet(font='small', width=180)
    banner_text = custom_fig.renderText('\tSMS GEN')
    banner = colored(banner_text, 'green', 'on_black', ['bold'])
    print(banner)

    sub_banner_text = "https://discord.gg/portlords\n"
    sub_banner = colored(sub_banner_text, 'green')
    print(sub_banner)

def generate_phone_numbers(country, num_numbers):
    # Check if selected country is in the phone_formats dictionary
    if country not in phone_formats:
        print("Invalid country selected.")
        exit()

    # Generate specified number of phone numbers for the selected country
    phone_numbers = []
    for i in range(num_numbers):
        phone_number = phone_formats[country]
        for j in range(10):
            phone_number = phone_number.replace('#', str(random.randint(0, 9)), 1)
        phone_numbers.append(phone_number)

    # Write generated phone numbers to file
    with open('C:\\Users\\portl\\Desktop\\Generator\\results\\generated.txt', 'w') as file:
        for number in phone_numbers:
            file.write(number + '\n')

    print(f"{num_numbers} Phone Numbers Generated and Saved To Generated.txt.")
    return phone_numbers

def validate_phone_numbers(phone_numbers):
    valid_numbers = []
    invalid_numbers = []
    for number in phone_numbers:
        try:
            parsed_number = phonenumbers.parse(number)
            if phonenumbers.is_valid_number(parsed_number):
                valid_numbers.append(number)
            else:
                invalid_numbers.append(number)
        except phonenumbers.phonenumberutil.NumberParseException:
            invalid_numbers.append(number)

    print(f"{len(valid_numbers)} Valid Phone Numbers Found.")
    print(f"{len(invalid_numbers)} Invalid Phone Numbers Found.")

    # Write valid and invalid numbers to separate files
    with open('C:\\Users\\portl\\Desktop\\Generator\\results\\valid.txt', 'a') as file:
        for number in valid_numbers:
            file.write(number + '\n')
    with open('C:\\Users\\portl\\Desktop\\Generator\\results\\invalid.txt', 'a') as file:
        for number in invalid_numbers:
            file.write(number + '\n')

# Print banner
print_banner()

# Get user input for country name or code and number of phone numbers to generate
print(" Supports All 191 Countries\n")
country_input = input(colored(" Please Enter a Country Name: ( In Capital Letters ) ", "green", "on_black"))
if country_input in phone_formats:
    country = country_input
else:
    for c, n in phone_formats.items():
        if country_input.lower() in [c.lower(), n[1:]]:
            country = c
            break
    else:
        print(" Invalid country name")
        exit()

num_numbers = int(input(colored(" Number Of Phones To Generate: ", "green", "on_black")))

# Generate specified number of phone numbers for the selected country
phone_numbers = generate_phone_numbers(country, num_numbers)

# Validate generated phone numbers
validate = input(colored(" Validate the Generated Phone Numbers? (Y/N) ", "green", "on_black")).lower()
if validate == 'y':
    validate_phone_numbers(phone_numbers)
elif validate == 'n':
    print(" Program exiting.")
else:
    print(" Invalid input. Program exiting.")
